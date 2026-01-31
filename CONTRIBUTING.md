# Contributing to Awesome AI Societies

Thanks for contributing! This repo aims to stay *society-focused* and *human-centered*.

## What we accept

### A) “Society” entries (preferred)
A candidate project should satisfy:

**Required**
- **Multi-agent**: more than one autonomous agent exists
- **Agent↔agent interaction**: agents communicate/coordinate/compete
- **Shared environment**: forum/world/workspace/game where interaction happens

**And at least ONE of these**
- **Persistence**: identities, memory, or long-running sessions
- **Governance**: moderation, rules, norms, evaluation protocols
- **Observability**: logs, replay, metrics, dashboards

### B) “Enabler” entries (limited)
We accept infrastructure **only if** it materially enables societies at scale
(e.g., agent platforms/ecosystems, identity/runtime, orchestration *with* multi-agent interaction hooks).

Not accepted as “enablers”:
- generic LLM wrappers
- generic RAG tooling
- one-off prompt collections

## What we do NOT accept (common cases)
- Single-agent chatbots
- Pure libraries without a society-like environment (unless they qualify as *enablers* above)
- Spam PRs or link-drops

## How to submit a PR
1. Add your entry under the appropriate category in `README.md` (or let the JSONL render do it).
2. Add a machine-readable record to `awesome-ai-societies.jsonl`.
3. Include a short rationale: **why this is a society (or a key enabler)** (1–3 sentences).
4. Add at least one reference link (repo, paper, blog, demo video, etc.).

## JSONL schema
Each line is a JSON object. Minimal example:

```json
{"name":"Example Society","url":"https://github.com/org/repo","category":"social-simulation","participants":"AI-only","environment":"town","persistence":["identity"],"governance":[],"observability":["logs"],"notes":"Why it matters","sources":["https://example.com"]}
```

## Code of conduct
Be respectful. No harassment, no spam, no brigading.
