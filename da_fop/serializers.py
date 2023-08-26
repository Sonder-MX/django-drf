from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")

    class Meta:
        model = Person
        exclude = ("id", "created")


class PersonDetailSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")

    class Meta:
        model = Person
        fields = "__all__"
