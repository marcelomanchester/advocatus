from django.contrib import admin
from django.urls import path, include
from appointment_calendar import views

from appointment_calendar.views import calendarPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
<<<<<<< Updated upstream
    path('agenda/', include('appointment_calendar.urls')),
=======
    path('agenda', calendarPage),
    path('adicionar/', views.adicionar_compromisso, name='adicionar_compromisso'),
    
>>>>>>> Stashed changes
]
