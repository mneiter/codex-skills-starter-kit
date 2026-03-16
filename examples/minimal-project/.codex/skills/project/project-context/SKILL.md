---
name: project-context
description: Capture repository-specific goals, terminology, constraints, and working assumptions for one adopted project. Use when Codex needs local context that should remain outside the canonical technology-agnostic base layer.
---

# Purpose

Provide project-local context that helps Codex operate inside one specific repository without pushing that context into the canonical starter kit.

# When To Use

Use this skill when:

- local terminology needs explanation
- repository-specific constraints matter
- project goals or boundaries are not obvious from the file tree alone

# Inputs

- repository-specific goals
- local terminology
- important constraints and non-goals
- project expectations for handoff or validation

# Process

1. Capture the minimum local context Codex needs to work effectively.
2. Keep the context specific to the adopting repository.
3. Update the skill when local rules change.
4. Avoid duplicating generic guidance already covered by the base layer.

# Outputs

- a concise repository-specific context reference
- clarified local terminology and expectations
- a clean separation between local and canonical guidance

# Guardrails

- Do not move project-specific content into base skills.
- Do not duplicate starter-kit architecture rules here.
- Keep the local context focused and maintainable.

# Verification

- The local context helps explain this repository without restating the base kit.
- Repository-specific content stays outside the canonical base layer.
- The skill remains specific to one adopted project.

# Escalation

Escalate when:

- local context grows broad enough to need several smaller project-local skills
- a reusable generic pattern should move into the base kit instead
