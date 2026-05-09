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

## ⚙️ What Is a Process?

A process is:

> A running instance of a program.

Examples:
- VS Code running
- FastAPI server running
- Chrome tabs
- Docker daemon

Each process gets:
- A PID (Process ID)
- Memory allocation
- CPU time

---

## 🆔 PID (Process ID)

Every running process has a unique ID.

Example:

```bash
python app.py
```

Might create:

```text
PID = 4123
```

Linux uses the PID to:
- Track processes
- Monitor resource usage
- Kill processes

---

## 🔍 Viewing Processes

### Basic Process View

```bash
ps
```

Shows currently running processes.

---

### Detailed Process View

```bash
ps aux
```

---

### 📊 Important `ps aux` Columns

| Column | Meaning |
|---|---|
| `USER` | Process owner |
| `PID` | Process ID |
| `%CPU` | CPU usage |
| `%MEM` | Memory usage |
| `COMMAND` | Running command |

---

## 📊 Real-Time Monitoring

### Using `top`

```bash
top
```

Displays:
- Live CPU usage
- RAM usage
- Running processes

Quit using:

```text
q
```

---

### ⚡ Better Alternative: `htop`

`htop` is:
- More visual
- Easier to read
- Interactive

Run:

```bash
htop
```

Install if missing:

```bash
sudo apt install htop
```

---

## 💀 Killing Processes

### Graceful Termination

```bash
kill PID
```

Example:

```bash
kill 4123
```

Sends:

```text
SIGTERM
```

Meaning:
> "Please stop gracefully."

The process gets time to:
- Save data
- Close files
- Clean up resources

---

## Force Kill

```bash
kill -9 PID
```

Sends:

```text
SIGKILL
```

Meaning:
> "Stop immediately."

⚠️ Dangerous if the process is writing data.

Can lead to:
- Corrupted files
- Incomplete writes
- Resource leaks

---

## 🔄 Foreground vs Background Processes

### Foreground Process

```bash
python app.py
```

Behavior:
- Occupies the terminal
- Blocks further commands

---

### Background Process

```bash
python app.py &
```

Behavior:
- Process runs in background
- Terminal remains usable

---

## 🧵 Jobs Management

### View Background Jobs

```bash
jobs
```

---

### Bring Job to Foreground

```bash
fg
```

---

### Suspend Running Process

Press:

```text
Ctrl + Z
```

This pauses the process.

---

### Continue Suspended Process in Background

```bash
bg
```

---

## ⚡ Hands-On Practice

---

### Step 1 — Start a Long Running Process

```bash
sleep 300
```

This process:
- Sleeps for 300 seconds
- Occupies the terminal

---

### Step 2 — Stop the Process

Press:

```text
Ctrl + C
```

This terminates the foreground process.

---

### Step 3 — Run Process in Background

```bash
sleep 300 &
```

Expected Output:

```text
[1] 1234
```

Where:
- `1` → Job number
- `1234` → PID

---

### Step 4 — View Jobs

```bash
jobs
```

Expected:

```text
[1]+ Running sleep 300 &
```

---

### Step 5 — View All Processes

```bash
ps aux
```

Look for:

```text
sleep 300
```

---

### Step 6 — Kill the Process

```bash
kill PID
```

Replace `PID` with the actual process ID.

---

### Step 7 — Verify Process Is Gone

```bash
ps aux | grep sleep
```

You should no longer see:

```text
sleep 300
```

---

### Step 8 — Monitor System with `top`

```bash
top
```

Observe:
- CPU usage
- Memory usage
- Running processes
- PIDs

Quit using:

```text
q
```

---

## 🧠 Interview Questions

### ❓ What is a process?

A running instance of a program managed by the operating system.

---

### ❓ What is a PID?

PID stands for:
> Process ID

A unique identifier assigned to each running process.

---

### ❓ Difference between `kill` and `kill -9`?

| Command | Meaning |
|---|---|
| `kill` | Graceful termination |
| `kill -9` | Forced immediate termination |

---

### ❓ Why avoid `kill -9`?

Because the process cannot:
- Clean up resources
- Save state
- Close files properly

