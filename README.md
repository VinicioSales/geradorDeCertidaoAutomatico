# Documentação do Projeto gerador_de_certidao_GRANDE_ORIENTE_DO_BRASIL

## Introdução
 - Gera certidões baseada no status de contas a receber de cada cliente

**Tecnologias utilizadas:**
	**1. FrontEnd**	
 - Linguagens: HTML, CSS, JavaScript
 
 **2. BackEnd**
 - Linguagens: Python
 - Framework: Flask
 - Bibliotecas: os, qrcode, datetime, PIL, reportlab, json, requests, threading, webbrowser, oauth2client
 
**3. Controle de Versão**
-    Git: Utilizado para o controle de versão do código-fonte
-   GitHub: Plataforma online para hospedar o repositório Git e colaboração em equipe

 **4. Ambiente de Desenvolvimento**

-   IDE (Integrated Development Environment): Visual Studio Code
-   Venv: Utilizado para isolar o ambiente de desenvolvimento Python

**5. Implantação**

-   Executável colocal (.exe)

# Backend

## Visão Geral

O backend do projeto consiste em um servidor Flask que fornece rotas para gerar certidões e obter informações relacionadas a clientes.

## Descrição do backend do projeto

O backend é responsável por fornecer as funcionalidades necessárias para gerar certidões positivas, certidões negativas e certidões positivas com efeito negativo de débitos. Além disso, o backend também permite obter informações sobre os clientes cadastrados.

## Linguagem de programação e framework utilizados

O backend do projeto foi desenvolvido utilizando a linguagem de programação Python e o framework Flask.

## Estrutura de pastas e arquivos principais

A estrutura de pastas e arquivos principais do backend do projeto é a seguinte:
	src
└── backEnd
    ├── server.py
    ├── funcs
    │   └── geradores.py
    └── modules
        ├── api
        │   ├── clientes.py
        │   ├── financas.py
        │   └── google.py
        └── funcs
            └── funcs.py

-   **src/backEnd/fonts**: Pasta que armazena arquivos de fontes utilizadas no projeto.
    
-   **src/backEnd/funcs/geradores.py**: Arquivo que contém funções relacionadas à geração de dados ou elementos no backend.
    
-   **src/backEnd/img**: Pasta que armazena arquivos de imagens utilizadas no projeto.
    
-   **src/backEnd/modules/api/clientes.py**: Arquivo que contém módulo/API responsável por lidar com as operações relacionadas aos clientes.
    
-   **src/backEnd/modules/api/financas.py**: Arquivo que contém módulo/API responsável por lidar com as operações relacionadas às finanças.
    
-   **src/backEnd/modules/api/google.py**: Arquivo que contém módulo/API responsável por integração com serviços do Google.
    
-   **src/backEnd/modules/data/credenciais.py**: Arquivo que contém módulo responsável por armazenar e gerenciar credenciais no projeto.
    
-   **src/backEnd/modules/funcs/funcs.py**: Arquivo que contém funções utilitárias e auxiliares utilizadas no backend.
    
-   **src/backEnd/modules/caminhos.py**: Arquivo que contém módulo responsável por definir os caminhos e rotas utilizados no projeto.
    
-   **src/backEnd/static/cores.py**: Arquivo que contém definições e constantes relacionadas às cores utilizadas no projeto.
    
-   **src/backEnd/static/fonts.py**: Arquivo que contém definições e constantes relacionadas às fontes utilizadas no projeto.
    
-   **src/backEnd/static/img.py**: Arquivo que contém definições e constantes relacionadas às imagens utilizadas no projeto.
    
-   **src/backEnd/credenciais_parceiro.json**: Arquivo JSON que armazena as credenciais do parceiro.
    
-   **src/backEnd/server.py**: Arquivo principal que contém o código do servidor Flask e define as rotas do projeto.


## Dependências e gerenciamento de pacotes

O backend do projeto utiliza as seguintes dependências:

-   Flask: Framework web utilizado para criar a aplicação.
-   Pillow: Biblioteca para manipulação de imagens.
-   ReportLab: Biblioteca para geração de PDFs.
-   qrcode: Biblioteca para geração de QR codes.
-   gspread: Biblioteca para interação com o Google Sheets.
-   oauth2client: Biblioteca para autenticação no Google API.

As dependências são gerenciadas utilizando o gerenciador de pacotes `pip`. Você pode instalar as dependências executando o seguinte comando no terminal:
- pip install Flask Pillow reportlab qrcode gspread oauth2client

Certifique-se de ter o Python e o pip instalados em seu ambiente de desenvolvimento.

##  API

Esta documentação descreve as APIs disponíveis no backend do projeto.

**Índice**

Endpoint

Método

Descrição

`/`

GET

Retorna a página inicial

`/gerar_certidao`

POST

Gera a certidão

`/get_nome_clientes`

GET

Obtém a lista de nomes de clientes

## `/`

Endpoint: `/`

Método: GET

