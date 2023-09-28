from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from order_manager.employee_manager import EmployeeManager


class Employee(AbstractUser):
    class PositionChoices(models.TextChoices):
        JUNIOR = "JR", _("Junior")
        MIDDLE = "ML", _("Middle")
        SENIOR = "SR", _("Senior")

    probation = models.BooleanField(default=True)
    position = models.CharField(
        max_length=2,
        choices=PositionChoices.choices,
        default=PositionChoices.JUNIOR
    )

    objects = EmployeeManager()

    class Meta:
        ordering = ["username"]


class Order(models.Model):
    task_id = models.UUIDField(max_length=16, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="orders"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.task_id)
