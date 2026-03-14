---
name: example-skill-name
description: Describe what the skill does and when it should be used. Keep the description clear enough to trigger the skill in the right contexts without depending on project-specific assumptions.
---

# Purpose

State the single primary responsibility of the skill and the outcome it is meant to produce.

# When To Use

Describe the conditions that make this skill the right choice. Prefer clear triggers over broad claims.

# Inputs

List the information, context, artifacts, or constraints needed before this skill runs.

# Process

1. Describe the core sequence of actions the skill should follow.
2. Keep the process focused on one responsibility.
3. Prefer concise steps that another Codex instance can execute reliably.

# Outputs

List the expected artifacts, decisions, or summaries produced by the skill.

# Guardrails

- State what the skill must not do.
- Keep the skill within one primary responsibility.
- Split the skill if it begins combining intake, routing, execution, verification, or documentation concerns.

# Verification

Describe how to tell whether the skill result is complete, correct, and within scope.

# Escalation

Describe when to stop and hand off to another skill, request clarification, or recommend a new reusable skill.
