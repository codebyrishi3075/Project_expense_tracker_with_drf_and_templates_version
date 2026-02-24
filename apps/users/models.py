from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    currency = models.CharField(max_length=10, default="INR")

    def __str__(self):
        return self.username