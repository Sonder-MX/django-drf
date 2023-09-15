from django.urls import path

from .views import chat_index

name = "da_chat"
urlpatterns = [
    path("", chat_index, name="chat_index"),
]
