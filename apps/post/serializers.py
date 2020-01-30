from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Comment
from apps.user.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    reply_to = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), allow_null=True)

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'content', 'date', 'post', 'reply_to', 'like')


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'owner', 'channel', 'title', 'content', 'image',
                  'date', 'like')


class PostSmallSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'owner', 'channel', 'title', 'image')
