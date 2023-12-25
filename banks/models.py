from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create your models here.


"""
bank has a name, swift code, institution number, and description
"""


class Bank(models.Model):
    owner = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    swift_code = models.CharField(max_length=100, null=False, blank=False, unique=True)

    institution_number = models.CharField(
        max_length=100, null=False, blank=False, unique=True)

    description = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"

"""A branch has a name, transit number, and address,"""


class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    transit_number = models.CharField(max_length=100, null=False, blank=False, unique=True)
    address = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True,
        validators=[EmailValidator(message="Enter a valid email address.")],
        default="admin@enigmatix.io"
    )
    capacity = models.PositiveIntegerField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
