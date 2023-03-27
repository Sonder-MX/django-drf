from time import time

from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenRefreshSerializer)
from rest_framework_simplejwt.settings import api_settings


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['expired'] = api_settings.ACCESS_TOKEN_LIFETIME.total_seconds() + int(time())
        data['refresh_expired'] = api_settings.REFRESH_TOKEN_LIFETIME.total_seconds() + int(time())
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['expired'] = api_settings.ACCESS_TOKEN_LIFETIME.total_seconds() + int(time())
        return data
