from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('mpesa/', views.MpesaPaymentCreateView.as_view(), name='mpesa_payment'),
    path('paypal/', views.PaypalPaymentCreateView.as_view(), name='paypal_payment'),
    path('bank/', views.BankPaymentCreateView.as_view(), name='bank_payment'),
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
]