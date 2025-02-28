from rest_framework.routers import SimpleRouter

from .views import DroneModelViewSet

router = SimpleRouter()
router.register("api/drones", DroneModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls
