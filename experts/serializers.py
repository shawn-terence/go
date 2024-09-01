from rest_framework import serializers
from .models import Expert, RetiredExpert

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'

class RetiredExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetiredExpert
        fields = '__all__'