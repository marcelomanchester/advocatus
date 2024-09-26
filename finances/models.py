from django.db import models
from processes.models import Process

# Create your models here.
class ProcessExpense(models.Model):
    EXPENSE_TYPES = (
        ('CP', 'Custas processuais'),
        ('HA', 'Honorários advocatícios'),
        ('DO', 'Despesas operacionais'),
        ('HT', 'Honorários de terceiros'),
        ('TD', 'Taxas de documentação'),
        ('MP', 'Multas ou penalidades'),
        ('NI', 'Notificações e intimações'),
    )

    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    expense_type = models.CharField(max_length=2, choices=EXPENSE_TYPES, default='CP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.description} - {self.amount}"