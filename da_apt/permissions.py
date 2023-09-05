# -*- coding: utf-8 -*-
"""
@Date    : 2023/08/31 09:38:20
@Author  : Sonder-MX
@File    : permissions.py
@Description: 自定义权限类
"""
from rest_framework import permissions
from rest_framework.request import Request


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    自定义权限类
    只允许超级用户进行增删改操作
    """

    def has_permission(self, request: Request, view):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """
        是否有权限操作对象
        :param view: 当前视图
        :param obj: 当前模型对象
        """
        return True
