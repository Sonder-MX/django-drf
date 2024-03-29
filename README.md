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
   在项目根目录终端中运行：
   - `python manage.py makemigrations`
   - `python manage.py migrate`
6. 创建超级用户
   - `python manage.py createsuperuser`
   - 按提示输入信息
7. 插入测试数据（非必须）
   - 打开目录 [sql_test_data](./sql_test_data)
   - 在数据库客户端中运行脚本
8. 启动
   `python manage.py runserver`

# WebApp 概览

## [1. 用户注册、登录发放 Token](./da_user)

- `/ft-user/` 前端页面
- `/api/user/` 用户注册
- `/api/token/` 获取用户 Token
- `/api/token/refresh/` Token 过期刷新 Token

## [2. 过滤、排序和分页](./da_fop)

- [过滤和排序](./da_fop/filters.py)
  - `/fop/persons/?name=明`
  - `/fop/persons/?sort=-age`
  - ......
- [分页](./da_fop/paginations.py)
  - `/fop/persons/?page=2`
  - `/fop/persons/?page=3&size=15`

## [3. Redis 缓存的基本使用](./da_redis)

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

## [4. 权限、认证、限流](./da_apt)

- `/apt/aptbooks/`

## [5. 统一返回数据格式](./da_unified/utils.py)

- `/unified/persons/`

## [6. WebSocket 实现简易聊天室](./da_chat)

**注：使用 WebSocket 要使用 asgi 启动**

- 启动
  - `uvicorn django_advance.asgi:application`
- 进入聊天界面
  - 分别使用 Edge 和 Chrome 浏览器打开
  - `/chat/?room=12345&uname=Jack`
  - `/chat/?room=12345&uname=Amy`
