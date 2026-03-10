from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
