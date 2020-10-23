# Documento de Visão

Sistema Web para Monitoramento de Tarefas em Projetos. Nele é possível criar tarefas, controlar o tempo de execução da tarefa, planejar, gerenciar e fechar tarefas.

## Equipe

Membro     |     Papel              |   E-mail             | github         |
---------  | ---------------------- | -------------------- | -------------- |
Taciano    | Cliente Professor      | tacianosilva@gmail.com  | tacianosilva               |
Arthur     | Analista, Dev e Tester | jonasfariasantos@hotmail.com | Jonasfaria |
Jonas      | Analista, Dev e Tester |          |                |
Pedro      | Analista, Dev e Tester |          |                |
Wanessa    | Analista, Dev e Tester |          |                |

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Ator/Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Gerente | Este usuário pode criar projetos, cadastrar uma equipe, cadastrar e gerenciar tarefas da equipe. Pode ver relatórios das tarefas e da equipe.
Usuário Membro | Este usuário pode cadastrar suas tarefas, executá-las, e ver relatórios sobre suas tarefas.

## Lista de Requisitos Funcionais

Requisito                    | Descrição   | Ator       |
---------                    | ----------- | ---------- |
RF001 - Cadatrar Usuário     | Um usuário pode se auto-cadastrar ou ser cadastrado. Um usuário tem código, nome, e-mail, github, senha | Administrador, Gerente, Usuário |
RF002 - Alterar Usuário     | Um usuário pode alterar seus dados. | Administrador, Gerente, Usuário |
RF003 - Consultar Usuários   | Consulta de todos os usuários com filtros. | Administrador, Gerente, Usuário |
RF004 - Vizualizar Usuário     | Um usuário pode vizualizar os detalhes do seus usuário. | Administrador, Gerente, Usuário   |
RF005 - Excluir Usuário     | Um usuário pode ser excluido ou pode apagar seu cadastrado. | Administrador, Gerente, Usuário |
RF006 - Cadatrar Tarefa     | Um usuário pode cadastrar tarefas. Um tarefa tem código, identificador, nome, descrição, links, data de criação, status (Planejada, Em Execução, Concluída, Cancelada), execuções (histórico de execuções), usuário, tags | Administrador, Gerente, Usuário |
RF007 - Alterar Tarefa     | Um usuário pode alterar suas tarefas. | Administrador, Gerente, Usuário |
RF008 - Consultar Tarefas     | Um usuário pode consultar todas as suas tarefas. | Administrador, Gerente, Usuário   |
RF009 - Vizualizar Tarefa     | Um usuário pode selecionar uma tarefa para vizualizar os detalhes. | Administrador, Gerente, Usuário   |
RF010 - Excluir Tarefa     | Um usuário pode excluir tarefas. | Administrador, Gerente, Usuário |
RF011 - Vizualizar Tarefas do Usuário | Um usuário pode vizualizar a lista de todas suas tarefas e selecionar uma tarefa para vizualizar os detalhes. | Administrador, Gerente, Usuário   |
