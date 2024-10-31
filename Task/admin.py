from django.contrib import admin
from Task.Models.taskModel import Task
from Task.Models.tagModel import Tag

admin.site.register(Task)
admin.site.register(Tag)

# Register your models here.
