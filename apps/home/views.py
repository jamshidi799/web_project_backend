from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.post.models import Post, Comment
from apps.post.serializers import PostSerializer


class TrendPosts(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        return Post.objects.all()

    def get(self, request, format=None):
        posts = Post.objects.all().filter(title="post2")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class SubPosts(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        return Post.objects.all()

    def get(self, request, format=None):
        posts = Post.objects.all().filter(title="post1")
        # posts = Post.objects.filter(owner=self.request.user.id)
        # posts2 = Comment.objects.filter(owner='auth.User')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class FollowedPosts(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        return Post.objects.all()

    def get(self, request, format=None):
        posts = Post.objects.all().filter(title="third post")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LatestPosts(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        return Post.objects.all()

    def get(self, request, format=None):
        posts = Post.objects.all().filter(title="post2")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
