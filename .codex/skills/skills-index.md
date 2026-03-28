# Skills Index

This index is the global skill catalog for `codex-skills-starter-kit`. It lists every actual skill that lives under `.codex/skills/`.

## Base Skills

### Orchestration

#### task-intake-supervisor

- Scope: `base`
- Layer: `orchestration`
- Purpose: Turn an incoming request into a clear task definition with goals, constraints, risks, and a ready handoff.
- When to use: Use when work begins with an ambiguous request, incomplete scope, unclear risks, or a need to prepare downstream skills.

#### skill-router

- Scope: `base`
- Layer: `orchestration`
- Purpose: Choose which skills should be used, in what order, and how outputs should flow between them.
- When to use: Use when a task spans multiple skills or when the correct execution sequence is not yet obvious.

### Guardrails

#### execution-memory-loop

- Scope: `base`
- Layer: `guardrails`
- Purpose: Preserve checkpoints, decisions, and next actions so long-running work stays coherent.
- When to use: Use during multi-step work, after interruptions, or whenever context must be refreshed without losing progress.

#### review-and-repair-loop

- Scope: `base`
- Layer: `guardrails`
- Purpose: Reinspect work, identify defects or gaps, repair them, and verify the repaired result.
- When to use: Use before closing work, after a failed validation step, or when quality concerns appear during review.

#### shared-boundary-guardrails

- Scope: `base`
- Layer: `guardrails`
- Purpose: Apply common operating limits that keep work generic, safe, and appropriately scoped.
- When to use: Use whenever there is risk of scope drift, unsafe assumptions, or mixing base-kit content with project-specific content.

### Atomic

#### ci-verification

- Scope: `base`
- Layer: `atomic`
- Purpose: Run relevant validation commands and interpret their outcomes.
- When to use: Use after making changes or when confirming whether a change is ready for review.

#### generate-pull-request

- Scope: `base`
- Layer: `atomic`
- Purpose: Convert a finished change into a reviewer-friendly pull request summary with evidence.
- When to use: Use when implementation is complete and the next step is to prepare a reviewable change description.

#### refactor-feature

- Scope: `base`
- Layer: `atomic`
- Purpose: Improve structure inside an existing feature while preserving intended behavior and boundaries.
- When to use: Use when maintainability needs improvement but the task does not call for new functionality.

#### unit-tests

- Scope: `base`
- Layer: `atomic`
- Purpose: Create or improve focused tests around small, stable units of behavior.
- When to use: Use when behavior needs regression protection, defect reproduction, or tighter verification coverage.

## Plugin Skills

Plugin: `skill-development`

### author-skill

- Scope: `plugin`
- Layer: `atomic`
- Purpose: Create a new skill with a clear responsibility, practical structure, and explicit boundaries.
- When to use: Use when a repository needs to draft a new skill and wants guidance on scope, trigger language, bundled resources, and review readiness.

### evaluate-skill

- Scope: `plugin`
- Layer: `guardrails`
- Purpose: Assess whether a skill is working as intended and identify the most useful next revision.
- When to use: Use when a skill exists already and the next step is to validate triggering, output quality, or scope discipline.

### optimize-skill-description

- Scope: `plugin`
- Layer: `atomic`
- Purpose: Improve a skill description so it triggers on the right user intent and stays distinct from nearby skills.
- When to use: Use when a skill workflow is mostly sound but its description is under-triggering, over-triggering, or colliding with adjacent skills.

Plugin: `devops`

### github-operations

- Scope: `plugin`
- Layer: `atomic`
- Purpose: Manage GitHub workflow state across repositories, pull requests, issues, reviews, and checks without absorbing verification, repair, refactoring, orchestration, or PR narrative work.
- When to use: Use when a repository needs GitHub-aware triage, blocked pull request inspection, review clustering, or a bounded GitHub-side lifecycle action.

## Project Skills

No project skills are registered in the starter kit by default. Adopting repositories should add project-specific skills under `.codex/skills/project/` and register them here when they exist.
