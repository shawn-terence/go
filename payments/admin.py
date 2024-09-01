from django.contrib import admin
from .models import MpesaPayment, PaypalPayment, BankPayment, Invoice

# admin.site.register(MpesaPayment)
# admin.site.register(PaypalPayment)
# admin.site.register(BankPayment)
# admin.site.register(Invoice)

@admin.register(MpesaPayment)
class MpesaPaymentAdmin(admin.ModelAdmin):
    list_display = ('mpesa_transaction_id', 'user', 'amount', 'status', 'created_at')
    search_fields = ('mpesa_transaction_id', 'user__username')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(PaypalPayment)
class PaypalPaymentAdmin(admin.ModelAdmin):
    list_display = ('paypal_transaction_id', 'user', 'amount', 'status', 'created_at')
    search_fields = ('paypal_transaction_id', 'user__username')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(BankPayment)
class BankPaymentAdmin(admin.ModelAdmin):
    list_display = ('bank_transaction_id', 'user', 'amount', 'status', 'created_at')
    search_fields = ('bank_transaction_id', 'user__username')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_method', 'payment_status', 'created_at')
    search_fields = ('user__username', 'payment_method')
    list_filter = ('payment_method', 'payment_status', 'created_at')
    ordering = ('-created_at',)