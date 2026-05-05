# 🐧 Linux Basics – Cheat Sheet & Interview Prep

## 📁 File System Overview

- Root directory: `/`
- `/home` → User files and projects  
- `/etc` → System configuration files  
- `/var/log` → Logs and runtime data  
- `/bin` → Essential system binaries  
- `/usr/bin` → User-installed programs  
- `/tmp` → Temporary files  

---

## 📍 Paths

- **Absolute Path** → Starts from root `/`
  - Example: `/home/user/project`
- **Relative Path** → Based on current directory
  - Example: `../project`

---

## ⚡ Core Commands

### 🔎 Navigation
- `pwd` → Print current directory  
- `ls` → List files  
  - `ls -l` → Detailed view  
  - `ls -a` → Show hidden files  
- `cd <dir>` → Change directory  

---

### 📂 File Operations
- `mkdir <dir>` → Create directory  
- `touch <file>` → Create file  
- `cp <src> <dest>` → Copy file  
- `mv <src> <dest>` → Move/rename file  
- `rm <file>` → Delete file  
- `rm -r <dir>` → Delete directory  

---

### 📖 File Viewing
- `cat <file>` → Print entire file  
- `less <file>` → Scroll through file  
- `head -n 10 <file>` → First 10 lines  
- `tail -n 10 <file>` → Last 10 lines  

---

## 🧠 Pro Tips

- Use `less` instead of `cat` for large files  
- Logs are typically stored in `/var/log`  
- Hidden files start with `.` (e.g., `.env`)  

---

# 🎯 Interview Questions

### ❓ What is the purpose of `/etc`?
Stores system-wide configuration files (e.g., server configs, database configs).

---

### ❓ Difference between `/bin` and `/usr/bin`?
- `/bin` → Essential commands required for system boot  
- `/usr/bin` → Additional user-installed programs  

---

### ❓ Absolute vs Relative path?
- Absolute → Full path starting from `/`  
- Relative → Path relative to current directory  

---

### ❓ How do you view large log files safely?
Use `less` or `tail` instead of `cat` to avoid loading the entire file into memory.

---

### ❓ How do you debug logs in real time?
```bash
tail -f <logfile>
