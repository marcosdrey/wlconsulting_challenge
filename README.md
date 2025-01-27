# Desafio de Código Back-End

Este projeto faz parte do desafio de código back-end [WL Consulting](https://github.com/WL-Consultings/challenges/tree/main/backend).

## Pré-requisitos

Antes de começar a usar a aplicação, siga os passos abaixo para configurar o ambiente e rodar o projeto localmente.

### 1. Instalar o Ambiente Virtual

Crie um ambiente virtual com o comando:

```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

### 3. Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e siga as nomenclaturas descritas no arquivo `.env.example`. Insira os valores de acordo com o seu banco de dados no PostgreSQL.

### 4. Realizar as Migrações

Após configurar o ambiente, execute as migrações para preparar o banco de dados:

```bash
python manage.py migrate
```

### 5. Popular o Banco de Dados (Opcional)

Se desejar, você pode popular o banco de dados com dados fictícios utilizando o script de popularação:

```bash
python manage.py populate_database
```

### 6. Criar o Superusuário

Para acessar o painel de administração, crie um superusuário com o comando:

```bash
python manage.py createsuperuser
```

### 7. Rodar o Servidor

Agora, inicie o servidor de desenvolvimento para explorar a API:

```bash
python manage.py runserver
```
## Tecnologias Utilizadas

- **Django**: Framework principal para desenvolvimento da API.
- **Django Rest Framework (DRF)**: Para construção de endpoints e consumo de dados em JSON.
- **PostgreSQL**: Banco de dados relacional.
- **JWT**: Autenticação via JSON Web Token.
- **Docker**: Para conteinerização do projeto.
- **Flake8**: Para garantir a qualidade do código.

## Como Executar com Docker

Caso prefira rodar o projeto dentro de containers Docker, siga os passos abaixo:

1. **Construir as imagens Docker**:

   ```bash
   docker-compose build
   ```

2. **Subir os containers**:

   ```bash
   docker-compose up
   ```

3. **Acessar a aplicação**:

   A aplicação estará disponível em `http://localhost:8000`.
