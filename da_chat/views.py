from django.http import HttpRequest
from django.shortcuts import render


def chat_index(request: HttpRequest):
    # eg: /chat/?room=123&uname=abc
    room_num = request.GET.get("room")
    user_name = request.GET.get("uname")
    return render(request, "chat.html", {"roomNum": room_num, "uname": user_name})
