from django.urls import path
from . import views


urlpatterns = [
    path('', views.prueba, name='prueba'),

    path('servicio', views.servicios, name='servicio'),
    
    path('contacto', views.post_new, name='contacto'),
]