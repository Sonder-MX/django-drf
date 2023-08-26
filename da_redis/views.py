from rest_framework import viewsets
from rest_framework_extensions.cache.decorators import cache_response

from .models import BOOK_CACHE_KEY, RedisBooks
from .serializers import RedisBooksSerializer


class RedisBooksViewSet(viewsets.ReadOnlyModelViewSet):
    """
    图书列表页、详情页
    客户端视图集，只读，在查询图书列表和图书详情时，会自动缓存
    """

    queryset = RedisBooks.objects.all()
    serializer_class = RedisBooksSerializer

    @cache_response(key_func=lambda *args, **kwargs: BOOK_CACHE_KEY)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


"""
若需要缓存单条数据，可以在视图集中做以下操作：

def custom_key(view_instance, # 视图集实例
                view_method, # 视图集方法
                request, # 请求对象
                args,
                kwargs):
    key = ...... # 一些自定义操作
    return key

@cache_response(key_func=custom_key)
def retrieve(self, request, *args, **kwargs):
    return super().retrieve(request, *args, **kwargs)
"""
