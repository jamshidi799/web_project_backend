from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

# from apps.post.serializers import PostSerializer, PostSmallSerializer
from .models import Profile, Connection


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Profile
        exclude = ['user', 'id']

    def validate(self, data):
        return data


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['following', 'creator']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    creator = ConnectionSerializer(many=True)
    following = ConnectionSerializer(many=True)

    # posts = PostSmallSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'creator', 'following']

    def validate(self, data):
        return data

    def update(self, instance, validated_data):
        instance.save()
        profile = instance.profile
        Profile.bio = validated_data.get('profile.bio', profile.bio)
        # user.email = user_validated_data.get('email', user.email)
        # instance.bio = validated_data.get('bio', instance.bio)
        profile.save()
        return instance


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        post = Post.objects.create(validated_data['owner'],
                                   validated_data['content'],
                                   validated_data['title'])
        # Profile.objects.create(user=user, bio=validated_data['profile']['bio'])
        return post


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
