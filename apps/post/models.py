from django.db import models
from apps.channel.models import Channel


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False)
    content = models.CharField(max_length=300, blank=False)
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    owner = models.ForeignKey('auth.User',
                              related_name='posts',
                              on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel,
                                related_name='posts',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    class Meta:
        ordering = ['date']


class Comment(models.Model):
    content = models.CharField(max_length=2083, default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User',
                              related_name='comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']


class Like(models.Model):
    comment = models.OneToOneField(Comment,
                                   on_delete=models.CASCADE,
                                   primary_key=True)


class DisLike(models.Model):
    comment = models.OneToOneField(Comment,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
