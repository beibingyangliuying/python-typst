---
name: typst-doc-verify
description: Use when checking Python implementation functions against official Typst documentation or reference behavior, especially to add, update, or validate Better Notes-style verification/TODO comments. Do not use for general Typst coding help.
---

# Typst Doc Verify

Use this skill when the user asks to verify whether one or more Python function implementations match official Typst behavior, syntax, APIs, reference semantics, or documented constraints.

This skill is for documentation-based verification and Better Notes-style comment maintenance. It is not a general Typst programming assistant. Do not use it merely to write Typst code, explain Typst syntax, design new Typst features, or debug a Typst document unless the task specifically involves checking a Python implementation against official Typst documentation.

## Goal

Check the current implementation against official Typst documentation, decide whether each target implementation is correct, and maintain concise dated comments that work well with Better Notes.

This skill supports both single-function and multi-function verification.

## Scope and Inputs

This skill is intended for Python functions that implement, wrap, emulate, translate, validate, render, or generate Typst behavior.

The primary signal that a function implements Typst behavior is the `@implement` decorator (from `typstpy._core.decorators`). Functions decorated with `@implement` carry parameters for `original_name`, `hyperlink`, and `version` that must be verified and kept up to date alongside the implementation.

Before verification, identify:

1. The target file path.
2. The target function name or target function set.
3. The intended Typst concept, function, type, syntax, API, or behavior.
4. If the target uses `@implement`, inspect its `original_name`, `hyperlink`, and `version` parameters.

If the target is not explicitly named, infer it from the user's request and nearby code. Functions decorated with `@implement` should be preferred as verification candidates. Ask for clarification only when the target cannot be identified safely.

Place verification comments immediately above the target function definition (above the `@implement` decorator when present). If the target is not a function, place the comment immediately above the smallest relevant implementation block.

If a recognized verification or TODO comment already exists for the same target, update that comment in place rather than adding a duplicate.

Every function that is checked must receive a verification comment. Do not leave a checked function without a structured comment. Verified functions get a `# *` comment; mismatched or inconclusive functions get a `# TODO` comment of the appropriate type.

## Official Sources

Use official sources as the basis for verification:

1. Typst documentation: https://typst.app/docs/
2. Typst reference: https://typst.app/docs/reference/
3. Typst official GitHub repository, only when the documentation is insufficient.

Do not treat third-party blog posts, forum answers, examples from unrelated projects, or model memory as authoritative.

Unofficial sources may be used only as search aids. They must not be the final basis for a verified conclusion.

## Workflow

1. Identify the target function or target function set.
2. For each function, determine the intended Typst concept, function, type, syntax, API, or behavior.
3. Inspect any existing Typst verification comment near each function.
4. Inspect any `@implement` decorator parameters (`original_name`, `hyperlink`, `version`) on the target function.
5. Search and read the relevant official Typst documentation before judging an implementation, unless an existing `# *` comment can be safely reused under the existing-comment rules.
6. Note the current Typst version as shown on the official documentation page (e.g., the version selector dropdown near the top of the page, or the page metadata).
7. Compare each implementation against the documented behavior independently.
8. Check the relevant verification dimensions:
   - accepted argument names and aliases;
   - required vs optional arguments;
   - default values;
   - valid values, value ranges, or enum-like constraints;
   - type expectations or accepted input forms;
   - return value, rendered output, or generated Typst syntax;
   - documented error cases, unsupported cases, or edge cases;
   - version-sensitive behavior;
   - deprecation or compatibility status (e.g., deprecated since Typst 0.x, existing as a soft/hard compatibility alias);
   - examples in official docs, if available.
   - whether the `@implement` `version` parameter matches the current Typst version shown in the official docs;
   - whether the `@implement` `hyperlink` parameter matches the official documentation URL used for verification.
9. If a function matches the documentation:
   - Add or update a `# *` verification comment near that function.
   - If the `@implement` `version` parameter is stale (older than the current Typst version from the docs), update it to the current version.
   - If the `@implement` `hyperlink` parameter does not match the official documentation URL used, update it.
10. If a function does not match the documentation, add or update a `# TODO` mismatch comment near that function and report the discrepancy.
11. If the official documentation does not provide enough evidence for a function, add or update a `# TODO` inconclusive comment instead of marking it verified.
12. When multiple functions are checked, provide a concise per-function summary.

## @implement Decorator Handling

The `@implement` decorator (defined in `typstpy._core.decorators`) is the primary mechanism for registering Python functions as Typst API wrappers. Each decorated function carries three metadata parameters relevant to verification:

- `original_name`: the Typst function name this Python function implements (e.g., `'bibliography'`, `'list.item'`).
- `hyperlink`: the URL of the official Typst documentation page for this function.
- `version`: the latest Typst stable version this implementation targets (e.g., `'0.13.x'`, `'0.14.x'`).

These parameters are part of the implementation contract and must be verified alongside the function signature and behavior.

### Determining the current Typst version

