# AGENTS.md

## Memory Policy

This project uses `opencode-plugin-simple-memory` for persistent local memory.

Memory should be used only for stable information that is likely to remain useful across future sessions.

### Good memory candidates

The assistant may propose storing memory for:

- Confirmed design decisions.
- Project-wide coding conventions.
- User workflow preferences.
- Repeated pitfalls or debugging conclusions.
- Module-specific definitions explicitly approved by the user.
- Constraints that should be respected in future tasks.

### Do not store

The assistant must not store:

- API keys, tokens, credentials, or private personal data.
- Temporary command output.
- Large code snippets.
- Unconfirmed guesses.
- One-off implementation details likely to become stale.
- Information that is only relevant to the current session.

### Before writing memory

Before calling any memory write/update tool, the assistant must first propose the memory item and wait for user confirmation, unless the user explicitly says "remember this", "store this", or gives an equivalent direct instruction.

Each proposed memory item should include:

- `content`: the concise memory text.
- `type`: one of `decision`, `learning`, `preference`, `blocker`, `context`, or `pattern`.
- `scope`: for example `user`, `project`, or `module:<name>`.
- `reason`: why this information is likely to remain useful.

The assistant should not write memory immediately after identifying a possible candidate. It should ask the user which candidate items should be stored.

### At the beginning of a new session

For a new session, the assistant should recall relevant memories before planning:

- Recall `project` memories for general project work.
- Recall `module:<name>` memories when the task is module-specific.
- Recall `user` memories for workflow preferences.

After recalling memory, the assistant should still rely on the current files, current task description, current git diff, and current test results as the source of truth.

### At the end of a substantial session

At the end of a substantial session, the assistant should summarize candidate long-term memories.

It should output a section like:

```text
## Candidate memories

1. content: ...
   type: decision
   scope: project
   reason: ...

2. content: ...
   type: pattern
   scope: module:<name>
   reason: ...
```

## Workflow

- Activate the virtual environment with: `& ./activate_venv.ps1`. This local script is intentionally ignored by git and should contain machine-specific activation logic.
- Only use common Python commands, such as `python -m` and `pytest`, after activating the virtual environment.
- Use `pytest` for testing. Test files should mirror the source tree structure as closely as practical.
- When modifying the code, be careful not to accidentally delete any TODOs that are unrelated to this task.

## Documentation

- `**_design.md` files are high-level design documents for specific modules and should not include concrete implementation details.
- `**_impl.md` files describe practical implementation constraints and design rules.

## Python Code Style

- Use short, purpose-revealing names for classes, functions, parameters, and variables. Appropriate abbreviations are acceptable, but names should remain compatible with the existing code style.
- Use Google-style docstrings. Keep them concise while clearly stating the contract and purpose. Docstrings for private components may be as short as one sentence.
- Prefer modern, idiomatic Python with clear type hints, `pathlib` for path handling, small typed data structures where useful, and concise standard-library-first solutions; avoid outdated or unnecessarily verbose legacy patterns.
