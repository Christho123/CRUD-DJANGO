import pytest
from django.urls import reverse
from productos.models import Libro

@pytest.mark.django_db
def test_agregar_libro_view_post_valido(client):
    url = reverse('agregar_libro')
    data = {
        'titulo': 'Nuevo Libro',
        'autor': 'Autor Prueba',
        'genero': 'Ficción',
        'fecha_publicacion': '2025-07-25T12:00',  # formato para datetime-local
    }

    response = client.post(url, data)

    # Verifica que redirige correctamente
    assert response.status_code == 302
    assert response.url == reverse('lista_libros')

    # Verifica que el libro fue creado
    libros = Libro.objects.all()
    assert libros.count() == 1
    libro = libros.first()
    assert libro.titulo == 'Nuevo Libro'
    assert libro.genero == 'Ficción'
    assert libro.autor == 'Autor Prueba'


@pytest.mark.django_db
def test_agregar_libro_view_post_invalido(client):
    url = reverse('agregar_libro')
    data = {
        'titulo': '',  # Título requerido, lo dejamos vacío
        'autor': 'Autor sin título',
        'genero': 'Acción',
        'fecha_publicacion': '2025-07-25T12:00',
    }

    response = client.post(url, data)

    # Debe quedarse en la misma página con errores
    assert response.status_code == 200
    assert 'form' in response.context
    assert Libro.objects.count() == 0
