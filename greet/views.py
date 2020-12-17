from django.shortcuts import render
from django.http import HttpResponse

def hello(requests):
    return HttpResponse("Hello World")

def home(requests):
    return HttpResponse("<h1> Example Django Application with Docker Implementation </h1> <br> <h2>Available URLs</h2> <br> <h3>/hello</h3>")