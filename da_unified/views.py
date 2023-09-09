from da_fop.models import Person
from rest_framework import viewsets

from .serializers import PersonCUDSerializer, PersonSerializer
from .utils import CustomJSONRenderer


class PersonViewSet(viewsets.ModelViewSet):
    """Person list/retrieve/create/update/delete 视图集"""

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    renderer_classes = [CustomJSONRenderer]

    def get_serializer_class(self):
        """动态选择序列化器"""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return PersonCUDSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            return self.queryset[:10]
        return self.queryset
