# Website development toolkit

This project has a strict zero-spend requirement. The toolkit below uses free/open-source software and optional free tiers. It does not require a paid subscription, paid model API, or paid component license.

The repository currently has no application scaffold, so frontend dependencies will be selected after the framework is chosen.

## 1. Install agent skills

Run from the repository root:

```bash
bash scripts/setup-agent-toolkit.sh
```

The installer sets up:

| Tool / skill | Purpose | Cost |
|---|---|---|
| [Motion AI kit](https://motion.dev/docs/react) | Motion for React documentation and agent tooling | Free/open source |
| [GSAP skills](https://github.com/greensock/gsap-skills) | Timelines, ScrollTrigger, React integration and performance | Free; GSAP's full toolset is free |
| [Taste](https://github.com/Leonxlnx/taste-skill) | Art direction, layout, typography and browser-based visual QA | Free; no API key |
| [21st.dev skills](https://github.com/21st-dev/skill) | Discover and adapt component patterns | Free skill; service has free-tier limits |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design systems, styles, palettes, typography and UX patterns | Open-source basic version |

Taste requires Node.js 22+ and Chrome, Edge or Chromium for its browser inspection script. It does not need API keys.

## 2. MCP integrations

Project configuration is in [.mcp.json](../.mcp.json).

| Server | Purpose | Cost / limit |
|---|---|---|
| shadcn | Search and install components from public shadcn-compatible registries | Free/open source |
| Watermelon UI | Search its component, block, dashboard and template catalog | Public MCP endpoint; no key configured |
| 21st.dev | Component search and retrieval | Free account supports 2 component-code retrievals per day; paid plan is not needed if we stay within that allowance |

21st.dev's free tier requires a free account/API token for most MCP clients. Set `API_KEY_21ST` in the environment used to launch the MCP client. Do not purchase Builder or AI credits. Its search/browsing is free and the free account currently includes 2 code retrievals daily. See [21st.dev MCP docs](https://docs.21st.dev/mcp) and [pricing/limits](https://mcp.21st.dev/pricing).

The project MCP format may need translation for clients that do not support Claude Code-style `.mcp.json`.

## 3. Component and visual libraries

Use these as source libraries, not as a reason to install every package.

| Resource | Use | Cost guidance |
|---|---|---|
| [React Bits](https://www.reactbits.dev/) | Animated React components, text effects, backgrounds and micro-interactions | Use the public open-source components; avoid Pro |
| [Watermelon UI](https://ui.watermelon.sh/) | React components, blocks, dashboards and templates | Use free/public components |
| [Motion Primitives](https://motion-primitives.com/) | Reusable motion-focused React components | Use free source components |
| [21st.dev](https://21st.dev/) | Component marketplace and retrieval | Free tier only; 2 code retrievals/day |
| [shadcn/ui](https://ui.shadcn.com/) | Base component primitives and registry workflow | Free/open source |
| [Haikei](https://haikei.app/) | Generate/export SVG backgrounds | Use free exports; do not buy assets |
| [Alibaba Page Agent](https://github.com/alibaba/page-agent) | Browser-side natural-language interaction with existing pages | Open-source project; optional |

React Bits repository is MIT + Commons Clause and describes the components as free for personal and commercial use. Still inspect individual third-party notices when using adapted effects. [Source](https://github.com/DavidHDev/react-bits).

### Animation choice

- Use Motion (package `motion`, imports from `motion/react`) for React component transitions, layout animation and gestures. Motion is MIT-licensed and free.
- Use GSAP for complex timelines and scroll choreography. Its full toolset, including formerly paid plugins, is now free.
- Do not animate the same element with both engines. Respect `prefers-reduced-motion`.
- Use CSS transitions for simple hover/focus states.

Do not install animation dependencies until the app framework is selected.

## 4. Strix without API spending

Strix is open source. It can use a local model through Ollama, so no paid LLM API key is required. This avoids API charges but requires local compute, disk space, Docker and model downloads. A large model may not run well on modest hardware.

Install Ollama, then download a model that your computer can handle. Strix's docs currently show this example:

```bash
ollama pull qwen3-vl
```

Install Strix and configure the local model:

```bash
curl -fsSL https://strix.ai/install | bash
export STRIX_LLM="ollama/qwen3-vl"
export LLM_API_BASE="http://localhost:11434"
strix -n --target ./ --scan-mode quick
```

Strix's local-model guide: [Ollama setup](https://github.com/usestrix/strix/blob/main/docs/llm-providers/local.mdx).

**Do not use the removed GitHub Actions Strix workflow.** Cloud CI scans with hosted LLM inference could create charges. Run Strix locally only, with the Ollama endpoint selected. Only test this repository or systems you are authorized to assess.

## 5. What is free and what has limits?

- Free/open source: GSAP, Motion, shadcn/ui, public React Bits components, UI/UX Pro Max basic, Taste, Strix software, Ollama.
- Free with a usage limit: 21st.dev component retrieval (2/day on its free account).
- No paid React Bits Pro license, 21st.dev subscription, Strix API key, hosted LLM, or AI credits should be purchased.
- Normal internet/data usage, local electricity, and computer storage are not included in software pricing.

## 6. Pending app scaffold

This repository currently has no `package.json`, React app, `components.json`, or deployment target. Do not install React, Next.js, Tailwind, Motion, GSAP, React Bits components, or Watermelon components until the framework and actual site requirements are selected.

Once the scaffold exists:
1. Initialize shadcn/ui.
2. Add free Watermelon UI components only when they solve a real requirement.
3. Copy/install public React Bits components selectively.
4. Add Motion and/or GSAP only where required.
5. Export Haikei SVG assets and commit them to the project.
