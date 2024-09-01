from rest_framework import generics, status
from rest_framework.response import Response
from .models import Notification, RoleBasedNotification
from .serializers import NotificationSerializer, RoleBasedNotificationSerializer
from rest_framework.permissions import IsAuthenticated

class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class NotificationMarkAsReadView(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.mark_as_read()
        return Response(status=status.HTTP_200_OK)

class RoleBasedNotificationCreateView(generics.CreateAPIView):
    queryset = RoleBasedNotification.objects.all()
    serializer_class = RoleBasedNotificationSerializer
    permission_classes = [IsAuthenticated]




    # def some_view(request):
    # notification = Notification.objects.create(
    #     user=request.user,
    #     notification_type='alert',
    #     message='This is an important alert!',
    # )
    # send_email_notification.delay(notification.id)