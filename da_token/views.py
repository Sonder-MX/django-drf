from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .serializers import DaRefreshTokenSerializer, DaTokenSerializer


class DaTokenObtainPairView(TokenObtainPairView):
    serializer_class = DaTokenSerializer


class DaTokenRefreshView(TokenRefreshView):
    serializer_class = DaRefreshTokenSerializer
