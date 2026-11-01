# Website development toolkit

This repository currently has no application scaffold. The setup prepares coding-agent skills and component-discovery integrations without prematurely choosing React, Next.js, Vite, or a package manager.

## 1. Install agent skills

From the repository root, run:

```bash
bash scripts/setup-agent-toolkit.sh
```

The script installs:

| Skill pack | Role |
|---|---|
| [Motion AI kit](https://motion.dev/docs/react) | Current Motion for React documentation, examples and agent tooling |
| [GSAP skills](https://github.com/greensock/gsap-skills) | GSAP timelines, ScrollTrigger, React integration, performance and animation implementation |
| [Taste](https://github.com/Leonxlnx/taste-skill) | Art direction, layout, typography, motion direction and browser-based visual QA |
| [21st.dev skills](https://github.com/21st-dev/skill) | Search, inspect, install and adapt 21st.dev components; explore and review UI |
| [Strix skills](https://github.com/usestrix/strix) | Authorized penetration testing, finding remediation and CI security scanning |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable design systems, styles, palettes, typography, UX patterns and stack-specific guidance |

The skills CLI installs into the coding agent's supported skill directory. UI/UX Pro Max targets the universal .agents/skills directory. Restart the coding agent after installation.

Taste's current skill expects Node.js 22+ and an installed Chromium-based browser for its visual inspection workflow.

## 2. MCP integrations

Project-level MCP configuration is in [.mcp.json](../.mcp.json).

| Server | Purpose | Authentication |
|---|---|---|
| shadcn | Search and install components from shadcn-compatible registries | None for public registries |
| 21st.dev | Discover, inspect and retrieve components from 21st.dev | API_KEY_21ST environment variable |
| Watermelon UI | Search its public React component, block, dashboard and template catalog | Public hosted MCP; no key |

Set API_KEY_21ST in the environment used to launch your MCP client. Copy .env.example as a local reference, but do not commit real credentials. The .mcp.json format is compatible with Claude Code-style project MCP configuration; other clients may require translating these entries into their own config format.

Official references:
- [shadcn MCP](https://ui.shadcn.com/docs/mcp)
- [21st.dev MCP](https://docs.21st.dev/mcp)
- [Watermelon UI MCP](https://ui.watermelon.sh/developers/status)

## 3. Component and visual source libraries

These are implementation sources, not all permanent runtime dependencies. Choose components selectively and adapt them to one project design system.

| Resource | Use |
|---|---|
| [React Bits](https://www.reactbits.dev/) | Animated React components, text effects, backgrounds and micro-interactions. Copy/install only the components actually needed. |
| [Watermelon UI](https://ui.watermelon.sh/) | Open-source React components, animated components, blocks, dashboards and templates. Its catalog is also available through the configured MCP server. |
| [Motion Primitives](https://motion-primitives.com/) | Reusable motion-focused React components and interaction patterns; its installer adds components to the app and uses the motion package. |
| [21st.dev](https://21st.dev/) | Searchable component marketplace and agent-assisted component retrieval. |
| [shadcn/ui](https://ui.shadcn.com/) | Base component primitives and registry installation workflow. |
| [Haikei](https://haikei.app/) | Generate and export custom SVG backgrounds and decorative assets. |
| [Alibaba Page Agent](https://github.com/alibaba/page-agent) | Browser-side natural-language agent for interacting with an existing webpage; use for browser automation, not as the core UI component framework. |

### Animation choice

- Framer Motion is now named Motion. For new React work, install the motion package and import from motion/react; use it for component transitions, layout animation and gesture-driven UI. The setup script runs npx motion-ai to add Motion agent tooling.
- Use GSAP for complex timelines, scroll choreography and tightly sequenced animation.
- Do not animate the same element with both engines. Respect prefers-reduced-motion.
- Use CSS transitions for simple hover/focus states; avoid adding an animation library for trivial effects.

## 4. React Bits Pro registry

The public React Bits library supports source copying/CLI installation. React Bits Pro additionally requires a paid license key and authenticated registries. Do not add a Pro key to GitHub. If a Pro license is available, follow the [official installation guide](https://pro.reactbits.dev/docs/installation) and store its key in a local ignored environment file.

## 5. Strix security scanning

A GitHub Actions workflow is included at [.github/workflows/strix-security.yml](../.github/workflows/strix-security.yml). It scans the checked-out repository in headless quick mode on pull requests and manual dispatch. It only runs when both secrets are configured:

- STRIX_LLM: LiteLLM-compatible model identifier, e.g. openai/<model-id>
- LLM_API_KEY: API key for that model provider

Add them under Repository → Settings → Secrets and variables → Actions. Never put them in workflow YAML or source files.

The workflow caps each scan at USD 10 and fails on high or critical findings. It performs a white-box scan of the repository checkout; it does not target a deployed site. A local directory can be mounted writable by Strix, so use a clean checkout for scans. Only run black-box tests against domains, APIs or IPs you own or have explicit permission to test.

Install Strix locally (Docker and a supported LLM key required) using:

```bash
curl -fsSL https://strix.ai/install | bash
export STRIX_LLM="openai/<model-id>"
export LLM_API_KEY="<provider-api-key>"
strix -n --target ./ --scan-mode quick --max-budget 10 --fail-on high
```

## 6. Current limitations / pending scaffold

This repository currently contains no package.json, React app, components.json, or deployment target. Therefore this setup deliberately does not install React, Next.js, Tailwind, Motion, GSAP, React Bits components, or Watermelon components yet. Those dependencies should be selected once the actual site architecture and framework are committed.

After the app scaffold exists:
1. Initialize shadcn/ui and configure its aliases in components.json.
2. Add Watermelon UI registry entries only when needed; its components install through the shadcn CLI.
3. Install React Bits components selectively; Pro registry setup is optional and license-gated.
4. Add motion and/or gsap only where the animation requirements justify them.
5. Export Haikei SVG assets into the repository and optimize them before production.
