from django.db import models
from utils.models import UUIDModel

# Create your models here.
class Class(UUIDModel):
    class Meta:
        verbose_name_plural = "classes"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
