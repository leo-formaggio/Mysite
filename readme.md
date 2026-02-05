
# Django Escola — Sistema de Cadastro de Professores, Cursos e Estudantes com Registro e Login de usuário

Este projeto foi desenvolvido utilizando **Python** e **Django**, com o objetivo de consolidar os principais conceitos do framework na construção de uma aplicação web completa, organizada e funcional, com o padrão MTV (Model-Template-View) que permite ler atualizações do blog, registrar, fazer login, editar perfil e avatar, cadastrar e listar entidades de uma escola:

🎓 Estudante
👩‍🏫 Professor
📘 Curso

Inclui:

Modelos de banco de dados para as três classes;

Formulários para inserir registros no banco;

Formulário de busca de estudantes, professores e cursos;

Templates com herança usando Bootstrap 5 para estilo básico e responsivo.

## Tecnologias e Dependências

Este projeto foi construído com:

- Python	≥ 3.8
- Django	≥ 4.x
- Bootstrap	5 (estilização)
- SQLite	Banco de dados padrão Django


## Estrutura e Funcionalidades Implementadas

### Autenticação e Permissões
- Sistema de **login, logout e registro** integrado ao banco de dados.
- Controle de acesso baseado em usuário autenticado.
- Navbar dinâmica (Login/Registrar ocultos após autenticação).
- Logout sem página própria, mantendo a navegação integrada à navbar.

### Perfil de Usuário
- Página de **detalhes do perfil**.
- **Edição e exclusão** do perfil do usuário.
- Implementação de **avatar com upload de imagem**.
- Criação automática do profile vinculado ao usuário.
- Tratamento de erros relacionados à inexistência de profile.

### Gestão de Entidades
CRUD completo para:
- **Estudantes**
- **Professores**
- **Cursos**

Funcionalidades:
- Listagem
- Criação
- Detalhes
- Edição
- Exclusão com página de confirmação

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

    
## Arquitetura e Templates

### Herança de Templates
O template base (base.html) contém a estrutura principal de navegação e footer, e é estendido pelos outros templates para reutilização de layout.

### Organização de Templates
- Templates organizados em **subpastas por entidade**.
- Uso de `base.html` para layout padrão.
- Reaproveitamento de componentes (navbar, formulários, etc.).

### Formulários
- Uso de `ModelForm`.
- Integração com Bootstrap para alinhamento e responsividade.
- Upload de arquivos com `enctype="multipart/form-data"`.

### Boas Práticas Aplicadas
- Uso correto de `pk` nas rotas.
- Views protegidas com autenticação.
- Separação clara entre models, views, urls e forms.
- Tratamento de erros comuns do Django (`RelatedObjectDoesNotExist`, `OperationalError`).

## Evolução do Projeto
Ao longo do desenvolvimento, o projeto evoluiu de páginas estáticas para um sistema dinâmico com autenticação, perfis personalizados e CRUD completo, seguindo boas práticas do Django e preparando a base para futuras expansões.


### Bootstrap 5
O estilo visual é feito com classes Bootstrap para responsividade e aparência básica.


## Autor

Leonardo Formaggio

- [github](https://www.github.com/leo-formaggio)
- [LinkedIn](https://www.linkedin.com/in/leonardoformaggio/)