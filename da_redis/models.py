from django.db import models

BOOK_CACHE_KEY = "book_list"


class RedisBooks(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="书名")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版日期", null=True, blank=True)
    publish = models.CharField(max_length=32, verbose_name="出版社")

    class Meta:
        db_table = "redis_books"
        verbose_name = "Redis - 图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
