from django.contrib.auth.models import User
from django.db import models


class Connection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        User,
        related_name="creator",
        on_delete=models.CASCADE,
        null=True,
    )
    following = models.ForeignKey(User,
                                  related_name="following",
                                  on_delete=models.CASCADE,
                                  null=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        unique=True,
        on_delete=models.CASCADE,
    )
    bio = models.CharField(max_length=300, blank=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'username: {self.user.username},' \
            f'email: {self.user.email}'
