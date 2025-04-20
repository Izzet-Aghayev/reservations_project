from django.db import models
from accounts.models import User


class Service(models.Model):
    SERVICE_CHOICES = [
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant')
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    description = models.TextField()


    def __str__(self):
        return self.name



class Reservation(models.Model):
    STATUS = [
        ('waiting', 'Waiting'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.service}'