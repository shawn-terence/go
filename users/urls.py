from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'organizations', views.OrganizationViewSet)

urlpatterns = router.urls