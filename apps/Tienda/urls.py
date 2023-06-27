from django.urls import path
from . import views
from .views import ProductoListAPIView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.cargarInicio),
    path('agregarProducto',views.cargarAgregarProducto, name='v_agregar'),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='v_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='v_logout'),
    path('gato/',views.cargarGato, name='v_gato'),
    path('perro/',views.cargarPerro, name='v_perro'),
    path('carro/',views.cargarCarrito, name='v_carro'),
    path('editar/',views.cargarEditar, name='v_editar'),
    path('agregar/',views.cargarAgregar, name='v_agregar'),
    path('registro/',views.cargarRegistro, name='v_registro'),
    path('registroForm',views.registro),
    path('api/productos/', ProductoListAPIView.as_view(), name='api-productos'),
    path('login/', views.login_view, name='v_login'),
    path('disminuir_stock/', views.disminuir_stock, name='disminuir_stock'),




]