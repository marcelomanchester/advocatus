from django.shortcuts import render, redirect
from .forms import CompromissoForm

<<<<<<< Updated upstream
def calendarPage(req): # request => req
    user = req.user

    if user.is_authenticated: # verificar se o usuario esta autenticado antes de renderizar qualquer pagina
        return render(req, "calendar_page.html")
=======
# Create your views here.
def calendarPage(request):
    return render(request, "appointment_calendar/calendar_page.html")

def adicionar_compromisso(request):
    if request.method == 'POST':
        form = CompromissoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda')  # Substitua por sua URL de agenda
    else:
        form = CompromissoForm()

    return render(request, 'appointment_calendar/adicionar_compromisso.html', {'form': form})
>>>>>>> Stashed changes
