from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return HttpResponse('''<h1> Home </h1> <a href ="https://mail.google.com/mail/u/0/"> e-mail <a/>''')

def youtube(request):
    return HttpResponse('''<h1> Home </h1> <a href ="https://www.youtube.com/"> Youtube </a>''')