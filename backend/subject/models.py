from django.db import models
from django.utils.translation import gettext_lazy as _

from teacher.models import Teacher
from utils.models import UUIDModel

# Create your models here.
class Subject(UUIDModel):
    class Priority(models.TextChoices):
        low = "low", _("Low")
        medium = "medium", _("Medium")
        high = "high", _("High")

    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=255, choices=Priority.choices, default=Priority.low
    )

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + " (" + self.teacher.get_full_name() + ")"
