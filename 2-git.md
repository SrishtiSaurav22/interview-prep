# 📚 Git Mastery (Interview + Real-World Backend)

---

# 🧠 Session 1 — Git Fundamentals

## 📖 Concepts

- What is Version Control?
- Why Git was created
- Git vs GitHub
- Repository (Repo)
- Working Directory
- Staging Area (Index)
- Local Repository
- Remote Repository
- Git Workflow

---

## 🛠️ Hands-on

- Install Git
- Configure Git
- Create your first repository
- Create your first commit

---

## ⚡ Commands

```bash
git init
git config
git status
git add
git commit
git log
```

---

## 🎯 Interview Questions

- Git vs GitHub
- Why use Version Control?
- What is a Commit?

---

# 🧠 Session 2 — Understanding Git Internals

> ⭐ This is where many interview candidates struggle.

## 📖 Concepts

- SHA-1 Hashes
- Commits
- Trees
- Blobs
- HEAD
- Branch Pointers
- Commit Graph

---

## 🧠 Understand

```text
Working Directory
        ↓
Staging Area
        ↓
Commit
        ↓
Git Database
```

---

## ⚡ Commands

```bash
git cat-file
git hash-object
git show
git log --graph
```

---

## 🎯 Interview Questions

- How does Git store files?
- What is HEAD?
- Why are commits immutable?

---

# 🧠 Session 3 — Branching

## 📖 Concepts

- What is a Branch?
- Why Branches exist
- Fast-forward Merge
- Detached HEAD
- Switching Branches

---

## ⚡ Commands

```bash
git branch
git switch
git checkout
git branch -d
```

---

## 🛠️ Hands-on

Create the following branch structure:

```text
main
 │
 ├── feature/login
 │
 └── feature/payment
```

Merge the feature branches back into `main`.

---

## 🎯 Interview Questions

- What is a Branch?
- What is Detached HEAD?

---

# 🧠 Session 4 — Merge & Merge Conflicts

## 📖 Concepts

- Merge
- Fast-forward Merge
- Three-way Merge
- Merge Conflicts

---

## ⚡ Commands

```bash
git merge
git diff
git mergetool
```

---

## 🛠️ Hands-on

- Create a merge conflict intentionally.
- Resolve the conflict.

---

## 🎯 Interview Questions

- Why do merge conflicts happen?
- How do you resolve merge conflicts?

---

# 🧠 Session 5 — Rebase

> ⭐ One of the most important Git interview topics.

## 📖 Concepts

- What is Rebase?
- Merge vs Rebase
- Interactive Rebase
- Squashing Commits

---

## ⚡ Commands

```bash
git rebase
git rebase -i
```

---

## 🛠️ Hands-on

- Clean up a messy commit history using Interactive Rebase.

---

## 🎯 Interview Questions

- Merge vs Rebase
- When should Rebase be avoided?

---

# 🧠 Session 6 — Stash & Cherry-pick

## 📖 Concepts

- Stashing Work
- Applying a Stash
- Dropping a Stash
- Cherry-picking Commits

---

## ⚡ Commands

```bash
git stash
git stash pop
git stash list
git cherry-pick
```

---

## 🛠️ Hands-on

- Pause your current feature using `git stash`.
- Switch branches.
- Recover your work.

---

## 🎯 Interview Questions

- When would you use `git stash`?
- What is `git cherry-pick`?

---

# 🧠 Session 7 — Reset, Restore & Revert

> ⭐ One of the most confusing Git topics.

## 📖 Concepts

- Soft Reset
- Mixed Reset
- Hard Reset
- Restore
- Revert

---

## ⚡ Commands

```bash
git reset
git restore
git revert
```

---

## 🧠 Visualize

```text
Working Directory
        ↓
Staging Area
        ↓
Commit History
```

Each command affects different parts of Git.

---

## 🎯 Interview Questions

- Reset vs Revert
- Hard Reset vs Soft Reset

---

# 🧠 Session 8 — Remote Repositories

## 📖 Concepts

- Origin
- Clone
- Fetch
- Pull
- Push
- Upstream Branches

---

## ⚡ Commands

```bash
git clone
git fetch
git pull
git push
git remote
```

---

## 🎯 Interview Questions

- Fetch vs Pull
- Why does `git push` sometimes fail?

---

# 🧠 Session 9 — Branching Strategies

## 📖 Concepts

- Feature Branches
- Release Branches
- Hotfix Branches
- GitFlow
- GitHub Flow
- Trunk-based Development (Overview)

---

## 🧠 Visualize

```text
main
 │
 ▼
develop
 │
 ├── feature/*
 │
 ▼
release
 │
 ▼
hotfix
```

---

## 🎯 Interview Questions

- What is GitFlow?
- Why use Feature Branches?

---

# 🧠 Session 10 — Real Developer Workflow

> Simulate a real software development team workflow.

## 🛠️ Project

```text
Backend API
      │
      ▼
Create Feature Branch
      │
      ▼
Commit Changes
      │
      ▼
Push to Remote
      │
      ▼
Create Pull Request
      │
      ▼
Code Review
      │
      ▼
Merge
      │
      ▼
Delete Feature Branch
```

---

## 🚀 You'll Practice

- Branching
- Rebasing
- Merging
- Resolving Merge Conflicts
- Pulling Changes
- Pushing Updates

---

# 🧠 Session 11 — Git Internals (Advanced)

> ⭐ Advanced topics for stronger interview preparation.

## 📖 Concepts

- Git Objects
- Reflog
- Pack Files
- Garbage Collection
- Detached Commits

---

## ⚡ Commands

```bash
git reflog
git gc
git fsck
```

---

## 🎯 Interview Questions

- How can Git recover deleted commits?
- What is `git reflog`?
- How does Git compress repositories?

---
