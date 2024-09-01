from django.db import models
from django.conf import settings
from django.utils import timezone

class Webinar(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.CharField(max_length=255)
    date = models.DateTimeField()
    duration = models.DurationField(help_text="Duration of the webinar")
    is_recorded = models.BooleanField(default=False)
    recorded_file = models.FileField(upload_to='webinars/recordings/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Webinar: {self.title} by {self.speaker} on {self.date}"

class WebinarRegistration(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='webinar_registrations')
    registered_at = models.DateTimeField(default=timezone.now)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"Registration for {self.webinar.title} by {self.user.username}"

class WebinarFeedback(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=3)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.user.username} for {self.webinar.title}"