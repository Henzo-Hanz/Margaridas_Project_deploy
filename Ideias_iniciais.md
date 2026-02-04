# Pontapé Inicial 

## A idealização desse projeto será separada em 3 sessões:

- __*Layout/estilo*__

- __*Backend*__

- __*Frontend*__ 

Com o objetivo de criar um gerenciador de senhas amigável com o usuário, com uma alta segurança e confiabilidade, além de uma UI intuitiva e bonita utilizando Python e FastApi para desenvolvimento Web e posteriormente utilizar o comando Flutter ` void main() => runApp(WebApp()); ` e abrir uma janela de navegador para utilizar a aplicação sem necessitar de um versionamento específico da aplicação para mobile (Com ObjetiveC,Swift,etc...). O projeto contará com auxílio de IA para a criação do projeto com modelos de Agentes como Gpt-codex,Sonnet 4.5, Compose 1.0 e etc... Presentes na IDE Cursor, servindo como Projeto "educacional" para se familiariar com a IDE e o uso de agentes de IA no desenvolvimento de projetos.

## __*Layout/estilo*__:
 Conceito inicial de Landing Page do projeto, com uma saudção ao usuário ("Olá Margarida, seja bem vinda ao seu jardim de senhas!") centralizada e grande, com o nome mudando dependendo de usuário pra usuário (na V1 apenas terá 1 usuário então deve ser uma implementação futura ou apenas parcialmente pronta), com um fundo branco ou azul e um "chão" verde e várias flores de cores diferentes (podendo ser aleatórias ou não) e uma pequena animação delas balançando e ao final de um "ciclo" desse uma de suas pétalas se solta dela e sobre, se tornando branca no caminho debaixo pra cima alem de mais arredondada e logo antes de atingir uma certa altura mostra no meio dela strings que aparentemente tenham encriptação e salt (como : "sy$gu89&87eudeu873j@hdj") e após isso, sumirem da tela ao atingir altura máxima de sua janela.

- separar componentes da landing page 

## __*Backend*__:
O Backend deve gerenciar as senhas de modo a "guardar" as senhas de maneira segura e prática, tendo um banco de dados local ou remoto. Além disso,deve, de maneira amigável e prática, providenciar alternativas para o frontend equivalentes a DML e DDL, ou seja pode adicionar senhas novas, editar senhas e/ou apagar senhas que perderam sua função com o tempo,(além de providenciar Backups (podendo ser via nuvem ou outras implementações, como o envio para aplicações de terceiros,como whatsapp,discord,drive e etc )), (\<-parte opicional, deve ter um plano de implementação à parte, visando a segurança dos dados enviados, portanto, a implementação principal deve priorizar no banco de dados local).

- __Definir o banco de dados usado__
    - definir qual sgbd
    - definir a orm usada -> possivelmente SqlAlchemy
    - estudar desempenho e segurança e implementar testes

- __Definir campos das tabelas__
    - modelar db e seus relacionamentos
        - Brmodelo e geradores de estrutura 
        - Alembic para gerenciar as versões e gerar as querys sem uso direto do SQL
            - Criar um model para teste

- __Definir permissões de Usuário e Gerenciamento__

- __Autenticação__
    - FastApi OAuth2 suport
    - InstantDB Magic number auth
    - Autenticações internas e Tokens


- __Deploiment do Serviço__
    - AWS 
    - Vercel
    - Servidor Próprio 

- __Debuggin,segurança e rastreamento__


## __*Frontend*__:

desc

- task
    - subtask 