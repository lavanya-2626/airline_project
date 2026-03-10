from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'booking_id', 'passenger_name', 'user', 'flight',
        'booking_date', 'status', 'payment_status', 'total_price',
    ]
    list_filter = ['status', 'payment_status', 'booking_date', 'flight__airline_name']
    search_fields = ['booking_id', 'passenger_name', 'user__username', 'passenger_email']
    readonly_fields = ['booking_id', 'created_at', 'updated_at', 'booking_date']
    fieldsets = (
        ('Booking Info', {'fields': ('booking_id', 'user', 'flight')}),
        ('Passenger', {'fields': ('passenger_name', 'passenger_email', 'passenger_phone', 'seat_number')}),
        ('Travel Docs', {'fields': ('date_of_birth', 'passport_number', 'nationality')}),
        ('Status & Payment', {'fields': ('status', 'payment_status', 'total_price')}),
        ('Timestamps', {'fields': ('booking_date', 'created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
