from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"persons", views.PersonViewSet, basename="persons")

name = "da_fop"
urlpatterns = [
    path("", include(router.urls)),
]
