---
name: author-skill
description: Create a new skill with a clear primary responsibility, practical trigger language, and appropriate bundled resources. Use when drafting a new skill or restructuring an early draft into a cleaner reusable skill.
---

# Purpose

Guide the creation of a new skill from idea to well-scoped draft. Keep the skill centered on one primary responsibility and make early decisions about descriptions, boundaries, and bundled resources.

# When To Use

Use this skill when:

- a new skill is being created from scratch
- an early draft exists but needs cleaner structure
- a workflow should become a reusable skill rather than an ad hoc process

# Inputs

- the intended user goal
- likely trigger situations
- expected outputs
- known constraints, boundaries, or neighboring skills

# Process

1. Define the skill's single primary responsibility.
2. Identify the user intents that should trigger the skill.
3. Define nearby cases that should not trigger it.
4. Draft the `SKILL.md` structure with clear inputs, process, outputs, guardrails, verification, and escalation.
5. Decide whether `scripts/`, `references/`, or `assets/` are needed.
6. Check whether the skill belongs in the canonical base layer, the project area, or a reusable plugin.

# Outputs

- a well-scoped skill draft
- a draft description with trigger and boundary language
- a recommendation on bundled resources
- a placement recommendation for base layer, plugin, or project use

# Guardrails

- Do not combine several unrelated concerns into one skill.
- Do not add resources unless they reduce repetition or improve reliability.
- Do not place specialized or vendor-specific content into the canonical base layer.

# Verification

- The skill has one clear responsibility.
- Trigger conditions and negative boundaries are explicit.
- The draft can be understood without hidden assumptions.
- The placement recommendation matches repository boundaries.

# Escalation

Escalate when:

- the skill overlaps heavily with an existing skill
- the workflow should be split into multiple smaller skills
- the content is too specialized for the canonical base layer
