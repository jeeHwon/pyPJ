from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sayHello(request, name):
    html = "<h1>Hello,{}!</h1>".format(name)
    return HttpResponse(html)
