# YAWN Architecture

YAWN is a persistence-first execution framework.

## Core Concepts

- **State**: Long-lived memory independent of any model
- **Storage**: Pluggable persistence backends
- **Continuity**: Resume or create state deterministically
- **Runner**: Executes logic against state
- **Roles**: Structured responsibilities, not agents

## Design Principles

- No hidden context
- No prompt replay
- Minimal token usage
- Deterministic state transitions

