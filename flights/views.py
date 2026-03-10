from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flight, Booking, UserProfile
import uuid


def home(request):
    """Home page view"""
    flights = Flight.objects.all()[:6]
    context = {
        'flights': flights,
    }
    return render(request, 'home.html', context)


def search_flights(request):
    """Search flights view"""
    flights = Flight.objects.all()
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')
    travel_date = request.GET.get('travel_date', '')

    if source:
        flights = flights.filter(source__icontains=source)
    if destination:
        flights = flights.filter(destination__icontains=destination)
    if travel_date:
        flights = flights.filter(departure_time__date=travel_date)

    context = {
        'flights': flights,
        'source': source,
        'destination': destination,
        'travel_date': travel_date,
    }
    return render(request, 'search_flight.html', context)


@login_required(login_url='login')
def book_flight(request, flight_id):
    """Book a flight view"""
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        passenger_name = request.POST.get('passenger_name')
        passenger_email = request.POST.get('passenger_email')
        passenger_phone = request.POST.get('passenger_phone')
        seat_number = request.POST.get('seat_number')

        if not all([passenger_name, passenger_email, passenger_phone, seat_number]):
            messages.error(request, 'Please fill in all fields')
            return redirect('book_flight', flight_id=flight_id)

        # Create booking
        booking_id = f"BK-{uuid.uuid4().hex[:8].upper()}"
        
        booking = Booking.objects.create(
            booking_id=booking_id,
            user=request.user,
            flight=flight,
            passenger_name=passenger_name,
            passenger_email=passenger_email,
            passenger_phone=passenger_phone,
            seat_number=seat_number,
            status='confirmed'
        )

        # Update available seats
        flight.seats_available -= 1
        flight.save()

        messages.success(request, f'Booking confirmed! Your booking ID: {booking_id}')
        return redirect('booking_confirmation', booking_id=booking.id)

    context = {
        'flight': flight,
    }
    return render(request, 'booking.html', context)


@login_required(login_url='login')
def booking_confirmation(request, booking_id):
    """Booking confirmation view"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    context = {
        'booking': booking,
    }
    return render(request, 'booking_confirmation.html', context)


@login_required(login_url='login')
def booking_history(request):
    """View booking history"""
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings,
    }
    return render(request, 'booking_history.html', context)


def register(request):
    """User registration view"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        # Validation checks
        if not all([username, email, password, password_confirm]):
            messages.error(request, 'All fields are required')
            return redirect('register')

        if len(username) < 3:
            messages.error(request, 'Username must be at least 3 characters long')
            return redirect('register')

        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long')
            return redirect('register')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email or login.')
            return redirect('register')

        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Create user profile
            UserProfile.objects.create(user=user)

            messages.success(request, 'Registration successful! Please login with your credentials.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('register')

    return render(request, 'register.html')


def user_login(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')


@login_required(login_url='login')
def user_profile(request):
    """View user profile"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        request.user.email = request.POST.get('email', request.user.email)
        request.user.first_name = request.POST.get('first_name', request.user.first_name)
        request.user.last_name = request.POST.get('last_name', request.user.last_name)
        request.user.save()

        profile.phone = request.POST.get('phone', profile.phone)
        profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)
