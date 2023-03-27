from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):

    identity = serializers.SerializerMethodField()

    def get_identity(self, obj):
        if not obj.is_superuser and not obj.is_staff:
            return 0
        return 2 if obj.is_superuser else 1

    class Meta:
        model = User
        fields = ['id', 'username', 'identity']


class UserRefisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'is_superuser': {
                'read_only': True
            },
            'is_staff': {
                'read_only': True
            },
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            pwd = validated_data.pop('password')
            instance.set_password(pwd)
        return super().update(instance, validated_data)
