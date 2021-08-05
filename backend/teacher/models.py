from django.db import models
from utils.models import UUIDModel

# Create your models here.
class Teacher(UUIDModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    phone = models.CharField(max_length=50)
    degree = models.CharField(max_length=50, null=True, blank=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        if self.degree:
            return "{} {}".format(self.degree, self.get_full_name())
        else:
            return self.get_full_name()
