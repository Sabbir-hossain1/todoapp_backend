from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskapp.Views.TaskModelView import TaskModelViewSet

taskapp_router = DefaultRouter()
taskapp_router.register(r"tasks", TaskModelViewSet, basename="tasks")


urlpatterns = [path("", include(taskapp_router.urls))]
