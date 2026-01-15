
# Django Escola — Sistema de Cadastro de Professores, Cursos e Estudantes

Esse é um site web desenvolvido em Django com o padrão MTV (Model-Template-View) que permite cadastrar e listar entidades de uma escola:

🎓 Estudante
👩‍🏫 Professor
📘 Curso

Inclui:

Modelos de banco de dados para as três classes;

Formulários para inserir registros no banco;

Formulário de busca de estudantes;

Templates com herança usando Bootstrap 5 para estilo básico e responsivo.

## Tecnologias e Dependências

Este projeto foi construído com:

- Python	≥ 3.8
- Django	≥ 4.x
- Bootstrap	5
- SQLite	Banco de dados padrão Django




## Funcionalidades

- Cadastrar Estudante, Professor e Curso
- Buscar estudantes por nome
- Navegação com barra responsiva Bootstrap
## Instalações

1. Clonar Repositório:

```bash
  git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
```

2. Criar e ativar o ambiente virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Instalar dependências:

```bash
pip install Django
```

4. Migrar o Banco de Dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Rodar o servidor do desenvolvimento:

```bash
python manage.py runserver
```

    
## Navegação e Ordem de Testes

Após rodar o servidor (por padrão em http://127.0.0.1:8000/
), siga a ordem abaixo para testar todas as funcionalidades:

1. Acessar a página Inicial:

URL: http://127.0.0.1:8000/

Verifique que o menu de navegação aparece com links para todos os forms.

2. Cadastrar um Estudante:

URL: http://127.0.0.1:8000/add_estudante/

Preencha nome, sobrenome e e-mail e clique em Salvar.

3. Cadastrar um Professor:

URL: http://127.0.0.1:8000/add_professor/

Preencha nome, sobrenome e e-mail e clique em Salvar.

4. Cadastrar um Curso:

URL: http://127.0.0.1:8000/add_curso/

Digite nome do curso e turma, depois Salvar.

5. Buscar um Estudante:

URL: http://127.0.0.1:8000/buscar/?q=

Use o campo de busca para pesquisar o nome do aluno.

6. Listar os Estudantes:

URL: http://127.0.0.1:8000/estudantes/

7. Listar os Professores:

URL: http://127.0.0.1:8000/professor/

8. Listar os Cursos:

URL: http://127.0.0.1:8000/curso/
## Arquitetura e Templates

### Herança de Templates
O template base (base.html) contém a estrutura principal de navegação e footer, e é estendido pelos outros templates para reutilização de layout.

### Bootstrap 5
O estilo visual é feito com classes Bootstrap para responsividade e aparência básica.


## Autor

Leonardo Formaggio

- [github](https://www.github.com/leo-formaggio)
- [LinkedIn](https://www.linkedin.com/in/leonardoformaggio/)