from rest_framework import serializers

from .models import RedisBooks


class RedisBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedisBooks
        fields = "__all__"
