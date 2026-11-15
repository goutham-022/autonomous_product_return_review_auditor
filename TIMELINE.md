# Master Project Roadmap & Timeline: Autonomous Product Return & Review Auditor

**Cadence:** 1.0 Hour / Day | 7 Days / Week (0 Planned Rest Days)  
**Start Date:** 2026-11-13  
**Core Target Completion (34 Days):** 2026-12-16  
**Final Target with 7-Day Buffer (41 Days):** **2026-12-23**  
**Current Status:** 🔄 Step 0 (Architecture & Workspace Setup)

---

## 1. Master Timeline Overview (The 8-Step Production Sequence)

| Step | Milestone Name | Day Window | Target Dates | Est. Hours | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Step 0** | Architecture Blueprint, Safety Specs & Tooling Scaffolding | Days 1–3 | Nov 13 – Nov 15 | 3.0 hrs | 🔄 In Progress |
| **Step 1** | PostgreSQL & pgvector Infrastructure (`docker-compose.yml`) | Day 4 | Nov 16 | 1.0 hr | ⏳ Not Started |
| **Step 2** | Relational DB Models, Seed Data & Safe Text-to-SQL (AST) | Days 5–8 | Nov 17 – Nov 20 | 4.0 hrs | ⏳ Not Started |
| **Step 3** | Hybrid RAG Engine, Policy Ingestion & Review Defect Miner | Days 9–13 | Nov 21 – Nov 25 | 5.0 hrs | ⏳ Not Started |
| **Step 4** | Model Context Protocol (MCP) Server & Inspector Evals | Days 14–17 | Nov 26 – Nov 29 | 4.0 hrs | ⏳ Not Started |
| **Step 5** | LangGraph Multi-Agent State Machine, Guardrails & `inspect_ai` | Days 18–26 | Nov 30 – Dec 08 | 9.0 hrs | ⏳ Not Started |
| **Step 6** | Production FastAPI Webhook Ingestion Layer | Days 27–29 | Dec 09 – Dec 11 | 3.0 hrs | ⏳ Not Started |
| **Step 7** | Multi-Stage Production Containerization (`Dockerfile`) | Days 30–31 | Dec 12 – Dec 13 | 2.0 hrs | ⏳ Not Started |
| **Step 8** | Kubernetes (K8s) Deployment Manifests & Portfolio Landing | Days 32–34 | Dec 14 – Dec 16 | 3.0 hrs | ⏳ Not Started |
| **Buffer** | Red-Teaming, Edge-Case Hardening & Portfolio Demo Polish | Days 35–41 | Dec 17 – Dec 23 | 7.0 hrs | ⏳ Buffer Reserve |
| **TOTAL** | **Full Production & AI Safety Portfolio System** | **41 Days** | **Nov 13 – Dec 23**| **41.0 hrs** | 🎯 On Track |

---

## 2. Granular Step-by-Step Checklist

### Step 0: Architecture Blueprint, Safety Specs & Tooling (Days 1–3)
- [x] **M0.1**: Engineering Design Document & ASCII Blueprint (`docs/architecture.md`) ✅ (2026-11-15)
- [x] **M0.2**: Anthropic Fellow AI Safety Guardrails Specification (`inspect_ai` alignment) ✅ (2026-11-15)
- [ ] **M0.3**: Python Virtual Environment Setup with `uv` and lockfile dependencies
- [ ] **M0.4**: Git Repository Initialization, `.gitignore`, and Feature Branch Scaffolding

### Step 1: Docker-Compose & Database Infrastructure (Day 4)
- [ ] **M1.1**: Stand up isolated PostgreSQL service with local volume persistence and health checks.
- [ ] **M1.2**: Configure dedicated read-only database user credentials for AST safety layer.

### Step 2: Relational DB & Safe Text-to-SQL Engine (Days 5–8)
- [ ] **M2.1**: Implement lean 4-table SQLAlchemy models (`customers`, `products`, `orders`, `returns`).
- [ ] **M2.2**: Generate realistic synthetic e-commerce seed data (VIP customers, serial returners, batch defects).
- [ ] **M2.3**: Build Text-to-SQL engine with `sqlglot` AST validation (read-only enforcement, table whitelisting, limit injection).

### Step 3: Hybrid RAG & Review Mining Engine (Days 9–13)
- [ ] **M3.1**: Ingest multi-tier policy documents using structural markdown header chunking and category metadata into PostgreSQL (`pgvector`).
- [ ] **M3.2**: Ingest customer review corpus into PostgreSQL with pgvector embeddings and SKU filtering.
- [ ] **M3.3**: Implement the 15% Defect Ratio aggregation algorithm to detect systemic product defects.

### Step 4: Model Context Protocol (MCP) Server (Days 14–17)
- [ ] **M4.1**: Implement standalone MCP Server exposing 4 Pydantic tool contracts (`query_order_db`, `search_policy_docs`, `get_product_review_defects`, `submit_decision_audit`).
- [ ] **M4.2**: Verify tool discovery and execution schemas visually via MCP Inspector with zero LLM API cost.

### Step 5: LangGraph Multi-Agent Orchestration, Guardrails & `inspect_ai` (Days 18–26)
- [ ] **M5.1**: Define `ReturnAuditorState` with trusted/untrusted input separation and structural XML delimiters.
- [ ] **M5.2**: Implement the 4 Sequential Desks: Order Verifier, Policy Auditor, Review Miner, Decision Synthesizer.
- [ ] **M5.3**: Programmatic Hard Safety Gates in Python (`MAX_AUTONOMOUS_REFUND_LIMIT = 5000.00`, 75% velocity cap, Order-ID scoping).
- [ ] **M5.4**: `inspect_ai` Safety Benchmark Task: Red-teaming indirect prompt injection resilience and tool boundary enforcement.

### Step 6: Production FastAPI Ingestion (Days 27–29)
- [ ] **M6.1**: Implement `POST /api/v1/returns/audit` webhook endpoint.
- [ ] **M6.2**: Add request/response validation, PII masking, and structured error handling.

### Step 7: Multi-Stage Production Containerization (Days 30–31)
- [ ] **M7.1**: Author production-ready, non-root, multi-stage `Dockerfile` with `uv` caching.
- [ ] **M7.2**: Orchestrate full app + database stack via production `docker-compose.prod.yml`.

### Step 8: Kubernetes (K8s) Deployment & Portfolio Landing (Days 32–34)
- [ ] **M8.1**: Write Kubernetes deployment manifests (Deployments, Services, ConfigMaps, Secrets, Ingress).
- [ ] **M8.2**: Package repository with comprehensive system design documentation, test results, and demo video.

### Buffer Reserve: Safety Hardening & Red-Teaming (Days 35–41)
- [ ] **M-BUF.1**: Edge-case adversarial test suite execution (`inspect_ai`).
- [ ] **M-BUF.2**: System latency and token cost optimization audit.
- [ ] **M-BUF.3**: Final presentation polish for FDE & Anthropic Fellow review.

---

## 3. Technical Notes & Milestone Log
- **2026-11-13 (Day 1)**: Problem scoping with client *CartNest*. Core boundaries established for SQL, RAG, and MCP.
- **2026-11-14 (Day 2)**: First-principles deconstruction of Tools, MCP vs REST APIs, and MCP Inspector.
- **2026-11-15 (Day 3)**: Co-designed 4-desk LangGraph waterfall, decision actions, and AI Safety specifications for `inspect_ai`. Fixed architecture visual preview with ASCII diagram. M0.1 and M0.2 completed.
