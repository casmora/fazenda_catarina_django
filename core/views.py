#from django.shortcuts import render
from django.http import HttpResponse

def teste(request):
    return HttpResponse("Olá mundo do Django.")

def teste2(request):
    return HttpResponse (" Uma nova página.")    




# Create your views here.
