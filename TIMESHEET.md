# Project Timesheet: Autonomous Product Return & Review Auditor

**Weekly Cadence Target:** 7.0 Hours / Week (1.0 Hour / Day, 0 Planned Rest Days)  
**Start Date:** 2026-11-13  

---

## 1. Weekly Summary Tracker

| Week | Date Range | Target Hours | Logged Hours | Deficit / Surplus | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Week 1** | 2026-11-13 to 2026-11-19 | 7.0 hrs | 6.6 hrs | -0.4 hrs | 🔄 In Progress |

---

## 2. Daily Session Logs (Week 1)

| Day | Date | Time Window (IST) | Duration | Phase & Milestone | What Was Built / Discussed | Key FDE / Interview Takeaway |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 1** | 2026-11-13 | 19:30 - 20:37 | 1.1 hrs | Step 0 (`M0.1`) | • FDE kickoff with client *CartNest*<br>• Decoupled Text-to-SQL vs RAG vs MCP<br>• Designed 4 core tables (`customers`, `products`, `orders`, `returns`)<br>• Defined 4 decision output actions | • Text-to-SQL for deterministic math/dates; RAG for semantic policy/sentiment<br>• MCP as the "USB-C standard" preventing vendor lock-in & securing DB credentials |
| **Day 2** | 2026-11-14 | 08:20 - 10:36 | 2.3 hrs | Step 0 (`M0.1`, `M0.2`) | • Active Recall Quiz (100% score)<br>• Deconstructed AI "Tools" from first principles (LLM as receiver/reasoner)<br>• Derived parameterized tool calling & schema menus from scratch<br>• Dissected $M \times N$ API fragmentation vs standardized protocols<br>• Clarified MCP role: "Swagger for AI tools" & decoupled microservice for our custom LangGraph AI app | • Tool Calling Anatomy: LLMs predict tool selection & extract arguments; orchestrator executes<br>• MCP Inspector: The "Swagger UI" for AI tools to test schemas with zero LLM API cost<br>• Architecture Clarity: We are building the full AI application (LangGraph) + tool server (MCP) |
| **Day 3** | 2026-11-15 | 00:03 - 01:22 | 1.3 hrs | Step 0 (`M0.1`, `M0.2`) | • Co-designed 4-desk LangGraph waterfall flow & 5 decision actions<br>• Aligned project for dual FDE & Anthropic AI Safety Fellows (`inspect_ai`)<br>• Baked in 4 safety guardrails: decoupled Pydantic tools, trusted/untrusted XML state partition, hard Python gates (Rs 5,000 cap), and structured `AuditRecord` trace<br>• Standardized 100% on unified PostgreSQL + pgvector (eliminated ChromaDB)<br>• Finalized 41-day timeline with 7-day buffer | • Dual-Track Architecture: Decoupling tools and state enables plug-and-play evaluation in UK AISI `inspect_ai`<br>• Programmatic Guardrails: Hard business caps must live in Python code gates, never relying on LLM prompt obedience<br>• Unified Database Architecture: PostgreSQL + pgvector eliminates dual-database sprawl and enables hybrid relational+vector SQL queries |
| **Day 4** | 2026-11-15 | 07:20 - 09:14 | 1.9 hrs | Step 0 (`M0.3`, `M0.4`), Step 1 (`M1.1`), Step 2 (`M2.1` in progress) | • Initialized tooling with `uv`, locked dependencies (`uv.lock`), `.python-version`<br>• Git initialized, `.gitignore` customized to protect secrets, created branch `feature-1`<br>• Scaffolded modular package directory structure under `src/`<br>• Authored `docker-compose.yaml` for PostgreSQL 16 + pgvector (`product_return_review_db` on port 5434)<br>• Diagnosed Docker Compose stack naming in Docker Desktop (`name: product_return_review`)<br>• Implemented enterprise Pydantic v2 `BaseSettings` config in `src/utils/configs.py`<br>• Solved `uv_build` package resolution failure via `[tool.uv] package = false`<br>• Verified live `.env` loading, type casting (`float` cap), and fail-fast guarantees in terminal | • Fail-Fast Secrets Management: Pydantic `BaseSettings` eliminates silent `NoneType` bugs and guardrail comparison crashes caused by naked `os.getenv()`<br>• Application vs Library Packaging: `[tool.uv] package = false` treats the repository as an application runtime rather than a wheel package, eliminating build overhead in containerized AI microservices |
| **Day 5** | 2026-11-16 | TBD | - | Step 2 (`M2.1`, `M2.2`) | TBD | TBD |
| **Day 6** | 2026-11-18 | TBD | - | Step 2 (`M2.3`) | TBD | TBD |
| **Day 7** | 2026-11-19 | TBD | - | Step 3 (`M3.1`, `M3.2`) | TBD | TBD |