This can cause:
- Corrupted data
- Incomplete writes

---

### ❓ What does `top` do?

Shows real-time:
- CPU usage
- Memory usage
- Active processes

---

### ❓ What does `&` do?

Runs a process in the background.

Example:

```bash
python app.py &
```

---

### ❓ Difference between foreground and background processes?

| Type | Behavior |
|---|---|
| Foreground | Occupies terminal |
| Background | Runs while terminal remains usable |

---

## 📝 Quick Cheat Sheet

---

# ⚙️ Process Basics

- Process = running program
- PID = Process ID

---

## ⚡ Essential Commands

| Command | Purpose |
|---|---|
| `ps` | Show processes |
| `ps aux` | Detailed process view |
| `top` | Live monitoring |
| `kill PID` | Gracefully stop process |
| `kill -9 PID` | Force stop process |
| `jobs` | Show background jobs |
| `fg` | Bring process to foreground |
| `bg` | Continue process in background |

---

## 🔄 Process Control

### Run in Background

```bash
command &
```

---

### Stop Foreground Process

```text
Ctrl + C
```

---

### Suspend Process

```text
Ctrl + Z
```

---

## ⚠️ Important Notes

- Use normal `kill` before `kill -9`
- `kill -9` should be last resort
- `top` is essential for backend debugging

---

## 🚀 Real Backend Relevance

You will use these commands constantly for:

- Killing stuck backend servers
- Monitoring APIs
- Debugging memory issues
- Managing Docker containers
- Restarting crashed services
- Inspecting resource-heavy applications

---

## 🌊 What Is a Pipe?

A pipe (`|`) takes:

> Output of one command → sends it as input to another command.

Think:

```text
Command A → Command B
```

Example:

```bash
ls | less
```

Meaning:
- `ls` produces output
- `less` receives it

---

## 🧠 Why Pipes Matter

Without pipes:
- Commands stay isolated

With pipes:
- Linux becomes composable
- Small tools combine into powerful workflows

This is a core Unix philosophy.

---

### 🔄 Output Redirection

Linux commands produce output.

You can:
- Display it
- Save it
- Append it

---

### ➡️ `>` (Overwrite Output)

```bash
ls > files.txt
```

Meaning:
- Saves output into `files.txt`
- Overwrites existing content

---

### ➕ `>>` (Append Output)

```bash
echo "new log" >> app.log
```

Meaning:
- Adds content to the end of a file
- Preserves existing content

---

### 📥 Input Redirection (`<`)

Less commonly used.

```bash
sort < names.txt
```

Meaning:
- File becomes command input

---

### 🔍 Searching with `grep`

`grep` is a search/filtering tool.

Example:

```bash
grep error app.log
```

Finds lines containing:

```text
error
```

---

## ⚡ Useful `grep` Options

### Ignore Case

```bash
grep -i error app.log
```

Matches:
- `error`
- `ERROR`
- `Error`

---

### Show Line Numbers

```bash
grep -n error app.log
```

---

### Invert Match

```bash
grep -v INFO app.log
```

Shows everything EXCEPT:

```text
INFO
```

---

## 🔥 Pipes + Grep = Real Power

Example:

```bash
ps aux | grep python
```

Flow:

```text
ps aux → grep python
```

Meaning:
- List all running processes
- Filter only Python-related ones

This is extremely common in backend/devops work.

---

## 📄 Real Log Debugging

Example:

```bash
cat app.log | grep ERROR
```

Meaning:
- Read log file
- Extract only errors

---

## ⚡ Hands-On Practice

---

### Step 1 — Create Practice Directory

```bash
mkdir pipes-practice
cd pipes-practice
```

---

### Step 2 — Create Fake Log File

```bash
touch app.log
```

Add logs:

```bash
echo "INFO Server started" >> app.log
echo "INFO Database connected" >> app.log
echo "ERROR Failed login" >> app.log
echo "WARNING Disk almost full" >> app.log
echo "ERROR Payment failed" >> app.log
```

---

### Step 3 — View Log File

```bash
cat app.log
```

Expected Output:

```text
INFO Server started
INFO Database connected
ERROR Failed login
WARNING Disk almost full
ERROR Payment failed
```

