"""
auth_app/views.py — Thin HTTP handlers for auth routes.
All logic is delegated to AuthService and Django Forms.
"""
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm
from .services import AuthService
from apps.core.exceptions import UserAlreadyExistsError, AuthError

logger = logging.getLogger('apps.auth_app')


def register(request):
    """Register a new user account."""
    if request.user.is_authenticated:
        logger.info("Register: User %s is already authenticated, redirecting home", request.user.username)
        return redirect('home')

    if request.method == 'POST':
        logger.info("Register: Received POST request")
        form = RegisterForm(request.POST)
        if form.is_valid():
            logger.info("Register: Form is valid, calling AuthService.register_user")
            try:
                AuthService.register_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                logger.info("Register: User successfully registered, redirecting to login")
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
            except UserAlreadyExistsError as e:
                logger.warning("Register: UserAlreadyExistsError: %s", str(e))
                messages.error(request, str(e))
            except Exception as e:
                logger.error("Register: UNEXPECTED ERROR: %s", str(e), exc_info=True)
                messages.error(request, f"An unexpected error occurred: {str(e)}")
        else:
            logger.warning("Register: Form is INVALID: %s", form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        logger.info("Register: Rendering registration form (GET)")
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    """Authenticate and log in a user."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = AuthService.authenticate_user(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            except AuthError as e:
                messages.error(request, str(e))
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    """Log out the current user."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
