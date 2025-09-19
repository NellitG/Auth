from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response as response
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from .models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            return response({"message": "Login successful", "user": UserSerializer(user).data})
        return response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)