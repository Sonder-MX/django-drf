from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from .models import DaUser
from .serializers import UserListSerializer, UserRegisterSerializer


class UserListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DaUser.objects.all()
    serializer_class = UserListSerializer


class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    # 注册时检查用户邮箱是否存在
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if DaUser.objects.filter(email=email).exists():
            return Response({'message': "该邮箱已被注册！"}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)
