from django.db import models
from django.conf import settings
from django.utils import timezone

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('message', 'Message'),
        ('reminder', 'Reminder'),
        ('alert', 'Alert'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    read_at = models.DateTimeField(null=True, blank=True)

    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Notification for {self.user.username} - {self.notification_type}"

class RoleBasedNotification(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('expert', 'Expert'),
        ('client', 'Client'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='role_based_notifications')

    def __str__(self):
        return f"Notification for role {self.role}"