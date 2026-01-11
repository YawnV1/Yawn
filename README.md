# YAWN

YAWN is a persistence-first execution framework designed to give Claude
long-lived memory, structured continuity, and deterministic workflows
across sessions.

YAWN separates **state**, **execution**, and **reasoning** so work can
continue without replaying context or wasting tokens.

---

## What YAWN Is

- A persistent state layer
- A deterministic execution engine
- A continuity manager for long-running work
- A clean integration point for Claude

## What YAWN Is Not

- Not a chatbot
- Not a prompt wrapper
- Not an agent swarm
- Not magic

---

## Core Concepts

- **State** — long-lived memory, independent of any model
- **Delta** — explicit changes applied to state
- **Storage** — pluggable persistence backends
- **Continuity** — resume or create state deterministically
- **Runner** — applies deltas and persists results
- **Roles** — structured responsibilities, not agents

---

## Usage

```bash
python cli/main.py run demo

