from django.shortcuts import render
import time

# Create your views here.
from django.http import HttpResponse

def index(request):
    today = time.localtime(time.time())
    newyear = today.tm_mon == 1 and today.tm_mday == 1
    return render(request, 'newyear/index.html',{
        'newyear':newyear
    })