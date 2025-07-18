from rest_framework.permissions import BasePermission, SAFE_METHODS


class Permissions(object):
    """
    A base class from which all permission classes should inherit.
    """
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True
    def has_object_permission(self, request, view, obj):
        """
         Return `True` if permission is granted, `False` otherwise.
        """
        return True
    
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user