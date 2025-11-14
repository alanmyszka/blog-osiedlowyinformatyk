"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from decouple import config
from blog.views import posts, post_content, upload_image
from django.conf.urls.static import static
from django.conf import settings

ADMIN_URL = config("DJANGO_ADMIN_URL", default="admin/")

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path('', posts),
    path('post/<slug:slug>/', post_content, name='post_content'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += [
    path("upload-image/", upload_image, name="upload_image"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)