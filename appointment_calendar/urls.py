from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('calendar/', views.adicionar_compromisso, name='calendar'),
]
