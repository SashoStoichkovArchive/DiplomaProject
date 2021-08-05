from django.db import models
from django.utils import timezone

from utils.models import UUIDModel
from group.models import Class
from subject.models import Subject

# Create your models here.
class TimeSlot(UUIDModel):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    is_available = models.BooleanField(default=True)
    room_name = models.CharField(max_length=50)

    group = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.start_time.strftime('%d-%m-%Y %H:%M')
