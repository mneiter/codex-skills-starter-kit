---
name: example-skill-name
description: Describe what the skill does and when it should be used. Keep the description clear enough to trigger the skill in the right contexts without depending on project-specific assumptions.
---

# Purpose

State the single primary responsibility of the skill and the outcome it is meant to produce. Keep the purpose centered on what the user is trying to achieve, not on the implementation details hidden inside the skill.

# When To Use

Describe the conditions that make this skill the right choice.

- use user-intent language rather than internal implementation terms
- mention a few strong trigger phrases or situations
- make clear when the skill should not trigger to avoid overlap with neighboring skills
- keep the description broad enough to generalize, but specific enough to be distinctive

# Inputs

List the information, context, artifacts, or constraints needed before this skill runs.

# Process

1. Describe the core sequence of actions the skill should follow.
2. Keep the process focused on one responsibility.
3. Prefer concise steps that another Codex instance can execute reliably.
4. When the skill grows large, point to bundled resources instead of expanding the main body indefinitely.

# Outputs

List the expected artifacts, decisions, or summaries produced by the skill. Be explicit about structure when the output format matters.

# Guardrails

- State what the skill must not do.
- Keep the skill within one primary responsibility.
- Split the skill if it begins combining intake, routing, execution, verification, or documentation concerns.
- Add `scripts/`, `references/`, or `assets/` only when they provide clear reusable value.
- Keep project-specific or vendor-specific guidance out of reusable base skills.

# Verification

Describe how to tell whether the skill result is complete, correct, and within scope.

- for objective skills, note a small validation path or expected checks
- for subjective skills, describe the review criteria clearly

# Escalation

Describe when to stop and hand off to another skill, request clarification, or recommend a new reusable skill.
