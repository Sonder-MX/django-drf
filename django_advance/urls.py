"""django_advance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from da_token.views import DaTokenObtainPairView, DaTokenRefreshView
from da_user import views as user_views

router = DefaultRouter()
router.register(r"user_list", user_views.UserListViewSet, basename="user_list")
router.register(r"user", user_views.UserViewSet, basename="user")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", DaTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", DaTokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    # frontend
    path("ft-user/", include("frontend.urls"), name="frontend"),
    # 过滤、排序、分页
    path("fop/", include("da_fop.urls"), name="fop"),
    # redis books
    path("rds/", include("da_redis.urls"), name="rds"),
    # 认证、鉴权、限流
    path("apt/", include("da_apt.urls"), name="apt"),
    # 统一接口
    path("unified/", include("da_unified.urls"), name="unified"),
    # websocket
    path("chat/", include("da_chat.urls"), name="chat"),
]
