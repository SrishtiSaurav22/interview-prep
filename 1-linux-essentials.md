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
```
---
## 🔐 Permissions & Ownership (`chmod`, `chown`)

> Environment: Windows Subsystem for Linux (WSL)

---

### 🔐 Why Permissions Exist

Linux is a **multi-user operating system**.

Permissions help:
- Prevent unauthorized access
- Protect sensitive files
- Control who can modify or execute files
- Improve security in backend systems

---

### 👥 Permission Levels

Every file and directory has permissions for:

| Level | Meaning |
|---|---|
| User (`u`) | File owner |
| Group (`g`) | Members of the file’s group |
| Others (`o`) | Everyone else |

---

### 🔑 Permission Types

| Symbol | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `x` | Execute |

---

### 🔍 Understanding Permission Strings

Example:

```bash id="jz04w4"
-rwxr-xr--
```


### 🔍 Permission String Breakdown

| Section | Meaning |
|---|---|
| `-` | Regular file |
| `rwx` | User permissions |
| `r-x` | Group permissions |
| `r--` | Others permissions |

---

### 📂 File Types in Permission Output

| Symbol | Type |
|---|---|
| `-` | File |
| `d` | Directory |
| `l` | Symbolic link |

Example:

```bash
drwxr-xr-x
```

`d` means directory.

---

### 🔢 Numeric (Octal) Permissions

Linux permissions are often represented numerically.

| Permission | Value |
|---|---|
| `r` | 4 |
| `w` | 2 |
| `x` | 1 |

Add them together:

| Number | Permission |
|---|---|
| `7` | `rwx` |
| `6` | `rw-` |
| `5` | `r-x` |
| `4` | `r--` |

---

### ⚡ Common Permission Values

| Value | Meaning |
|---|---|
| `755` | `rwxr-xr-x` |
| `644` | `rw-r--r--` |
| `600` | `rw-------` |

---

### ⚠️ Why `777` Is Dangerous

```bash
chmod 777 file.txt
```

This gives:
- Read
- Write
- Execute

to everyone.

❌ Major security risk in production systems.

Avoid using `777`.

---

### 👤 Ownership

Every file has:
- An owner (user)
- A group

Check ownership:

```bash
ls -l
```

Example:

```bash
-rw-r--r-- 1 srishti srishti file.txt
```

- First `srishti` → owner
- Second `srishti` → group

---

## ⚡ Core Commands

### 🔍 View Permissions

```bash
ls -l
```

---

### 🔐 Change Permissions

#### Numeric mode

```bash
chmod 755 file.txt
```

#### Add execute permission

```bash
chmod +x script.sh
```

#### Remove write permission

```bash
chmod -w file.txt
```

---

### 👤 Change Ownership

```bash
chown user file.txt
```

Change user and group:

```bash
chown user:group file.txt
```

---

## ⚡ WSL Hands-On Practice

### Step 1 — Navigate to Windows Files

In WSL, Windows drives are mounted under:

```bash
/mnt
```

Your Windows `C:` drive:

```bash
/mnt/c
```

Navigate there:

```bash
cd /mnt/c
```

---

### Step 2 — Create Practice Folder

```bash
mkdir linux_permissions_practice
cd linux_permissions_practice
```

---

### Step 3 — Create Files

```bash
touch file.txt
touch secret.env
touch run.sh
```

---

### Step 4 — Inspect Permissions

```bash
ls -l
```

Observe:
- Permission string
- Owner
- Group

---

### Step 5 — Restrict Access to `.env`

```bash
chmod 600 secret.env
```

Meaning:
- Owner → read/write
- Others → no access

Verify:

```bash
ls -l
```

---

### Step 6 — Make Script Executable

Add content:

```bash
echo "echo Hello Biblo" > run.sh
```

Try running:

```bash
./run.sh
```

It should fail initially.

Fix:

```bash
chmod +x run.sh
./run.sh
```

---

### Step 7 — Remove Permissions Completely

```bash
chmod 000 file.txt
```

Now nobody can:
- Read
- Write
- Execute

Restore:

```bash
chmod 644 file.txt
```

---

# 🧠 Interview Questions

## ❓ What does `chmod 755` mean?

- Owner → read/write/execute
- Group → read/execute
- Others → read/execute

Equivalent:

```bash
rwxr-xr-x
```

---

## ❓ Difference between `chmod` and `chown`?

| Command | Purpose |
|---|---|
| `chmod` | Changes permissions |
| `chown` | Changes ownership |

---

## ❓ Why is `chmod 777` dangerous?

Because everyone gets full access to the file, creating a serious security vulnerability.

---

## ❓ Why does a script need execute permission?

Without `x`, Linux will not allow the script to run directly.

---

## ❓ Typical permission for `.env` files?

```bash
chmod 600 .env
```

Only the owner can read/write.

---

## ❓ What happens if a directory lacks execute permission?

You cannot:
- Enter it using `cd`
- Access files inside it

---

# 📝 Quick Cheat Sheet

## 🔢 Permission Numbers

| Number | Permission |
|---|---|
| `7` | `rwx` |
| `6` | `rw-` |
| `5` | `r-x` |
| `4` | `r--` |

---

## ⚡ Common Permissions

| Value | Meaning |
|---|---|
| `755` | Public executable scripts |
| `644` | Normal files |
| `600` | Secure/private files |

---

## ⚡ Essential Commands

| Command | Purpose |
|---|---|
| `ls -l` | View permissions |
| `chmod` | Change permissions |
| `chmod +x` | Make executable |
| `chown` | Change ownership |

---

## 🧠 Security Best Practices

- Never use `777`
- Secure `.env` files with `600`
- Give only necessary permissions
- Scripts require execute permission

---

# 🐧 Linux Practice Progress Summary (WSL)

> Environment: Windows Subsystem for Linux (WSL)

This document summarizes the Linux commands practiced so far along with their expected behavior/results.

---

## 📍 Navigation & File System Commands

### Print Current Directory

```bash
pwd
```

#### Purpose
Shows the current working directory.

#### Example Result
```bash
/home/srishti
```

---

### List Files

```bash
ls
```

#### Purpose
Lists visible files and folders.

---

### Show Hidden Files

```bash
ls -a
```

#### Purpose
Shows all files including hidden files.

#### Example Hidden Files
```bash
.bashrc
.profile
.env
```

---

### Detailed File Listing

```bash
ls -l
```

#### Purpose
Displays:
- Permissions
- Owner
- Group
- File size

#### Example Output
```bash
-rw-r--r-- 1 srishti srishti 0 May 8 sample-file.txt
```

---

### Navigate Directories

#### Go to Home Directory

```bash
cd ~
```

---

#### Move One Level Up

```bash
cd ..
```

---

#### Access Windows Drives in WSL

```bash
cd /mnt/c
```

#### Purpose
Accesses the Windows `C:` drive from Linux.

---

## 📂 Creating Files & Directories

### Create Directory

```bash
mkdir linux-practice
```

#### Result
Creates a new folder.

---

### Create File

```bash
touch sample-file.txt
```

#### Result
Creates an empty file.

---

## 🔐 Permissions Practice

### Remove All Permissions

```bash
chmod 000 sample-directory/sample-file.txt
```

#### Result
Nobody can:
- Read
- Write
- Execute

#### Example Permission Output
```bash
---------- sample-file.txt
```

---

### Give Full Permissions

```bash
chmod 777 sample-directory/sample-file.txt
```

#### Result
Everyone can:
- Read
- Write
- Execute

#### Example Permission Output
```bash
-rwxrwxrwx sample-file.txt
```

⚠️ Dangerous in production systems.

---

### View Updated Permissions

```bash
ls -a -l sample-directory/sample-file.txt
```

#### Purpose
Confirms permission changes.

---

## 📄 File Reading Practice

### Read File Content

```bash
cat sample-directory/sample-file.txt
```

#### Result
Prints file content to terminal.

#### Important Observation
Even with `000`, owner/root behavior in WSL can sometimes behave differently depending on mount settings.

---

## 👤 User Information

### Check Current User

```bash
whoami
```

#### Example Result
```bash
srishti
```

---

## 🖥️ Shell Script Practice

### Create Script

```bash
touch sample-script.sh
```

---

### Add Content to Script

```bash
echo "echo Hello Srishti" > sample-script.sh
```

#### Result
Writes command into script file.

---

### Read Script

```bash
cat sample-script.sh
```

#### Example Output
```bash
echo Hello Srishti
```

---

### Make Script Executable

```bash
chmod a+x sample-script.sh
```

#### Result
Adds execute permission for:
- User
- Group
- Others

---

### Execute Script

```bash
./sample-script.sh
```

#### Expected Output
```bash
Hello Srishti
```

---

### Incorrect Script Execution Attempts

#### Incorrect

```bash
./run.sh
```

#### Result
Fails because file does not exist.

---

#### Incorrect

```bash
./run sample-script.sh
```

#### Result
Fails because syntax is invalid.

---

## 📂 Directory Permission Experiment

### Create Directory

```bash
mkdir test-direc
```

---

### Remove Write Permission

```bash
chmod 400 test-direc
```

#### Meaning
- Read only for owner
- No execute permission

---

### Attempt to Create File Inside Directory

```bash
touch test-direc/test-file.txt
```

#### Expected Behavior
Should fail because directory lacks execute/write permissions.

#### Important Linux Concept
Directories require:
- `x` → access/open directory
- `w` → modify contents

---

## ⚠️ Common Mistakes Encountered

### Incorrect Path

```bash
chmod 000 /config/.env
```

#### Problem
`/config` refers to a folder at root level, not current directory.

#### Correct Command
```bash
chmod 000 config/.env
```

---

## 🧠 Key Concepts Learned

- Linux paths are case-sensitive
- WSL mounts Windows drives under `/mnt`
- `chmod` changes permissions
- `777` is unsafe
- Scripts require execute permission
- Directories need execute permission to access contents
- Hidden files begin with `.`

# NOTE: 📂 Why Directories Need Execute (`x`) Permission

One of the most counter-intuitive parts of Linux is that **directories need execute permission to access their contents**.

At first glance, it feels like write permission should be enough — but Linux treats directories differently from regular files.

---

## 🧠 Core Idea

A directory is actually a **special type of file** that stores:
- File names
- File locations
- References to files

To understand directory permissions, separate:
- **Modifying the list**
from
- **Walking through the directory**

---

## 🚪 The "Locked Room" Analogy

Think of a directory as a room with a file cabinet inside.

---

### 👀 Read (`r`) = Looking Through the Window

Read permission lets you:
- See the names of files inside the directory

But:
- You cannot enter the room
- You cannot access the files themselves

---

### ✍️ Write (`w`) = Rearranging Furniture

Write permission lets you:
- Add files
- Delete files
- Rename files

But:
- You still cannot enter the room without execute permission

---

### 🔑 Execute (`x`) = The Key to the Room

Execute permission on a directory means:
- You can enter the directory
- You can traverse paths through it
- You can access files inside it

Without execute permission:
- `cd directory` → fails
- Accessing files inside → fails

---

## ❗ Why Write Permission Alone Is Not Enough

If you have write permission but not execute permission:

- You are technically allowed to modify contents
- But you are not allowed to enter the directory

It is like:
> "You may rearrange the furniture, but you are not allowed to open the door."

---

## ⚡ Common Directory Permission Scenarios

| Permissions | Meaning |
|---|---|
| `r--` | Can see file names only |
| `--x` | Can access files if filename is already known |
| `rw-` | Mostly useless for directories |
| `r-x` | Can enter and view files |
| `rwx` | Full directory access |

---

## 🔍 Detailed Examples

### `r--` (Read Only)

You can:
- See filenames

You cannot:
- `cd` into directory
- Access files
- See detailed metadata

---

### `--x` (Execute Only)

You cannot:
- List directory contents

But if you already know a filename:
```bash
cat secret_room/note.txt
```

may work.

---

### `rw-` (Read + Write, No Execute)

This is surprisingly useless.

You can:
- See filenames
- Theoretically modify contents

But you cannot:
- Enter the directory
- Access files inside

---

### `r-x` (Read + Execute)

This is the most common safe directory setup.

You can:
- Enter directory
- List files
- Read accessible files

You cannot:
- Create/delete files

---

### `rwx` (Full Access)

You can:
- Enter directory
- View files
- Create files
- Delete files
- Rename files

---

## 🧪 Hands-On Experiment

Try this in your Linux home directory:

---

### Step 1 — Create Directory

```bash
mkdir secret_room
```

---

### Step 2 — Create File Inside

```bash
touch secret_room/note.txt
```

---

### Step 3 — Remove Execute Permission

```bash
chmod 600 secret_room
```

Meaning:
- Read ✅
- Write ✅
- Execute ❌

---

### Step 4 — Try Entering Directory

```bash
cd secret_room
```

#### Expected Result

```bash
Permission denied
```

Even though:
- You own the directory
- You have read/write permissions

You still cannot enter because:
- Execute permission acts as the "key"

---

## 🔐 Why Directories Commonly Use `755` or `700`

### `755`

```bash
rwxr-xr-x
```

- Owner → full access
- Others → can enter and read

Common for:
- Public project folders
- Web directories

---

### `700`

```bash
rwx------
```

- Only owner can access

Common for:
- Private directories
- SSH configs
- Sensitive data

---

## 🧠 Key Takeaways

- Directories are special files
- Execute permission on directories means:
  - "allowed to traverse/access"
- Write permission alone is insufficient
- Most directory access problems happen because execute permission is missing

---

## 🚀 Important Interview Insight

A very common Linux interview question is:

> "Why can’t you access a file even though the file itself has correct permissions?"

Correct answer:
- One of the parent directories likely lacks execute permission.
