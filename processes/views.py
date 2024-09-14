from django.shortcuts import render

def process(req):
  user = req.user

  if user.is_authenticated:
    return render(req, 'index.html')
  

def register_process(req):
  user = req.user

  if user.is_authenticated:
    return render(req, 'process_register.html')