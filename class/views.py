from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home page for the class application</h1>')


def about(request):
    return HttpResponse('<h1>This is about page of our application.</h1>')
