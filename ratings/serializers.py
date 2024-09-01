from rest_framework import serializers
from .models import Rating, AverageRating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class AverageRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AverageRating
        fields = '__all__'