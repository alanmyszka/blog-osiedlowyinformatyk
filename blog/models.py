from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.SlugField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title