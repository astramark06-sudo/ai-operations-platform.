#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root. These skills and tools are free to install.
# No paid API keys or subscriptions are required by this installer.

echo "Installing Motion for React documentation and agent skills..."
npx motion-ai

echo "Installing GSAP skills..."
npx skills add https://github.com/greensock/gsap-skills

echo "Installing Taste frontend design skill..."
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

echo "Installing 21st.dev agent skills..."
npx skills add https://github.com/21st-dev/skill

echo "Installing UI/UX Pro Max into the universal .agents/skills directory..."
npx --yes ui-ux-pro-max-cli init --ai universal

echo
echo "Agent skills installed. Restart your coding agent so it reloads them."
echo "Strix is installed separately and can use a local Ollama model; see docs/DEVELOPMENT-TOOLKIT.md."
echo "21st.dev offers a free tier; set API_KEY_21ST only if you choose to use its MCP."
