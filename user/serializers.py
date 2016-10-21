from rest_framework import serializers

from captcha.constants import ALINK_VERIFY_CODE_LENGTH
from .models import User


# User Auth
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'id', 'is_staff')


class UserSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar')


class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)


class UserLinkActivateSerializer(serializers.Serializer):
    captcha = serializers.CharField(max_length=ALINK_VERIFY_CODE_LENGTH)
