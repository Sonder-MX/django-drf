from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AptBooksViewSet

router = DefaultRouter()
router.register(r"aptbooks", AptBooksViewSet, basename="aptbooks")

name = "da_apt"
urlpatterns = [
    path("", include(router.urls)),
]
