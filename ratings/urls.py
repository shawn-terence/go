from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [
    path('create/', views.RatingCreateView.as_view(), name='rating_create'),
    path('', views.RatingListView.as_view(), name='rating_list'),
    path('average/', views.AverageRatingDetailView.as_view(), name='average_rating_detail'),
]