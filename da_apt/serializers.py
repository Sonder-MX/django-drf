# -*- coding: utf-8 -*-
"""
@Date    : 2023/08/31 08:36:33
@Author  : Sonder-MX
@File    : serializers.py
@Remark  : 使用 da_redis/models.py 中的 RedisBooks 模型类
"""
from rest_framework import serializers

from da_redis.models import RedisBooks


class AptBooksSerializer(serializers.ModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = RedisBooks
        fields = "__all__"
