from django.urls import path
from . import views

app_name = 'partnerships'

urlpatterns = [
    path('', views.PartnershipListView.as_view(), name='partnership_list'),
    path('request/', views.PartnershipRequestCreateView.as_view(), name='partnership_request_create'),
    path('request/<int:pk>/approve/', views.PartnershipRequestApproveView.as_view(), name='partnership_request_approve'),
    path('request/<int:pk>/decline/', views.PartnershipRequestDeclineView.as_view(), name='partnership_request_decline'),
]