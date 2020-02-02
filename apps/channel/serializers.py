from rest_framework import serializers
from .models import Channel
from apps.post.models import Post
from apps.post.serializers import PostSerializer, PostSmallSerializer
from apps.user.serializers import UserSmallSerializer


class ChannelSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True)
    posts = PostSmallSerializer(many=True, read_only=True)
    authors = UserSmallSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = ('id', 'name', 'owner', 'authors', 'about', 'image', 'date',
                  'posts')


class ChannelSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name')
