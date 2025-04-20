from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager



class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.username
