from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CarViewSet
app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register('cars',
                   CarViewSet,
                   basename='cars')

urlpatterns = [
    path('', include(router_v1.urls)),
]
