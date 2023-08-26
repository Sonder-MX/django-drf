from rest_framework import viewsets

from .filters import PersonFilter
from .models import Person
from .paginations import PersonPagination
from .serializers import PersonDetailSerializer, PersonSerializer


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_class = PersonFilter  # 过滤
    pagination_class = PersonPagination  # 分页

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PersonDetailSerializer
        return super().get_serializer_class()
