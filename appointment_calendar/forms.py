# appointment_calendar/forms.py
from django import forms
from .models import Compromisso

class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ['titulo', 'descricao', 'data_hora_inicio', 'data_hora_fim']
