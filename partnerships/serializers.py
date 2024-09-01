from rest_framework import serializers
from .models import Partnership, PartnershipRequest

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'

class PartnershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipRequest
        fields = '__all__'