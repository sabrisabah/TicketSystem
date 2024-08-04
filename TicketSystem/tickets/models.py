from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('close', 'Close'),
        ('in_progress', 'In Progress'),
        ('refarl', 'Refarl'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
