from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
admin.autodiscover()
from . models import User 
from rest_framework import  serializers

from rest_framework.validators import ValidationError

#serializer for creating of user account
class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        

        return user
class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username','is_active']
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customize token to add user name
    in encoding.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

