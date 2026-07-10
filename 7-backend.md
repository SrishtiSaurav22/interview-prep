# 📚 Backend

---

# 🧠 Session 53 — Backend Fundamentals

## 📖 Concepts

- What is a backend?
- Client-server architecture
- APIs
- Request-response lifecycle
- Stateless systems
- Backend responsibilities

---

## 🧠 Backend Responsibilities

| Responsibility | Examples |
|---|---|
| Authentication | Login/signup |
| Database access | PostgreSQL queries |
| Business logic | Payments/orders |
| API responses | JSON data |
| Validation | Request checking |

---

## 🛠️ Hands-on

- Run FastAPI server
- Create first endpoint
- Test using browser/Postman

---

## 🎯 Interview Focus

- What does a backend do?
- Difference between frontend and backend
- What is stateless architecture?

---

# 🧠 Session 54 — FastAPI Fundamentals

## 📖 Concepts

- What is FastAPI?
- ASGI
- Route handlers
- JSON APIs
- Automatic docs

---

## ⚡ Install FastAPI

```bash
pip install fastapi uvicorn
```

---

## ⚡ Basic FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Biblo backend running"}
```

---

## ⚡ Run Server

```bash
uvicorn main:app --reload
```

---

## 🛠️ Hands-on

- Create GET endpoint
- Create POST endpoint
- Test Swagger docs

---

## 🎯 Interview Focus

- Why FastAPI is popular
- What is ASGI?
- Difference between Flask and FastAPI

---

# 🧠 Session 55 — Request Handling & Validation

## 📖 Concepts

- Request body
- Query parameters
- Path parameters
- Validation
- Error responses

---

## ⚡ Example

```python
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
```

---

## ⚡ Endpoint Example

```python
@app.post("/books")
def create_book(book: Book):
    return book
```

---

## 🛠️ Hands-on

- Validate request body
- Test invalid requests
- Create CRUD endpoints

---

## 🎯 Interview Focus

- Why validation matters
- What is Pydantic?
- Difference between query and path params

---

# 🧠 Session 56 — Dependency Injection

## 📖 Concepts

- Dependency Injection (DI)
- Shared resources
- Reusable dependencies
- Authentication dependencies

---

## ⚡ Example

```python
from fastapi import Depends

def get_db():
    return "database"

@app.get("/")
def root(db=Depends(get_db)):
    return {"db": db}
```

---

## 🛠️ Hands-on

- Create reusable DB dependency
- Inject authentication dependency

---

## 🎯 Interview Focus

- What is dependency injection?
- Benefits of DI
- Why FastAPI uses Depends()

---

# 🧠 Session 57 — Async vs Sync

## 📖 Concepts

- Blocking vs non-blocking
- Async IO
- Concurrency
- await
- Event loop

---

## ⚡ Sync Example

```python
def get_data():
    return "data"
```

---

## ⚡ Async Example

```python
async def get_data():
    return "data"
```

---

## 🛠️ Hands-on

- Convert endpoint to async
- Simulate slow API calls

---

## 🎯 Interview Focus

- Difference between async and sync
- When async improves performance
- Why async matters in APIs

---

# 🧠 Session 58 — Error Handling

## 📖 Concepts

- HTTP exceptions
- Status codes
- Validation errors
- Custom error handling

---

## ⚡ Example

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Book not found"
)
```

---

## 🛠️ Hands-on

- Create custom error responses
- Handle invalid IDs

---

## 🎯 Interview Focus

- Difference between 400 and 404
- Why proper status codes matter
- Backend error handling strategies

---

# 🧠 Session 59 — REST API Design

## 📖 Concepts

- REST architecture
- Resources
- HTTP methods
- Stateless APIs
- API naming conventions

---

## ⚡ Common HTTP Methods

| Method | Purpose |
|---|---|
| GET | Fetch data |
| POST | Create data |
| PUT | Replace |
| PATCH | Partial update |
| DELETE | Remove |

---

