from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    rating = models.IntegerField(choices=RATING_CHOICES)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating {self.rating} for {self.content_object} by {self.user.username}"

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')


class AverageRating(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    average_rating = models.FloatField(default=0)
    rating_count = models.PositiveIntegerField(default=0)

    def update_average(self, new_rating):
        total_score = self.average_rating * self.rating_count
        self.rating_count += 1
        self.average_rating = (total_score + new_rating) / self.rating_count
        self.save()

    def __str__(self):
        return f"Average Rating for {self.content_object}: {self.average_rating} based on {self.rating_count} ratings"

