

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request

from blog.models import BlogPost


def home(request):

 posts = BlogPost.objects.all()
 return render(request, 'blog/home.html',{'posts':posts})

def post_detail(request, post_id):

    post = get_object_or_404(BlogPost, id=post_id)

    return render(request, 'blog/post_detail.html', {'post':post})