## 🛠️ Hands-on

- Design RESTful routes
- Create CRUD API for books

---

## 🎯 Interview Focus

- Difference between PUT and PATCH
- What makes an API RESTful?
- Why stateless APIs scale better

---

# 🧠 Session 60 — HTTP Status Codes

## 📖 Concepts

- Response categories
- Success codes
- Client errors
- Server errors

---

## ⚡ Important Codes

| Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

---

## 🛠️ Hands-on

- Return proper status codes
- Simulate API failures

---

## 🎯 Interview Focus

- Difference between 401 and 403
- When to use 201
- Why status codes matter

---

# 🧠 Session 61 — JWT Authentication

## 📖 Concepts

- Authentication vs authorization
- JWT structure
- Access tokens
- Refresh tokens
- Token expiry

---

## 🧠 JWT Structure

```text
HEADER.PAYLOAD.SIGNATURE
```

---

## ⚡ Example Payload

```json
{
  "user_id": 1,
  "role": "admin"
}
```

---

## 🛠️ Hands-on

- Create login endpoint
- Generate JWT token
- Protect routes

---

## 🎯 Interview Focus

- What is JWT?
- Why JWT is stateless
- Difference between access and refresh token

---

# 🧠 Session 62 — Authentication Security

## 📖 Concepts

- Password hashing
- bcrypt
- Secret management
- Token expiration
- Security pitfalls

---

## ⚡ Example

```python
from passlib.hash import bcrypt

hashed = bcrypt.hash("password")
```

---

## 🛠️ Hands-on

- Hash passwords
- Verify passwords
- Store secrets in `.env`

---

## 🎯 Interview Focus

- Why passwords should never be stored plainly
- Why JWT secrets matter
- Common authentication vulnerabilities

---

# 🧠 Session 63 — Background Tasks

## 📖 Concepts

- Async background jobs
- Deferred execution
- Non-blocking responses

---

## ⚡ Example

```python
from fastapi import BackgroundTasks
```

---

## 🛠️ Hands-on

- Send fake email in background
- Log background tasks

---

## 🎯 Interview Focus

- Why background tasks improve UX
- Difference between sync tasks and background jobs

---

# 🧠 Session 64 — Database Integration

## 📖 Concepts

- ORM basics
- Database sessions
- SQLAlchemy
- CRUD operations

---

## ⚡ Example

```python
from sqlalchemy.orm import Session
```

---

## 🛠️ Hands-on

- Connect PostgreSQL
- Create user table
- Implement CRUD APIs

---

## 🎯 Interview Focus

- What is an ORM?
- Benefits of SQLAlchemy
- Session lifecycle

---

# 🧠 Session 65 — API Versioning & Best Practices

## 📖 Concepts

- API versioning
- Scalability
- Maintainability
- Backward compatibility

---

## ⚡ Example

```text
/api/v1/books
```

---

## 🛠️ Hands-on

- Create v1 routes
- Simulate API upgrade

---

## 🎯 Interview Focus

- Why API versioning matters
- Breaking changes
- REST best practices

---

# 🧠 Session 66 — Real Backend Project Architecture

## 🛠️ Build Production Backend for Biblo

### Features

- Authentication
- PostgreSQL integration
- JWT security
- CRUD APIs
- Environment variables
- Docker support
- Modular architecture

---

## 📂 Suggested Structure

```text
app/
├── routes/
├── models/
├── schemas/
├── services/
├── database/
├── auth/
└── main.py
```

---

## 🚀 Production Features

- Validation
- Logging
- Security
- Error handling
- Scalable structure
- Environment configs

---

# 🧠 Important Backend Concepts Summary

| Concept | Importance |
|---|---|
| FastAPI | High-performance APIs |
| Validation | Prevent bad requests |
| JWT | Stateless auth |
| Async | Scalability |
| Dependency Injection | Reusable architecture |
| REST | Standardized APIs |
| Status Codes | Clear communication |
| Background Tasks | Better performance |

---


