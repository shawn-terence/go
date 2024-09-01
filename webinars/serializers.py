from rest_framework import serializers
from .models import Webinar, WebinarRegistration, WebinarFeedback

class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = '__all__'

class WebinarRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarRegistration
        fields = '__all__'

class WebinarFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarFeedback
        fields = '__all__'