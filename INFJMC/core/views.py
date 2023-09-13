from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hola Mundo")
def carreras(request):
    return HttpResponse("chao mundo")
def docentes(request):
    return HttpResponse("jeje mundo")