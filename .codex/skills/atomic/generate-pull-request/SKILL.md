---
name: generate-pull-request
description: Draft a reviewer-friendly pull request narrative from completed work and verification evidence. Use when implementation is done and the next step is to summarize changes, rationale, risk, and validation in a concise review package.
---

# Purpose

Turn finished work into a clear pull request summary. Make it easy for reviewers to understand what changed, why it changed, how it was verified, and what risks remain.

# When To Use

Use this skill when:

- changes are ready for review
- a concise summary is needed for reviewers
- verification evidence exists and should be communicated
- the user asks for a pull request description, summary, or review package

# Inputs

- the implemented change set
- the reason for the change
- verification results
- known risks, limitations, or follow-up items

# Process

1. Identify the user-visible or reviewer-relevant changes.
2. Summarize the motivation in plain language.
3. Capture how the work was validated.
4. Note residual risk, tradeoffs, or deferred work.
5. Present the result in a concise structure suitable for a pull request body.

# Outputs

- a pull request title or summary line
- a concise change summary
- validation evidence
- residual risks or follow-up notes

# Guardrails

- Do not invent validation that did not happen.
- Do not dump a file inventory without context.
- Keep the summary review-oriented, not implementation-noise heavy.
- Call out meaningful risk rather than hiding it in generic wording.

# Verification

- Reviewers can understand the purpose and impact of the change quickly.
- Validation details match the actual checks performed.
- Residual risk is explicit when present.
- The summary is concise enough to scan but complete enough to review.

# Escalation

Escalate when:

- the change set is too unclear to summarize reliably
- verification evidence is missing
- unresolved issues materially affect reviewer confidence
