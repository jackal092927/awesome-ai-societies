<p align="center">
  <img src="assets/banner.png" alt="Awesome AI Societies banner" width="100%">
</p>

<p align="center">
  <img src="assets/logo.png" alt="Awesome AI Societies logo" width="120">
</p>

# Awesome AI Societies 🤖🌐

> A human-centered index of places where AI agents **meet**, **learn norms**, **form communities**, and **co-create** with us.

We’re entering an era where “society” is no longer human-only.
Agents will inhabit forums, towns, games, and shared spaces—shaping norms, culture, and collective intelligence.
This repo curates **living examples** of AI societies to help builders and observers:
- **see what’s emerging**
- **borrow good patterns**
- **avoid repeating bad ones**
- **build something worth joining**

## What we mean by “AI society”
Usually has:
- **multiple autonomous agents**
- **agent↔agent interaction**
- a **shared environment** (forum/world/workspace)
- some form of **persistence** (identity, memory, long-running sessions)
- **observability** (logs/replay/metrics) and/or **governance** (rules/moderation/eval)

> Note: We keep *tooling* separate. This is primarily a list of **society-like environments**, plus a small section of **enablers** that materially power them.

---

## Categories

### 1) AI-only Public Communities (agents post/engage at scale)
- **[Moltbook](https://www.theverge.com/ai-artificial-intelligence/871006/social-network-facebook-for-ai-agents-moltbook-moltbot-openclaw)** — AI-only public community (forum-style)

### 2) Hybrid Human+AI Community Spaces (group chat / rooms)
- **[Character.AI](https://blog.character.ai/new-feature-announcement-character-group-chat/)** — Character Group Chat (multi-AI + humans)
- **[Inworld](https://inworld.ai/blog/multi-agent-feature-npc-to-npc)** — multi-agent character group conversations
- **[AI Dungeon](https://help.aidungeon.com/faq/do-you-support-multiplayer)** — multiplayer mode

### 3) Social Simulation Worlds (town/city/world sandboxes)
- **[Generative Agents](https://github.com/joonspk-research/generative_agents)** — classic generative agents simulation
- **[AI Town](https://github.com/a16z-infra/ai-town)** — town sandbox where agents live and chat
- **[AgentSociety](https://github.com/tsinghua-fib-lab/AgentSociety)** — city-scale social simulation
- **[Sotopia](https://github.com/sotopia-lab/sotopia)** — open-ended social learning environment
- **[AgentVerse](https://github.com/OpenBMB/AgentVerse)** — multi-agent simulation framework
- **[SocioVerse](https://github.com/FudanDISC/SocioVerse)** — world model for social simulation

### 4) Enablers (agent platforms that power societies)
These are not "societies" by themselves, but **core infrastructure** that enables many agents to exist, act, and interact.

- **[OpenClaw](https://github.com/openclaw/openclaw)** — agent platform / ecosystem

---

## Recommended entry schema (fields)
Each entry should ideally include:
- **Name / Link**
- **Category**
- **Participants**: `AI-only | Human+AI | Human-driven | Infra`
- **Environment**: `forum | chat room | town | city | workspace | game | infra`
- **Persistence**: identity / memory / long-running sessions
- **Governance**: moderation / rules / eval
- **Observability**: logs / replay / metrics
- **Activity**: stars, commits, releases (optional; can be auto-updated)

To keep this repo machine-friendly, also add items to `awesome-ai-societies.jsonl`.

---

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Tooling (optional)
- `scripts/update_github_stars.py`: fetch GitHub stars and update JSONL entries (requires a GitHub token).
- `scripts/render_readme.py`: render README sections from the JSONL file (optional workflow).
