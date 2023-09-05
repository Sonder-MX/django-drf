# -*- coding: utf-8 -*-
"""
@Date    : 2023/08/31 09:38:39
@Author  : Sonder-MX
@File    : authentications.py
@Description: 自定义认证类
"""
from rest_framework.authentication import BaseAuthentication


class MyAuthentication(BaseAuthentication):
    """
    自定义认证类
    """

    def authenticate(self, request):
        """
        这个方法必须被重写，用于认证用户
        """
        pass

    def authenticate_header(self, request):
        """
        如果返回None，表示使用默认的认证头
        """
        pass
