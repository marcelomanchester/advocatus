from django.shortcuts import render, redirect
from .models import Process
from django.contrib import messages
from django.contrib.messages import constants

def process(req):
  user = req.user

  if user.is_authenticated:
    return render(req, 'processes.html')
  

def register_process(req):
  user = req.user

  if user.is_authenticated:

    if req.method == 'POST':
        tipo = req.POST.get('tipo')
        titulo = req.POST.get('titulo')
        tipo_acao = req.POST.get('tipo_acao')
        cliente = req.POST.get('cliente')
        contrario = req.POST.get('contrario')
        numero_pasta = req.POST.get('numero_pasta')
        numero_cnj = req.POST.get('numero_cnj')
        detalhes_pasta = req.POST.get('detalhes_pasta')
        advogado = req.POST.get('advogado')
        push_andamentos = req.POST.get('push_andamentos')
        comarca = req.POST.get('comarca')
        juiz = req.POST.get('juiz')
        risco = req.POST.get('risco')
        tribunal = req.POST.get('tribunal')
        uf = req.POST.get('uf')
        instancia = req.POST.get('instancia')
        vara = req.POST.get('vara')
        valor_causa = req.POST.get('valor_causa')
        valor_possivel = req.POST.get('valor_possivel')
        valor_provisionado = req.POST.get('valor_provisionado')

        if not tipo or not titulo or not tipo_acao or not cliente or not contrario or not numero_pasta or not numero_cnj or not detalhes_pasta or not advogado or not push_andamentos or not comarca or not juiz or not risco or not tribunal or not uf or not instancia or not vara or not valor_causa or not valor_possivel or not valor_provisionado:
            messages.add_message(req, constants.ERROR, "Todos os campos são obrigatórios.")
            return redirect('/processes/process_register')

        try:
            valor_causa = float(valor_causa)
            valor_possivel = float(valor_possivel)
            valor_provisionado = float(valor_provisionado)
        except ValueError:
            messages.add_message(req, constants.ERROR, "Os valores financeiros devem ser números válidos.")
            return redirect('/processes/process_register')

        if valor_causa < 0 or valor_possivel < 0 or valor_provisionado < 0:
            messages.add_message(req, constants.ERROR, "Os valores financeiros não podem ser negativos.")
            return redirect('/processes/process_register')

        process = Process.objects.create(
            tipo=tipo,
            titulo=titulo,
            tipo_acao=tipo_acao,
            cliente=cliente,
            contrario=contrario,
            numero_pasta=numero_pasta,
            numero_cnj=numero_cnj,
            detalhes_pasta=detalhes_pasta,
            advogado=advogado,
            push_andamentos=push_andamentos,
            comarca=comarca,
            juiz=juiz,
            risco=risco,
            tribunal=tribunal,
            uf=uf,
            instancia=instancia,
            vara=vara,
            valor_causa=valor_causa,
            valor_possivel=valor_possivel,
            valor_provisionado=valor_provisionado
        )

        messages.add_message(req, constants.SUCCESS, "Processo cadastrado com sucesso!")
        return redirect('/processes')

    if req.method == 'GET':
      riscos_choices = Process.RISCO_CHOICES
      uf_choices = Process.UF_CHOICES
      instancia_choices = Process.INSTANCIA_CHOICES

      return render(req, 'process_register.html', {
        'riscos': riscos_choices,
        'ufs': uf_choices,
        'instacias': instancia_choices
      })
      
