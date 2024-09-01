from django.db import models
from users.models import User


class Template(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, help_text="Category like Health, Education, Technology, etc.")
    preview = models.FileField(upload_to='templates/previews/')
    file = models.FileField(upload_to='templates/files/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class ProjectProposal(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposals')
    title = models.CharField(max_length=255)
    sector = models.CharField(max_length=100, help_text="Sector like Health, Education, Technology, etc.")
    background = models.TextField()
    methodology = models.TextField()
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.client.username})'