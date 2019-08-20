from django.shortcuts import render

from .models import Post


def home(request):
    context = {
        'title': 'Blog Home',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About Us'})
