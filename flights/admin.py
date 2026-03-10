from django.contrib import admin
from .models import Flight, Booking, UserProfile, Review, Notification


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_id', 'airline_name', 'source', 'destination', 'departure_time', 'price', 'seats_available', 'is_fully_booked', 'is_active']
    list_filter = ['airline_name', 'source', 'destination', 'departure_time', 'is_active', 'aircraft_type']
    search_fields = ['flight_id', 'airline_name', 'source', 'destination']
    readonly_fields = ['created_at', 'updated_at', 'booking_percentage']
    fieldsets = (
        ('Flight Information', {
            'fields': ('flight_id', 'airline_name', 'source', 'destination', 'aircraft_type')
        }),
        ('Schedule', {
            'fields': ('departure_time', 'arrival_time')
        }),
        ('Capacity & Pricing', {
            'fields': ('price', 'seats_total', 'seats_available', 'booking_percentage')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def is_fully_booked(self, obj):
        return obj.is_fully_booked()
    is_fully_booked.boolean = True
    is_fully_booked.short_description = 'Fully Booked'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'passenger_name', 'user', 'flight', 'booking_date', 'status', 'payment_status']
    list_filter = ['status', 'payment_status', 'booking_date', 'flight__airline_name']
    search_fields = ['booking_id', 'passenger_name', 'user__username', 'passenger_email']
    readonly_fields = ['booking_id', 'created_at', 'updated_at', 'booking_date']
    fieldsets = (
        ('Booking Information', {
            'fields': ('booking_id', 'user', 'flight')
        }),
        ('Passenger Details', {
            'fields': ('passenger_name', 'passenger_email', 'passenger_phone', 'seat_number')
        }),
        ('Additional Info', {
            'fields': ('date_of_birth', 'passport_number', 'nationality')
        }),
        ('Status & Payment', {
            'fields': ('status', 'payment_status', 'total_price')
        }),
        ('Timestamps', {
            'fields': ('booking_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'country', 'newsletter_subscribed', 'created_at']
    list_filter = ['country', 'created_at', 'newsletter_subscribed']
    search_fields = ['user__username', 'user__email', 'phone', 'passport_number']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'phone')
        }),
        ('Personal Details', {
            'fields': ('date_of_birth', 'passport_number', 'nationality')
        }),
        ('Address Information', {
            'fields': ('address', 'city', 'country', 'zipcode')
        }),
        ('Preferences', {
            'fields': ('preferred_currency', 'newsletter_subscribed')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'flight', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at', 'flight']
    search_fields = ['title', 'comment', 'user__username', 'flight__flight_id']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_type', 'title', 'is_read', 'created_at']
    list_filter = ['notification_type', 'is_read', 'created_at']
    search_fields = ['title', 'message', 'user__username']
    readonly_fields = ['created_at']
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'Mark selected as read'
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = 'Mark selected as unread'
