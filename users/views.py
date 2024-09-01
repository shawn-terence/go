from rest_framework import viewsets, generics
from .models import User
from rest_framework.response import Response
from .models import Profile, Organization
from .serializers import ProfileSerializer, OrganizationSerializer
from .permissions import IsProfileOwnerOrAdmin, IsAdmin
from .serializers import UserRegistrationSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Organization.objects.all()
        return Organization.objects.filter(user=self.request.user)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer