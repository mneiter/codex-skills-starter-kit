---
name: execution-memory-loop
description: Preserve checkpoints, decisions, and next-step clarity during longer or multi-step work. Use when execution may span several phases, include interruptions, or require disciplined state tracking to avoid losing context.
---

# Purpose

Maintain working continuity during execution. Capture what was learned, what changed, what remains open, and what should happen next so the task can continue without re-deriving prior decisions.

# When To Use

Use this skill when:

- the task has multiple steps or phases
- work may pause and resume later
- several decisions or findings need to stay visible
- the agent risks losing track of progress or open items

# Inputs

- the current task frame
- completed actions and observed results
- unresolved issues or pending validations
- the immediate next actions

# Process

1. Record the current checkpoint in a compact form.
2. Separate completed work from open work.
3. Capture decisions, assumptions, and blockers.
4. Keep the next action explicit and small enough to execute.
5. Refresh the checkpoint after meaningful progress or interruptions.
6. Preserve only the information needed to continue confidently.

# Outputs

- a current progress checkpoint
- a list of open issues or unknowns
- explicit next actions
- a short memory of important decisions and why they were made

# Guardrails

- Do not turn checkpoints into long diaries.
- Prefer current actionable state over exhaustive history.
- Remove stale assumptions when new facts replace them.
- Keep memory artifacts aligned with the actual task scope.

# Verification

- Another pass can resume work from the checkpoint without rereading everything.
- Open items are distinguishable from completed work.
- Next actions are concrete and sequenced.
- The checkpoint reflects the latest known state.

# Escalation

Escalate when:

- the task has changed enough that the checkpoint no longer matches reality
- unresolved blockers require a change in direction
- memory overhead is growing because the workflow is too broad and needs to be split
