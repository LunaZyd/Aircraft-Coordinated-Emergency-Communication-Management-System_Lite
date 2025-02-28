from django.urls import path
from .views import MapDataListCreate
from .views import get_drone_position

urlpatterns = [
    path('map-data/', MapDataListCreate.as_view(), name='map-data-list-create'),
    path('api/getDronePosition/', get_drone_position, name='get_drone_position'),

]


# from rest_framework.routers import SimpleRouter
#
# from .views import MapDataListCreate
# from .views import get_drone_position
#
# router = SimpleRouter()
# router.register("api/map-data", MapDataListCreate),
# # path('api/getDronePosition/', get_drone_position, name='get_drone_position'),
# # router.register("api/getDronePosition",get_drone_position)
#
#
# urlpatterns = [
# ]
# urlpatterns += router.urls