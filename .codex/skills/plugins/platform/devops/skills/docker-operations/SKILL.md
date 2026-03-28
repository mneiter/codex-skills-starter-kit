---
name: docker-operations
description: Manage Docker workflow state across Dockerfiles, build context, images, containers, and compose services. Use when work needs Docker-aware triage or bounded Docker-side inspection, while keeping orchestration, verification, repair, refactoring, and PR writeups in separate skills.
---

# Purpose

Manage Docker workflow state without absorbing implementation, orchestration, or verification work. This skill inspects Dockerfiles, build context, images, containers, and compose services, summarizes likely Docker-side causes of build or runtime symptoms, and ends with a clear next Docker-native step or handoff.

# When To Use

Use this skill when:

- the user wants a Dockerfile, image, container, or compose-context state summary
- image size, layering, or build-context hygiene needs triage
- a container fails to start or exits unexpectedly and the likely Docker-side causes should be identified
- runtime logs, inspect output, or container metadata need interpretation
- compose setup should be reviewed only as it affects container or image behavior
- the next Docker-native diagnostic step needs to be identified before broader repair work

# When Not To Use

Do not use this skill when:

- the task needs multi-skill sequencing or workflow design; use `skill-router`
- the task needs validation execution or readiness evidence; use `ci-verification`
- the task needs a reviewer-facing pull request summary; use `generate-pull-request`
- the task needs code or content repair after findings; use `review-and-repair-loop`
- the task is a behavior-preserving structural cleanup; use `refactor-feature`
- the task asks for Kubernetes orchestration, infrastructure provisioning, CI or CD authoring, application-code fixes, or production-readiness claims

# Inputs

- the repository, checkout, or filesystem context in scope
- the relevant Dockerfile, compose file, `.dockerignore`, or container configuration when available
- the image, container, or service target in scope
- the symptom summary, log output, inspect output, or runtime error already observed
- Dependencies: Docker access when available, plus `skill-router`, `ci-verification`, `generate-pull-request`, `review-and-repair-loop`, and `refactor-feature`

# Capabilities

- inspect Dockerfile and build-context quality at a triage level
- reason about image layering, cache behavior, and likely size drivers
- inspect container runtime state and Docker-reported metadata
- summarize likely Docker-side causes of startup or runtime symptoms
- explain compose context only as it affects container or image behavior
- recommend the next Docker-native diagnostic step

# Process

1. Resolve the Docker target and the symptom or question in scope.
2. Classify the request as build-context, image-hygiene, runtime-state, compose-context, or startup-failure triage.
3. Gather only the Docker-side evidence needed to answer the request.
4. Summarize likely Docker-side causes conservatively and keep the reasoning inside Docker boundaries.
5. Recommend the next Docker-native diagnostic step or hand off when the next owner is outside Docker triage.

# Outputs

- a concise Docker-state summary
- the likely Docker-side cause cluster relevant to the request
- the next Docker-native diagnostic step
- an explicit handoff when the next owner is outside Docker triage

# Boundaries

- `skill-router` chooses when several skills are needed; `docker-operations` handles only the Docker workflow slice once the task is in scope.
- `ci-verification` owns running checks and producing readiness evidence; `docker-operations` only summarizes Docker-side state and likely causes.
- `generate-pull-request` owns reviewer-facing pull request narrative; `docker-operations` may prepare context but does not write the summary.
- `review-and-repair-loop` owns repair passes and re-verification; `docker-operations` may surface Docker-side findings but does not fix them.
- `refactor-feature` owns behavior-preserving structural cleanup; `docker-operations` may identify that need but does not perform it.

# Handoffs

- hand off to `skill-router` when the task mixes Docker state work with other execution concerns
- hand off to `ci-verification` when validation evidence or readiness claims are required
- hand off to `review-and-repair-loop` when the diagnosis becomes repair work
- hand off to `refactor-feature` when the next step is code restructuring rather than Docker triage
- hand off to `generate-pull-request` when the change is done and reviewer-facing narrative is next

# Example Workflows

1. Image bloat triage: inspect the Dockerfile, build context, and image history to explain likely size drivers.
2. Startup failure triage: inspect container state, logs, and runtime metadata to identify likely Docker-side causes for an immediate exit.
3. Compose-context review: summarize how service definitions, mounts, or environment wiring may be affecting container behavior.
4. Next-step guidance: summarize the current Docker-side evidence and identify the next inspection step without claiming a fix.

# Guardrails

- Do not perform state-changing Docker actions in v1.
- Specifically do not run `docker build`, `docker run`, `docker restart`, `docker stop`, `docker rm`, `docker compose up`, `docker compose down`, `docker push`, or `docker pull`.
- Do not drift into Kubernetes, infrastructure orchestration, networking architecture design, or CI and CD workflow authoring.
- Do not claim that an image, container setup, or compose stack is production-ready without separate verification evidence.
- Ask or hand off instead of guessing when the target, symptom, or next owner is unclear.

# Verification

- The result stays inside Docker, container, image, and build-context operations.
- Any likely cause or next step is tied to observed Docker-side evidence rather than assumption.
- No readiness, fix, or production claims are made without separate validation evidence.
- Work that required orchestration, repair, refactoring, validation, or PR narrative was handed off instead of absorbed here.

# Escalation

Escalate when:

- the Docker target or relevant access cannot be resolved
- the task mixes Docker triage with broader execution concerns and routing materially affects the outcome
- the symptoms clearly point to application, infrastructure, or CI and CD work outside Docker triage
