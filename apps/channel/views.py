from django.shortcuts import render
from rest_framework import viewsets
from apps.channel.models import Channel
from apps.channel.serializers import ChannelSerializer


class ChannelView(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    # permission class ----------

    
