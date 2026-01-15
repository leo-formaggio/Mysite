
from django.urls import path
from .views import home, lista_estudantes, add_estudante, detalhe_estudante, lista_professor, add_professor, detalhe_professor, lista_curso, add_curso, detalhe_curso, buscar_estudante

urlpatterns = [
    path('', home, name='home'),
    path('estudantes/', lista_estudantes, name='lista_estudantes'),
    path('add_estudante/', add_estudante, name='add_estudante'),
    path('estudantes/<int:pk>/', detalhe_estudante, name='detalhe_estudante'),
    path('professor/', lista_professor, name='lista_professor'),
    path('add_professor/', add_professor, name='add_professor'),
    path('professor/<int:pk>/', detalhe_professor, name='detalhe_professor'),
    path('curso/', lista_curso, name='lista_curso'),
    path('add_curso/', add_curso, name='add_curso'),
    path('curso/<int:pk>/', detalhe_curso, name='detalhe_curso'),
    path('buscar/', buscar_estudante, name='buscar_estudante'),
]