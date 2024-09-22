from django.shortcuts import render

def home (request):
    return render(request, "client_home.html")

def register(request):
    return render(request, "client_register.html")