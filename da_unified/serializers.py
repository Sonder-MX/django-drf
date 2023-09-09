from da_fop.models import Person
from django.utils import timezone
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    """Person list/retrieve 序列化器"""

    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = ("id", "created")


class PersonCUDSerializer(serializers.ModelSerializer):
    """Person create/update/delete 序列化器"""

    class Meta:
        model = Person
        fields = ["name", "gender", "age", "birthday"]
        extra_kwargs = {
            "age": {"read_only": True},
            "birthday": {"read_only": True},
        }

    def create(self, validated_data):
        birthday = timezone.now().date() - timezone.timedelta(days=365 * 20)
        validated_data["birthday"] = birthday
        validated_data["age"] = 20
        return super().create(validated_data)
