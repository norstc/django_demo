from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Greet a")

def greet(request,name):
    return HttpResponse("Hello %s" % name)