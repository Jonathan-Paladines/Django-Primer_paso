from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    mensaje = 1 + 1
    html = "<h1>Hola, de parte de Jonathan</h1>"
    Nombre = "Jonathan Leandro Paladines Navarrete"
    return HttpResponse(html)
