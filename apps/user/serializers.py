from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile


class UserSmallSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length)

    class Meta:
        model = User
        fields = ['username']


class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'bio']


class ProfileSmallSerializer(serializers.ModelSerializer):
    user = UserSmallSerializer()

    class Meta:
        model = Profile
        fields = ['bio']
