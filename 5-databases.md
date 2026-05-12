# 📚 Databases

---

# 🧠 Session 41 — Database Fundamentals

## 📖 Concepts

- What is a database?
- Why databases exist
- Structured vs unstructured data
- Relational databases
- NoSQL databases
- Persistence

---

## 🧠 Database Types

| Type | Examples |
|---|---|
| Relational (SQL) | PostgreSQL, MySQL |
| NoSQL | MongoDB, Redis |

---

## 🧠 SQL vs NoSQL

| SQL | NoSQL |
|---|---|
| Tables | Documents |
| Fixed schema | Flexible schema |
| Strong consistency | Flexible scaling |
| Joins | Embedded data |

---

## 🛠️ Hands-on

- Install PostgreSQL
- Install MongoDB
- Connect using terminal/client

---

## 🎯 Interview Focus

- Difference between SQL and NoSQL
- When to use relational databases
- Why persistence matters

---

# 🧠 Session 42 — PostgreSQL Basics

## 📖 Concepts

- Databases
- Tables
- Rows
- Columns
- Primary keys
- Data types

---

## ⚡ Basic SQL Commands

```sql
CREATE DATABASE
CREATE TABLE
INSERT
SELECT
UPDATE
DELETE
```

---

## 🛠️ Hands-on

### Create Database

```sql
CREATE DATABASE biblo;
```

---

### Create Table

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  email TEXT
);
```

---

### Insert Data

```sql
INSERT INTO users(name, email)
VALUES ('Srishti', 'srishti@example.com');
```

---

### Query Data

```sql
SELECT * FROM users;
```

---

## 🎯 Interview Focus

- What is a primary key?
- Difference between DELETE and DROP
- Why data types matter

---

# 🧠 Session 43 — SQL Queries & Filtering

## 📖 Concepts

- WHERE clause
- Filtering
- Sorting
- Limiting results
- Pattern matching

---

## ⚡ SQL Commands

```sql
SELECT
WHERE
ORDER BY
LIMIT
LIKE
IN
BETWEEN
```

---

## 🛠️ Hands-on

### Filter Data

```sql
SELECT * FROM users
WHERE name = 'Srishti';
```

---

### Sort Data

```sql
SELECT * FROM users
ORDER BY id DESC;
```

---

### Limit Results

```sql
SELECT * FROM users
LIMIT 5;
```

---

## 🎯 Interview Focus

- Difference between WHERE and HAVING
- Why indexing matters for filtering
- SQL query execution basics

---

# 🧠 Session 44 — Joins

## 📖 Concepts

- Relationships
- Foreign keys
- JOIN operations
- One-to-many relationships

---

## ⚡ Types of Joins

| Join | Meaning |
|---|---|
| INNER JOIN | Matching rows only |
| LEFT JOIN | All left rows + matches |
| RIGHT JOIN | All right rows + matches |
| FULL JOIN | Everything |

---

## 🛠️ Hands-on

### Example Tables

```sql
users
orders
```

---

### INNER JOIN

```sql
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
```

---

## 🎯 Interview Focus

- Difference between INNER and LEFT JOIN
- Why joins are expensive
- Foreign key purpose

---

# 🧠 Session 45 — Indexing

## 📖 Concepts

- What is an index?
- Query optimization
- B-tree indexes
- Tradeoffs

---

## ⚡ Commands

```sql
CREATE INDEX
EXPLAIN
```

---

## 🛠️ Hands-on

### Create Index

```sql
CREATE INDEX idx_users_email
ON users(email);
```

---

### Analyze Query

```sql
EXPLAIN SELECT * FROM users
WHERE email='abc@example.com';
```

---

## 🎯 Interview Focus

- Why indexes improve performance
- Downsides of indexes
- Why indexes slow writes

---

# 🧠 Session 46 — ACID & Transactions

## 📖 Concepts

- Transactions
- Atomicity
- Consistency
- Isolation
- Durability

---

## ⚡ Transaction Example

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

COMMIT;
```

---

## 🛠️ Hands-on

- Simulate money transfer
- Test rollback behavior

