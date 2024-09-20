from django.shortcuts import render, redirect


def calendarPage(req): # request => req
    user = req.user

    if user.is_authenticated: # verificar se o usuario esta autenticado antes de renderizar qualquer pagina
        return render(req, "calendar_page.html")
