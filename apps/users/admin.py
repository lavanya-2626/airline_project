from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'country', 'newsletter_subscribed', 'created_at']
    list_filter = ['country', 'created_at', 'newsletter_subscribed']
    search_fields = ['user__username', 'user__email', 'phone', 'passport_number']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User Information', {'fields': ('user', 'phone')}),
        ('Personal Details', {'fields': ('date_of_birth', 'passport_number', 'nationality')}),
        ('Address', {'fields': ('address', 'city', 'country', 'zipcode')}),
        ('Preferences', {'fields': ('preferred_currency', 'newsletter_subscribed')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
