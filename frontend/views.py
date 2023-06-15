from django.shortcuts import render

from frontend import urls


def home(request):
    data_li = []
    for urls_item in urls.urlpatterns[1::]:
        data_li.append({
            'name': urls_item.name,
            'route': str(urls_item.pattern),
        })
    return render(request, 'home.html', {'data': data_li})


def register(request):
    """登录 注册"""
    return render(request, 'register/index.html')
