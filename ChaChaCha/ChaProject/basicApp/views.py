from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'home.html', None)

def contact(request) :
    return render(request, 'contact.html', None)