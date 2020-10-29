# Task Tracking

Sistema Web para Monitoramento de Tarefas em Projetos.

## Documentação

Documentação do Projeto.

* [Documento de Visão](docs/doc-visao.md)

## Desenvolvimento

Passo a passo para preparar o ambiente de desenvolvimento.

### Criar o Ambiente Virtual (Opcional)

### Instalar dependência do projeto

```shell
pip install -r requirements.txt
```

### Executar as migrações

```shell
python manage.py makemigrations
python manage.py migrate
```

### Executar servidor de teste

```
python manage.py runserver
```

### Configure o Python Interpreter no VSCode

Ctrl + Shift + P → Python: Select Interpreter
    → escolha um dos interpretadores que aparecer na lista:

![VSCode](https://i.stack.imgur.com/XQEku.gif)

fonte: [Stack Overflow](https://stackoverflow.com/questions/53939751/pylint-unresolved-import-error-in-visual-studio-code)