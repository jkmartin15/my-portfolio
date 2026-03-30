from django.shortcuts import render, get_object_or_404
from .models import Post, Project

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'blog/portfolio.html', {'projects': projects})