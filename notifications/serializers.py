from rest_framework import serializers
from .models import Notification, RoleBasedNotification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class RoleBasedNotificationSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()

    class Meta:
        model = RoleBasedNotification
        fields = '__all__'