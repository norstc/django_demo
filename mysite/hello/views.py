from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("hello django from github and without pyc files")

def greet(request,name):
    return HttpResponse("Greet %s" % 'name')
