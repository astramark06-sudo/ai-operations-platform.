#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root in a compatible coding-agent environment.
# These are free/open-source agent skills; this does not install the website app.

echo "Installing Motion for React documentation and agent skills..."
npx motion-ai

echo "Installing GSAP skills..."
npx skills add https://github.com/greensock/gsap-skills

echo "Installing Taste frontend design skill..."
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

echo "Installing Vercel React performance and web design skills..."
npx skills add vercel-labs/agent-skills --skill react-best-practices --skill web-design-guidelines

echo "Installing 21st.dev agent skills..."
npx skills add https://github.com/21st-dev/skill

echo "Installing UI/UX Pro Max into the universal .agents/skills directory..."
npx --yes ui-ux-pro-max-cli init --ai universal

echo
echo "Agent skills installed. Restart the coding agent so it reloads them."
echo "The design-to-code skill is already included at .agents/skills/design-to-code/."
echo "This script does not install or build the website application."
echo "Strix is a separate local-only option; see docs/DEVELOPMENT-TOOLKIT.md."
echo "21st.dev has free-tier limits. Set API_KEY_21ST only if you choose to use its MCP."
echo "Context7 supports anonymous use at lower rate limits; authenticate only with a free allowance."
