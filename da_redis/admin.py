from django.contrib import admin
from django_redis import get_redis_connection

from .models import BOOK_CACHE_KEY, RedisBooks


@admin.register(RedisBooks)
class RedisBooksAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "pub_date")
    search_fields = ("name",)

    # 以下三个方法在管理员进行增删改操作时，会自动清除缓存，以保证数据的一致性
    # 若客户端也需要增删改操作，将以下三个方法注释，在model中重写save和delete方法，手动清除缓存
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        conn = get_redis_connection("default")
        conn.delete(":1:" + BOOK_CACHE_KEY)

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        conn = get_redis_connection("default")
        conn.delete(":1:" + BOOK_CACHE_KEY)

    def delete_queryset(self, request, queryset):
        super().delete_queryset(request, queryset)
        conn = get_redis_connection("default")
        conn.delete(":1:" + BOOK_CACHE_KEY)
