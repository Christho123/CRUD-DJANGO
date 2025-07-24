from django.db import models

class Libro(models.Model):
    id_libro = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField()  # 👈 el usuario podrá ingresarla

    class Meta:
        db_table = "libros"
