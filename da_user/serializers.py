from rest_framework import serializers

from .models import DaUser


class UserListSerializer(serializers.ModelSerializer):
    """用户列表序列化器"""

    class Meta:
        model = DaUser
        fields = ('id', 'username', 'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = DaUser
        fields = ['email', 'password']

    # 在反序列化时进行检查，即在反序列化时，检查邮箱是否存在
    def to_internal_value(self, data):
        if DaUser.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({'message': "该邮箱已被注册！"})
        return super().to_internal_value(data)

    # 保存
    def create(self, validated_data):
        return DaUser.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    """用户更新序列化器"""

    class Meta:
        model = DaUser
        fields = ['username', 'email', 'password']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