---

## 🎯 Interview Focus

- Explain ACID
- Why transactions matter
- What is rollback?

---

# 🧠 Session 47 — Database Normalization

## 📖 Concepts

- Redundancy
- Data consistency
- Normal forms
- Denormalization

---

## 🧠 Important Forms

| Form | Purpose |
|---|---|
| 1NF | Atomic values |
| 2NF | Remove partial dependency |
| 3NF | Remove transitive dependency |

---

## 🛠️ Hands-on

- Normalize user/order schema
- Identify duplicated data

---

## 🎯 Interview Focus

- Why normalization matters
- Tradeoff between normalization and performance
- What is denormalization?

---

# 🧠 Session 48 — Window Functions

## 📖 Concepts

- Analytical queries
- Ranking
- Running totals
- Partitioning

---

## ⚡ Example

```sql
SELECT
  name,
  salary,
  RANK() OVER (ORDER BY salary DESC)
FROM employees;
```

---

## 🛠️ Hands-on

- Rank users
- Calculate running totals
- Group analytics

---

## 🎯 Interview Focus

- Difference between GROUP BY and window functions
- Why window functions are powerful

---

# 🧠 Session 49 — MongoDB Fundamentals

## 📖 Concepts

- Document databases
- Collections
- BSON documents
- Flexible schema

---

## ⚡ MongoDB Basics

| SQL | MongoDB |
|---|---|
| Table | Collection |
| Row | Document |
| Column | Field |

---

## ⚡ Commands

```javascript
db.users.insertOne()
db.users.find()
db.users.updateOne()
db.users.deleteOne()
```

---

## 🛠️ Hands-on

### Insert Document

```javascript
db.users.insertOne({
  name: "Srishti",
  email: "srishti@example.com"
})
```

---

### Query Documents

```javascript
db.users.find()
```

---

## 🎯 Interview Focus

- SQL vs MongoDB
- Advantages of document databases
- Flexible schema tradeoffs

---

# 🧠 Session 50 — MongoDB Aggregation Pipeline

## 📖 Concepts

- Aggregation
- Data transformation
- Pipeline stages

---

## ⚡ Common Stages

| Stage | Purpose |
|---|---|
| $match | Filter |
| $group | Aggregate |
| $sort | Sort |
| $project | Shape output |

---

## 🛠️ Hands-on

### Aggregation Example

```javascript
db.orders.aggregate([
  { $match: { status: "SUCCESS" } },
  { $group: { _id: "$userId", total: { $sum: "$amount" } } }
])
```

---

## 🎯 Interview Focus

- Why aggregation pipelines matter
- Aggregation vs SQL GROUP BY
- MongoDB analytics workflows

---

# 🧠 Session 51 — Schema Design & SQL vs NoSQL Tradeoffs

## 📖 Concepts

- Schema design
- Embedding vs referencing
- Scalability
- Consistency vs flexibility

---

## 🧠 Tradeoffs

| SQL | NoSQL |
|---|---|
| Strong consistency | Flexible schema |
| Complex joins | Easier horizontal scaling |
| Structured relations | Fast iteration |

---

## 🛠️ Hands-on

- Design schema for Biblo
- Decide SQL vs MongoDB use cases

---

## 🎯 Interview Focus

- When to choose PostgreSQL
- When MongoDB is better
- Scalability tradeoffs

---

# 🧠 Session 52 — Real Backend Database Design

## 🛠️ Build Real Database Architecture for Biblo

### Design Tables/Collections

- Users
- Books
- Reviews
- Favorites
- Authentication

---

## 🚀 Features

- Proper indexing
- Relationships
- Optimized queries
- Environment configs
- Production-ready structure

---

## 🧠 Important Database Concepts Summary

| Concept | Importance |
|---|---|
| Indexing | Faster queries |
| Transactions | Data integrity |
| Joins | Relational querying |
| Aggregation | Analytics |
| Schema Design | Scalability |
| ACID | Reliability |
| Normalization | Reduced redundancy |
| Window Functions | Advanced analytics |

---
