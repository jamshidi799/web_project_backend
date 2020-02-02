from apps.post.models import Post
from apps.channel.models import Channel
from django.contrib.auth.models import User
from apps.post.serializers import PostSmallSerializer
from apps.channel.serializers import ChannelSmallSerializer
from apps.user.serializers import UserSmallSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class TrendingList(GenericAPIView):
    serializer_class = PostSmallSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class LatestList(GenericAPIView):
    serializer_class = PostSmallSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        posts = Post.objects.all().order_by('date')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class SubscriptionsList(GenericAPIView):
    serializer_class = PostSmallSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        posts = Post.objects.filter(owner__following__creator=request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class LikedList(GenericAPIView):
    serializer_class = PostSmallSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        posts = request.user.liked_posts.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class SearchView(GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, key, format=None):
        posts = Post.objects.filter(title=key)
        post_serializer = PostSmallSerializer(posts, many=True)
        channels = Channel.objects.filter(name=key)
        channel_serializer = ChannelSmallSerializer(channels, many=True)
        users = User.objects.filter(username=key)
        user_serializer = UserSmallSerializer(users, many=True)
        return Response({
            'posts': post_serializer.data,
            'channels': channel_serializer.data,
            'users': user_serializer.data
        })
