# 📚 Bash Scripting Overview

---

# 🧠 Session 8 — Bash Scripting Basics

## 📖 Concepts

- What is a shell script?
- Shebang (`#!/bin/bash`)
- Running scripts
- Execute permissions
- Comments
- Basic syntax

---

## 🛠️ Hands-on

- Create first `.sh` file
- Print messages
- Run using:

```bash
bash script.sh
./script.sh
```

---

## 🎯 Interview Questions

- Difference between shell and terminal?
- Why is shebang needed?
- Why execute permission required?

---

# 🧠 Session 9 — Variables & User Input

## 📖 Concepts

- Variables
- Quoting
- Command substitution
- Environment variables
- `read`

---

## 🛠️ Hands-on

- Ask user name
- Store project path
- Print dynamic messages

---

## ⚡ Commands / Concepts

```bash
NAME="Srishti"
echo $NAME
read USERNAME
```

---

## 🎯 Interview Focus

- Difference between local variable and exported variable
- Single vs double quotes

---

# 🧠 Session 10 — Conditionals

## 📖 Concepts

- `if`
- `elif`
- `else`
- Test operators

---

## 📄 File Checks

```bash
-f
-d
-e
```

---

## 🔢 Numeric Comparisons

```bash
-eq
-gt
-lt
```

---

## 🔤 String Comparisons

```bash
=
!=
-z
```

---

## 🛠️ Hands-on

- Check if file exists
- Validate `.env`
- Check if directory exists

---

## 🚀 Real Backend Relevance

Deployment scripts heavily use conditionals.

---

# 🧠 Session 11 — Loops

## 📖 Concepts

- `for` loop
- `while` loop

---

## 🛠️ Hands-on

- Loop through files
- Batch rename files
- Process logs

---

## ⚡ Example

```bash
for file in *.txt
do
  echo $file
done
```

---

## 🎯 Interview Focus

- Difference between `for` and `while`
- Infinite loops

---

# 🧠 Session 12 — Functions

## 📖 Concepts

- Function syntax
- Parameters
- Return codes

---

## ⚡ Example

```bash
greet() {
  echo "Hello $1"
}
```

---

## 🛠️ Hands-on

- Reusable backup function
- Health-check function

---

## 🚀 Backend Relevance

Production scripts are modularized using functions.

---

# 🧠 Session 13 — Arguments & Exit Codes

## 📖 Concepts

### Script Arguments

```bash
$1
$2
$@
$#
```

---

### Exit Codes

```bash
echo $?
```

---

## ⚡ Important

```text
0 = success
non-zero = failure
```

---

## 🛠️ Hands-on

Build script:

```bash
./deploy.sh production
```

---

## 🚀 Backend Relevance

CI/CD pipelines depend heavily on exit codes.

---

# 🧠 Session 14 — File Operations & Automation

## 📖 Concepts

- Creating files
- Reading files
- Appending logs
- Checking permissions

---

## ⚡ Commands

```bash
touch
cat
grep
find
cp
mv
rm
```

---

## 🛠️ Hands-on

- Backup script
- Log cleaner
- Deployment prep script

---

# 🧠 Session 15 — Processes in Scripts

## 📖 Concepts

- Background jobs
- Checking running processes
- Killing processes

---

## ⚡ Commands

```bash
ps
grep
kill
pkill
```

---

## 🛠️ Hands-on

- Restart FastAPI automatically
- Detect crashed service

---

## 🚀 Real Backend Relevance

Very common in DevOps.

---

# 🧠 Session 16 — Pipes, Grep & Log Processing

## 📖 Concepts

- Pipes
- Filtering logs
- Parsing output

---

## ⚡ Commands

```bash
grep
awk
sed
cut
sort
uniq
```

---

## 🛠️ Hands-on

- Extract ERROR logs
- Count failed requests
- Analyze access logs

---

## 🎯 Interview Relevance

Extremely common Linux/backend questions.

---

# 🧠 Session 17 — Real Automation Scripts

## 🛠️ Build Real Scripts

### 1️⃣ FastAPI Startup Script

- activate venv
- export env vars
- start server

---

### 2️⃣ Backup Script

- zip logs
- timestamp backups
- move to archive folder

---

### 3️⃣ Health Check Script

- ping backend
- restart if dead

---

### 4️⃣ Git Automation Script

- git add
- git commit
- git push

---

# 🧠 Session 18 — Bash + Cron Integration

## 📖 Concepts

- Automating scripts with cron
- Scheduled cleanup
- Log rotation

---

## 🛠️ Hands-on

- Daily backup cron
- Cleanup temp files
- Scheduled database dump

---

# 🚀 Final Outcome

By the end of these sessions, you should be comfortable with:

- Linux fundamentals
- Bash scripting
- Process management
- Permissions
- Log debugging
- Environment variables
- Automation
- Cron jobs
- Deployment scripting
- Backend server workflows
- DevOps foundations

---

# 🐧 Bash Scripting Fundamentals Interview Prep
