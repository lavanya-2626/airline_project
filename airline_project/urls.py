from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.flights.urls')),
    path('auth/', include('apps.auth_app.urls')),
    path('users/', include('apps.users.urls')),
    path('bookings/', include('apps.bookings.urls')),
]
