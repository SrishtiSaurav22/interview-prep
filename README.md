# Interview Prep — Srishti Saurav

8-week structured prep for Backend, Full-stack, Cloud, and Flutter roles.
**30–45 min/day** on skill revision, alongside DSA (separate track), Biblo, and job hunting.

---

## Repo Structure

```
interview-prep/
├── week1-2-linux-bash-git/
├── week3-4-docker-cicd/
├── week5-databases/
├── week6-backend/
├── week7-aws/
├── week8-review/
└── README.md
```

Each folder contains scripts/code written that week, a short weekly README, and any config files (Dockerfiles, YAML workflows, SQL queries, etc.).

---

## The Plan

### Weeks 1–2 — Linux, Bash & Git
> Shakiest area · priority block

**Linux essentials**
- File system hierarchy, permissions (`chmod`/`chown`), process management (`ps`, `kill`, `top`), cron jobs, users & groups
- ~3 sessions × 40 min

**Bash scripting**
- Variables, conditionals, loops, functions, piping, redirects, writing automation scripts
- Practice: write 5 real scripts for tasks you'd do anyway
- ~3 sessions × 40 min

**Git internals for interviews**
- Rebase vs merge, cherry-pick, stash, reset vs revert, conflict resolution, branching strategies (GitFlow basics)
- ~2 sessions × 40 min

---

### Weeks 3–4 — Docker & CI/CD
> Shakiest area · priority block

**Docker fundamentals**
- Images vs containers, Dockerfile writing, multi-stage builds, volumes, networking (bridge/host), docker-compose
- Practice: containerise Biblo's backend
- ~4 sessions × 40 min

**GitHub Actions (CI/CD)**
- Workflow YAML syntax, triggers, jobs/steps, secrets, matrix builds, caching
- Practice: add a real pipeline to Biblo — lint + test + build on push
- ~3 sessions × 40 min — this also improves the Biblo project directly

---

### Week 5 — Databases
> SQL & NoSQL

**PostgreSQL / MySQL (interview depth)**
- Joins, indexing strategy, EXPLAIN plans, transactions & ACID, normalization, window functions
- Already using this in Biblo — focus on the *why*, not the *how*
- ~3 sessions × 40 min

**MongoDB**
- Document model, aggregation pipeline, indexing, schema design trade-offs vs relational
- Key interview question to be able to answer: *when would you pick MongoDB over Postgres?*
- ~2 sessions × 40 min

---

### Week 6 — Backend
> FastAPI, REST & JWT · Biblo-reinforced

**FastAPI & Pydantic**
- Dependency injection, async vs sync handlers, request validation, error handling, background tasks, OpenAPI generation
- Revisit Biblo's backend with interview eyes
- ~3 sessions × 40 min

**REST principles & JWT**
- Idempotency, HTTP verbs, status codes, versioning
- JWT: structure, signing, expiry, refresh token pattern, security pitfalls
- ~2 sessions × 40 min

---

### Week 7 — AWS / Cloud
> Real strength — focus is articulation, not learning

**Storytelling your AWS experience**
- Translate each service (OpenSearch, MSK, Kinesis, Kendra) into a 2-min STAR story
- 350+ resolved customer cases — interviewers don't need theory; they need to hear you reason about systems
- ~2 sessions × 40 min — write the stories out, don't just think them

**System design with AWS primitives**
- Practice designing 2–3 systems using services you've touched: a real-time data pipeline, a search system, a notification system
- Know the trade-offs, not just the services
- ~3 sessions × 40 min

---

### Week 8 — Review & Mock Interviews
> Consolidation

**Weak spot revisit**
- Spend the first half of the week on whichever of weeks 1–7 felt least solid
- Plug the single biggest gap — don't try to cover everything
- ~3 sessions × 40 min

**Mock interview practice**
- 2–3 timed mock sessions (Pramp, Interviewing.io, or with a friend)
- One DSA round + one system design round + one behavioural round per session
- ~2–3 sessions × 40 min

---

## What's Not Here (and Why)

| Skill | Reason |
|---|---|
| Flutter | Biblo is the live project. Building > studying. |
| C / C++ | Covered by the DSA track. |
| Dart | Comes with Flutter. Passive reinforcement is enough. |
| Python | Being written actively in Biblo's backend. |
| Canva, JSON, YAML | Not interview topics. |

---

## Parallel Tracks (not in this repo)

| Track | Format | Time |
|---|---|---|
| DSA | [Miscellaneous repo](https://github.com/SrishtiSaurav22/Miscellaneous-Mixed-Programs) + Udemy course | Mornings & early evenings |
| Biblo | [Biblo repo](https://github.com/SrishtiSaurav22/biblo) | Ongoing |
| French | Grammar / Comprehension / Writing / Practice | 30 min/day |
| Book reading | Physical books | 30 min/day |
| Job hunting | Applications & outreach | Late evenings |

---

## Notes System

- **Physical cheat sheets** — A4 notebook, one sheet per week block (6 total). Consistent layout: topic at top, key concepts in the middle, "things I always forget" at the bottom.
- **This repo** — all code, scripts, Dockerfiles, YAML configs, and weekly READMEs.
- **Cheat sheet count:** 6 over 8 weeks (weeks 1–2 share one, weeks 3–4 share one, then one each for weeks 5, 6, 7, 8).
