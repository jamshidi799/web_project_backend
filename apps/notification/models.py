from django.db import models


class Notification(models.Model):
    CHOICES = [('post', 'like your post'),
               ('comment', 'a new comment added to '),
               ('follow', 'follow you')]
    created = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length=50, choices=CHOICES)
    creator = models.CharField(max_length=50, default="lucky")
    target = models.ForeignKey('auth.User',
                               related_name="notifications",
                               on_delete=models.CASCADE,
                               null=True)
    target_post = models.CharField(max_length=50, blank=True)
