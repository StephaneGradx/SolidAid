from django.db import models

# Create your models here.
class Checkout(models.Model):
    montant = models.IntegerField()
