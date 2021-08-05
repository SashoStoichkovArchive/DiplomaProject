from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.models import UUIDModel

# from group.models import Class
# from subject.models import Subject

# Create your models here.
class TimeSlot(UUIDModel):
    class WeekDay(models.IntegerChoices):
        MONDAY = 0, _("Monday")
        TUESDAY = 1, _("Tuesday")
        WEDNESDAY = 2, _("Wednesday")
        THURSDAY = 3, _("Thursday")
        FRIDAY = 4, _("Friday")
        SATURDAY = 5, _("Saturday")
        SUNDAY = 6, _("Sunday")

    day = models.IntegerField(choices=WeekDay.choices, default=WeekDay.MONDAY)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    is_available = models.BooleanField(default=True)

    # This data will be added later
    # room_name = models.CharField(max_length=50)
    # group = models.ForeignKey(Class, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"{self.WeekDay.choices[self.day][1]} {self.start_time} - {self.end_time}"
        )
