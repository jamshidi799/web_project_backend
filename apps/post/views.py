from apps.post.models import Post, Comment
from apps.post.serializers import PostSerializer, CommentSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostList(GenericAPIView):
    serializer_class = PostSerializer

    # queryset = Post.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.request.user)
        return Post.objects.all()

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(GenericAPIView):
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikePost(GenericAPIView):
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def post(self, request, pk, user_id):
        post = self.get_object(pk)
        post.like.add(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, user_id):
        post = self.get_object(pk)
        post.like.remove(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, post_id):
        queryset = self.queryset.filter(post_id=post_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, post_id, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(GenericAPIView):
    serializer_class = CommentSerializer

    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, post_id, comment_id, format=None):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_id, comment_id, format=None):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, comment_id, format=None):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLikeView(GenericAPIView):
    serializer_class = CommentSerializer

    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def post(self, request, comment_id, user_id):
        comment = self.get_object(comment_id)
        comment.like.add(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentDislikeView(GenericAPIView):
    serializer_class = CommentSerializer

    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def post(self, request, comment_id, user_id):
        comment = self.get_object(comment_id)
        comment.dislike.add(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)