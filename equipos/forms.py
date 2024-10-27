from django import forms
from equipos.models import Equipo

class FormularioEquipo(forms.ModelForm):
    class Meta:
        model= Equipo
        fields = '__all__'