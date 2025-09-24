# Petshop - Sistema de Gerenciamento de Pets e Serviços

## Descrição

Este projeto é um sistema completo de gerenciamento para petshops, permitindo cadastrar pets, listar, filtrar, remover e registrar serviços adquiridos por cada pet, como banho, tosa, consulta, vacinação, entre outros. O sistema foi desenvolvido com backend em Python utilizando FastAPI e PostgreSQL, e frontend em Angular, consumindo os dados do backend.

## Tecnologias Utilizadas

* **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL
* **Frontend:** Angular, Bootstrap
* **Outros:** Pydantic (validação de dados), CORS habilitado para integração com Angular

## Estrutura do Projeto

```
petshop/
├─ backend/
│  ├─ main.py          # Endpoints do FastAPI
│  ├─ database.py      # Configuração do PostgreSQL
│  ├─ models.py        # Modelos SQLAlchemy
│  ├─ schemas.py       # Schemas Pydantic
│  ├─ crud.py          # Funções de acesso a dados
│  └─ requirements.txt # Dependências Python

├─ frontend/
│  ├─ src/
│  │  ├─ app/
│  │  │  ├─ components/
│  │  │  │  ├─ pet-list/
│  │  │  │  │  ├─ pet-list.component.ts
│  │  │  │  │  └─ pet-list.component.html
│  │  │  │  └─ pet-form/
│  │  │  │     ├─ pet-form.component.ts
│  │  │  │     └─ pet-form.component.html
│  │  │  └─ services/
│  │  │     └─ pet.service.ts
│  │  └─ styles.css
│  └─ angular.json
```

## Banco de Dados

As tabelas principais são `pets` e `servicos`.

```sql
CREATE TABLE pets (
 id SERIAL PRIMARY KEY,
 nome TEXT NOT NULL,
 especie TEXT NOT NULL CHECK (especie IN ('Cachorro','Gato','Outro')),
 tutor TEXT NOT NULL,
 criado_em TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE servicos (
 id SERIAL PRIMARY KEY,
 pet_id INT NOT NULL REFERENCES pets(id) ON DELETE CASCADE,
 descricao TEXT NOT NULL,
 data TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Endpoints do Backend

| Método | Endpoint                     | Descrição                                            |
| ------ | ---------------------------- | ---------------------------------------------------- |
| GET    | /health                      | Health check do sistema                              |
| GET    | /pets?busca=\&especie=       | Listar pets com busca por nome ou filtro por espécie |
| POST   | /pets                        | Cadastrar novo pet                                   |
| DELETE | /pets/{id}                   | Remover pet                                          |
| POST   | /pets/{id}/servicos          | Adicionar serviço a um pet                           |
| GET    | /pets/{id}/servicos?limite=5 | Listar últimos serviços de um pet                    |

## Como Rodar o Backend

1. Instalar PostgreSQL e criar banco de dados:

```sql
CREATE DATABASE petshop;
CREATE USER usuario WITH ENCRYPTED PASSWORD 'senha';
GRANT ALL PRIVILEGES ON DATABASE petshop TO usuario;
```

2. Criar ambiente virtual e instalar dependências:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar string de conexão em `database.py`:

```python
DATABASE_URL = "postgresql://usuario:senha@localhost:5432/petshop"
```

4. Rodar servidor FastAPI:

```bash
uvicorn main:app --reload
```

5. Testar health check: `http://localhost:8000/health`

## Como Rodar o Frontend

1. Navegue até a pasta frontend e instale dependências:

```bash
cd frontend
npm install
```

2. Certifique-se de que `FormsModule`, `ReactiveFormsModule` e `HttpClientModule` estão importados em `app.module.ts`.
3. Rodar Angular:

```bash
ng serve
```

4. Acesse `http://localhost:4200/` no navegador.

## Funcionalidades do Sistema

### Pets

* Cadastro de pets com validação de campos (nome, espécie, tutor).
* Listagem em tabela com busca por nome e filtro por espécie.
* Remoção de pets com confirmação.

### Serviços

* Adicionar serviços a um pet (descrição).
* Listar últimos serviços adquiridos de um pet (limitado a 5, ajustável via query string).
* Modal no frontend mostrando histórico de serviços de cada pet.

## Observações

* O backend utiliza CORS liberado para qualquer origem durante o desenvolvimento.
* Ao excluir um pet, todos os serviços relacionados são removidos automaticamente (cascade).
* A interface frontend é responsiva utilizando Bootstrap.
* Todos os dados são persistidos no PostgreSQL, garantindo integridade referencial.

## Contato

Para dúvidas ou sugestões, entre em contato com o desenvolvedor responsável.
