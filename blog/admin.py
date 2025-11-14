from django.contrib import admin
from .models import Post, Tag
from django.db import models
from tinymce.widgets import TinyMCE

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    
    class Media:
        js = ('admin/js/tinymce_csrf.js',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)