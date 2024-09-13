from rest_framework import serializers
from .models import User, Profile, Organization
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "role",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'role']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             email=validated_data['email'],
#             role=validated_data['role']
#         )
#         return user