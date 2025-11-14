from django.shortcuts import render, get_object_or_404
from .models import Post

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {
        'posts': posts
    })
    
def post_content(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_content.html', {'post': post})