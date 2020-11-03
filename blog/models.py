from django.db import models
from django.utils import timezone



class Servicio(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    precio = models.CharField(max_length=10)
        
    
    def __str__(self):
        return self.title

class Reclamo(models.Model):

    Rut=models.CharField(max_length=10)
    Nombres=models.CharField(max_length=50)
    Apellidos=models.CharField(max_length=50)
    Correo=models.EmailField()
    Telefono=models.CharField(max_length=50)
    Asunto=models.TextField()

    def __str__(self):
        return self.Rut
