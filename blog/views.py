from django.shortcuts import render, get_object_or_404

# access items from the database
from .models import Blog


def allblogs(request):
    # this next line grabs all the jobs from the database
    blogs = Blog.objects
    # then pass a dictionary to the render function
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
