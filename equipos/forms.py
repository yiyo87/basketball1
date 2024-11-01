from django import forms
from equipos.models import Equipo,Jugador,Partido

class FormularioEquipo(forms.ModelForm):
    class Meta:
        model= Equipo
        fields = '__all__'

class FormularioJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class FormularioPartido(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'


