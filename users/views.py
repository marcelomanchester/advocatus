from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def register(req):
    if req.method == 'GET':
        return render(req, 'register.html')
    elif req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm-password')
 
        if password != confirm_password:
            messages.add_message(req, constants.ERROR, "As senhas não coincidem")
            return redirect('/register')

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(req, constants.ERROR, "Usuario já cadastrado")
            return redirect('/login')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login')


def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username, email, password = req.POST.get('username'), req.POST.get('email'), req.POST.get('password')

        try:
            user = auth.authenticate(req, username=username, email=email, password=password)
            if user:
                auth.login(req, user)
                return redirect('/')
        except:
            pass
        else:
            messages.add_message(req, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/login')

def home(req):
    return render(req, 'home.html')


def app(req):
    return render(req, 'app.html')