---

### Step 4 — Search Errors

```bash
grep ERROR app.log
```

Expected:

```text
ERROR Failed login
ERROR Payment failed
```

---

### Step 5 — Ignore Case

```bash
grep -i error app.log
```

---

### Step 6 — Show Line Numbers

```bash
grep -n ERROR app.log
```

Expected:

```text
3:ERROR Failed login
5:ERROR Payment failed
```

---

### Step 7 — Exclude INFO Logs

```bash
grep -v INFO app.log
```

---

### Step 8 — Use Pipe

```bash
cat app.log | grep ERROR
```

---

### Step 9 — Save Output to File

```bash
grep ERROR app.log > errors.txt
```

Check:

```bash
cat errors.txt
```

---

### Step 10 — Append New Error

```bash
echo "ERROR Database crashed" >> errors.txt
```

Verify:

```bash
cat errors.txt
```

---

### Step 11 — Search Running Processes

```bash
ps aux | grep bash
```

---

## 🧠 Interview Questions

### ❓ What does a pipe (`|`) do?

Sends output of one command as input to another command.

---

### ❓ Difference between `>` and `>>`?

| Operator | Behavior |
|---|---|
| `>` | Overwrites file |
| `>>` | Appends to file |

---

### ❓ What is `grep` used for?

Searching/filtering text.

Commonly used for:
- Logs
- Processes
- Config files

---

### ❓ What does this command do?

```bash
ps aux | grep python
```

Lists all running processes and filters only Python-related ones.

---

### ❓ Why are pipes powerful?

Because Linux commands become composable.

Small commands combine into complex workflows.

---

### ❓ How would you debug logs on a Linux server?

Typical answer:

```bash
grep ERROR app.log
tail -f app.log
```

---

## 📝 Quick Cheat Sheet

---

### 🌊 Pipes

```bash
command1 | command2
```

Output of one command becomes input of another.

---

### ➡️ Redirects

| Operator | Purpose |
|---|---|
| `>` | Overwrite file |
| `>>` | Append to file |
| `<` | Input from file |

---

### 🔍 Grep Commands

| Command | Purpose |
|---|---|
| `grep text file` | Search text |
| `grep -i` | Ignore case |
| `grep -n` | Show line numbers |
| `grep -v` | Invert match |

---

## ⚡ Common Real Commands

### Search Logs

```bash
grep ERROR app.log
```

---

### Filter Processes

```bash
ps aux | grep python
```

---

### Save Errors

```bash
grep ERROR app.log > errors.txt
```

---

## 🚀 Real Backend Relevance

You’ll use these constantly for:
- Searching production logs
- Debugging failed APIs
- Monitoring servers
- Filtering Docker output
- Investigating crashes
- CI/CD troubleshooting

---

## 👤 Linux Is a Multi-User System

Linux was designed for:
- Multiple users
- Shared systems
- Different permission levels

Every file and process belongs to:
- A user
- A group

---

## 👑 What Is `root`?

`root` is:

> The superuser (administrator)

Root can:
- Access all files
- Kill any process
- Install software
- Modify system configurations
- Create/delete users

---

## ⚠️ Why Normal Users Exist

Using `root` all the time is dangerous.

Example mistake:

```bash
rm -rf /
```

This could destroy the entire system.

So Linux encourages:
- Normal users for daily work
- `sudo` for temporary administrative access

---

## 🔑 What Is `sudo`?

`sudo` means:

```text
SuperUser DO
```

Example:

```bash
sudo apt update
```

Meaning:

> Run command with administrator privileges.

---

## 👤 Current User

### `whoami`

```bash
whoami
```

Example Output:

```text
srishti
```

---

## 🆔 User & Group Information

### `id`

```bash
id
```

Example Output:

```text
uid=1000(srishti) gid=1000(srishti) groups=1000(srishti),27(sudo)
```

---

## 🧩 Understanding Groups

Groups are collections of users.

Purpose:
- Shared permissions
- Shared access control

Examples:
- `sudo`
- `docker`
- `developers`

---

### 👥 View User Groups

#### `groups`

```bash
groups
```

Example Output:

