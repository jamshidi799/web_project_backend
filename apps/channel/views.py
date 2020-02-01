from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.channel.models import Channel
from apps.channel.serializers import ChannelSerializer, ChannelSmallSerializer


class ChannelList(GenericAPIView):
    serializer_class = ChannelSerializer

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Channel.objects.all()

    def get(self, request, format=None):
        channels = self.get_queryset()
        serializer = ChannelSmallSerializer(channels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChannelDetail(GenericAPIView):
    serializer_class = ChannelSerializer

    def get_object(self, pk):
        try:
            return Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        channel = self.get_object(pk)
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChannelAuthorsView(GenericAPIView):
    serializer_class = ChannelSerializer

    def get_object(self, pk):
        try:
            return Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            raise Http404

    def post(self, request, pk, author_id):
        channel = self.get_object(pk)
        channel.authors.add(author_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, author_id):
        channel = self.get_object(pk)
        channel.authors.remove(author_id)
        return Response(status=status.HTTP_204_NO_CONTENT)