When visiting an official Typst documentation page, look for a version selector (typically a dropdown near the top of the page, e.g., "v0.14.0" or "stable (0.14)"). The version shown in the selector is the version that the documentation page describes. Use this as the canonical version for verification.

If the version selector is not visible or the page does not display a version, check the page metadata or the Typst GitHub repository for the latest stable release tag instead.

### Updating `@implement` parameters

When a function is verified:

- If `@implement.version` does not match the current Typst version from the official docs, update it. Round to a minor-version wildcard format (e.g., `'0.14.x'` for a `0.14.0` or `0.14.3` release).
- If `@implement.hyperlink` does not match the official documentation URL used for verification, update it to the correct URL.
- If `@implement.original_name` does not match the documented Typst function name, report it as a mismatch.

When updating a `# *` verification comment, the `@implement` parameters should be checked and updated at the same time. Stale decorator parameters alongside a fresh verification comment are a sign of incomplete verification.

If a function does not carry an `@implement` decorator but is otherwise a valid verification target, skip the decorator parameter checks and proceed with the implementation-only verification. The coverage requirement (every checked function receives a comment) still applies.

## Multi-Function Rules

- Treat each function as a separate verification target.
- Do not mark a group of functions as verified unless each function has been individually checked.
- A shared official documentation URL may be reused across functions, but each function still needs its own conclusion.
- Partial success is acceptable: verified functions may receive `# *` comments while mismatched or uncertain functions receive `# TODO` comments.
- If changing implementation code is needed, report the issue first unless the user explicitly asked for implementation fixes.
- Do not silently fix implementation code during verification. First report the mismatch and add or update the TODO comment. Modify implementation code only when the user explicitly asks for fixes.

## Verification Comments

Use the current system date in `YYYY-MM-DD` format.

This skill is intended for Python code. Use Python line comments for all verification comments.

Successful verification:

```python
# * Typst docs v<version> verified on YYYY-MM-DD: <official-doc-url>; behavior matches implementation.
```

If the function is deprecated in the official Typst documentation, note its deprecation status in the comment:

```python
# * Typst docs v<version> verified on YYYY-MM-DD: <official-doc-url>; behavior matches implementation. Deprecated since Typst <version>.
```

Mismatch or required fix:

```python
# TODO Typst docs mismatch on YYYY-MM-DD: <official-doc-url>; expected <documented behavior>, implementation <actual behavior>.
```

Inconclusive official documentation:

```python
# TODO Typst docs inconclusive on YYYY-MM-DD: <official-doc-url>; official docs do not fully confirm behavior.
```

Use `verified` only when an official Typst source supports the conclusion.

If the implementation is plausible but the official source does not explicitly support the key behavior being checked, mark it inconclusive rather than verified.

When the official documentation marks a function as deprecated, a compatibility alias, or a legacy API:
- Still verify the implementation against the documented behavior of the deprecated version.
- Add a `# *` comment if it matches, noting the deprecation status.
- If the documentation explicitly warns that the function may be removed or has changed behavior in a newer version, note this in the comment and consider whether the `@implement.version` needs adjustment.

Keep comments short and factual. Avoid long explanations inside code comments; put detailed reasoning in the response summary instead.

## Existing Comment Handling

Recognize only structured comments that start with one of the following as this skill's own comments (the version token `v<version>` in verified comments is optional for matching purposes):

```python
# * Typst docs v<version> verified on
# * Typst docs verified on
# TODO Typst docs mismatch on
# TODO Typst docs inconclusive on
```

When a function already has a recognized `# * Typst docs ... verified on ...` comment:

1. Extract the verification date and official documentation URL.
2. Inspect the `@implement` decorator parameters on the target function, if present.
   - If `@implement.version` differs from the current Typst version shown in the official docs, mark it for update.
   - If `@implement.hyperlink` differs from the official documentation URL used, mark it for update.
3. Try to determine whether the official source changed after the verification date.
4. Prefer reliable official update signals in this order:
   - an explicit last-updated date on the official Typst documentation page;
   - the latest relevant commit date for the corresponding source file in the official Typst GitHub repository;
   - a trustworthy HTTP `Last-Modified` header from the official source.
5. If a reliable official source update date exists and it is not newer than the verification date, skip deep re-verification and leave the comment unchanged. Still apply any pending `@implement` parameter updates (version or hyperlink) that were identified in step 2.
6. If the source is newer, unavailable, or unreliable, re-check the implementation against the current official documentation.
7. If source-change detection would require excessive investigation, perform a direct re-check against the current official documentation instead of spending time proving whether the source changed.
8. If the implementation still matches:
   - Update the `# *` comment date to the current system date and ensure the version token reflects the current Typst version.
   - Update the `@implement` `version` parameter if stale.
   - Update the `@implement` `hyperlink` parameter if it differs from the official documentation URL used.
9. If the implementation does not match, replace or add a `# TODO` mismatch comment.
10. If the implementation cannot be confirmed from the official documentation, replace or add a `# TODO` inconclusive comment.

