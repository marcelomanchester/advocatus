from django.urls import path
from . import views

urlpatterns = [
    path("", views.process, name="processes"),
    path("process_register", views.register_process, name="process_register")
]
