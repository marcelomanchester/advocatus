from django.shortcuts import render
from . import models

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

    if req.method == 'GET':
      riscos_choices = models.Process.RISCO_CHOICES
      uf_choices = models.Process.UF_CHOICES
      instancia_choices = models.Process.INSTANCIA_CHOICES

      return render(req, 'process_register.html', {
        'riscos': riscos_choices,
        'ufs': uf_choices,
        'instacias': instancia_choices
      })
      
