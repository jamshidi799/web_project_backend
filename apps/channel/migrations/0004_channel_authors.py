# Generated by Django 3.0.2 on 2020-01-29 13:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel', '0003_channel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to=settings.AUTH_USER_MODEL),
        ),
    ]
