from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title