from django.shortcuts import render,get_object_or_404
from .models import BlogPage


def allblogs(request):
    blogs = BlogPage.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):
    detailblog= get_object_or_404(BlogPage,pk=blog_id)
    return render(request,'blog/detail.html',{'detailblog':detailblog})
