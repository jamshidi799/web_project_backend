from rest_framework import serializers

from .models import Post, Comment
from apps.user.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'content', 'date', 'post')


class PostSerializer(serializers.ModelSerializer):
    # owner = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'owner', 'channel', 'title', 'content', 'image',
                  'date')
