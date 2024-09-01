from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'proposals', views.ProjectProposalViewSet)
router.register(r'templates', views.TemplateViewSet)

urlpatterns = router.urls