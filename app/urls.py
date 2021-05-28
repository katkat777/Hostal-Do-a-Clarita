from django.urls import path
from .views import home, contacto, galeria, registro, registrohabitacion

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('registrohabitacion/', registrohabitacion, name="registrohabitacion")



]
