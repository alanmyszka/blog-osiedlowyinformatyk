from django.db import models
from tinymce.models import HTMLField
from django.utils.html import strip_tags
import re
import html

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    content = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def excerpt(self, words=30):
        text = strip_tags(self.content)
        text = html.unescape(text)
        text = re.sub(r'\s+', ' ', text).strip()
        word_list = text.split()
        if len(word_list) > words:
            return ' '.join(word_list[:words]) + "…"
        return text