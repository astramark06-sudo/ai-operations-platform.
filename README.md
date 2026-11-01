# Website Creation

Repository for building the website and its supporting development workflow.

## Cost policy

This project uses free and open-source tools only. No paid subscriptions, paid API inference, or paid component licenses are required. Optional free tiers may have usage limits.

## Getting started

Run the agent toolkit installer from the repository root:

```bash
bash scripts/setup-agent-toolkit.sh
```

Project MCP servers are configured in `.mcp.json`. 21st.dev is optional and has a limited free allowance; set `API_KEY_21ST` only if you choose to use it.

See [docs/DEVELOPMENT-TOOLKIT.md](docs/DEVELOPMENT-TOOLKIT.md) for setup, free-tier limits, local Strix security testing and component sources.

Coding agents should read [AGENTS.md](AGENTS.md) before making changes.

## Current state

- Free agent skill installation script: available
- shadcn and Watermelon UI MCP: configured
- 21st.dev MCP: optional, free tier only
- Strix: local Ollama model workflow; no paid API key
- Frontend framework and app scaffold: not yet selected
