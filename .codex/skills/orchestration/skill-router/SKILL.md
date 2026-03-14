---
name: skill-router
description: Select the right skills, determine their execution order, and define handoffs between them. Use when a task spans multiple responsibilities, needs a layered workflow, or risks mixing orchestration, guardrails, and atomic work in one step.
---

# Purpose

Choose the smallest effective set of skills for a task and order them into a coherent workflow. Keep responsibilities separated so the overall system stays composable and easy to extend.

# When To Use

Use this skill when:

- more than one skill may apply
- execution order matters
- a task risks collapsing several concerns into one broad workflow
- a clean handoff between planning, guardrails, and atomic work is needed

# Inputs

- the normalized task definition
- the currently available skill catalog
- any repository-specific constraints that affect sequencing
- known risks that require guardrails

# Process

1. Break the task into distinct concerns.
2. Match each concern to the most appropriate skill layer.
3. Select the minimum useful set of skills.
4. Define execution order and the handoff output expected from each step.
5. Note any guardrails that should remain active throughout the workflow.
6. Prefer simple routing over elaborate orchestration.

# Outputs

- a selected skill sequence
- a short rationale for each chosen skill
- handoff expectations between steps
- any always-on guardrails for the task

# Guardrails

- Do not route around a missing skill by overloading an unrelated one.
- Do not select extra skills that do not materially improve the workflow.
- Keep the route stable and easy to follow.
- If a skill combines unrelated concerns, recommend splitting rather than stretching the routing logic.

# Verification

- Every chosen skill has a clear reason to exist in the sequence.
- The order is actionable and not circular.
- Guardrail skills are attached where real risk exists.
- The workflow can be executed without inventing more routing decisions later.

# Escalation

Escalate when:

- the current catalog cannot cover the task cleanly
- a new reusable skill may be needed
- conflicting routing choices would materially change outcomes
