from django.db import models
from django.utils import timezone



class Servicio(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    precio = models.CharField(max_length=10)
        
    
    def __str__(self):
        return self.title
