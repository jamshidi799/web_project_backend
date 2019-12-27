from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    owner = models.ForeignKey(User, related_name="Posts",
    on_delete=models.CASCADE, null=True)
