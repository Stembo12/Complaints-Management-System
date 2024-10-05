from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.   
class Staff(AbstractUser):
    role =[
        ('customer_support', 'Customer Support'),
        ('manager', 'Manager'),
    ]
    email = models.EmailField(max_length=254, unique=True)
    phone_number = PhoneNumberField()
    branch = models.ForeignKey("branches.Branch", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email



