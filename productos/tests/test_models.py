import pytest
from productos.models import Libro

@pytest.mark.django_db
def test_libro_str():
    libro = Libro(titulo="Prueba", autor="Autor", descripcion="Desc", precio=10)
    assert str(libro) == "Prueba"