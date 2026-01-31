# Awesome AI Societies 🤖🌐
> A curated list of projects that enable **multi-agent social interaction**: AI-only communities, hybrid human+AI spaces, social simulation worlds, and organizational societies.

---

## What counts as an "AI society"?
Usually has:
- **multiple autonomous agents** (not just a single chatbot)
- **agent↔agent interaction**
- a **shared environment** (forum/world/workspace)
- some form of **persistence** (identity, memory, long-running sessions)
- **observability** (logs/replay/metrics) and/or **governance** (rules/moderation/eval)

> Maintainer note: This repo intentionally prioritizes *society-like environments* over generic tooling.

---

## Categories (no ranking)

### 1) AI-only Public Communities (agents post/engage at scale)
- **Moltbook** — AI-only public community (forum-style); included for its *community form* (not “rank”).
  - Reference: https://www.theverge.com/ai-artificial-intelligence/871006/social-network-facebook-for-ai-agents-moltbook-moltbot-openclaw

### 2) Hybrid Human+AI Community Spaces (group chat / rooms)
- **Character.AI** — Character Group Chat (multi-AI + humans): https://blog.character.ai/new-feature-announcement-character-group-chat/
- **Inworld** — multi-agent character group conversations: https://inworld.ai/blog/multi-agent-feature-npc-to-npc
- **AI Dungeon** — multiplayer mode: https://help.aidungeon.com/faq/do-you-support-multiplayer

### 3) Social Simulation Worlds (town/city/world sandboxes)
- **Generative Agents** — https://github.com/joonspk-research/generative_agents
- **AI Town** — https://github.com/a16z-infra/ai-town
- **AgentSociety** — https://github.com/tsinghua-fib-lab/AgentSociety
- **Sotopia** — https://github.com/sotopia-lab/sotopia
- **AgentVerse** — https://github.com/OpenBMB/AgentVerse
- **SocioVerse** — https://github.com/FudanDISC/SocioVerse

### 4) Organizational Societies (virtual teams / “AI companies”)
- **MetaGPT** — https://github.com/FoundationAgents/MetaGPT
- **AutoGen** — https://github.com/microsoft/autogen
- **CrewAI** — https://github.com/crewAIInc/crewAI
- **ChatDev** — https://github.com/OpenBMB/ChatDev
- **CAMEL** — https://github.com/camel-ai/camel

---

## Recommended entry schema (fields)
Each entry should ideally include:
- **Name / Link**
- **Category**
- **Participants**: `AI-only | Human+AI | Human-driven`
- **Environment**: `forum | chat room | town | city | workspace | game`
- **Persistence**: identity / memory / long-running sessions
- **Governance**: moderation / rules / eval
- **Observability**: logs / replay / metrics
- **Activity**: stars, commits, releases (optional; can be auto-updated)

To keep this repo machine-friendly, also add items to `awesome-ai-societies.jsonl`.

---

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Tooling
- `scripts/update_github_stars.py`: optional helper to fetch GitHub stars and update the JSONL entries (requires a GitHub token).
- `scripts/render_readme.py`: render README sections from the JSONL file (optional workflow).
