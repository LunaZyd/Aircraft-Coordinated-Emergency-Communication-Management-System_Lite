# from rest_framework.routers import SimpleRouter
# from django.urls import path
# from .views import FormdataModelViewSet
#
# router = SimpleRouter()
# router.register("api/satellite001", FormdataModelViewSet)
#
# urlpatterns = [
# ]
# urlpatterns += router.urls
#

from django.urls import path
from .views import SatelliteDataViewSet

urlpatterns = [
    path('api/satellite001/', SatelliteDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='satellite001-list'),
    path('api/satellite001/<int:pk>/', SatelliteDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='satellite001-detail'),
]