from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudante, Professor, Curso
from .forms import ProfessorForm, CursoForm, EstudanteForm

def home(request):
    return render(request, 'base.html')

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'estudantes_list.html', {'estudantes': estudantes})

def add_estudante(request):
    form = EstudanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_estudantes')
    return render(request, 'estudante_form.html', {'form': form})

def detalhe_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'estudante_detail.html', {'estudante': estudante})

def lista_professor(request):
    professor = Professor.objects.all()
    return render(request, 'professor_list.html', {'professor': professor})

def add_professor(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_professor')
    return render(request, 'professor_form.html', {'form': form})

def detalhe_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'professor_detail.html', {'professor': professor})

def lista_curso(request):
    curso = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso': curso})

def add_curso(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_curso')
    return render(request, 'curso_form.html', {'form': form})

def detalhe_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'curso_detail.html', {'curso': curso})

def buscar_estudante(request):
    termo = request.GET.get('q', '')
    estudantes = Estudante.objects.filter(nome__icontains=termo)
    return render(request, 'buscar_estudante.html', {'estudantes': estudantes, 'termo': termo})