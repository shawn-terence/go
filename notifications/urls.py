from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notification_list'),
    path('create/', views.NotificationCreateView.as_view(), name='notification_create'),
    path('<int:pk>/mark-as-read/', views.NotificationMarkAsReadView.as_view(), name='notification_mark_as_read'),
    path('role-based/create/', views.RoleBasedNotificationCreateView.as_view(), name='role_based_notification_create'),
]