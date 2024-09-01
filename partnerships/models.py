from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import Organization

class Partnership(models.Model):
    PARTNERSHIP_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='initiated_partnerships')
    partner_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='received_partnerships')
    status = models.CharField(max_length=10, choices=PARTNERSHIP_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def approve(self):
        self.status = 'active'
        self.approved_at = timezone.now()
        self.save()

    def cancel(self):
        self.status = 'cancelled'
        self.save()

    def complete(self):
        self.status = 'completed'
        self.save()

    def __str__(self):
        return f"Partnership between {self.organization} and {self.partner_organization} - {self.status}"

class PartnershipRequest(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='sent_requests')
    partner_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='received_requests')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    responded_at = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def approve(self):
        self.is_approved = True
        self.responded_at = timezone.now()
        self.save()
        Partnership.objects.create(
            organization=self.organization,
            partner_organization=self.partner_organization,
            status='active'
        )

    def decline(self):
        self.is_approved = False
        self.responded_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Partnership request from {self.organization} to {self.partner_organization}"