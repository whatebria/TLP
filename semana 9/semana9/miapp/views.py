from django.shortcuts import render

# Create your views here.

def index(request):
    title = "inicio"

    data = {
            "title" : title
    }

    return render(request,'miapp/index.html', data)

def carreras(request):
    title = "carreras"
    return render(request,'miapp/carreras.html')