from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from user.models import CustomUser
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
class RegisterView(APIView):
    permission_classes = []
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)  # Hash the password
        user.save()

        return Response({"username": user.username, "email": user.email}, status=status.HTTP_201_CREATED)
class LoginView(APIView):
    permission_classes = [AllowAny]  
    authentication_classes = [BasicAuthentication]  

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Debugging output

        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)

        print("Authentication failed.")
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
