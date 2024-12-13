# Criação da Estrutura do projeto

um script shell (script.sh) para criar a estrutura de pastas e arquivos inicial para o desafio no novo diretório L:\VSCode\PYTHON\DIO\APP_local_TDD.

## Script

    #!/bin/bash

    # Definir o diretório base
    BASE_DIR="L:/VSCode/PYTHON/DIO/APP_local_TDD"

    # Criar diretório base
    mkdir -p "$BASE_DIR"
    cd "$BASE_DIR"

    # Criar a estrutura de pastas
    mkdir -p store/{controllers,models,routers,core}
    touch store/{__init__.py,controllers/__init__.py,models/__init__.py,routers/__init__.py,core/__init__.py}

    # Criar arquivos principais
    touch store/controllers/{insurance.py,retirement.py}
    touch store/models/{insurance.py,retirement.py}
    touch store/core/{config.py,exceptions.py}
    touch store/routers/__init__.py

    touch store/main.py

    # Criar arquivos de configuração principais
    touch .gitignore README.md pyproject.toml poetry.lock

    echo "Estrutura de projeto criada em: $BASE_DIR"

### execução

Conceda permissões de execução ao script (caso necessário):

chmod +x script.sh

Execute o script:

./script.sh

Após a execução, o script criará a estrutura no diretório especificado (L:/VSCode/PYTHON/DIO/APP_local_TDD). Use o explorador de arquivos ou o terminal para verificar.
