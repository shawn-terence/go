from django.urls import path
from . import views

app_name = 'proposals'

urlpatterns = [
    path('proposals/', views.ProposalListCreateView.as_view(), name='proposal_list_create'),
    path('proposals/<int:pk>/', views.ProposalDetailView.as_view(), name='proposal_detail'),
    path('templates/', views.TemplateListView.as_view(), name='template_list'),
    path('templates/<int:pk>/', views.TemplateDetailView.as_view(), name='template_detail'),
]