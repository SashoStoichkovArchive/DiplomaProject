import uuid
from django.db import models

# Create your models here.
class Class(models.Model):
    class Meta:
        verbose_name_plural = "Classes"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
