from django.db import models
from users.models import User

class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)  # e.g., Health, Education
    services_offered = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Only for active experts
    ratings = models.FloatField(default=0.0)
    reviews = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Distinguish between active and retired experts

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.specialization}'


class RetiredExpert(models.Model):
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE)
    volunteer_services = models.TextField()  # Services offered voluntarily
    years_of_experience = models.IntegerField()
    previous_positions = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Retired Expert: {self.expert.user.get_full_name()}'