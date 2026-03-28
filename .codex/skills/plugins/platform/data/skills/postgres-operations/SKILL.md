---
name: postgres-operations
description: Manage PostgreSQL operational state across sessions, queries, locks, indexes, and schema-risk signals. Use when work needs PostgreSQL-aware triage or bounded read-only diagnostics, while keeping orchestration, verification, repair, refactoring, and PR writeups in separate skills.
---

# Purpose

Manage PostgreSQL operational state without absorbing implementation, migration, or verification work. This skill inspects safe PostgreSQL evidence around queries, sessions, locks, indexes, and schema-risk signals, summarizes likely database-side causes conservatively, and ends with a clear next PostgreSQL-native step or handoff.

# When To Use

Use this skill when:

- the user wants a PostgreSQL state summary for a query, workload symptom, or database concern
- slow-query, plan, or index-usage symptoms need diagnostic triage
- connection pressure, waits, or lock symptoms need interpretation
- schema-risk or migration-risk concerns need conservative review before broader implementation work
- database-side evidence should be gathered and interpreted without destructive action
- the next PostgreSQL-native diagnostic step needs to be identified before repair or refactoring work

# When Not To Use

Do not use this skill when:

- the task needs multi-skill sequencing or workflow design; use `skill-router`
- the task needs validation execution or measured evidence for success claims; use `ci-verification`
- the task needs a reviewer-facing pull request summary; use `generate-pull-request`
- the task needs code, migration, or content repair after findings; use `review-and-repair-loop`
- the task is a behavior-preserving structural cleanup; use `refactor-feature`
- the task asks for destructive SQL, schema changes, migration execution, ORM refactors, application-layer bug fixes, full DBA ownership, or claims that performance is fixed

# Inputs

- the database, schema, or connection context in scope
- the query text, plan output, schema snippet, or migration snippet when available
- the table, index, session, lock, or workload symptom already observed
- the logs, metrics, or database-side evidence already available
- Dependencies: read-only PostgreSQL access when available, plus `skill-router`, `ci-verification`, `generate-pull-request`, `review-and-repair-loop`, and `refactor-feature`

# Capabilities

- inspect PostgreSQL operational state through safe read-only evidence
- interpret session, connection, wait, and lock symptoms
- analyze query-plan and index signals conservatively
- identify schema-risk or migration-risk patterns
- recommend the next PostgreSQL-native diagnostic step
- stay hypothesis-driven instead of prescribing implicit fixes

# Process

1. Resolve the target query, workload symptom, or database concern in scope.
2. Classify the request as query, lock, connection, index, or migration-risk triage.
3. Gather only non-destructive PostgreSQL evidence needed to answer the request.
4. Summarize likely database-side causes conservatively and keep the reasoning inside PostgreSQL boundaries.
5. Recommend the next safe PostgreSQL-native diagnostic step or hand off when the next owner is outside database operational triage.

# Outputs

- a concise PostgreSQL-state summary
- the likely bottleneck, wait, or risk cluster relevant to the request
- the next safe PostgreSQL-native diagnostic step
- an explicit handoff when the next owner is outside database operational triage

# Boundaries

- `skill-router` chooses when several skills are needed; `postgres-operations` handles only the PostgreSQL operational slice once the task is in scope.
- `ci-verification` owns running checks and producing validation evidence; `postgres-operations` only summarizes database-side state and likely causes.
- `generate-pull-request` owns reviewer-facing pull request narrative; `postgres-operations` may prepare context but does not write the summary.
- `review-and-repair-loop` owns repair passes and re-verification; `postgres-operations` may surface database-side findings but does not fix them.
- `refactor-feature` owns behavior-preserving structural cleanup; `postgres-operations` may identify that need but does not perform it.

# Handoffs

- hand off to `skill-router` when the task mixes PostgreSQL triage with other execution concerns
- hand off to `ci-verification` when measured evidence or validation claims are required
- hand off to `review-and-repair-loop` when the diagnosis becomes repair or migration work
- hand off to `refactor-feature` when the next step is code or query-layer restructuring rather than database triage
- hand off to `generate-pull-request` when the change is done and reviewer-facing narrative is next

# Example Workflows

1. Slow-query triage: inspect query text, plan output, and index signals to explain likely database-side bottlenecks.
2. Lock or wait inspection: summarize blocking, waiting, or connection pressure symptoms from safe database evidence.
3. Migration-risk review: inspect schema or migration snippets for likely operational risk before implementation work begins.
4. Next-step guidance: summarize the current PostgreSQL-side evidence and identify the next safe diagnostic step without claiming a fix.

# Guardrails

- Perform read-only diagnostics only in v1.
- Do not run destructive or mutating SQL, including DDL, DML, migration execution, session termination, stats resets, or maintenance commands.
- Do not run `EXPLAIN ANALYZE`; prefer plain `EXPLAIN` or plan artifacts already provided.
- Do not imply that an index, rewrite, or schema change should be applied as if it were already validated.
- Keep recommendations diagnostic, conservative, and hypothesis-driven.
- Ask or hand off instead of guessing when the target, risk, or next owner is unclear.

# Verification

- The result stays inside PostgreSQL operational diagnosis and safe evidence gathering.
- Any likely cause or next step is tied to observed PostgreSQL evidence rather than assumption.
- No destructive or mutating database action is performed or implied as already validated.
- Work that required orchestration, repair, refactoring, validation, or PR narrative was handed off instead of absorbed here.

# Escalation

Escalate when:

- the PostgreSQL target or relevant access cannot be resolved
- the request is risky, ambiguous, or mixes database triage with broader execution concerns
- the symptoms clearly require implementation, migration execution, repair, or broader system routing outside PostgreSQL operational diagnosis
