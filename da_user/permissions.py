from rest_framework.permissions import BasePermission


class IsLogin(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user
