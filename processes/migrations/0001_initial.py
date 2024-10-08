# Generated by Django 5.1 on 2024-09-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=200)),
                ('tipo_acao', models.CharField(max_length=200)),
                ('cliente', models.CharField(max_length=200)),
                ('contrario', models.CharField(max_length=200)),
                ('numero_pasta', models.CharField(max_length=100)),
                ('numero_cnj', models.CharField(max_length=100)),
                ('detalhes_pasta', models.TextField()),
                ('advogado', models.CharField(max_length=200)),
                ('push_andamentos', models.CharField(max_length=200)),
                ('comarca', models.CharField(max_length=200)),
                ('juiz', models.CharField(max_length=200)),
                ('risco', models.CharField(choices=[('B', 'Baixo'), ('M', 'Médio'), ('A', 'Alto')], default='M', max_length=1)),
                ('tribunal', models.CharField(max_length=200)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2)),
                ('instancia', models.CharField(choices=[('1', 'Primeira Instância'), ('2', 'Segunda Instância'), ('3', 'Tribunais Superiores')], default='1', max_length=1)),
                ('vara', models.CharField(max_length=200)),
                ('valor_causa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_possivel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_provisionado', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
