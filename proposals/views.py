from rest_framework import generics
from .models import ProjectProposal, Template
from .serializers import ProjectProposalSerializer, TemplateSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics
# from .models import ProjectProposal, Notification
# from notifications.tasks import send_email_notification
# from .serializers import ProjectProposalSerializer

class ProposalListCreateView(generics.ListCreateAPIView):
    queryset = ProjectProposal.objects.all()
    serializer_class = ProjectProposalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProjectProposal.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class ProposalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectProposal.objects.all()
    serializer_class = ProjectProposalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProjectProposal.objects.filter(client=self.request.user)

class TemplateListView(generics.ListAPIView)
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsAuthenticated]

class TemplateDetailView(generics.RetrieveAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [IsAuthenticated]



# class ProposalSubmissionView(generics.CreateAPIView):
#     queryset = ProjectProposal.objects.all()
#     serializer_class = ProjectProposalSerializer

#     def perform_create(self, serializer):
#         proposal = serializer.save(client=self.request.user)
        
#         # Create a notification for the user
#         notification = Notification.objects.create(
#             user=proposal.client,
#             notification_type='message',
#             message=f"Your proposal '{proposal.title}' has been successfully submitted.",
#         )

#         # Optionally send an email notification
#         send_email_notification.delay(notification.id)