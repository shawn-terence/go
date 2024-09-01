from rest_framework import serializers
from .models import MpesaPayment, PaypalPayment, BankPayment, Invoice

class MpesaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields = '__all__'

class PaypalPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaypalPayment
        fields = '__all__'

class BankPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankPayment
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'