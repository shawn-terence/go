from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rating, AverageRating
from .serializers import RatingSerializer, AverageRatingSerializer
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(self.request.data['content_type'])
        object_id = self.request.data['object_id']
        rating = serializer.save(user=self.request.user, content_type=content_type, object_id=object_id)
        
        # Notify the user being rated (e.g., expert)
        if content_type.model == 'expert':
            expert = content_type.get_object_for_this_type(id=object_id)
            Notification.objects.create(
                user=expert.user,
                notification_type='message',
                message=f"You have received a new rating: {rating.rating} stars.",
            )

        # Update or create the average rating
        average_rating, created = AverageRating.objects.get_or_create(
            content_type=content_type,
            object_id=object_id,
        )
        average_rating.update_average(rating.rating)

class RatingListView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        content_type = ContentType.objects.get_for_model(self.request.query_params.get('content_type'))
        object_id = self.request.query_params.get('object_id')
        return Rating.objects.filter(content_type=content_type, object_id=object_id)

class AverageRatingDetailView(generics.RetrieveAPIView):
    queryset = AverageRating.objects.all()
    serializer_class = AverageRatingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        content_type = ContentType.objects.get_for_model(self.request.query_params.get('content_type'))
        object_id = self.request.query_params.get('object_id')
        return AverageRating.objects.get(content_type=content_type, object_id=object_id)