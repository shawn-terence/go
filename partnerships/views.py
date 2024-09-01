from rest_framework import generics, status
from rest_framework.response import Response
from .models import Partnership, PartnershipRequest
from .serializers import PartnershipSerializer, PartnershipRequestSerializer
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification

class PartnershipListView(generics.ListAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter to only show partnerships for the user's organization
        user_organization = self.request.user.organization
        return Partnership.objects.filter(models.Q(organization=user_organization) | models.Q(partner_organization=user_organization))

class PartnershipRequestCreateView(generics.CreateAPIView):
    queryset = PartnershipRequest.objects.all()
    serializer_class = PartnershipRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        partnership_request = serializer.save(organization=self.request.user.organization)
        # Notify the recipient organization
        Notification.objects.create(
            user=partnership_request.partner_organization.user,
            notification_type='message',
            message=f"You have received a new partnership request from {self.request.user.organization.name}."
        )

class PartnershipRequestApproveView(generics.UpdateAPIView):
    queryset = PartnershipRequest.objects.all()
    serializer_class = PartnershipRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partnership_request = self.get_object()
        partnership_request.approve()
        return Response({"status": "Partnership approved"}, status=status.HTTP_200_OK)

class PartnershipRequestDeclineView(generics.UpdateAPIView):
    queryset = PartnershipRequest.objects.all()
    serializer_class = PartnershipRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partnership_request = self.get_object()
        partnership_request.decline()
        return Response({"status": "Partnership declined"}, status=status.HTTP_200_OK)