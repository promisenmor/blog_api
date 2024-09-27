from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
