from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenRefreshSerializer)


class DaTokenSerializer(TokenObtainPairSerializer):
    """自定义获取token序列化器"""

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)  # 获取Token对象
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        return token


class DaRefreshTokenSerializer(TokenRefreshSerializer):
    """自定义刷新token序列化器"""

    def validate(self, attrs):
        data = super(DaRefreshTokenSerializer, self).validate(attrs)
        return data
