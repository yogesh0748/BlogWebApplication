from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post,Category




# from blog.models import Category


# Create your views here.

def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post,'cats':cats})

def category(request , url):
    cat = Category.objects.get(url=url)
    posts= Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})