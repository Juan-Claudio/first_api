from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello first Django App</h1>')

def about(request):
    return HttpResponse("<h1>About us</h1> <p>We love learning and we learn quickly</p>")