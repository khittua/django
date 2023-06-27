from django.shortcuts import render, redirect, reverse
from .models import *
import os
from django.conf import settings
from rest_framework import generics
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.


def cargarInicio(request):
    return render(request,"inicio.html")
    

@login_required
def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregarProducto.html",{"cate":categorias, "prod":productos})


def agregarProducto(request):
    #print("PRODUCTO AGREGAR", request.POST)

    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_img = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku,nombre = v_nombre,stock = v_stock,precio = v_precio,descripcion = v_descripcion, id_categoria = v_categoria, imagen_url = v_img)        

    return redirect('/agregar')



def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":productos,"cate":categorias})

def editarProducto(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    v_descripcion = request.POST['txtDescripcion']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try:
        v_img = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagen_url))
        os.remove(ruta_imagen)
    except:
        v_img = productoBD.imagen_url


    productoBD.nombre = v_nombre
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.descripcion = v_descripcion
    productoBD.imagen_url = v_img
    productoBD.id_categoria = v_categoria

    productoBD.save()


    return redirect('/editar')


def eliminarProducto(request,sku):
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagen_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            # Aquí se pasa el mensaje de error a la plantilla
            return render(request, 'login.html', {'error': True})

    return render(request, 'login.html')
def cargarGato(request):
    productos = Producto.objects.all()
    categoria_perros = Producto.objects.filter(id_categoria = 1)
    categoria_gatos = Producto.objects.filter(id_categoria = 2)
    return render(request,"gato.html",{"prod":productos,"cate_gatos":categoria_gatos,"cate_perros":categoria_perros})

def cargarPerro(request):
    productos = Producto.objects.all()
    categoria_perros = Producto.objects.filter(id_categoria = 1)
    categoria_gatos = Producto.objects.filter(id_categoria = 2)
    return render(request,"perro.html",{"prod":productos,"cate_gatos":categoria_gatos,"cate_perros":categoria_perros})

def cargarCarrito(request):
    return render(request,"carrito.html")

def cargarEditar(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"editar.html",{"cate":categorias, "prod":productos})

def cargarAgregar(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"agregar.html",{"cate":categorias, "prod":productos})

def cargarRegistro(request):
    usuario = Usuario.objects.all()
    return render(request,"registro.html",{"user":usuario})

def registro(request):
    v_nombre = request.POST['txtNombre']
    v_usuario = request.POST['txtUsuario']
    v_correo = request.POST['txtCorreo']
    v_contraseña = request.POST['txtContraseña']
    
    print("Datos del formulario:")
    print("Nombre:", v_nombre)
    print("Usuario:", v_usuario)
    print("Correo:", v_correo)
    print("Contraseña:", v_contraseña)
    
    Usuario.objects.create(nombre=v_nombre, usuario=v_usuario, correo=v_correo, contraseña=v_contraseña)        

    return redirect('/')
class ProductoListAPIView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def disminuir_stock(request):
    if request.method == 'POST':
        sku = request.POST.get('sku')
        producto = Producto.objects.get(sku=sku)
        producto.stock -= 1
        producto.save()
        # No se devuelve ninguna respuesta explícita
        # Redireccionamiento automático a la misma página
        return redirect(request.META['HTTP_REFERER'])