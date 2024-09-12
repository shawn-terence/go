from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import SignUpView, LoginView, ProfileViewSet, OrganizationViewSet
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('profiles/<int:pk>/', ProfileViewSet.as_view(), name='profile_detail'),
    # path('organizations/<int:pk>/', OrganizationViewSet.as_view(), name='organization_detail'),
    # path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]