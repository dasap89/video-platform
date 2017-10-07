from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Video(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    rent_start_time = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )
    rent_by = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    rent_by_phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    rent_available = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )
    rent_manager = models.ForeignKey(
        User,
        related_name='rent_manager',
        null=True,
        blank=True
    )

    def __str__(self):
        return '{}'.format(self.title)
