from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        exclude = ['id_libro']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'dd/mm/aaaa',
            }),
        }
        labels = {
            'fecha_publicacion': 'Fecha Publicación',
        }
