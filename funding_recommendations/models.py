from django.db import models
from django.conf import settings
from django.utils import timezone

class FundingOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sector = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    link = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class UserPreference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='preferences')
    preferred_sector = models.CharField(max_length=100, blank=True, null=True)
    preferred_region = models.CharField(max_length=100, blank=True, null=True)
    notify_by_email = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommendations')
    funding_opportunity = models.ForeignKey(FundingOpportunity, on_delete=models.CASCADE, related_name='recommendations')
    recommended_at = models.DateTimeField(default=timezone.now)
    is_viewed = models.BooleanField(default=False)

    def mark_as_viewed(self):
        self.is_viewed = True
        self.save()

    def __str__(self):
        return f"Recommendation for {self.user.username} - {self.funding_opportunity.title}"