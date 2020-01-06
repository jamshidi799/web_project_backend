from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
