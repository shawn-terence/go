from rest_framework import generics
from .models import ProjectProposal, Template
from .serializers import ProjectProposalSerializer, TemplateSerializer
from rest_framework.permissions import IsAuthenticated

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