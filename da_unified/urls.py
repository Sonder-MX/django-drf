from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet

name = "da_unified"
router = DefaultRouter()

router.register(r"persons", PersonViewSet, basename="persons")

urlpatterns = [
    path("", include(router.urls)),
]
