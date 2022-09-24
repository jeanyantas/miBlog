from django import forms
from .models import Comment

# Creación de Formularios a partir de modelos tipo ModelForm
class CommentForm(forms.ModelForm):
    # Para crear un formulario a partir de un modelo, solo necesita indicar qué modelo usar para construir el formulario en la clase Meta del formulario. Django hace una introspección del modelo y crea el formulario dinámicamente para usted.
    class Meta:
        model = Comment
        # Cada tipo de campo de modelo tiene un tipo de campo de formulario predeterminado correspondiente. La forma en que define los campos de su modelo se tiene en cuenta para la validación del formulario. Por defecto, Django construye un campo de formulario para cada campo contenido en el modelo. Sin embargo, puede decirle explícitamente al marco qué campos desea incluir en su formulario usando una lista de campos, o definir qué campos desea excluir usando una lista de exclusión de campos. Para su formulario CommentForm, solo usará los campos de Nombre, Correo y Comentario, porque esos son los únicos campos que sus usuarios podrán completar.
        fields = ('nombre', 'correo', 'comentario')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }