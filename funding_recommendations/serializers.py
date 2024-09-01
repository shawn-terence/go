from rest_framework import serializers
from .models import FundingOpportunity, UserPreference, Recommendation

class FundingOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingOpportunity
        fields = '__all__'

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    funding_opportunity = FundingOpportunitySerializer()

    class Meta:
        model = Recommendation
        fields = '__all__'