from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<H1>Hello World</H1>')