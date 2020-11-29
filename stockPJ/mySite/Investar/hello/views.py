from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sayHello(request, name):
    html = "<h1>Hello, {}!</h1>".format(name)
    return HttpResponse(html)