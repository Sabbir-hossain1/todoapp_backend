from rest_framework import viewsets
from taskapp.Serializers.TaskModelSerializer import (
    TaskCreateUpdateSerializer,
    TaskListSerializer,
    TaskRetrieveSerializer,
    TaskDeleteSerializer,
)
from rest_framework.exceptions import PermissionDenied
from taskapp.Models.taskModel import TaskModel
from taskapp.Permissions import IsOwner
from django.db.models import Q


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return TaskCreateUpdateSerializer
        elif self.action == "list":
            return TaskListSerializer
        elif self.action == "retrieve":
            return TaskRetrieveSerializer
        elif self.action == "delete":
            return TaskDeleteSerializer

    def get_queryset(self):
        return TaskModel.objects.filter(
            Q(created_by=self.request.user) | Q(assigned_to=self.request.user)
        )

    def perform_update(self, serializer):

        if "assigned_to" in serializer.validated_data:
            if self.get_object().assigned_to is not None:
                raise PermissionDenied("Assigned Task can not be reassigned")
            serializer.save()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        return super().perform_destroy(instance)
