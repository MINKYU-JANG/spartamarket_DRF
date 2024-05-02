from rest_framework import serializers
from .models import CustomUser


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'nickname',
                  'birthday', 'gender', 'introduction']
