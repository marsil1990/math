from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to= 'blog')
    title = models.CharField(max_length=200)
    desc = models.TextField()
    content = models.TextField()
    urls =  models.URLField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']