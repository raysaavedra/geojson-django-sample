from rest_framework.routers import DefaultRouter

from .api import ProviderViewSet


router = DefaultRouter()
router.register(r"providers", ProviderViewSet, basename="provider")
urlpatterns = router.urls
