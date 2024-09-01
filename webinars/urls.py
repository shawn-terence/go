from django.urls import path
from . import views

app_name = 'webinars'

urlpatterns = [
    path('', views.WebinarListCreateView.as_view(), name='webinar_list_create'),
    path('<int:pk>/', views.WebinarDetailView.as_view(), name='webinar_detail'),
    path('<int:pk>/register/', views.WebinarRegistrationCreateView.as_view(), name='webinar_register'),
    path('feedback/', views.WebinarFeedbackCreateView.as_view(), name='webinar_feedback_create'),
    path('feedback/list/', views.WebinarFeedbackListView.as_view(), name='webinar_feedback_list'),
]