Do not skip re-verification solely because a `# *` comment exists.

When a function already has a recognized `# TODO` comment:

- Re-check it against the official documentation.
- If it now matches, replace the `# TODO` comment with a `# *` verification comment. Also check and update `@implement` parameters.
- If it still does not match, keep or update the `# TODO` mismatch comment.
- If the official documentation is still inconclusive, keep or update a `# TODO` inconclusive comment.

When a function has an unrecognized old verification-like comment:

- Do not delete it unless the user explicitly asks.
- Add a new structured comment if verification, mismatch, or inconclusive status is established.
- Avoid creating duplicate structured comments for the same target.

## Decision Table

| Prior state | Documentation/source state | Implementation state | @implement state | Action |
| --- | --- | --- | --- | --- |
| No recognized comment | Checked | Matches | Any | Add `# *` verified comment; update `@implement` version and hyperlink if needed. |
| No recognized comment | Checked | Mismatch | Any | Add `# TODO` mismatch comment. |
| No recognized comment | Inconclusive | Unknown | Any | Add `# TODO` inconclusive comment. |
| Existing `# *` | Official source reliably unchanged | Not rechecked | Version/hyperlink current | Leave comment unchanged; summarize as skipped. |
| Existing `# *` | Official source reliably unchanged | Not rechecked | Version or hyperlink stale | Update `@implement` version/hyperlink; leave comment unchanged. |
| Existing `# *` | Source newer, unavailable, unreliable, or costly to check | Matches after re-check | Any | Update `# *` date and version token; update `@implement` version/hyperlink. |
| Existing `# *` | Source newer, unavailable, unreliable, or costly to check | Mismatch after re-check | Any | Replace or add `# TODO` mismatch comment. |
| Existing `# *` | Source newer, unavailable, unreliable, or costly to check | Inconclusive after re-check | Any | Replace or add `# TODO` inconclusive comment. |
| Existing `# TODO` | Checked | Matches | Any | Replace with `# *` verified comment; update `@implement` version/hyperlink if needed. |
| Existing `# TODO` | Checked | Still mismatches | Any | Keep or update `# TODO` mismatch comment. |
| Existing `# TODO` | Inconclusive | Unknown | Any | Keep or update `# TODO` inconclusive comment. |
| Unrecognized old verification-like comment | Checked | Any | Any | Preserve old comment and add or update a structured comment. |

## Constraints

- Do not claim verification without an official Typst documentation source.
- Do not use unofficial sources as the final authority.
- Do not rewrite functions unless the user explicitly asks for implementation fixes.
- Do not remove unrelated comments or TODOs.
- Do not delete unrecognized old verification-like comments unless the user explicitly asks.
- Keep verification comments short and factual.
- Include the official documentation URL in the comment whenever practical.
- Include the current Typst version from the official docs in the `# *` comment.
- For multi-function checks, keep conclusions independent per function.
- Treat `# *` comments as "verified as of this date against this source", not as permanent truth.
- Prefer direct, local edits around the target function. Do not reformat unrelated code.
- If official documentation and implementation terminology differ, explain the mapping in the response summary.
- Every checked function must receive a structured verification comment: `# *` when verified, `# TODO mismatch` or `# TODO inconclusive` when not.
- When a `# *` comment is added or updated, also check and update the `@implement` `version` and `hyperlink` parameters if present and stale. Do not leave stale decorator metadata alongside a fresh verification comment.

## Output Requirements

When modifying files, report:

1. Which functions were checked.
2. Which official source was used for each function.
3. Whether each function was verified, mismatched, inconclusive, or skipped.
4. Which comment action was taken:
   - added;
   - updated;
   - replaced;
   - left unchanged;
   - skipped.
5. Which `@implement` decorator changes were applied, if any:
   - `version` updated (`old` → `new`);
   - `hyperlink` updated (`old` → `new`);
   - no changes needed.
6. Any mismatch or uncertainty that still requires user attention.

For multi-function checks, end with a concise summary such as:

```text
Verification summary:
- render_text: verified; comment updated; @implement version 0.13.x → 0.14.x; source: <url>.
- render_heading: source unchanged since prior verification; skipped; @implement hyperlink updated; source: <url>.
- render_list: mismatch; TODO updated; expected <documented behavior>, implementation <actual behavior>.
- render_table: inconclusive; TODO added; missing evidence: <reason>.
```

## Typical Use Cases

Use this skill for requests such as:

- "Check whether these Typst wrapper functions match the official docs."
- "Verify this renderer function against Typst documentation and add Better Notes comments."
- "Review the existing Typst docs verified comments and update stale ones."
- "For these functions, mark which ones are verified and which ones need TODOs."

Do not use this skill for requests such as:

- "Teach me Typst."
- "Write a Typst document."
- "Convert this Markdown to Typst."
- "Design a new Typst rendering architecture."
- "Debug a Typst compile error" unless the task specifically asks to verify a Python implementation against official Typst documentation.