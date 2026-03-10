"""
core/mixins.py — Reusable view mixins for common patterns.
"""
from django.contrib import messages
from django.shortcuts import redirect


class SuccessMessageMixin:
    """Add a success message after a successful form submission."""
    success_message = ''
    success_url = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response
