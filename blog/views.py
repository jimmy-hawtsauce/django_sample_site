from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html', context={'title': 'Blog Home'})


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About Us'})
