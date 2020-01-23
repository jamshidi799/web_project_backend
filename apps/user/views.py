from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response

from apps.user.serializers import ProfileSerializer, UserSerializer, ProfileSmallSerializer, UserSmallSerializer
from .models import Profile


class ProfileView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        user = self.get_queryset().get(user__username=username)
        data = self.get_serializer(user).data
        return Response(data=data, status=HTTP_200_OK)


class ProfileSmallList(GenericAPIView):
    serializer_class = ProfileSmallSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        serializer = ProfileSmallSerializer(self.get_queryset(), many=True)
        return Response(data=serializer.data)
