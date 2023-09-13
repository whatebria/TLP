from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    page = "<html>"
    page += "<head>"
    page += "</head>"
    page += "<body>"
    page += "<h1>Inicio<h1>"
    page += "</body>"
    return HttpResponse(page)

def carreras(request):
    page = "<html>"
    page += "<head>"
    page += "</head>"
    page += "<body>"
    page += "<h1>Carreras<h1>"
    page += "</body>"
    return HttpResponse(page)

def docentes(request):
    page = "<html>"
    page += "<head>"
    page += "</head>"
    page += "<body>"
    page += "<h1>Docentes<h1>"
    page += "</body>"
    return HttpResponse(page)