Descrição: Retorna a página inicial.

Retorno:

-   Tipo: string
-   Descrição: O conteúdo da página inicial.

## `/gerar_certidao`

Endpoint: `/gerar_certidao`

Método: POST

Descrição: Rota para gerar a certidão.

Parâmetros:

-   `status` (string, obrigatório): O status de acesso (valor "liberado" para permitir o acesso).

Retorno:

-   Tipo: dict
-   Descrição: O objeto JSON contendo a mensagem de resposta.

Exemplo de uso:

bashCopy code

`curl -X POST -H "Content-Type: application/json" -d '{"status":"liberado"}' http://localhost:5000/gerar_certidao` 

## `/get_nome_clientes`

Endpoint: `/get_nome_clientes`

Método: GET

Descrição: Rota para obter a lista de nomes de clientes.

Retorno:

-   Tipo: dict
-   Descrição: O objeto JSON contendo a lista de nomes de clientes.

Exemplo de uso:

bashCopy code

`curl -X GET http://localhost:5000/get_nome_clientes`

## Autenticação e Autorização
- Utilizado planilha google sheets para liberação do acesso
- Arquivo: src\backEnd\modules\api\google.py
- A liberação é feita quando existe a string "liberado", retirado da Google Sheets.
- Conta Google: Parceiro
- Planilha: acesso
- Aba: gerador_de_certidao_GRANDE_ORIENTE_DO_BRASIL
- Célula: A2
-  Liberado:
	| status |  |
	|--|--|
	| liberado |  |
- Bloquado
	| status |  |
	|--|--|
	| [any]|  |

# Frontend

Esta documentação descreve o frontend do projeto.

## Visão Geral

O frontend do projeto é responsável pela interface de usuário e interação com o usuário. Ele é desenvolvido utilizando as seguintes tecnologias:

-   Linguagens: HTML, CSS, JavaScript
-   Frameworks/Bibliotecas: N/A

## Estrutura de Pastas e Arquivos Principais

A estrutura de pastas e arquivos principais do frontend é a seguinte:


src/
└── frontEnd/
    ├── static/
    │   ├── scripts/
    │   │   └── index.js
    │   └── styles/
    │       └── index.css
    └── templates/
        └── index.html 

-   `src/frontEnd/static/scripts/index.js`: Arquivo JavaScript responsável pela lógica e interação da página.
-   `src/frontEnd/static/styles/index.css`: Arquivo CSS que define o estilo da página.
-   `src/frontEnd/templates/index.html`: Arquivo HTML que contém a estrutura da página.

## Dependências e Gerenciamento de Pacotes

O frontend do projeto não possui dependências externas ou gerenciamento de pacotes específico.

## Telas e Componentes

### Tela Inicial

Descrição: A tela inicial exibe o formulário de geração de certidão.

Componentes:

-   Logo
-   Formulário de geração de certidão

### Componentes Reutilizáveis

-   Nenhum componente reutilizável foi identificado no frontend do projeto.

## Fluxo de Navegação

O fluxo de navegação do frontend é simples:

1.  O usuário acessa a página inicial.
2.  O usuário preenche o formulário com a razão social e clica no botão "Gerar Certidão".
3.  A ação é processada pelo backend e uma certidão é gerada.
4.  O resultado é exibido na página ou uma mensagem de erro é mostrada em caso de falha.

Por favor, note que o frontend se comunica com o backend por meio de chamadas de API, que são processadas pelo backend para retornar os resultados esperados.

# Como Executar o Projeto

Esta seção descreve os passos necessários para executar o projeto.

## Pré-requisitos

Antes de executar o projeto, verifique se o seguinte software está instalado no seu sistema:

-   Python 3.x

## Passos para instalação

1.  Faça o download ou clone o repositório do projeto para o seu computador.
2.  Navegue até o diretório raiz do projeto.

## Configuração do ambiente

1.  Crie um ambiente virtual (opcional, mas recomendado):
    
    -   Abra o terminal ou prompt de comando.
    -   Execute o seguinte comando para criar um ambiente virtual:
    `python -m venv venv`
    
	 -  Ative o ambiente virtual:
		-   No Windows:
		- `venv\Scripts\activate`
		- No macOS e Linux:
		- `source venv/bin/activate`
2. Instale as dependências:

-   Execute o seguinte comando para instalar as dependências necessárias:
- `pip install -r requirements.txt`

## Comandos para execução

Existem duas formas de executar o projeto:

### Método 1: Executar `server.py` diretamente

1.  Navegue até o diretório `src/backEnd/` do projeto.
2.  Execute o seguinte comando:
	`python server.py`	
3.  O servidor será iniciado e o navegador será aberto com o frontend do projeto.

### Método 2: Executar `executar.py`

1.  Navegue até o diretório raiz do projeto.
2.  Execute o seguinte comando
 `python executar.py`
 3.  O servidor será iniciado em segundo plano e o navegador será aberto com o frontend do projeto.
