from django.shortcuts import render

# Create your views here.

def get (rec):
    x = 10
    return render(rec, "index.html", {"x":x})