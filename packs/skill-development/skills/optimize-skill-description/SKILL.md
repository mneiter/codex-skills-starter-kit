---
name: optimize-skill-description
description: Improve a skill description so it better matches user intent, uses stronger trigger language, and avoids false triggers. Use when a skill workflow is sound but the description is too weak, too vague, or too broad.
---

# Purpose

Refine the frontmatter description of an existing skill so it triggers on the right user intent and stays distinct from nearby skills.

# When To Use

Use this skill when:

- the skill should trigger more often than it currently does
- the skill is triggering in the wrong situations
- the workflow is mostly sound but the description is weak
- neighboring skills are overlapping because the current wording is unclear

# Inputs

- the current skill description
- the skill's actual purpose and boundaries
- examples of should-trigger and should-not-trigger cases
- nearby skills that may overlap

# Process

1. Identify the user intent the description should capture.
2. Identify likely trigger phrases or situations.
3. Identify negative boundaries for adjacent cases.
4. Rewrite the description to be concise, distinctive, and intent-focused.
5. Check whether the new wording avoids overfitting to narrow examples.

# Outputs

- an improved skill description
- a short rationale for the change
- clearer trigger and non-trigger boundaries

# Guardrails

- Do not widen the skill beyond its actual responsibility.
- Do not stuff the description with long keyword lists.
- Do not use implementation detail as the primary framing when user intent is clearer.

# Verification

- The revised description matches the actual skill purpose.
- Trigger language is clearer than before.
- Negative boundaries reduce overlap with neighboring skills.
- The final wording remains concise and reusable.

# Escalation

Escalate when:

- the real problem is the skill workflow, not the description
- the skill is overloaded and needs splitting
- the description cannot be improved without first redefining the skill
