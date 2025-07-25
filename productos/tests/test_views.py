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
        'fecha_publicacion': '2025-07-25T12:00',
    }

    response = client.post(url, data)

    assert response.status_code == 302
    assert response.url == reverse('lista_libros')

    libros = Libro.objects.all()
    assert libros.count() == 1
    libro = libros.first()
    assert libro.titulo == 'Nuevo Libro'
    assert libro.genero == 'Ficción'

@pytest.mark.django_db
def test_agregar_libro_view_post_invalido(client):
    url = reverse('agregar_libro')
    data = {

        'id_libro': 'LIB999',
        'titulo': '',
        'autor': 'Autor sin título',
        'genero': 'Acción',
        'fecha_publicacion': '2025-07-25T12:00',
    }

    response = client.post(url, data)

    assert response.status_code == 200
    assert 'form' in response.context
    assert Libro.objects.count() == 0
