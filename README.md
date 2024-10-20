# Flask-Database

## Descrição

Este é um projeto básico de gerenciamento de banco de dados usando Flask e SQLite, estruturado de forma modular para fácil manutenção e escalabilidade. O projeto inclui funcionalidades de transação, configurações dinâmicas, rotas e modelos integrados com um sistema de banco de dados SQLite.

## Pré-requisitos

Python 3.x

Virtualenv

Flask

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente e executar o projeto localmente.

### 1. Clonar o Repositório

````
git clone https://github.com/m4n1nh0/Flask-database.git
cd Flask-database
````
### 2. Criar e Ativar um Ambiente Virtual

Crie o ambiente virtual para isolar as dependências do projeto.

````
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual (Linux/MacOS)
source .venv/bin/activate

# Ativar o ambiente virtual (Windows)
.venv\Scripts\activate
````

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt.

````
pip install -r requirements.txt
````

### 4. Configurar Variáveis de Ambiente

Certifique-se de configurar suas variáveis de ambiente (por exemplo, detalhes de conexão com o banco de dados) no arquivo .env. Um exemplo básico de como deve ser o arquivo .env para usar SQLite:

````
FLASK_APP=settings.flask_app
FLASK_ENV=development
DATABASE_URL=sqlite:///seu_banco_de_dados.db
````

Por padrão, o SQLite cria um arquivo de banco de dados local. Se o arquivo seu_banco_de_dados.db não existir, ele será criado automaticamente na raiz do projeto.

### 5. Inicializar o Banco de Dados

Execute os comandos de migração do banco de dados, se aplicável, para configurar o SQLite.

````
flask db upgrade
````

Caso você não utilize migrações automáticas, poderá criar o banco de dados manualmente, garantindo que ele esteja pronto para uso.

### 6. Executar a Aplicação

Para iniciar o servidor Flask, execute o comando abaixo:

````
flask run
````

A aplicação estará disponível em http://127.0.0.1:5000/.


## Estrutura do Projeto

* database/: Configurações do banco de dados e sessão.

* model/: Modelos de dados, definindo a estrutura das entidades do banco.

* routes/: Definição das rotas (endpoints) da aplicação.

* settings/: Configurações do Flask e da aplicação.

* main.py: Ponto de entrada da aplicação.

## Testes

Para rodar os testes (se houverem), utilize o comando:

````
pytest
````

## Contribuições

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nome-da-feature).
3. Faça commit de suas alterações (git commit -m 'Adiciona nova feature').
4. Envie para a branch original (git push origin feature/nome-da-feature).
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
