from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
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

@require_POST
def upload_image(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)
    
    if not request.user.is_staff:
        return JsonResponse({"error": "Permission denied"}, status=403)
    
    token = request.META.get('HTTP_X_CSRFTOKEN', '')
    if not token:
        return JsonResponse({"error": "CSRF token missing"}, status=403)
    
    if request.FILES.get("file"):
        image = request.FILES["file"]
        path = default_storage.save(f"uploads/{image.name}", image)
        url = request.build_absolute_uri(default_storage.url(path))
        return JsonResponse({"location": url})
    
    return JsonResponse({"error": "No file uploaded"}, status=400)