from django.db import models


class Channel(models.Model):
    owner = models.ForeignKey('auth.User',
                              on_delete=models.CASCADE,
                              related_name='channels')
    authors = models.ManyToManyField('auth.User',
                                     related_name='authors',
                                     blank=True)
    name = models.CharField(max_length=20, default='')
    about = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'