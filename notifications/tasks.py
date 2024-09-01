from celery import shared_task
from .models import Notification

@shared_task
def send_email_notification(notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        # Logic to send email (e.g., using Django's send_mail function)
    except Notification.DoesNotExist:
        pass