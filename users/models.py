from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.   
class Staff(AbstractUser):
    role =[
        ('Customer Support', 'Customer Support'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    ]
    email = models.EmailField(max_length=254, unique=True)
    phone_number = PhoneNumberField()
    branch = models.ForeignKey("branches.Branch", on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=20, choices=role, null=True)
    
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email



