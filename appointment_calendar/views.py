from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Commitment

def adicionar_compromisso(req):
    if req.method == "POST":
        time_start = req.POST.get('hora_inicio')
        time_end = req.POST.get('hora_fim')
        processes = req.POST.get('processo')
        location = req.POST.get('local')
        description = req.POST.get('observacoes')  # Pode ser None se não for preenchido

        if time_start and time_end and processes and location:
            compromisso = Commitment(
                time_start=time_start,
                time_end=time_end,
                processes=processes,
                location=location,
                description=description
            )
            compromisso.save()
            messages.success(req, 'Compromisso adicionado com sucesso!')
            return redirect('nome_da_url_para_redirect')  # Altere para o nome da URL definido no seu arquivo urls.py
        else:
            messages.error(req, 'Por favor, preencha todos os campos obrigatórios.')
    
    return render(req, 'add_commitment.html')  # Assegure-se de que o caminho do template está correto.