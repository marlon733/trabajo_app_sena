from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar aprendices"""
    
    class Meta:
        model = Aprendiz
        # CORREGIDO: Usando los nombres exactos del modelo
        fields = [
            'documento_identificacion',
            'nombre',
            'apellido',
            'telefono',
            'email',
            'fecha_nacimiento',
            'ciudad'
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            # CORREGIDO: Nombre del campo
            'documento_identificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            # CORREGIDO: Nombre del campo
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad de residencia'
            })
        }
        # Etiquetas personalizadas
        labels = {
            # CORREGIDO: Nombre del campo
            'documento_identificacion': 'Documento de Identidad',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            # CORREGIDO: Nombre del campo
            'email': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'ciudad': 'Ciudad'
        }

    # Validaciones personalizadas
    
    # CORREGIDO: Nombre de la función de validación
    def clean_documento_identificacion(self):
        """Validar que el documento contenga solo números"""
        # CORREGIDO: Nombre del campo al obtener los datos
        documento = self.cleaned_data.get('documento_identificacion')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_telefono(self):
        """Validar que el teléfono contenga solo números"""
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if telefono and len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono