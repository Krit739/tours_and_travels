from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def nepal(request):
    return HttpResponse("Nepal")

def india(request):
    return HttpResponse("India")

def bhutan(request):
    return HttpResponse("Bhutan")

def china(request):
    return HttpResponse("China")
