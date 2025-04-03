<h1> 📦 Installation and Startup</h1>

## 🛠 Pre-requisites
1. Install [PostgreSQL](https://www.postgresql.org/download/) and create a database
2. Ensure Python 3.8+ is installed

## 🔧 Installation
```bash
# Create virtual environment
python -m venv venv
# Activate environment (Linux/macOS)
source venv/bin/activate
# Activate environment (Windows)
.\venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
```

### Environment Configuration
Create a `.env` file in the project root with:
```python
DATABASE_URL=postgresql://username:password@localhost/book_db
FLASK_APP=__init__.py
FLASK_ENV=development
```

### Database Setup
```bash
# Initialize migrations (run once)
flask db init
# Create migration
flask db migrate -m "Initial migration"
# Apply migrations
flask db upgrade
```

### 🚀 Launch Application
```bash
flask run
```
Application will be available at: [http://localhost:5000](http://localhost:5000)

---

# 📡 API Endpoints

| Method | Endpoint        | Description               | Body Required |
|--------|-----------------|---------------------------|---------------|
| `GET`  | `/`             | Welcome message           | ❌ No         |
| `POST` | `/books`        | Add new book              | ✔️ Yes        |
| `GET`  | `/books`        | List all books            | ❌ No         |
| `PUT`  | `/books/<id>`   | Update book information   | ✔️ Yes        |
| `DELETE`| `/books/<id>`   | Delete book               | ❌ No         |

---

# 🧪 Example Requests

## Create Book
```bash
curl -X POST http://localhost:5000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Dune", "author": "Frank Herbert"}'
```

## List Books
```bash
curl http://localhost:5000/books
```

## Update Book
```bash
curl -X PUT http://localhost:5000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Messiah of Dune"}'
```

## Delete Book
```bash
curl -X DELETE http://localhost:5000/books/1
```

---

# ⚡ Server Responses

## ✅ Successful Responses
- `200 OK` - GET/PUT requests
- `201 Created` - Resource created
- `204 No Content` - DELETE requests

## ❌ Error Responses
- `400 Bad Request` - Invalid request format
- `404 Not Found` - Book not found
- `500 Internal Server Error` - Server error
```
