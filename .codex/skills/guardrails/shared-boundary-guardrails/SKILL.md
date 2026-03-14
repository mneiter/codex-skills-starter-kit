---
name: shared-boundary-guardrails
description: Apply common operating boundaries that keep work safe, generic, and appropriately scoped. Use when there is risk of scope drift, unsafe assumptions, project-specific leakage, or mixing the base skill layer with add-on concerns.
---

# Purpose

Define and enforce the shared boundaries that apply across many tasks. This skill keeps execution inside the requested scope and protects the canonical base layer from accidental specialization.

# When To Use

Use this skill when:

- work touches shared starter-kit content
- there is a risk of mixing reusable guidance with local project rules
- scope drift is likely
- the task needs a stable boundary statement before execution proceeds

# Inputs

- the task scope
- the current repository boundaries
- known exclusions and non-goals
- any extension rules that apply to the task

# Process

1. Identify the requested scope and the nearby out-of-scope areas.
2. Check whether the task belongs in the base layer, a local skill, or a future pack.
3. State the boundaries that must remain true during execution.
4. Revisit those boundaries when the task changes or expands.
5. Stop and escalate if the work would pollute the base layer.

# Outputs

- a clear statement of in-scope and out-of-scope work
- boundary checks for the current task
- a recommendation when the work belongs outside the base layer

# Guardrails

- Do not let convenience override repository boundaries.
- Do not place specialized guidance into shared base skills.
- Prefer additive extensions over modifying canonical base content to fit a niche need.
- Keep the boundary statement short, explicit, and enforceable.

# Verification

- The task output stays inside the stated scope.
- Base skills remain generic after the work is done.
- Out-of-scope concerns were not silently folded into shared assets.
- Extension recommendations are consistent with repository policy.

# Escalation

Escalate when:

- the request would make a base skill technology-specific
- a new pack or local skill is the cleaner solution
- the correct boundary between shared and specialized content is disputed
