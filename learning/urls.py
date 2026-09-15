
from rest_framework.routers import DefaultRouter

from learning.views import StudyMaterialViewSet

router = DefaultRouter()

router.register('materials', StudyMaterialViewSet, 'study-materials')

urlpatterns = router.urls