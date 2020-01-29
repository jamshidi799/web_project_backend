# Generated by Django 3.0.2 on 2020-01-29 11:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='DisLike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
