from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Comment
from apps.user.serializers import UserSerializer


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'owner', 'content', 'date', 'like', 'dislike')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    # reply_to = CommentReplySerializer()

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'post', 'content', 'date', 'reply_to', 'like',
                  'dislike')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'owner', 'channel', 'title', 'content', 'image',
                  'comments', 'date', 'like')


class PostSmallSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'owner', 'channel', 'title', 'image', 'like', 'date')
