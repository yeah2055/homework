from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request,"home.html",{'kkk' : blogs})

def detail(request):
    return render(request,"detail.html")

def show(request):
    # yourtext = request.GET['fulltext']
    abcde = request.GET["fulltext"]
    return render(request,"show.html",{"aaa":abcde})