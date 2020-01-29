from django.contrib.auth.models import User
from django.db import models


class Connection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User,
                                related_name="friendship_creator_set",
                                on_delete=models.CASCADE)
    following = models.ForeignKey(User,
                                  related_name="friend_set",
                                  on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        unique=True,
        on_delete=models.CASCADE,
    )
    bio = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'username: {self.user.username},' \
            f'email: {self.user.email}'
