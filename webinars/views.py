from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Webinar, WebinarRegistration, WebinarFeedback
from .serializers import WebinarSerializer, WebinarRegistrationSerializer, WebinarFeedbackSerializer
from notifications.models import Notification

class WebinarListCreateView(generics.ListCreateAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [IsAuthenticated]

class WebinarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [IsAuthenticated]

class WebinarRegistrationCreateView(generics.CreateAPIView):
    queryset = WebinarRegistration.objects.all()
    serializer_class = WebinarRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        registration = serializer.save(user=self.request.user)
        # Notify the user
        Notification.objects.create(
            user=self.request.user,
            notification_type='reminder',
            message=f"You have successfully registered for the webinar: {registration.webinar.title}.",
        )

class WebinarFeedbackCreateView(generics.CreateAPIView):
    queryset = WebinarFeedback.objects.all()
    serializer_class = WebinarFeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WebinarFeedbackListView(generics.ListAPIView):
    serializer_class = WebinarFeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        webinar_id = self.request.query_params.get('webinar_id')
        return WebinarFeedback.objects.filter(webinar_id=webinar_id)