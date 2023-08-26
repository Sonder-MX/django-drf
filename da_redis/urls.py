from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RedisBooksViewSet

name = "da_redis"
router = DefaultRouter()

router.register(r"rbooks", RedisBooksViewSet, basename="rbooks")

urlpatterns = [
    path("", include(router.urls)),
]
