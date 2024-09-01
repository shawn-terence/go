from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'organizations', views.OrganizationViewSet)

urlpatterns = router.urls + [
    path('register/', views.UserRegistrationView.as_view(), name='user_register'),
    path('api/login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]