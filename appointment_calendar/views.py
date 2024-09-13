from django.shortcuts import render

# Create your views here.
def calendarPage(request):
    return render(request, "appointment_calendar/calendar_page.html")