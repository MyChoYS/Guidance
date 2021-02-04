from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def review(request) :
    return render(request, 'review.html', None)
