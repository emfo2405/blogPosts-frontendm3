from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
