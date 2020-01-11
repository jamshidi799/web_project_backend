from django.db import models


class Channel(models.Model):
    owner = models.ForeignKey('auth.User',
                              on_delete=models.CASCADE,
                              related_name='channels')
    name = models.CharField(max_length=20, default='')
    about = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
