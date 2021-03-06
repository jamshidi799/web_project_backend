from django.db import models
from apps.channel.models import Channel


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=300, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to='post')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    owner = models.ForeignKey('auth.User',
                              default="3",
                              related_name='posts',
                              on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel,
                                related_name='posts',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    like = models.ManyToManyField('auth.User',
                                  related_name="liked_posts",
                                  blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    content = models.CharField(max_length=2083, default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User',
                              related_name='comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    reply_to = models.ForeignKey('Comment',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)

    like = models.ManyToManyField('auth.User',
                                  related_name="like_comments",
                                  blank=True)
    dislike = models.ManyToManyField('auth.User',
                                     related_name="dislike_comments",
                                     blank=True,
                                     null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.content}'
