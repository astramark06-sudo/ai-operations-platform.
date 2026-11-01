#!/usr/bin/env bash
set -euo pipefail

# Run from the repository root. These skills and tools are free to install.
# No paid API keys or subscriptions are required by this installer.
# The Skills CLI emits anonymous usage telemetry by default; disable it here.

if ! command -v node >/dev/null 2>&1 || ! command -v npm >/dev/null 2>&1 || ! command -v npx >/dev/null 2>&1; then
  echo "Node.js and npm are required. Install a supported Node.js 22.20+ release, then rerun." >&2
  exit 1
fi

NODE_VERSION="$(node -p 'process.versions.node')"
NODE_MAJOR="${NODE_VERSION%%.*}"
NODE_REMAINDER="${NODE_VERSION#*.}"
NODE_MINOR="${NODE_REMAINDER%%.*}"
if (( NODE_MAJOR < 22 || (NODE_MAJOR == 22 && NODE_MINOR < 20) )); then
  echo "Node.js 22.20 or newer is required by the current Skills CLI (found ${NODE_VERSION})." >&2
  exit 1
fi

export DISABLE_TELEMETRY=1

echo "Using Node.js ${NODE_VERSION}; agent-skill telemetry disabled."
echo "Installing Motion for React documentation and agent skills..."
npx --yes motion-ai

echo "Installing GSAP skills..."
npx --yes skills add https://github.com/greensock/gsap-skills

echo "Installing Taste frontend design skill..."
npx --yes skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

echo "Installing 21st.dev agent skills..."
npx --yes skills add https://github.com/21st-dev/skill

echo "Installing UI/UX Pro Max into the universal .agents/skills directory..."
npx --yes ui-ux-pro-max-cli init --ai universal

echo
echo "Agent skills installed. Restart your coding agent so it reloads them."
echo "Strix is installed separately and can use a local Ollama model; see docs/DEVELOPMENT-TOOLKIT.md."
echo "21st.dev offers a free tier; set API_KEY_21ST only if you choose to use its MCP."
