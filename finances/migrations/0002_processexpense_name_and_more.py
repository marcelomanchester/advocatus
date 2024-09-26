# Generated by Django 5.1 on 2024-09-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processexpense',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='processexpense',
            name='expense_type',
            field=models.CharField(choices=[('CP', 'Custas processuais'), ('HA', 'Honorários advocatícios'), ('DO', 'Despesas operacionais'), ('HT', 'Honorários de terceiros'), ('TD', 'Taxas de documentação'), ('MP', 'Multas ou penalidades'), ('NI', 'Notificações e intimações')], default='CP', max_length=2),
        ),
    ]
