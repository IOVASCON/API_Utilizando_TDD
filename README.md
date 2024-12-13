# API de Seguros e Planos de Aposentadoria

Este projeto consiste em uma API desenvolvida com FastAPI para gerenciar seguros e planos de aposentadoria.

## Requisitos

- Python 3.12+
- Poetry para gerenciamento de dependências
- SQLite como banco de dados local

## Como usar

### Clonar o repositório

git clone <URL_DO_REPOSITORIO>
cd app_local_tdd

## Configurar o ambiente

1. Instale o Poetry:

    pip install poetry

2. Instale as dependências:

    poetry install

3. Ative o ambiente virtual:

    poetry shell

## Executar o servidor

Para iniciar o servidor, execute:

poetry run uvicorn store.main:app --reload

A API estará disponível em <http://127.0.0.1:8000>.

## Endpoints disponíveis

    /insurance/: Lista de seguros fictícios.
    /retirement/: Lista de planos de aposentadoria fictícios.

## Documentação da API

1. Swagger UI
2. ReDoc

## Estrutura do projeto

    app_local_tdd/
    ├── store/
    │   ├── controllers/
    │   │   ├── insurance.py
    │   │   └── retirement.py
    │   ├── core/
    │   │   ├── config.py
    │   │   └── database.py
    │   ├── models/
    │   ├── routers/
    │   │   └── __init__.py
    │   ├── main.py
    ├── README.md
    ├── pyproject.toml
    ├── .gitignore

## Imagens do Desenvolvimento do Projeto

Abaixo estão as imagens capturadas durante o desenvolvimento do projeto:

### 1. Configuração do Ambiente Virtual

![Ambiente Virtual Local](img_dev/Ambiente_Virtual_Local.PNG)

### 2. Ativação do Ambiente Virtual Local

![Ativando Ambiente Virtual Local](img_dev/Ativando_Ambiente_Virtual_Local.PNG)

### 3. Configuração das Bibliotecas

![Configurando Demais Bibliotecas](img_dev/Configurando_Demais_Bibliotecas.PNG)

### 4. Estrutura do Projeto

![Estrutura do Projeto](img_dev/Estrutura_Projeto.PNG)

### 5. Instalação das Bibliotecas com Poetry

![Instalação das Bibliotecas](img_dev/Instalacao_bibliotecas_install.PNG)

### 6. Ambiente Virtual no Python

![Python Ambiente Virtual](img_dev/Python_Ambiente_Virtual.PNG)

### 7. Gerando o `poetry.lock`

![Regenerando poetry.lock](img_dev/Regenerando_poetry_lock.PNG)

### 8. Script de Criação da Estrutura

![Script Criação Estrutura](img_dev/Script_Criacao_Estrutura.PNG)

### 9. Mensagem de Boas-Vindas no Servidor

![Servidor Boas-Vindas](img_dev/Servidor_Boas_Vindas.PNG)

### 10. Documentação da API

![Servidor Documentação](img_dev/Servidor_Documentacao.PNG)

### 11. Endpoint `/insurance`

![Servidor Insurance](img_dev/Servidor_insurance.PNG)

### 12. Endpoint `/retirement`

![Servidor Retirement](img_dev/Servidor_retirement.PNG)

## Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests. Feedbacks e melhorias são sempre bem-vindos!

## Licença

MIT
