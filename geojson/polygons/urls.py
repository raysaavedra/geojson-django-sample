from rest_framework.routers import DefaultRouter

from .api import PolygonViewSet


router = DefaultRouter()
router.register(r"polygons", PolygonViewSet, basename="polygon")
urlpatterns = router.urls
