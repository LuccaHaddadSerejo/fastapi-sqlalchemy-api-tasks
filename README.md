# Enxerto-Agro-teste V2

 1. Instale o seu ambiente virtual com o seguinte comando: **python -m venv venv**
 2. Entre no seu ambiente virtual com o comando: **source venv/Scripts/activate (windows)** ou **source venv/Bin/activate (linux)**
 3. Instale as dependências do projeto que estão no arquivo requirements.txt com o comando: **pip install -r requirements.txt**
 4. A API foi desenvolvida em  **PostgreSQL**. Para iniciar basta criar e configurar um arquivo  **.env** na raiz do projeto com base no arquivo  **.env.example**. Não se esqueça de criar o database com o mesmo nome que colocar no .env
 5. Faça a migração das models com o seguinte comando: **alembic upgrade head**
 6. **Somente o ADMIN consegue criar outros usuários. O ADMIN é criado junto com as tabelas do banco de dados**
 7. Credenciais do ADMIN > **username: admin | password: admin1234**

## Requisitos do Serviço

Esse serviço possui uma API REST para criar, listar, atualizar e deletar os dados do banco de dados.

- O banco de dados utilizado foi  o **PostgreSQL**.
- Foi desenvolvido com FastAPI, SQLalchemy, Pydantic e Alembic

## Endpoints do serviço

| Método | Endpoint             | Responsabilidade                               | Permissão           |
| ------ | -------------------- | ---------------------------------------------- | ------------------- |
| POST   | /login               | Faz login do usuário                           | N/A                 |
| POST   | /user                | Cria um novo usuário                           | Somente Admin       |
| GET    | /user                | Lista todos os usuários                        | Somente Admin       |
| GET    | /user/id             | Lê um usuário com base no ID                   | Somente Admin       |
| PATCH  | /user/id             | Atualiza um usuário                            | Somente Admin       | 
| DELETE | /user/id             | Deleta um usuário                              | Somente Admin       |
| POST   | /task                | Cria uma task                                  | Admin e Manager     |
| GET    | /task                | Lista todas as tasks                           | Admin e Manager     |
| GET    | /task/list/todo      | Lista todas as tasks com status = "todo"       | Usuário autenticado |
| GET    | /task/id             | Lê uma task com base no ID                     | Usuário autenticado |
| PATCH  | /task/id             | Atualiza uma task                              | Admin e Manager     |
| DELETE | /task/id             | Deleta uma task                                | Admin e Manager     |
| DOCS   | /docs                | Acesso a documentação                          | N/A                 |
