from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from da_redis.models import RedisBooks

from .authentications import MyAuthentication
from .permissions import IsSuperUserOrReadOnly
from .serializers import AptBooksSerializer


class AptBooksViewSet(viewsets.ModelViewSet):
    queryset = RedisBooks.objects.all()
    serializer_class = AptBooksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [MyAuthentication]  # 演示自定义认证类，实际使用JWTAuthentication认证类

    def get_permissions(self):
        if self.action == "destory":  # 如果请求为delete，需要管理员权限
            return [IsSuperUserOrReadOnly()]
        if self.action in ["create", "update", "partial_update"]:  # 如果请求为post、put、patch，需要登录
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_authenticators(self):
        # return super().get_authenticators()
        return [JWTAuthentication()]  # 只使用JWTAuthentication认证类
