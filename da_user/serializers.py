from rest_framework import serializers

from .models import DaUser


class UserListSerializer(serializers.ModelSerializer):
    """用户列表序列化器"""

    class Meta:
        model = DaUser
        fields = ('id', 'username', 'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    password = serializers.CharField(write_only=True, help_text='密码')

    class Meta:
        model = DaUser
        fields = ['email', 'password']

    # 验证
    # def validate(self, attrs):
    #     return attrs

    # 保存
    def create(self, validated_data):
        return DaUser.objects.create_user(**validated_data)
