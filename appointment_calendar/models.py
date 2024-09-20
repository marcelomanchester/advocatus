from django.db import models

# Create your models here.
class Compromisso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo