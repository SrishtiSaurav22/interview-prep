# 📚 CI/CD

---

# 🧠 Session 29 — CI/CD Fundamentals

## 📖 Concepts

- What is CI/CD?
- Continuous Integration
- Continuous Deployment
- Continuous Delivery
- Automation pipelines
- Why CI/CD matters

---

## 🧠 Key Ideas

| Concept | Meaning |
|---|---|
| CI | Automatically test/build code |
| CD | Automatically deploy applications |
| Pipeline | Automated workflow |
| Runner | Machine executing jobs |

---

## ⚡ Common CI/CD Platforms

- GitHub Actions
- GitLab CI
- Jenkins
- CircleCI
- Azure DevOps

---

## 🛠️ Hands-on

- Explore GitHub Actions tab
- Understand pipeline flow
- Connect Git workflow to CI/CD thinking

---

## 🎯 Interview Focus

- Difference between CI and CD
- Benefits of automation
- Why CI/CD improves reliability

---

# 🧠 Session 30 — GitHub Actions Basics

## 📖 Concepts

- Workflow files
- YAML syntax
- Events/triggers
- Jobs and steps
- Runners

---

## 📂 Workflow Location

```text
.github/workflows/
```

---

## ⚡ First Workflow

```yaml
name: First Workflow

on: [push]

jobs:
  hello:
    runs-on: ubuntu-latest

    steps:
      - name: Print message
        run: echo "Hello CI/CD"
```

---

## 🛠️ Hands-on

- Create first workflow
- Push to GitHub
- Watch workflow execute

---

## 🎯 Interview Focus

- What triggers workflows?
- What is a runner?
- Why YAML is used?

---

# 🧠 Session 31 — Workflow Triggers & Events

## 📖 Concepts

- Push events
- Pull request events
- Manual workflows
- Scheduled workflows
- Branch filtering

---

## ⚡ Common Triggers

### Push Trigger

```yaml
on:
  push:
```

---

### Pull Request Trigger

```yaml
on:
  pull_request:
```

---

### Scheduled Trigger

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
```

---

### Manual Trigger

```yaml
on:
  workflow_dispatch:
```

---

## 🛠️ Hands-on

- Run workflow on push
- Trigger on pull requests
- Create manual workflow

---

## 🎯 Interview Focus

- Difference between push and PR workflows
- Why scheduled workflows matter
- CI/CD + cron relationship

---

# 🧠 Session 32 — Jobs, Steps & Actions

## 📖 Concepts

- Workflow structure
- Jobs
- Steps
- Reusable actions
- Sequential vs parallel execution

---

## ⚡ Example

```yaml
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install dependencies
        run: pip install -r requirements.txt
```

---

## 🧠 Common GitHub Actions

| Action | Purpose |
|---|---|
| actions/checkout | Clone repo |
| actions/setup-python | Setup Python |
| actions/cache | Dependency caching |

---

## 🛠️ Hands-on

- Checkout code
- Setup Python
- Install dependencies
- Run shell commands

---

## 🎯 Interview Focus

- Difference between jobs and steps
- Why reusable actions matter
- Parallel jobs vs sequential jobs

---

# 🧠 Session 33 — Running Tests in CI

## 📖 Concepts

- Automated testing
- Failing pipelines
- Exit codes
- Test validation

---

## ⚡ Example Workflow

```yaml
- name: Run Tests
  run: pytest
```

---

## 🛠️ Hands-on

- Add pytest
- Run tests automatically
- Intentionally fail tests
- Observe CI behavior

---

## 🎯 Interview Focus

- Why automate tests?
- What happens if tests fail?
- Why exit codes matter?

---

# 🧠 Session 34 — Linting & Code Quality

## 📖 Concepts

- Static analysis
- Code formatting
- Linting
- Style consistency

---

## ⚡ Tools

| Tool | Purpose |
|---|---|
| flake8 | Python linting |
| black | Formatting |
| isort | Import sorting |

---

## ⚡ Example

```yaml
- name: Run Linter
  run: flake8 .
