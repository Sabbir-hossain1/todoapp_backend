from django.db import models
from User.models import CustomUser


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="M")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    # Relationships for subtasks and dependencies
    parent_task = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="subtasks"
    )
    dependencies = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="dependent_tasks"
    )

    # Tags for flexible categorization
    tags = models.ManyToManyField("Tag", blank=True, related_name="tasks")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["priority", "due_date"]
