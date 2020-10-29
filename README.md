# Task Tracking

Sistema Web para Monitoramento de Tarefas em Projetos.

## Documentação

Documentação do Projeto.

* [Documento de Visão](docs/doc-visao.md)

## Desenvolvimento

Passo a passo para preparar o ambiente de desenvolvimento.

### Criar o Ambiente Virtual (Opcional)

### Instalar dependência do projeto

```bash
pip install -r requirements.txt
```

### Executar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### Executar servidor de teste

```bash
python manage.py runserver
```

### Configure o Python Interpreter no VSCode

Ctrl + Shift + P → Python: Select Interpreter
    → escolha um dos interpretadores que aparecer na lista:

![VSCode](https://i.stack.imgur.com/XQEku.gif)

fonte: [Stack Overflow](https://stackoverflow.com/questions/53939751/pylint-unresolved-import-error-in-visual-studio-code)

#### Unresolved import warnings

Erro de imports no **Pylance - VSCode** são causados pela ausência de um diretório **src/**. Como o projeto segue o estilo Django, não tem diretório **src/**, talvez devessemos criar???.

Para resolver precisamos ensinar os diretórios extras para o vscode analisar:

```json
{
    "python.analysis.extraPaths": ["./sources"]
}
```

fonte: [PyLance](https://github.com/microsoft/pylance-release/blob/master/TROUBLESHOOTING.md#unresolved-import-warnings)
