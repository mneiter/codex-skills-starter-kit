---
name: task-intake-supervisor
description: Normalize incoming work into a clear task definition with goals, constraints, risks, and handoff guidance. Use when a request is ambiguous, incomplete, high-impact, or needs to be prepared for downstream skills before execution starts.
---

# Purpose

Turn an incoming request into an execution-ready task frame. Reduce ambiguity, surface missing constraints, define success conditions, and prepare a clean handoff for the next skill or workflow step.

# When To Use

Use this skill when:

- the request is broad or underspecified
- multiple interpretations are possible
- the work affects several files, systems, or decision points
- downstream skills need a normalized brief before execution

# Inputs

- the original user request
- any repository or environment context already discovered
- known constraints, deadlines, or non-goals
- known risks, open assumptions, or dependencies

# Process

1. Restate the request as a concrete task with a clear outcome.
2. Separate confirmed facts from assumptions.
3. Identify scope boundaries, likely touchpoints, and major risks.
4. Define practical success criteria that can be verified later.
5. Identify what kind of downstream skill should take over next.
6. Produce a concise handoff that preserves the task frame without repeating noise.

# Outputs

- a normalized task statement
- explicit success criteria
- a list of relevant constraints and assumptions
- a short risk summary
- a recommended next skill or workflow step

# Guardrails

- Do not start implementation inside this skill.
- Do not silently invent product intent when the environment already answers the question.
- Keep the output compact and reusable by other skills.
- Preserve the distinction between known facts and inferred assumptions.

# Verification

- The task can be understood without rereading the original request.
- Success criteria are concrete enough to check later.
- Constraints and risks are visible and not buried in prose.
- The proposed handoff matches the actual shape of the work.

# Escalation

Escalate when:

- the request contains contradictory goals
- the scope could change production behavior in unclear ways
- essential intent cannot be discovered from context and materially changes the solution
