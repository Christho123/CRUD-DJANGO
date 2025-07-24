from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('editar/<str:pk>/', views.editar_libro, name='editar_libro'),
    path('eliminar/<str:pk>/', views.eliminar_libro, name='eliminar_libro')

]
