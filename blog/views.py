from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Home page</h2>')

def about(request):
    return HttpResponse('<h2>About page</h2>')
 