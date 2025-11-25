# 📚 **Projeto Curso – API com FastAPI + SQLAlchemy Assíncrono**

Este projeto é uma API REST desenvolvida com **FastAPI**, utilizando **SQLAlchemy assíncrono** para interação com um banco de dados PostgreSQL.
A aplicação fornece um CRUD completo para gerenciamento de cursos, seguindo uma arquitetura organizada e escalável.

---

## 🚀 **Tecnologias Utilizadas**

* **Python 3.12+**
* **FastAPI**
* **Uvicorn**
* **SQLAlchemy (async)**
* **PostgreSQL**
* **Pydantic**
* **Asyncpg**

---

## 📁 **Estrutura do Projeto**

```
projeto_curso/
│
├── api/
│   └── v1/
│       ├── api.py               # Define as rotas gerais da versão 1
│       └── endpoints/
│           └── curso.py         # CRUD completo de cursos
│
├── core/
│   ├── configs.py               # Configurações globais (DB_URL, API_V1_STR)
│   ├── database.py              # Conexão com o banco e sessão assíncrona
│   └── deps.py                  # Dependências (get_session)
│
├── models/
│   └── curso_model.py           # Modelo SQLAlchemy do curso
│
├── schemas/
│   └── curso_schema.py          # Schemas Pydantic (create, update, response)
│
├── criar_tabelas.py             # Script para criar tabelas no banco
├── main.py                      # Inicialização da aplicação FastAPI
└── requirements.txt             # Dependências do projeto
```

---

## 🗃️ **Modelo do Curso**

Cada curso possui as seguintes informações:

* **id**: inteiro, gerado automaticamente
* **title**: título do curso
* **number_of_classes**: quantidade de aulas
* **hours**: carga horária

---

## 🔌 **Endpoints Disponíveis**

### ✔ **Criar um curso**

`POST /api/v1/cursos/`

**Body JSON:**

```json
{
  "title": "FastAPI",
  "number_of_classes": 40,
  "hours": 120
}
```

---

### ✔ **Listar todos os cursos**

`GET /api/v1/cursos/`

---

### ✔ **Buscar um curso pelo ID**

`GET /api/v1/cursos/{curso_id}`

---

### ✔ **Atualizar um curso**

`PUT /api/v1/cursos/{curso_id}`

**Body JSON:**

```json
{
  "title": "FastAPI Avançado",
  "number_of_classes": 55,
  "hours": 200
}
```

---

### ✔ **Deletar um curso**

`DELETE /api/v1/cursos/{curso_id}`

---

## 🗄️ **Configuração do Banco de Dados**

A conexão é definida em **core/configs.py**:

```python
DB_URL = "postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco"
```

Certifique-se de:

1. Ter um banco PostgreSQL rodando
2. Substituir as credenciais corretamente
3. Instalar o driver async `asyncpg`

Para criar as tabelas:

```bash
python criar_tabelas.py
```

---

## ▶️ **Como Rodar o Projeto**

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### 2️⃣ Ativar ambiente

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar a API

```bash
uvicorn main:app --reload
```

A aplicação iniciará em:

👉 **[http://localhost:8000](http://localhost:8000)**

### 📌 Documentação automática (Swagger)

👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 🤝 **Contribuições**

Sinta-se à vontade para enviar melhorias, abrir issues ou sugerir novas funcionalidades!

---

## 📜 **Licença**

Este projeto é distribuído sob a licença MIT.
