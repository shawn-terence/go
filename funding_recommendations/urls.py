from django.urls import path
from . import views

app_name = 'funding_recommendations'

urlpatterns = [
    path('opportunities/', views.FundingOpportunityListView.as_view(), name='funding_opportunity_list'),
    path('preferences/', views.UserPreferenceDetailView.as_view(), name='user_preference_detail'),
    path('recommendations/', views.RecommendationListView.as_view(), name='recommendation_list'),
    path('recommendations/<int:pk>/viewed/', views.RecommendationMarkAsViewedView.as_view(), name='recommendation_mark_as_viewed'),
]