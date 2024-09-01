from django.db import models
from django.conf import settings
from django.utils import timezone

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class MpesaPayment(Payment):
    mpesa_transaction_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"MPESA Payment - {self.mpesa_transaction_id}"

class PaypalPayment(Payment):
    paypal_transaction_id = models.CharField(max_length=100, unique=True)
    paypal_email = models.EmailField()

    def __str__(self):
        return f"PayPal Payment - {self.paypal_transaction_id}"

class BankPayment(Payment):
    bank_transaction_id = models.CharField(max_length=100, unique=True)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Bank Payment - {self.bank_transaction_id}"

class Invoice(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('mpesa', 'MPESA'),
        ('paypal', 'PayPal'),
        ('bank', 'Bank Transfer'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invoices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=10, choices=Payment.PAYMENT_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invoice - {self.id} - {self.payment_status}"

    def mark_as_paid(self):
        self.payment_status = 'completed'
        self.paid_at = timezone.now()
        self.save()