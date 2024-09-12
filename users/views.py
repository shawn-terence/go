from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from .models import User, Profile, Organization
from .serializers import SignUpSerializer, ProfileSerializer, OrganizationSerializer
from .tokens import create_jwt_pair_for_user
from .permissions import IsProfileOwnerOrAdmin, IsAdmin

# Sign-up view
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "User Created Successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login view (JWT Authentication)
class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login Successful", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)


# Profile view
class ProfileViewSet(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)


# Organization view
class OrganizationViewSet(generics.RetrieveUpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Organization.objects.all()
        return Organization.objects.filter(user=self.request.user)


# # User Registration view (Admin or Users can create accounts)
# class UserRegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegistrationSerializer

#     def perform_create(self, serializer):
#         user = serializer.save(is_active=True)
#         user.set_password(serializer.validated_data['password'])
#         user.is_active = True
#         user.save()


# JWT Token views from rest_framework_simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)