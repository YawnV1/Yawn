# YAWN
---
<p align="center">
  <img src="assets/yawnbanna.png" alt="YAWN banner" width="60%" />
</p>

---
YAWN is a persistence-first execution framework for long-running,
model-assisted work.

It is designed to give systems built on Claude (or other LLMs)
**continuity, explicit memory, and deterministic execution**
across sessions — without relying on conversation replay.

YAWN is not a chatbot.
YAWN is not a prompt wrapper.
YAWN is an execution substrate.

---

## Why YAWN Exists

Most LLM tooling treats models as stateless processes.
When a session ends, memory is lost and must be reconstructed by
replaying prompts, summaries, or conversation history.

This approach has problems:
- token waste
- loss of precision
- drift over time
- fragile prompt engineering

YAWN takes the opposite approach.

Memory is external.
State is explicit.
Execution is resumable.

---

## Core Idea

Instead of asking a model to *remember*, YAWN asks it to
**produce explicit state changes**.

Those changes are:
- applied deterministically
- persisted outside the model
- reusable across runs

The model does not hold memory.
The system does.

---

## High-Level Architecture

```text
CLI
 |
 v
Continuity Manager
 |
 v
State  <-->  Storage
 |
 v
Runner
 |
 v
Deltas
```
---

## Concepts (Concrete)

### State

State is a structured, serializable object that represents
everything the system needs to continue work.

Examples:
- progress counters
- flags
- intermediate artifacts
- execution metadata
- hashes or checkpoints

State lives on disk (or another backend), not in the model.

---

### Delta

A delta is a **minimal, explicit mutation** to state.

Instead of rewriting memory wholesale, YAWN applies deltas
incrementally. This makes execution:
- predictable
- auditable
- resumable

---

### Continuity

Continuity determines whether execution:
- resumes existing state
- or initializes new state

Given the same state ID, YAWN will reliably continue where it left off.

---

### Runner

The runner is responsible for:
1. loading state
2. applying deltas
3. persisting results

It contains no business logic and no model-specific behavior.

---

### Roles

Roles define structured responsibilities such as:
- planner
- executor
- reviewer

They are not autonomous agents.
They are deterministic execution units operating on state.

---

## Repository Structure

cli/ → command-line entrypoint
config/ → role and execution configuration
core/ → state, deltas, continuity logic
executor/ → role registry and execution runners
storage/ → persistence backends
docs/ → roadmap and design notes

---


Each layer is intentionally small and replaceable.

---

## Execution Flow (Step by Step)

1. User runs YAWN with a state ID
2. Continuity manager loads or creates state
3. Runner invokes configured roles
4. Roles emit deltas
5. Deltas are applied to state
6. Updated state is persisted
7. Execution ends — state remains

Re-running with the same ID resumes at step 2.

---

## Example

```bash
python cli/main.py run demo

