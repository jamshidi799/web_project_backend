from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from knox.models import AuthToken

from apps.user.serializers import ProfileSerializer, UserSerializer, RegisterSerializer, LoginSerializer, ConnectionSerializer
from .models import Profile, Connection
from apps.notification.models import Notification


# Register API
class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":
            UserSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user":
            UserSerializer(user, context=self.get_serializer_context()).data,
            "token":
            AuthToken.objects.create(user)[1]
        })


# Get User API
class UserAPI(RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileDetail(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(self.get_queryset(), username=username)
        data = self.get_serializer(user).data
        return Response(data=data)

    def put(self, request, username):
        user = get_object_or_404(self.get_queryset(), username=username)
        user_serializer = UserSerializer(user)
        user_serializer.update(instance=request.user,
                               validated_data=request.data)
        return Response(user_serializer.data)


class ProfileList(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnectionList(GenericAPIView):
    serializer_class = ConnectionSerializer
    queryset = Connection.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            target = User.objects.get(id=request.data['following'])
            notification = Notification(kind="follow",
                                        creator=request.user.username,
                                        target=target)
            notification.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnectionDetail(GenericAPIView):
    serializer_class = ConnectionSerializer
    queryset = Connection.objects.all()

    def delete(self, request, creator, following, format=None):
        connection = self.get_queryset().get(creator=creator,
                                             following=following)
        connection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)