from .forms import ProfessorForm, CursoForm, EstudanteForm, PageForm, CustomUserCreationForm, CustomUserEditForm, ProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudante, Professor, Curso, Page, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout

def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'estudantes/estudantes_list.html', {'estudantes': estudantes})

def add_estudante(request):
    form = EstudanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_estudantes')
    return render(request, 'estudantes/estudante_form.html', {'form': form})

def detalhe_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'estudantes/estudante_detail.html', {'estudante': estudante})

@login_required
def edit_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)

    if request.method == 'POST':
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudantes')
    else:
        form = EstudanteForm(instance=estudante)

    return render(request, 'estudantes/estudante_edit.html', {'form': form})

@login_required
def delete_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)

    if request.method == 'POST':
        estudante.delete()
        return redirect('lista_estudantes')

    return render(request, 'estudantes/estudante_confirm_delete.html', {'estudante': estudante})

User = get_user_model()

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        user_form = CustomUserEditForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileForm(
            request.POST or None,
            request.FILES or None,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = CustomUserEditForm(
            instance=request.user
        )
        profile_form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'perfil/profile_edit.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
        }
    )

@login_required
def profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('home')

    return render(request, 'perfil/profile_confirm_delete.html')

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    return render(
        request,
        'perfil/profile.html',
        {
            'user_profile': request.user,
            'profile': profile,
        }
    )

def lista_professor(request):
    professor = Professor.objects.all()
    return render(request, 'professores/professor_list.html', {'professor': professor})

def add_professor(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_professor')
    return render(request, 'professores/professor_form.html', {'form': form})

def detalhe_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'professores/professor_detail.html', {'professor': professor})

def buscar_professor(request):
    termo = request.GET.get('q', '')
    professores = Professor.objects.filter(nome__icontains=termo)
    return render(request, 'professores/buscar_professor.html', {'professores': professores, 'termo': termo})

@login_required
def edit_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('lista_professor')
    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'professores/professor_edit.html', {'form': form})

@login_required
def delete_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)

    if request.method == 'POST':
        professor.delete()
        return redirect('lista_professor')

    return render(request, 'professores/professor_confirm_delete.html', {'professor': professor})

def lista_curso(request):
    curso = Curso.objects.all()
    return render(request, 'cursos/curso_list.html', {'curso': curso})

def add_curso(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_curso')
    return render(request, 'cursos/curso_form.html', {'form': form})

@login_required
def edit_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_curso')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'cursos/curso_edit.html', {'form': form})

@login_required
def delete_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)

    if request.method == 'POST':
        curso.delete()
        return redirect('lista_curso')

    return render(request, 'cursos/curso_confirm_delete.html', {'curso': curso})

def detalhe_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/curso_detail.html', {'curso': curso})

def buscar_curso(request):
    termo = request.GET.get('q', '')
    cursos = Curso.objects.filter(nome__icontains=termo)
    return render(request, 'cursos/buscar_curso.html', {'cursos': cursos, 'termo': termo})

def buscar_estudante(request):
    termo = request.GET.get('q', '')
    estudantes = Estudante.objects.filter(nome__icontains=termo)
    return render(request, 'estudantes/buscar_estudante.html', {'estudantes': estudantes, 'termo': termo})


def pages(request):
    paginas = Page.objects.all().order_by('-criado_em')
    return render(request, 'paginas/pages.html', {'paginas': paginas})

def page_detail(request, pk):
    pagina = get_object_or_404(Page, pk=pk)
    return render(request, 'paginas/page_detail.html', {'pagina': pagina})

@login_required
def page_create(request):
    form = PageForm(request.POST or None)
    if form.is_valid():
        pagina = form.save(commit=False)
        pagina.autor = request.user
        pagina.save()
        return redirect('pages')

    return render(request, 'paginas/page_form.html', {'form': form})

@login_required
def edit_page(request, pk):
    pagina = get_object_or_404(Page, pk=pk)

    if request.method == 'POST':
        form = PageForm(request.POST, instance=pagina)
        if form.is_valid():
            form.save()
            return redirect('pages')
    else:
        form = PageForm(instance=pagina)

    return render(request, 'paginas/page_edit.html', {'form': form})

@login_required
def delete_page(request, pk):
    pagina = get_object_or_404(Page, pk=pk)

    if request.method == 'POST':
        pagina.delete()
        return redirect('pages')

    return render(request, 'paginas/page_confirm_delete.html', {'pagina': pagina})
