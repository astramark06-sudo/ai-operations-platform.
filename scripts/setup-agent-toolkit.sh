#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root in a compatible coding-agent environment.
# This installer adds free/open-source agent skills; it does not install the app.

echo "Installing Motion for React documentation and agent skills..."
npx motion-ai

echo "Installing GSAP skills..."
npx skills add https://github.com/greensock/gsap-skills

echo "Installing Taste frontend design skill..."
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

echo "Installing Vercel React best-practices skill..."
npx skills add vercel-labs/agent-skills --skill react-best-practices

echo "Installing Vercel web design guidelines skill..."
npx skills add vercel-labs/agent-skills --skill web-design-guidelines

echo "Installing 21st.dev agent skills..."
npx skills add https://github.com/21st-dev/skill

echo "Installing UI/UX Pro Max into the universal .agents/skills directory..."
npx --yes ui-ux-pro-max-cli init --ai universal

echo
echo "Agent skills installed. Restart the coding agent so it reloads them."
echo "This script does not install or build the website application."
echo "Strix is a separate local-only option; see docs/DEVELOPMENT-TOOLKIT.md."
echo "21st.dev has free-tier limits; configure API_KEY_21ST only if you choose to use its MCP."
