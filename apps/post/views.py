from apps.post.models import Post, Comment
from apps.post.serializers import PostSerializer, CommentSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostList(GenericAPIView):
    serializer_class = PostSerializer
    # queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    """
    Retrieve, update or delete a Post instance.
    """
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


class CommentList(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # def get_queryset(self):
    #     query_set = Comment.objects.filter(post=post_id)
    #     return query_set

    def get(self, request, post_id):
        queryset = self.queryset.filter(post_id=post_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentDetail(GenericAPIView):
    serializer_class = CommentSerializer

    def get_object(self, id):
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, post_id, id, format=None):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        comment = self.get_object(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
