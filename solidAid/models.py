from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class Adherant(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    type = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse("actions")
    
    

class Actions(models.Model):
    image = models.ImageField(upload_to="media")
    desc = models.TextField(max_length=200)
    
    def get_absolute_url(self):
        return reverse("actions")

    



