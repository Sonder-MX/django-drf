from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **kwargs)


class DaUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="邮箱地址", max_length=60, unique=True)
    username = models.CharField(verbose_name="用户昵称", max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name="注册时间", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    last_login = False

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username if self.username else self.email

    class Meta:
        db_table = "da_user"
        verbose_name = '用户'
        verbose_name_plural = verbose_name
