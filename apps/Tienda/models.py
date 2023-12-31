from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        txt = "Nombre: {0} - Id: {1}"
        return txt.format(self.nombre_categoria,self.id_categoria)

class Producto(models.Model):
    sku = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen_url = models.ImageField(upload_to='imagenesProducto')

    def __str__(self):
        txt = "N° {0} - Stock: {1} - nombre: {2}"
        return txt.format(self.sku,self.stock, self.nombre)
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, unique= True)
    usuario = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    USERNAME_FIELD = 'usuario'

    def __str__(self):
        txt = "Usuario: {1} - Nombre: {0}"
        return txt.format(self.usuario,self.nombre)
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'