#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root. Installs skills into the detected coding agent.
# Frontend packages are intentionally not installed before the app scaffold exists.

echo "Installing GSAP skills..."
npx skills add https://github.com/greensock/gsap-skills

echo "Installing Taste frontend design skill..."
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

echo "Installing 21st.dev agent skills..."
npx skills add https://github.com/21st-dev/skill

echo "Installing Strix security testing skills..."
npx skills add https://github.com/usestrix/strix

echo "Installing UI/UX Pro Max into the universal .agents/skills directory..."
npx --yes ui-ux-pro-max-cli init --ai universal

echo
echo "Agent skills installed. Restart your coding agent so it reloads them."
echo "MCP servers are configured in .mcp.json; provide API_KEY_21ST in the agent process environment."
