# AWS Revision Syllabus

> **Goal:** Not to learn AWS from scratch — you already know it.
> The goal is to articulate what you know confidently in interviews — **as an engineer, not as a support person.**

---

## Table of Contents

- [Block 1 — Core Services (Articulation Focus)](#block-1--core-services-articulation-focus)
- [Block 2 — Supporting Services](#block-2--supporting-services-depth-on-what-you-used)
- [Block 3 — System Design with AWS Primitives](#block-3--system-design-with-aws-primitives)
- [Block 4 — SAA-C03 Certification Gaps](#block-4--the-saa-c03-certification-gap)
- [Block 5 — Storytelling Your Experience](#block-5--storytelling-your-experience)

---

## Block 1 — Core Services (Articulation Focus)

> These are services you worked with daily.
> You need to explain them at **architecture level**, not just usage level.

### 🔍 Amazon OpenSearch

| Topic | What to Know |
|---|---|
| Cluster architecture | Data nodes, master nodes, UltraWarm |
| Index lifecycle management | Hot / warm / cold tiers |
| Shard allocation | Why yellow/red states happen and how to fix them |
| Indexing performance | Refresh interval, bulk indexing, mapping design |

> 💡 **You built a chatbot to automate yellow/red state troubleshooting — own this story.**

**Common interview question:**
> *"Design a search system at scale"* — you can answer this from real production experience.

---

### 📨 Amazon MSK (Managed Streaming for Kafka)

| Topic | What to Know |
|---|---|
| Kafka fundamentals | Topics, partitions, consumer groups, offsets |
| MSK-specific | Broker sizing, storage, MSK Connect, schema registry |
| Streaming concepts | At-least-once vs exactly-once delivery, lag monitoring |

**Common interview question:**
> *"How would you build a real-time data pipeline?"* — real experience, speak to it directly.

---

### 🌊 Amazon Kinesis Suite

| Topic | What to Know |
|---|---|
| Service comparison | Kinesis Data Streams vs Firehose vs Data Analytics — when to use which |
| Streams internals | Sharding, enhanced fan-out, data retention |
| KDA / Flink | Windowing, stateful processing basics |

---

### ⚡ Amazon Managed Streaming for Flink (MSF)

| Topic | What to Know |
|---|---|
| Flink fundamentals | Stateful stream processing, checkpointing, watermarks |
| MSF vs self-managed | Key differences and when MSF makes sense |
| Use cases | Real-time aggregations, sessionisation, anomaly detection |

---

## Block 2 — Supporting Services (Depth on What You Used)

### 📊 CloudWatch

| Topic | What to Know |
|---|---|
| Three pillars | Metrics vs Logs vs Traces |
| Operationalisation | Alarms, dashboards, log insights queries |
| Custom metrics | How to instrument an application |

**Common interview question:**
> *"How would you monitor a distributed system?"* — CloudWatch is your answer.

---

### 🔎 CloudTrail

| Topic | What to Know |
|---|---|
| CloudWatch vs CloudTrail | Know the difference cold — what each captures and why |
| Use cases | Audit, compliance, security forensics |

**Common interview question:**
> *"How do you audit API calls in AWS?"*

---

### 🔐 IAM

| Topic | What to Know |
|---|---|
| Policy types | Identity-based vs resource-based |
| Principals | Roles vs users vs groups |
| Advanced | Cross-account access, assume role |
| Core principle | Least privilege — be able to design a policy in an interview |

---

### 🌐 VPC

| Topic | What to Know |
|---|---|
| Subnets | Public vs private — routing implications |
| Security | Security groups (stateful) vs NACLs (stateless) |
| Connectivity | VPC peering, NAT gateway, internet gateway |

**Common interview question:**
> *"Walk me through how you'd architect a secure VPC."*

---

### 🗂️ Other Services on Your Resume

| Service | Key Concepts |
|---|---|
| **S3** | Storage classes, lifecycle policies, versioning, bucket policies |
| **EC2** | Instance types, AMIs, auto scaling groups, placement groups |
| **RDS** | Multi-AZ vs read replicas, automated backups, parameter groups |
| **Lambda** | Cold starts, concurrency limits, event sources, layers |
| **Kendra / Q Business** | What they are, when you'd recommend them |
| **AppFlow** | Data integration, source/destination connectors |

---

## Block 3 — System Design with AWS Primitives

> This is where interviews actually test you.
> For **each design**, be ready to answer: *why this service over alternatives, what breaks at scale, how you'd monitor it.*

---

### Design 1 — Real-Time Streaming Data Pipeline

```
Kinesis → Lambda / Flink → OpenSearch → CloudWatch
```

You've seen this architecture in production. Write it out. Know the trade-offs at each step.

**Key discussion points:**
- Why Kinesis over Kafka here (or vice versa)?
- When would you use Flink vs Lambda for processing?
- How do you handle backpressure and failures?
- How do you monitor lag and throughput?

---

### Design 2 — Search System at Scale

```
S3 → OpenSearch + API Gateway + Lambda → CloudFront
```

**Key discussion points:**
- Indexing strategy — how do you structure mappings for performance?
- Query optimisation — filters vs queries, caching
- High availability — multi-AZ OpenSearch, replica shards
- How do you handle re-indexing without downtime?

---

### Design 3 — Event-Driven Notification System

```
SNS → SQS → Lambda → DynamoDB / RDS
```

**Key discussion points:**
- Fan-out pattern — SNS topic → multiple SQS queues
- Dead letter queues — what they are and when to use them
- Idempotency — why it matters and how to implement it
- At-least-once vs exactly-once delivery trade-offs

---

## Block 4 — The SAA-C03 Certification Gap

> Your cert is valid until May 2027 but interviews often go deeper than the exam.

### Cost Optimisation
- Savings Plans vs Reserved Instances vs Spot — know when each makes sense
- Right-sizing — how you'd approach it for a real workload

### High Availability Patterns
- Multi-AZ vs multi-region — trade-offs in cost and complexity
- Failover strategies — Route 53, RDS failover, warm standby vs pilot light

### Storage Decision Matrix

| Use Case | Service |
|---|---|
| Object storage, static files, backups | S3 |
| Shared file system for EC2 (Linux) | EFS |
| Block storage attached to a single EC2 | EBS |
| Windows file shares, high-performance NAS | FSx |

### Database Decision Matrix

| Use Case | Service |
|---|---|
| Relational, ACID, complex queries | RDS / Aurora |
| Key-value, massive scale, low-latency | DynamoDB |
| Managed Postgres/MySQL with auto-scaling | Aurora Serverless |
| Data warehousing, analytical queries | Redshift |

### Compute Trade-offs

| Option | When to Choose |
|---|---|
| Lambda (Serverless) | Event-driven, short-lived, unpredictable traffic |
| ECS / EKS (Containers) | Microservices, consistent workloads, more control |
| EC2 | Long-running, stateful, custom OS requirements |

---

## Block 5 — Storytelling Your Experience

> Write each story in **STAR format** (Situation → Task → Action → Result).
> Practise saying them out loud — the content is real, the delivery needs work.

### Stories to Prepare

| # | Story | Your Strongest Asset |
|---|---|---|
| 1 | Diagnosing a complex distributed systems issue | Pick your best case from the 350+ resolved |
| 2 | Improving an internal process | **The OpenSearch chatbot — your single strongest story** |
| 3 | Explaining a technical issue to a non-technical stakeholder | Customer communication at AWS |
| 4 | Deep root cause analysis that uncovered something unexpected | Real debugging war story |
| 5 | Working under pressure to resolve a production-impacting incident | Live debugging sessions |

### STAR Format Reminder

```
Situation — What was the context? What was broken or at risk?
Task       — What were you responsible for?
Action     — What did you specifically do? (Use "I", not "we")
Result     — What was the measurable outcome?
```

> ⏱️ **Target:** 2 minutes per story. Time yourself.

---

