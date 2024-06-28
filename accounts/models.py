from django.db import models

# Create your models here.

class Users(models.Model):
    TYPES_CHOICES = [
        ('benevole', 'Benevole'),
         ('membre', 'Membre'),
    ]
    nom = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    type = models.CharField(max_length=30, choices=TYPES_CHOICES)
    motif = models.CharField(max_length=1000)
