from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from .models import DaUser
from .permissions import IsLogin, IsOwner
from .serializers import (UserListSerializer, UserRegisterSerializer, UserUpdateSerializer)


class UserListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DaUser.objects.all()
    serializer_class = UserListSerializer


class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    # 注册时检查用户邮箱是否存在
    def post(self, request, *args, **kwargs):
        print("检查邮箱")
        email = request.data.get('email')
        if DaUser.objects.filter(email=email).exists():
            return Response({'message': "该邮箱已被注册！"}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = DaUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsLogin, IsOwner]

    def get_permissions(self):
        if self.action == 'create':
            return []
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserRegisterSerializer
        return UserUpdateSerializer
