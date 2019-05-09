from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'class/home.html')


def about(request):
    return render(request, 'class/about.html', {'title': 'About'})


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'class/blog.html', context)
