from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'

class IsExpert(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'expert'

class IsRetiredExpert(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'retired_expert'

class IsProfileOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.role == 'admin'