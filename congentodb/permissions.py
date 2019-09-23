from rest_framework import permissions

from .models import CongentoMember


class CustomPermission(permissions.BasePermission):
    message = "You are not allowed to access this API."

    def has_permission(self, request, view):
        return (
            not request.user.is_anonymous
            and CongentoMember.objects.filter(api_user=request.user).exists()
        )
