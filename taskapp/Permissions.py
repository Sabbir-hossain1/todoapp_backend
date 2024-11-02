from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == "destroy":
            return obj.created_by == request.user
        return obj.created_by == request.user or obj.assigned_to == request.user
