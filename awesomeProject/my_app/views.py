from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User  #import models
from .serializers import RegistrationSerializer, LoginSerializer  #import serializers

# impot any packages
import six # Python 2 and 3 compatibility library package

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Access the validated data from the serializer
            username = six.b(serializer.validated_data['username']) 
            password = six.b(serializer.validated_data['password'])  

            user = User(username=username, password=password)
            user.save()

            return Response({"message": "user registered successfully"}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = six.b(serializer.validated_data['username']) 
            password = six.b(serializer.validated_data['password'])  

            try:
                user = User.objects.get(username=username)  
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"username": username})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        