from django.urls import path
from . import views


urlpatterns = [
    path('', views.prueba, name='prueba'),

    path('servicio', views.servicios, name='servicio'),
    path('contacto', views.contacto, name='contacto'),
    path('servicio/new', views.post_new, name='servicio_new'),
]