```

---

## 🛠️ Hands-on

- Install flake8
- Add lint workflow
- Fix lint errors

---

## 🎯 Interview Focus

- Why linting matters
- Difference between linting and testing
- Static analysis benefits

---

# 🧠 Session 35 — Environment Variables & Secrets

## 📖 Concepts

- CI/CD secrets
- Environment variables
- Secure credential handling
- Secret injection

---

## ⚡ GitHub Secrets

Repository:

```text
Settings → Secrets and variables → Actions
```

---

## ⚡ Example

```yaml
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

---

## 🛠️ Hands-on

- Create GitHub secret
- Access secret in workflow
- Use environment variables securely

---

## 🎯 Interview Focus

- Why secrets should never be hardcoded
- Difference between env vars and secrets
- CI/CD credential security

---

# 🧠 Session 36 — Docker in CI/CD

## 📖 Concepts

- Automated Docker builds
- CI container workflows
- Image tagging
- Registry pushes

---

## ⚡ Example

```yaml
- name: Build Docker Image
  run: docker build -t biblo-backend .
```

---

## 🛠️ Hands-on

- Build Docker image in pipeline
- Run container tests
- Push image to Docker Hub

---

## 🎯 Interview Focus

- Why Docker fits CI/CD well
- Benefits of containerized builds
- Reproducible environments

---

# 🧠 Session 37 — Matrix Builds & Multiple Environments

## 📖 Concepts

- Matrix testing
- Multiple Python versions
- Parallel builds

---

## ⚡ Example

```yaml
strategy:
  matrix:
    python-version: [3.10, 3.11, 3.12]
```

---

## 🛠️ Hands-on

- Run tests across Python versions
- Observe parallel jobs

---

## 🎯 Interview Focus

- Why matrix builds matter
- Cross-version compatibility
- Parallel execution benefits

---

# 🧠 Session 38 — Dependency Caching

## 📖 Concepts

- Faster pipelines
- Cache reuse
- Dependency optimization

---

## ⚡ Example

```yaml
- uses: actions/cache@v4
```

---

## 🛠️ Hands-on

- Cache pip dependencies
- Compare execution times

---

## 🎯 Interview Focus

- Why caching matters
- Pipeline optimization
- Faster CI execution

---

# 🧠 Session 39 — Deployment Pipelines

## 📖 Concepts

- Deployment automation
- SSH deployment
- Production pipelines
- Deployment environments

---

## ⚡ Example Flow

```text
Push → Test → Build → Deploy
```

---

## 🛠️ Hands-on

- Simulate deployment pipeline
- Deploy FastAPI app to server
- Restart service automatically

---

## 🎯 Interview Focus

- Difference between CI and deployment
- Safe deployment practices
- Rollback strategies

---

# 🧠 Session 40 — Real CI/CD Project Pipeline

## 🛠️ Build Complete Pipeline for Biblo

### Pipeline Includes

- Install dependencies
- Run tests
- Run lint checks
- Build Docker image
- Push image
- Deploy backend

---

## 📄 Example Flow

```text
Git Push
   ↓
GitHub Actions
   ↓
Run Tests
   ↓
Lint Code
   ↓
Build Docker Image
   ↓
Push to Registry
   ↓
Deploy Server
```

---

## 🚀 Production Features

- Secrets management
- Automated testing
- Dockerized deployment
- Environment configs
- Rollback-ready workflows

---

# 🧠 Important CI/CD Concepts Summary

| Concept | Importance |
|---|---|
| Automation | Reduces manual work |
| Testing | Prevents broken code |
| Linting | Maintains code quality |
| Secrets | Secure deployments |
| Docker | Reproducible builds |
| Pipelines | Structured automation |
| Caching | Faster builds |
| Deployment | Production delivery |

---
