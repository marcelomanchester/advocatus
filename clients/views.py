from django.shortcuts import render

def home (rec):
    return render(rec, "client_home.html")

def register(request):
    return render(request, "client_register.html")