from django.shortcuts import render
from .models import Post  # Import the Post model from the current app's models.py file


# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

    
