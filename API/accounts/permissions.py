from .models import User

from rest_framework.request import Request
from rest_framework.permissions import BasePermission
from rest_framework.views import View
import pdb


class IsAccountOwnerOrSuperuser(BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if request.user.is_superuser:
            return True

        return request.user.is_authenticated and obj == request.user


class IsSuperuser(BasePermission):
    def has_permission(self, request: Request, view):
        if request._request.method == "GET":
            return bool(request.user.is_superuser and request.user.is_authenticated)

        return True