```text
srishti sudo docker
```

---

## 📄 Important System Files

---

### `/etc/passwd`

Stores:
- User accounts
- Home directories
- Default shells

View:

```bash
cat /etc/passwd
```

---

### `/etc/group`

Stores:
- Group information

View:

```bash
cat /etc/group
```

---

## 🏠 Home Directories

Each user usually has:

```text
/home/username
```

Example:

```text
/home/srishti
```

---

## 🔐 Ownership Review

Example:

```bash
ls -l
```

Output:

```text
-rw-r--r-- 1 srishti developers file.txt
```

Meaning:
- Owner → `srishti`
- Group → `developers`

---

## ⚡ Changing Ownership

### `chown`

```bash
sudo chown user file.txt
```

Change owner and group:

```bash
sudo chown user:group file.txt
```

---

## 🚫 Why Some Commands Need `sudo`

Example:

```bash
apt install nginx
```

Fails because:
- Installing software modifies system files

Using:

```bash
sudo apt install nginx
```

works correctly.

---

## ⚡ Hands-On Practice

---

### Step 1 — Check Current User

```bash
whoami
```

---

### Step 2 — View Detailed User Info

```bash
id
```

Observe:
- UID
- GID
- Group memberships

---

### Step 3 — View Your Groups

```bash
groups
```

---

### Step 4 — View Home Directory

```bash
echo $HOME
```

Expected Output:

```text
/home/srishti
```

---

### Step 5 — Inspect `/etc/passwd`

```bash
cat /etc/passwd
```

Observe entries like:

```text
root:x:0:0:root:/root:/bin/bash
```

---

### Step 6 — Inspect `/etc/group`

```bash
cat /etc/group
```

---

### Step 7 — Create Practice File

```bash
touch ownership-test.txt
ls -l
```

---

### Step 8 — Try Changing Ownership

```bash
sudo chown root ownership-test.txt
```

Check:

```bash
ls -l
```

Owner should now show:

```text
root
```

---

### Step 9 — Restore Ownership

```bash
sudo chown srishti ownership-test.txt
```

---

#### Step 10 — Try Command Without `sudo`

Example:

```bash
apt update
```

This will likely fail.

Now try:

```bash
sudo apt update
```

---

## 🧠 Interview Questions

### ❓ What is `root`?

The Linux superuser with unrestricted system access.

---

### ❓ What does `sudo` do?

Runs a command with elevated (administrator) privileges.

---

### ❓ Difference between user and group?

| Concept | Meaning |
|---|---|
| User | Individual account |
| Group | Collection of users |

---

### ❓ What does `id` show?

Displays:
- UID
- GID
- Group memberships

---

### ❓ Why avoid using `root` directly?

Because mistakes can damage the entire system.

Safer approach:
- Use normal user accounts
- Use `sudo` only when necessary

---

### ❓ What is stored in `/etc/passwd`?

User account information:
- Username
- Home directory
- Default shell

---

### ❓ Why are groups useful?

They simplify permission management for multiple users.

Example:
- Entire backend team shares access to a deployment folder

---

## 📝 Quick Cheat Sheet

---

### 👤 User Commands

| Command | Purpose |
|---|---|
| `whoami` | Current user |
| `id` | User + group details |
| `groups` | Show user groups |

---

### 🔑 `sudo`

```bash
sudo command
```

Runs a command with administrator privileges.

---

### 📄 Important Files

| File | Purpose |
|---|---|
| `/etc/passwd` | User accounts |
| `/etc/group` | Group information |

---

### 🔐 Ownership

#### View Ownership

```bash
ls -l
```

---

#### Change Ownership

```bash
sudo chown user file.txt
```

---

#### 🏠 Home Directory

```bash
echo $HOME
```

---

## ⚠️ Important Notes

- Linux is a multi-user system
- `root` has unrestricted access
- Use `sudo` carefully
- Ownership affects permissions
- Groups simplify shared access

---

## 🚀 Real Backend Relevance

You’ll use this constantly for:
- Deploying backend applications
- Managing Linux servers
- Docker permissions
- CI/CD runners
- SSH access
- File ownership debugging
- Cloud infrastructure management

---
