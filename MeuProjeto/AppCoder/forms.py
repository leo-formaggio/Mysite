from django import forms
from .models import Estudante, Professor, Curso 

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = '__all__'
