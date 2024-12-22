from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        # return request.user and request.user.role == "seller"
        return (
            request.user.is_authenticated and 
            getattr(request.user, 'role', None) == "seller"
        )