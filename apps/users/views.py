"""
users/views.py — Thin views for user profile management.
"""
import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProfileUpdateForm
from .services import UserService

logger = logging.getLogger('apps.users')


@login_required(login_url='login')
def user_profile(request):
    """View and update the logged-in user's profile."""
    profile = UserService.get_or_create_profile(request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            UserService.update_profile(request.user, form.cleaned_data)
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        # Pre-populate form with current values
        form = ProfileUpdateForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone': profile.phone,
            'nationality': profile.nationality,
            'city': profile.city,
            'country': profile.country,
        })

    return render(request, 'users/profile.html', {'form': form, 'profile': profile})
