---
name: evaluate-skill
description: Evaluate whether an existing skill triggers correctly, stays within scope, and produces useful results. Use when reviewing a skill draft, diagnosing weak behavior, or deciding the next revision step.
---

# Purpose

Review a skill's current effectiveness and identify the smallest high-value improvement. Focus on trigger quality, output quality, scope discipline, and whether the skill needs revision, more resources, or a split.

# When To Use

Use this skill when:

- a skill draft already exists
- a skill appears to under-trigger or over-trigger
- output quality is uncertain
- the next step needs to be chosen after a review pass

# Inputs

- the current skill
- realistic prompts or review scenarios
- expected outcomes
- any existing review notes, findings, or examples

# Process

1. Review the description and identify the intended trigger surface.
2. Select a small set of realistic prompts or review cases.
3. Compare results against the expected outcomes and scope boundaries.
4. Note whether problems come from the description, the workflow, or missing resources.
5. Record a decision using a small set of explicit outcomes.

# Outputs

- a skill review summary
- findings on trigger quality and scope discipline
- a recommended next action
- a final decision such as keep, revise, add resources, split, or move to pack

# Guardrails

- Do not invent elaborate evaluation tooling when lightweight review is enough.
- Do not treat superficial success as proof that the skill is strong.
- Keep findings tied to observable prompts, behavior, and outputs.

# Verification

- The review makes a clear recommendation.
- Findings distinguish between trigger issues, workflow issues, and placement issues.
- The skill's scope remains visible throughout the review.

# Escalation

Escalate when:

- the skill needs several conflicting changes at once
- the skill overlaps too much with a neighboring skill
- the right answer is architectural rather than evaluative
