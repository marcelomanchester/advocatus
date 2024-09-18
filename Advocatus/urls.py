from django.contrib import admin
from django.urls import path, include

from appointment_calendar.views import calendarPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('agenda/', include('appointment_calendar.urls')),
]
