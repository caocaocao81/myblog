from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # 对所有人允许get head options请求
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


