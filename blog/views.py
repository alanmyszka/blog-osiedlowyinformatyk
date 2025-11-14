from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import JsonResponse
from .models import Post

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {
        'posts': posts
    })
    
def post_content(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_content.html', {'post': post})

@csrf_exempt
@login_required
@require_POST
def upload_image(request):
    if request.method == "POST" and request.FILES.get("file"):
        image = request.FILES["file"]
        path = default_storage.save(f"uploads/{image.name}", image)
        url = default_storage.url(path)
        return JsonResponse({"location": url})
    return JsonResponse({"error": "No file uploaded"}, status=400)