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
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = DaUser
        fields = ['username', 'old_password', 'new_password']

    # 检查旧密码是否正确
    def validate_old_password(self, value):
        instance = self.instance
        if not instance:
            raise serializers.ValidationError("用户不存在！")
        if not instance.check_password(value):
            raise serializers.ValidationError("原密码不正确！请重新输入！")
        return value

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('new_password'))
        instance.save()
        return instance
