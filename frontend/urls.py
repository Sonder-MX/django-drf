from django.urls import path

from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.home, name='home'),
    path('pages/register', views.register, name='register'),
    path('pages/userinfo_update', views.userinfo_update, name='userinfo_update')
]
