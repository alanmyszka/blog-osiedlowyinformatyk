from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def excerpt(self, chars=150):
        if len(self.content) > chars:
            return self.content[:chars].rstrip() + "…"
        return self.content