from rest_framework import serializers
from taskapp.Models.taskModel import TaskModel


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"
        read_only_fields = ["created_by"]


class TaskRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"


class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"


class TaskDropdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"
