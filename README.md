# Website Creation

Repository for building the website and its supporting development workflow.

## Getting started

The application scaffold has not been selected yet. First prepare the coding-agent toolkit:

```bash
bash scripts/setup-agent-toolkit.sh
```

Project MCP servers are configured in .mcp.json. Set API_KEY_21ST in the environment used by your MCP client to enable authenticated 21st.dev component retrieval.

See docs/DEVELOPMENT-TOOLKIT.md for the skills, component sources, MCP setup, animation strategy and Strix security workflow.

## Agent instructions

Coding agents should read AGENTS.md before making changes.

## Current state

- Agent skill installation script: available
- shadcn, 21st.dev and Watermelon UI MCP configuration: committed
- Strix GitHub Actions workflow: committed; requires repository Actions secrets
- Frontend framework and app scaffold: not yet selected
