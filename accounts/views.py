from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import AccountSerializer
from .serializers import UserProfileSerializer
from .models import CustomUser


class UserSignupAPIView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            if CustomUser.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenObtainPairSerializer(
                data={"refresh": str(refresh), "access": str(refresh.access_token)})
            serializer.is_valid()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
