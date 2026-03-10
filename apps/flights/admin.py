from django.contrib import admin
from .models import Flight, Review


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        'flight_id', 'airline_name', 'source', 'destination',
        'departure_time', 'price', 'seats_available', 'is_fully_booked', 'is_active',
    ]
    list_filter = ['airline_name', 'source', 'destination', 'is_active', 'aircraft_type']
    search_fields = ['flight_id', 'airline_name', 'source', 'destination']
    readonly_fields = ['created_at', 'updated_at', 'booking_percentage']
    fieldsets = (
        ('Flight Info', {'fields': ('flight_id', 'airline_name', 'source', 'destination', 'aircraft_type')}),
        ('Schedule', {'fields': ('departure_time', 'arrival_time')}),
        ('Capacity & Pricing', {'fields': ('price', 'seats_total', 'seats_available', 'booking_percentage')}),
        ('Status', {'fields': ('is_active',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )

    def is_fully_booked(self, obj):
        return obj.is_fully_booked()
    is_fully_booked.boolean = True
    is_fully_booked.short_description = 'Fully Booked'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'flight', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['title', 'comment', 'user__username', 'flight__flight_id']
    readonly_fields = ['created_at', 'updated_at']
