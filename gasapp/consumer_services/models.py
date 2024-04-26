from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = (
        ('NEW_CONNECTION', 'New Connection'),
        ('METER_READING', 'Meter Reading'),
        ('LEAK_REPAIR', 'Leak Repair'),
        
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=255, choices=REQUEST_TYPE_CHOICES)
    description = models.TextField()
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='PENDING')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(blank=True, null=True)
    attached_file = models.FileField(upload_to='service_requests/', blank=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.request_type}"  


