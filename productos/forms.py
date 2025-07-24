from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
        }),
        label='Fecha de Publicación',
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:
        model = Libro
        exclude = ['id_libro']  # No mostrar el ID en el form
