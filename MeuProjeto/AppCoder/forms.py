from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import Estudante, Professor, Curso
from django.contrib.auth import get_user_model
from django import forms
from .models import Page

User = get_user_model()

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

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

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo', 'conteudo']

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
