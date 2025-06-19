
````markdown
# FastAPI Todo API

A simple **Todo List REST API** built with **FastAPI** and **MySQL** using async database operations.

---

## Features

- Create, Read, Update, Delete (CRUD) todo items
- Async interaction with MySQL database using `databases` and `SQLAlchemy`
- Data validation with Pydantic models
- CORS enabled for frontend integration
- Clear error handling with HTTP status codes

---

## Tech Stack

- **Python 3.10+**
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework
- [Uvicorn](https://www.uvicorn.org/) – ASGI server
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM & database schema management
- [Databases](https://www.encode.io/databases/) – Async database support
- **MySQL** – Relational database
- [Pydantic](https://pydantic.dev/) – Data validation
- [aiomysql](https://github.com/aio-libs/aiomysql) – Async MySQL driver

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-todo.git
   cd fastapi-todo
````

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Setup your MySQL database and update the `DATABASE_URL` environment variable:

   ```
   mysql+aiomysql://username:password@host:port/database_name
   ```

---

## Environment Variables

Set environment variables before running:

* `DATABASE_URL` – Async connection string for MySQL database

Example:

```bash
export DATABASE_URL="mysql+aiomysql://root:password@localhost:3306/todos"
```

---

## Running the App

Start the FastAPI server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be accessible at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| GET    | `/`                | Health check / welcome message |
| POST   | `/items`           | Create a new todo item         |
| GET    | `/items`           | Get list of todo items         |
| GET    | `/items/{item_id}` | Get a specific todo item       |
| PUT    | `/items/{item_id}` | Update a todo item             |
| DELETE | `/items/{item_id}` | Delete a todo item             |

---

## Project Structure

```
app/
├── main.py           # FastAPI app and routes
├── models.py         # SQLAlchemy table definition
├── schemas.py        # Pydantic models
├── database.py       # Database connection and metadata
requirements.txt      # Python dependencies
```

---

## Notes

* Make sure your MySQL server is running and accessible.
* The API supports asynchronous operations for performance.
* CORS middleware is enabled to allow frontend apps to consume this API.

---

## License

This project is licensed under the MIT License.

---

Feel free to contribute or open issues!

---

```

If you want, I can also help you generate a `requirements.txt` or Dockerfile!
```
