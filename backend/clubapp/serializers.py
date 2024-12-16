from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PlayerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PlayerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PlayerProfile
        fields = ['user', 'bio', 'age', 'team', 'position', 'profile_pic']
