from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(help_text='Format: +263778123456')
    loyalty_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
 
   
class Complaint(models.Model):
    complaint_type = [
        ('Product Issue', 'Product Issue'),
        ('Billing Issue', 'Billing Issue'),
        ('Staff Behavior', 'Staff Behavior'),   
    ]
    status = [
        ('Pending', 'Pending'),
        ('Received', 'Received'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),      
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=50, choices=complaint_type)
    details = models.TextField(verbose_name='Message')
    branch = models.ForeignKey("branches.Branch", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=status, default='open')
    date_submitted = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    assigned_to = models.ForeignKey("users.Staff", on_delete=models.CASCADE, null=True, blank=True)
    
