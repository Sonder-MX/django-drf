from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .serializers import (CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
