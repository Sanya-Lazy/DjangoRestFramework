from rest_framework import serializers
from .models import User # import required models

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    # example for password
    # password = serializers.CharField(write_only=True)

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # Define the fields for login

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
