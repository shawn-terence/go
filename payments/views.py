from rest_framework import generics
from .models import MpesaPayment, PaypalPayment, BankPayment, Invoice
from .serializers import MpesaPaymentSerializer, PaypalPaymentSerializer, BankPaymentSerializer, InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Invoice, Notification
# from notifications.tasks import send_email_notification

class MpesaPaymentCreateView(generics.CreateAPIView):
    queryset = MpesaPayment.objects.all()
    serializer_class = MpesaPaymentSerializer
    permission_classes = [IsAuthenticated]

class PaypalPaymentCreateView(generics.CreateAPIView):
    queryset = PaypalPayment.objects.all()
    serializer_class = PaypalPaymentSerializer
    permission_classes = [IsAuthenticated]

class BankPaymentCreateView(generics.CreateAPIView):
    queryset = BankPayment.objects.all()
    serializer_class = BankPaymentSerializer
    permission_classes = [IsAuthenticated]

class InvoiceListView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)



# class CompletePaymentView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Payment processing logic here
#         invoice_id = kwargs.get('invoice_id')
#         invoice = Invoice.objects.get(id=invoice_id)

#         # Assuming payment is successful
#         invoice.mark_as_paid()

#         # Create a notification for the user
#         notification = Notification.objects.create(
#             user=invoice.user,
#             notification_type='alert',
#             message=f"Your payment for Invoice #{invoice.id} has been successfully processed.",
#         )

#         # Optionally send an email notification
#         send_email_notification.delay(notification.id)

#         return Response({"message": "Payment completed successfully"}, status=status.HTTP_200_OK)