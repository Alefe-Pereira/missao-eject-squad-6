# 🚀 Missão EJECT 2026.1 — Squad 6

Projeto desenvolvido como parte do desafio técnico da **EJECT — Empresa Júnior da ECT/UFRN**.

## 👥 Identificação do Squad

**Squad 6**

| Nome | Função |
|------|--------|
| Alefe Pereira | Front-end |
| Pedro Alves | Back-end |
| Arthur | Back-end |

## 🔗 Links

- 🖥️ **Repositório Front-end:** https://github.com/Alefe-Pereira/missao-eject-squad-6
- ⚙️ **Repositório Back-end:** https://github.com/PedroGH96/missao-eject-squad-6
- 🌐 **Deploy:** https://pedrogh96.pythonanywhere.com

## 📋 Sobre o Projeto

Site do **Restaurante Apollo** — uma aplicação web desenvolvida com Django no back-end e HTML/CSS/JS no front-end.

### Funcionalidades

- Homepage com destaques dinâmicos
- Blog com listagem e leitura de artigos
- Sistema de reservas
- Página Sobre Nós
- Painel administrativo para gerenciamento de conteúdo

## 🛠️ Tecnologias

- Python 3.14
- Django 6.0
- SQLite
- HTML5, CSS3, JavaScript
- PythonAnywhere (deploy)

## ⚙️ Como rodar localmente

```bash
# Clonar o repositório
git clone https://github.com/PedroGH96/missao-eject-squad-6.git
cd missao-eject-squad-6

# Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Rodar as migrations
python manage.py migrate

# Popular o banco com dados iniciais
python manage.py seed

# Criar superusuário
python manage.py createsuperuser

# Rodar o servidor
python manage.py runserver
```

## 🧪 Testes

```bash
python manage.py test restaurante
```

13 testes unitários cobrindo models, views e regras de negócio.

## 📁 Estrutura do Projeto

```
missao-eject-squad-6/
├── assets/          # CSS, JS e imagens do front-end
├── core/            # Configurações do Django
├── restaurante/     # App principal
│   ├── models.py    # Modelos do banco de dados
│   ├── views.py     # Lógica das páginas
│   ├── admin.py     # Configuração do admin
│   ├── tests.py     # Testes unitários
│   ├── templates/   # Templates HTML dinâmicos
│   └── management/  # Comandos customizados (seed)
├── manage.py
└── requirements.txt
```
