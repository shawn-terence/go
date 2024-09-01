from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'experts', views.ExpertViewSet)
router.register(r'retired-experts', views.RetiredExpertViewSet)

urlpatterns = router.urls