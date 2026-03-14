---
name: review-and-repair-loop
description: Reinspect completed work, identify defects or gaps, repair them, and re-verify the result. Use when quality must be confirmed, validation failed, or work should be tightened before handoff or closure.
---

# Purpose

Provide a disciplined loop for checking work, fixing what is wrong, and confirming that the fix actually solved the issue. This keeps quality work separate from initial execution.

# When To Use

Use this skill when:

- implementation is complete and needs review
- a validation step failed
- defects, omissions, or regressions were found
- work should be tightened before final delivery

# Inputs

- the current implementation or artifact
- validation output, review findings, or defect reports
- the intended success criteria
- any constraints that fixes must respect

# Process

1. Review the work against the success criteria and known findings.
2. Identify the highest-impact issues first.
3. Repair one coherent set of issues at a time.
4. Re-run the relevant verification after each repair pass.
5. Stop when the result meets the task bar or when a higher-level decision is required.

# Outputs

- a prioritized list of findings
- a repair pass that addresses the findings
- updated verification evidence
- any residual risks or limitations that remain

# Guardrails

- Do not mask missing verification with confidence language.
- Do not widen scope while fixing defects.
- Keep findings concrete and tied to observable behavior.
- If no issue exists, state that clearly instead of inventing work.

# Verification

- Reported issues are either fixed or explicitly deferred.
- The relevant verification was rerun after repairs.
- Residual risk is visible when complete confidence is not possible.
- The final state is stronger than the initial reviewed state.

# Escalation

Escalate when:

- fixing one issue would require changing the requested scope
- repeated repair passes keep failing on the same class of defect
- the task needs a design decision rather than another repair loop
