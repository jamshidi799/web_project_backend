from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Profile
        exclude = ['user']

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


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

    def validate(self, data):
        return data


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])

        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
