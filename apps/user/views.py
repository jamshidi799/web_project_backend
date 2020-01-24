from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response

from apps.user.serializers import ProfileSerializer, UserSerializer, ProfileSmallSerializer, UserSmallSerializer
from .models import Profile


class ProfileDetail(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset

    def get(self, request, username):
        print(username)
        user = self.get_queryset().get(user__username=username)
        # user = User.objects.filter(username=username)
        data = self.get_serializer(user).data
        return Response(data=data)


class ProfileList(GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        serializer = ProfileSerializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)
