# Skills Index

This index is a quick catalog of the canonical base skills.

## Orchestration

### task-intake-supervisor

- Layer: `orchestration`
- Purpose: Turn an incoming request into a clear task definition with goals, constraints, risks, and a ready handoff.
- When to use: Use when work begins with an ambiguous request, incomplete scope, unclear risks, or a need to prepare downstream skills.

### skill-router

- Layer: `orchestration`
- Purpose: Choose which skills should be used, in what order, and how outputs should flow between them.
- When to use: Use when a task spans multiple skills or when the correct execution sequence is not yet obvious.

## Guardrails

### execution-memory-loop

- Layer: `guardrails`
- Purpose: Preserve checkpoints, decisions, and next actions so long-running work stays coherent.
- When to use: Use during multi-step work, after interruptions, or whenever context must be refreshed without losing progress.

### review-and-repair-loop

- Layer: `guardrails`
- Purpose: Reinspect work, identify defects or gaps, repair them, and verify the repaired result.
- When to use: Use before closing work, after a failed validation step, or when quality concerns appear during review.

### shared-boundary-guardrails

- Layer: `guardrails`
- Purpose: Apply common operating limits that keep work generic, safe, and appropriately scoped.
- When to use: Use whenever there is risk of scope drift, unsafe assumptions, or mixing base-kit content with project-specific content.

## Atomic

### ci-verification

- Layer: `atomic`
- Purpose: Run relevant validation commands and interpret their outcomes.
- When to use: Use after making changes or when confirming whether a change is ready for review.

### generate-pull-request

- Layer: `atomic`
- Purpose: Convert a finished change into a reviewer-friendly pull request summary with evidence.
- When to use: Use when implementation is complete and the next step is to prepare a reviewable change description.

### refactor-feature

- Layer: `atomic`
- Purpose: Improve structure inside an existing feature while preserving intended behavior and boundaries.
- When to use: Use when maintainability needs improvement but the task does not call for new functionality.

### unit-tests

- Layer: `atomic`
- Purpose: Create or improve focused tests around small, stable units of behavior.
- When to use: Use when behavior needs regression protection, defect reproduction, or tighter verification coverage.
