from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(help_text='Format: +263778123456')

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
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),      
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    complaint_type = models.CharField(max_length=50, choices=complaint_type)
    details = models.TextField(verbose_name='Message')
    branch = models.ForeignKey("branches.Branch", on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=status, default='open')
    date_submitted = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.complaint_type} from [{self.customer}]'
         
@receiver(post_save, sender=Complaint)
def send_new_complaint_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "complaints_notifications",  # Group name defined in consumer
            {
                "type": "send_notification",
                "message": f"Complaint: {instance.complaint_type} from {instance.customer}"
            }
        )
    
class Assign(models.Model):
    complaint = models.ForeignKey("complaints.Complaint", on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey("users.Staff", on_delete=models.SET_NULL, null=True, blank=True)
    date_assigned = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.complaint} to {self.staff}'
     
class Feedback(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    remarks = models.TextField()
    user = models.ForeignKey("users.Staff", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Feedback for {self.complaint.customer}'
    