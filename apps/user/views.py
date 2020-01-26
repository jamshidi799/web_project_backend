from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from apps.user.serializers import ProfileSerializer, UserSerializer, ProfileSmallSerializer, UserSmallSerializer
from .models import Profile


class ProfileDetail(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(self.get_queryset(), user__username=username)
        data = self.get_serializer(user).data
        return Response(data=data)

    def put(self, request, username):
        profile = get_object_or_404(self.get_queryset(),
                                    user__username=username)
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(GenericAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
