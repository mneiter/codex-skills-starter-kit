---
name: ci-verification
description: Run relevant repository validation steps and interpret the results. Use when changes need evidence, a task must be checked before handoff, or failures from existing verification commands need to be understood and reported clearly.
---

# Purpose

Confirm whether a change passes the repository's available verification steps. Translate raw command results into a concise status that others can use for review or follow-up work.

# When To Use

Use this skill when:

- implementation is complete
- a change needs validation evidence
- repository checks failed and need interpretation
- work should not be handed off without verification

# Inputs

- the set of relevant validation commands or checks
- the current repository state
- the scope of the change being validated
- any known test limitations or missing environments

# Process

1. Identify the smallest relevant validation set for the change.
2. Run the checks without rewriting repository-tracked files.
3. Capture pass, fail, or unable-to-run outcomes.
4. Summarize failures with the specific evidence needed for repair.
5. Report any validation gaps that remain.

# Outputs

- a concise validation summary
- command results or evidence references
- the relevant failures or warnings
- any known gaps in coverage or environment limits

# Guardrails

- Do not claim validation succeeded if checks were skipped.
- Do not run unrelated commands just to appear thorough.
- Keep the result focused on change safety and next actions.
- Report environment blockers explicitly.

# Verification

- The chosen checks match the scope of the change.
- Results are accurately reported.
- Failures are actionable and not buried in raw output.
- Any skipped or unavailable checks are clearly disclosed.

# Escalation

Escalate when:

- no reliable verification path exists
- failures point to broader repository issues outside the requested scope
- the required environment is unavailable and materially affects confidence
