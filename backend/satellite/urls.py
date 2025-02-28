from rest_framework.routers import SimpleRouter

from .views import SatelliteModelViewSet

router = SimpleRouter()
router.register("api/satellite", SatelliteModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls
