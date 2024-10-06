from User.models import CustomUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from User.Serializers.UserModelSerializer import (
    UserModelCreateUpdateSerializer,
    UserModelRetrieveSerializer,
    UserModelDeleteSerializer,
    UserModelListSerializer,
)
from User.permissions import IsAdmin, IsManager


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # Admins and Managers can create, update, and delete users
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsAdmin | IsManager]
        # All authenticated users can view (list and retrieve)
        elif self.action in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]
        return super(UserModelViewSet, self).get_permissions()

    def get_serializer_class(self):
        # Use different serializers based on the action
        if self.action in ["create", "update", "partial_update"]:
            return UserModelCreateUpdateSerializer
        elif self.action == "retrieve":
            return UserModelRetrieveSerializer
        elif self.action == "list":
            return UserModelListSerializer
        elif self.action == "destroy":  # Adjust for delete action
            return UserModelDeleteSerializer
        return super(UserModelViewSet, self).get_serializer_class()

    def get_queryset(self):
        # Optionally filter the queryset based on user roles if needed
        return CustomUser.objects.all()
