from datetime import timezone
from django.db import models

# Create your models here.
# tickets/models.py

class Note(models.Model):
    text = models.TextField()

class Ticket(models.Model):
    DEMOGRAPHIC_CHOICES = [
        ('Technical', 'Technical'),
        ('Billing', 'Billing'),
        ('Service', 'Service'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=DEMOGRAPHIC_CHOICES)
    notes = models.ManyToManyField(Note, blank=True)
    status = models.CharField(max_length=20, default='Open')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s Ticket"

