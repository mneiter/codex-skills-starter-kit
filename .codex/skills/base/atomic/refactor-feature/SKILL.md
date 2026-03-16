---
name: refactor-feature
description: Improve the internal structure of an existing feature while preserving intended behavior and scope. Use when maintainability, clarity, or duplication should be improved without adding new functionality or widening the task.
---

# Purpose

Refactor an existing feature in a bounded way. Improve structure, naming, cohesion, or duplication while keeping behavior aligned with the original intent.

# When To Use

Use this skill when:

- code or content structure needs cleanup
- behavior should stay effectively the same
- complexity or duplication is making changes harder
- the task calls for improvement without feature expansion

# Inputs

- the current feature implementation
- the intended existing behavior
- the requested refactoring goal
- any validation paths that protect behavior

# Process

1. Identify the specific structural problem to improve.
2. Define the behavioral boundaries that must remain unchanged.
3. Make the smallest coherent structural change that solves the problem.
4. Re-run the relevant validation to confirm behavior holds.
5. Summarize the refactor in terms of maintainability gains and preserved behavior.

# Outputs

- a bounded refactor change
- a short explanation of what improved
- evidence that intended behavior was preserved
- any remaining structural debt not addressed in scope

# Guardrails

- Do not smuggle new features into a refactor.
- Do not widen scope because cleanup opportunities exist nearby.
- Prefer incremental, reviewable changes over sweeping rewrites.
- Keep intent preservation explicit.

# Verification

- The target structural issue is reduced or removed.
- Behavior remains aligned with the pre-refactor intent.
- Relevant validation or review confirms no obvious regression.
- The change is easier to understand than the previous version.

# Escalation

Escalate when:

- the requested cleanup actually requires a behavior change
- the code shape suggests a broader redesign instead of a bounded refactor
- behavior is too unclear to preserve safely
