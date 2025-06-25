# Invista-Me 💰

Um sistema de gerenciamento de investimentos desenvolvido em Django, permitindo aos usuários registrar, visualizar e gerenciar seus investimentos de forma simples e intuitiva.

## 📋 Funcionalidades

- **Autenticação de Usuários**
  - Registro de novos usuários
  - Login e logout
  - Sistema de sessões

- **Gerenciamento de Investimentos**
  - Cadastro de novos investimentos
  - Visualização de lista de investimentos
  - Detalhes de cada investimento
  - Edição de investimentos existentes
  - Exclusão de investimentos

- **Interface Responsiva**
  - Design moderno com Bootstrap 5
  - Navbar dinâmica baseada no status de autenticação
  - Formulários estilizados com Django Crispy Forms

## 🚀 Tecnologias Utilizadas

- **Backend**: Django 5.2.2
- **Frontend**: Bootstrap 5.3.0
- **Banco de Dados**: SQLite (desenvolvimento)
- **Formulários**: Django Crispy Forms
- **Styling**: Crispy Bootstrap5

## 📁 Estrutura do Projeto

```
projeto_invistame/
├── invistame/                 # App principal (investimentos)
│   ├── models.py             # Modelo Investimento
│   ├── views.py              # Views para CRUD de investimentos
│   ├── forms.py              # Formulários
│   └── templates/            # Templates HTML
├── usuarios/                 # App de usuários
│   ├── views.py              # Views de autenticação
│   ├── forms.py              # Formulário de registro
│   └── templates/            # Templates de login/logout
├── projeto_abidu/            # Configurações do projeto
│   ├── settings.py           # Configurações Django
│   └── urls.py               # URLs principais
└── manage.py                 # Script de gerenciamento Django
```

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd projeto_invistame
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente virtual**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Instale as dependências**
   ```bash
   pip install django
   pip install django-crispy-forms
   pip install crispy-bootstrap5
   ```

5. **Execute as migrações**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

8. **Acesse a aplicação**
   Abra seu navegador e vá para `http://127.0.0.1:8000`

## 📊 Modelo de Dados

### Investimento
- `id`: Identificador único
- `investimento`: Nome/tipo do investimento (TextField)
- `valores`: Valor investido (FloatField)
- `pago`: Status de pagamento (BooleanField)
- `data`: Data do investimento (DateField)
- `nivel`: Nível de risco (CharField com choices)

## 🎯 Como Usar

1. **Registro**: Crie uma conta através do link "Fazer cadastro"
2. **Login**: Faça login com suas credenciais
3. **Adicionar Investimento**: Clique em "Registrar Investimento" para adicionar um novo investimento
4. **Visualizar**: Veja todos seus investimentos na página principal
5. **Gerenciar**: Use os botões de Detalhe, Editar ou Excluir para gerenciar seus investimentos

## 🔧 Configurações

### Bootstrap e Crispy Forms
O projeto utiliza Bootstrap 5 para estilização e Django Crispy Forms para renderização de formulários. As configurações estão em `settings.py`:

```python
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

### Redirecionamentos
- **Login**: Redireciona para a página de investimentos
- **Logout**: Mostra página de confirmação

## 📝 Licença

Este projeto é desenvolvido para fins educacionais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através do GitHub.