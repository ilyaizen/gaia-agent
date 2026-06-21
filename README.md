<p align="center">
  <img src="assets/banner.png" alt="Gaia Agent" width="100%">
</p>

# Gaia Agent ☤

**The self-improving AI agent originally built by [Nous Research](https://nousresearch.com) as [Hermes Agent](https://hermes-agent.nousresearch.com/).** This is a local-first, terminal-first fork — stripped of Electron GUI, web UI, and Nous provider baggage. Gaia keeps what works: the CLI, gateway, skills, and the parts that make daily use better.

Use any model you want — [OpenRouter](https://openrouter.ai) (200+ models), [NovitaAI](https://novita.ai), [NVIDIA NIM](https://build.nvidia.com), [Xiaomi MiMo](https://platform.xiaomimimo.com), [z.ai/GLM](https://z.ai), [Kimi/Moonshot](https://platform.moonshot.ai), [MiniMax](https://www.minimax.io), [Hugging Face](https://huggingface.co), OpenAI, Anthropic, or your own endpoint. Switch with `gaia model` — no code changes, no lock-in.

<table>
<tr><td><b>A real terminal interface</b></td><td>Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.</td></tr>
<tr><td><b>Lives where you do</b></td><td>Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.</td></tr>
<tr><td><b>A closed learning loop</b></td><td>Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall.</td></tr>
<tr><td><b>Scheduled automations</b></td><td>Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.</td></tr>
<tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
<tr><td><b>Runs anywhere</b></td><td>Six terminal backends — local, Docker, SSH, Singularity, Modal, and Daytona. Run it on a $5 VPS or a GPU cluster.</td></tr>
<tr><td><b>Research-ready</b></td><td>Batch trajectory generation, trajectory compression for training the next generation of tool-calling models.</td></tr>
</table>

---

## Quick Start

```bash
# Install
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Start chatting
source ~/.bashrc
gaia

# Choose your model
gaia model

# Configure tools
gaia tools

# Start the gateway
gaia gateway setup
gaia gateway start
```

---

## Getting Started

```bash
gaia              # Interactive CLI — start a conversation
gaia model        # Choose your LLM provider and model
gaia tools        # Configure which tools are enabled
gaia config set   # Set individual config values
gaia gateway      # Start the messaging gateway
gaia setup        # Run the full setup wizard
gaia update       # Update to the latest version
gaia doctor       # Diagnose any issues
```

---

## What Gaia Skips

This fork intentionally removes:

- **Electron GUI / Desktop app** — terminal-first, no web layer
- **Docusaurus website** — docs are upstream, not bundled
- **Nous provider / auth** — not used locally; stubs provided for import compatibility
- **Non-English locales** — English only

See `plan.md` and `gaia-agent.md` in the vault for the full fork philosophy.

---

## Contributing

This is a personal fork. Contributions are welcome but the scope is intentionally narrow — local-first, terminal-first, no bloat.

```bash
git clone https://github.com/ilyaizen/gaia-agent.git
cd gaia-agent
uv pip install -e ".[all,dev]"
```

---

## License

MIT — see [LICENSE](LICENSE).

Originally built by [Nous Research](https://nousresearch.com). Forked and maintained by [ilyaizen](https://github.com/ilyaizen).
