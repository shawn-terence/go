from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FundingOpportunity, UserPreference, Recommendation
from .serializers import FundingOpportunitySerializer, UserPreferenceSerializer, RecommendationSerializer
from notifications.models import Notification

class FundingOpportunityListView(generics.ListAPIView):
    queryset = FundingOpportunity.objects.all()
    serializer_class = FundingOpportunitySerializer
    permission_classes = [IsAuthenticated]

class UserPreferenceDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return UserPreference.objects.get(user=self.request.user)

class RecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Recommendation.objects.filter(user=self.request.user).order_by('-recommended_at')

class RecommendationMarkAsViewedView(generics.UpdateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        recommendation = self.get_object()
        recommendation.mark_as_viewed()
        return Response({"status": "Recommendation marked as viewed"})



def generate_recommendations():
    users = UserPreference.objects.all()
    for user_pref in users:
        opportunities = FundingOpportunity.objects.filter(
            sector=user_pref.preferred_sector,
            region=user_pref.preferred_region,
            deadline__gt=timezone.now()
        )
        for opportunity in opportunities:
            if not Recommendation.objects.filter(user=user_pref.user, funding_opportunity=opportunity).exists():
                recommendation = Recommendation.objects.create(
                    user=user_pref.user,
                    funding_opportunity=opportunity,
                )
                Notification.objects.create(
                    user=user_pref.user,
                    notification_type='alert',
                    message=f"New funding opportunity recommended: {opportunity.title}",
                )