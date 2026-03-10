from django.urls import path
from . import views

urlpatterns = [
    path('book/<str:flight_id>/', views.book_flight, name='book_flight'),
    path('booking-confirmation/<str:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('cancel-booking/<str:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
