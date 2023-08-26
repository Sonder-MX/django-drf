from django.db import models


class Person(models.Model):
    GENDER_CHOICES = (
        (0, "女"),
        (1, "男"),
    )

    name = models.CharField(max_length=20, verbose_name="姓名")
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    birthday = models.DateField(verbose_name="生日")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "fop_person"
        verbose_name = "人员信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
