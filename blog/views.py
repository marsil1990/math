from django.shortcuts import render,  HttpResponse
from .models import Post

# Create your views here.
def posts(request):
    first_post  = Post.objects.first()
    posts = Post.objects.all()
    return render (request, 'blogs.html', {'first_post':first_post, 'posts':posts})

def post(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog.html', {'post':post})