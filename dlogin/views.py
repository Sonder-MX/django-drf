from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserListSerializer, UserRefisterSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserListSerializer
        return UserRefisterSerializer
