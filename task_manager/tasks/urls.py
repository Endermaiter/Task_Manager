from rest_framework.routers import DefaultRouter
from .views import TareaViewSet, FamiliaViewSet

router = DefaultRouter()
router.register(r'tasks', TareaViewSet)
router.register(r'families', FamiliaViewSet)

urlpatterns = router.urls