# 📚 Docker

---

# 🧠 Session 19 — Docker Fundamentals

## 📖 Concepts

- What is Docker?
- Containers vs virtual machines
- Images vs containers
- Why Docker exists
- Container lifecycle

---

## 📌 Important Terms

| Term | Meaning |
|---|---|
| Image | Blueprint/template |
| Container | Running instance of image |
| Docker Engine | Runtime |
| Registry | Stores images |

---

## ⚡ Commands

```bash
docker --version
docker ps
docker ps -a
docker images
docker pull
docker run
docker stop
docker rm
```

---

## 🛠️ Hands-on

- Install Docker
- Pull Ubuntu image
- Run first container
- Stop/remove containers
- Explore Docker Hub

---

## 🎯 Interview Focus

- Difference between image and container
- Why containers are lightweight
- Containers vs VMs

---

# 🧠 Session 20 — Running Containers

## 📖 Concepts

- Interactive containers
- Detached mode
- Port mapping
- Container naming
- Logs

---

## ⚡ Commands

```bash
docker run
docker exec
docker logs
docker stop
docker start
docker restart
```

---

## 🛠️ Hands-on

### Run Ubuntu Container

```bash
docker run -it ubuntu bash
```

---

### Run Nginx

```bash
docker run -d -p 8080:80 nginx
```

---

### View Logs

```bash
docker logs container_name
```

---

## 🎯 Interview Focus

- What does `-it` mean?
- What does `-d` do?
- Port mapping explanation

---

# 🧠 Session 21 — Dockerfile Basics

## 📖 Concepts

- What is a Dockerfile?
- Layers
- Build process
- Reproducibility

---

## ⚡ Core Dockerfile Instructions

```dockerfile
FROM
WORKDIR
COPY
RUN
CMD
EXPOSE
ENV
```

---

## 🛠️ Hands-on

### Dockerize FastAPI App

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Build Image

```bash
docker build -t biblo-backend .
```

---

### Run Container

```bash
docker run -p 8000:8000 biblo-backend
```

---

## 🎯 Interview Focus

- Why COPY requirements first?
- What does WORKDIR do?
- Difference between RUN and CMD

---

# 🧠 Session 22 — Volumes & Persistent Data

## 📖 Concepts

- Ephemeral containers
- Persistent storage
- Named volumes
- Bind mounts

---

## ⚡ Commands

```bash
docker volume ls
docker volume create
docker run -v
```

---

## 🛠️ Hands-on

### Bind Mount

```bash
docker run -v $(pwd):/app ubuntu
```

---

### PostgreSQL Volume

```bash
docker run -v pgdata:/var/lib/postgresql/data postgres
```

---

## 🎯 Interview Focus

- Why volumes matter
- Bind mount vs named volume
- Why databases need persistence

---

# 🧠 Session 23 — Docker Networking

## 📖 Concepts

- Container networking
- Bridge network
- Host communication
- Service discovery

---

## ⚡ Commands

```bash
docker network ls
docker network create
docker inspect
```

---

## 🛠️ Hands-on

- Create custom network
- Connect FastAPI + PostgreSQL
- Test container communication

---

## 🎯 Interview Focus

- How containers communicate
- Why localhost inside container differs
- Exposing ports

---

# 🧠 Session 24 — Docker Compose

## 📖 Concepts

- Multi-container apps
- Service orchestration
- Shared networking
- Environment management

---

## ⚡ Commands

```bash
docker compose up
docker compose down
docker compose ps
```

---

## 🛠️ Hands-on

### Create Full Stack Setup

Services:
- FastAPI
- PostgreSQL
- pgAdmin

---

### Example Compose File

```yaml
services:
  backend:
    build: .
    ports:
      - "8000:8000"

  db:
    image: postgres
```

---

## 🎯 Interview Focus

- Why Compose is useful
- Networking between services
- Difference between Compose and Dockerfile

---

# 🧠 Session 25 — Environment Variables in Docker

## 📖 Concepts

- ENV variables
- `.env`
- Secrets
- Config injection

---

## ⚡ Commands

```bash
docker run -e
docker compose --env-file
```

---

## 🛠️ Hands-on

- Inject `DATABASE_URL`
- Use `.env`
- Configure FastAPI container

---

## 🎯 Interview Focus

- Why not hardcode secrets
- Passing configs securely
- Production environment management

---

# 🧠 Session 26 — Multi-Stage Builds

## 📖 Concepts

- Build optimization
- Smaller images
- Dependency separation

---

## 🛠️ Hands-on

### Flutter/Web Multi-Stage Build

```dockerfile
FROM node AS builder
# build app

FROM nginx
# copy built files
```

---

## 🎯 Interview Focus

- Why multi-stage builds matter
- Image size optimization
- Production vs development containers

---

# 🧠 Session 27 — Docker Debugging & Best Practices

## 📖 Concepts

- Container debugging
- Logs
- Resource usage
- Image optimization

---

## ⚡ Commands

```bash
docker exec
docker logs
docker stats
docker inspect
```

---

## 🛠️ Hands-on

- Debug failing FastAPI container
- Inspect logs
- Investigate port conflicts

---

## 🎯 Interview Focus

- Common Docker issues
- Why containers fail
- Debugging workflow

---

# 🧠 Session 28 — Real Project Containerization

## 🛠️ Containerize Biblo

Build:
- FastAPI backend
- PostgreSQL
- Redis (optional)
- Flutter web frontend

---

## 🚀 Features

- Environment variables
- Persistent database
- Docker Compose setup
- Production-ready structure

---

