from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):
    follower = models.ForeignKey(User,
                                 related_name='following',
                                 on_delete=models.CASCADE)
    following = models.ForeignKey(User,
                                  related_name='followers',
                                  on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    bio = models.CharField(max_length=300)
    image = models.ImageField()
    follow = models.OneToOneField(Follower,
                                  related_name='Follower',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f'username: {self.user.username},' \
            f'email: {self.user.email}'
