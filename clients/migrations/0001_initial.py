# Generated by Django 5.1.1 on 2024-09-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('number', models.CharField(max_length=255, unique=True)),
                ('birthdate', models.DateTimeField()),
                ('role', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255, unique=True)),
                ('adress', models.CharField(max_length=255)),
                ('complement', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('document_id', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('deleted_on', models.DateTimeField()),
            ],
        ),
    ]
