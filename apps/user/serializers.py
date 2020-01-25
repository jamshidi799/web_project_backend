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

    def validate(self, data):
        return data


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'bio']

    def validate(self, data):
        return data

    def update(self, instance, validated_data):
        user = instance.user
        user_validated_data = validated_data.pop('user')
        user.username = user_validated_data.get('username', user.username)
        user.email = user_validated_data.get('email', user.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        user.save()
        return instance


class ProfileSmallSerializer(serializers.ModelSerializer):
    user = UserSmallSerializer()

    class Meta:
        model = Profile
        fields = ['bio']
