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

        if not username:
            messages.add_message(req, constants.ERROR, "Digite o seu nome de usuario")
            return redirect('/users/register')

        
        if len(password) < 6:
            messages.add_message(req, constants.ERROR, "As senhas precisam ter no minimo 6 digitos")
            return redirect('/users/register')
        
        if password != confirm_password:
            messages.add_message(req, constants.ERROR, "As senhas não coincidem")
            return redirect('/users/register')

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(req, constants.ERROR, "Usuario já cadastrado")
            return redirect('/users/register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        User.save(user)

        return redirect('/users/login')


def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username, email, password = req.POST.get('username'), req.POST.get('email'), req.POST.get('password')

        if not username or not email or not password:
            messages.add_message(req, constants.ERROR, 'Preencha todos os campos')
            return redirect('/users/login')

        try:
            user = auth.authenticate(req, username=username, email=email, password=password)
            if user:
                auth.login(req, user)
                return HttpResponse('home')
                # return redirect('/') -- HOME
        except:
            messages.add_message(req, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/users/login')
        