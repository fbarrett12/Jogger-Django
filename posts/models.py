from django.db import models

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)