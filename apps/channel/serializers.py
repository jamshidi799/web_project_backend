from rest_framework import serializers
from .models import Channel
from apps.post.models import Post


class ChannelSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Post.objects.all())

    class Meta:
        model = Channel
        fields = ('id', 'owner', 'about', 'image', 'date', 'posts')
