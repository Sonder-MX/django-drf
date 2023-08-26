# Django + DRF 简单示例

1. 创建 python 虚拟环境
   在项目根目录打开终端运行 `python -m venv pyweb`
2. 启动虚拟环境
   - CMD ：`./pyweb/Scripts/activate`
   - PowerShell ：`./pyweb/Script/Activate.ps1`
3. 安装依赖
   终端运行命令：`pip install -r requirements.txt`
4. 修改配置文件
   打开根目录下`django_advance`下的 `settings.py` 文件，修改 DATABASES 字段

   ```python
   DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 若使用mysql需要先安装，然后简历数据库 -> create database django_advance
    # 或者直接使用sqlite数据库
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_advance',
        'USER': '用户名',
        'PASSWORD': '密码',
        'HOST': '127.0.0.1',
        'PROT': 3306,
    }
   }
   ```

5. 数据库迁移
   在项目根目录终端中运行：`python manage.py migrate`
6. 启动
   `python manage.py runserver`

# WebApp 概览

## [1. 用户注册、登录发放 Token](./da_user)

- `/ft-user/` 前端页面
- `/api/user/` 用户注册
- `/api/token/` 获取用户 Token
- `/api/token/refresh/` Token 过期刷新 Token

## [2. Redis 缓存的基本使用](./da_redis)

- 在 settings.py 中配置 Redis Caches
  ```python
  CACHES = {
     "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1", # 使用 1 号库
        "OPTIONS": {
              "PASSWORD": "pwd", # redis密码，没有则注释
              "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
     }
  }
  ```
- API
  - `/rds/rbooks/`
  - `/rds/rooks/{id}/`
