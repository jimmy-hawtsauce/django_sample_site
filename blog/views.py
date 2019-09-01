from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    # naming convention :
    # <app>/<model>_<viewtype>.html
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', context={'title': 'About Us'})
