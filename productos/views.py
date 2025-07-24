from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'productos/lista_libros.html', {'libros': libros})

def agregar_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'productos/form_libro.html', {'form': form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, id_libro=pk)  # 👈 CAMBIO AQUÍ
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'productos/form_libro.html', {'form': form})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, id_libro=pk)  # 👈 CAMBIO AQUÍ
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'productos/eliminar_libro.html', {'libro': libro})
