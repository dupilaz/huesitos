from django.shortcuts import render
from django.utils import timezone
from .models import Servicio

# Create your views here.


def prueba(request):
    
    return render(request, 'blog/prueba.html')

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, 'blog/servicio.html', {"servicios":servicios})    
def contacto(request):
    
    return render(request, 'blog/contacto.html')      