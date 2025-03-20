# Projeto Django Blog

## Descrição
Este projeto é um aplicativo web estilo blog desenvolvido com Django. Ele inclui funcionalidades como:
- Página inicial (home)
- Página "Sobre"
- Listagem e detalhe dos posts
- CRUD de posts
- Sistema de autenticação (login, logout, registro)
- Perfil do usuário com edição e alteração de senha
- Sistema de mensagens entre usuários

## Instruções de Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Acesse a pasta do projeto:
   ```bash
   cd seu-repositorio

3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv env
   env\Scripts\activate

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt

5. Instale as dependências:
   ```bash
   python manage.py migrate

6. Inicie o servidor:
   ```bash
   python manage.py runserver

## Como Executar o Servidor Localmente
Após seguir as instruções acima, abra o navegador e acesse: http://127.0.0.1:8000

## Funcionalidades Implementadas
Página inicial e "Sobre"
CRUD de posts com visualização de listagem e detalhes
Autenticação e gerenciamento de perfil
Sistema de mensagens entre usuários