from django.conf import settings

from django.db import models
from django.contrib.auth.models import User

class AdvertisementStatusChoices(models.TextChoices):
    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = 'DRAFT', 'Черновик'


class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField(default=''
            )
    status = models.TextField(
            choices=AdvertisementStatusChoices.choices,
            default=AdvertisementStatusChoices.DRAFT
            )
    creator = models.ForeignKey(User,
            on_delete=models.CASCADE
            )
    created_at = models.DateTimeField(auto_now_add=True
            )
    updated_at = models.DateTimeField(auto_now=True
            )
