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
| [Vercel React best practices](https://github.com/vercel-labs/agent-skills) | React and Next.js performance guidelines | Open source |
| [Vercel web design guidelines](https://github.com/vercel-labs/agent-skills) | UX, accessibility, responsive behavior and interface review | Open source |
| [21st.dev skills](https://github.com/21st-dev/skill) | Discover and adapt component patterns | Free skill; service has free-tier limits |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design systems, styles, palettes, typography and UX patterns | Open-source basic version |
| [Design-to-code skill](../.agents/skills/design-to-code/SKILL.md) | Translate Penpot, Lunacy or connected Figma designs into accessible, token-based UI | Included in this repository |

Taste requires Node.js 22+ and Chrome, Edge or Chromium for its browser inspection script. It does not need API keys.

## 2. MCP integrations

Project configuration is in [.mcp.json](../.mcp.json).

| Server | Purpose | Cost / limit |
|---|---|---|
| shadcn | Search and install components from public shadcn-compatible registries | Free/open source |
| Watermelon UI | Search its component, block, dashboard and template catalog | Public MCP endpoint; no key configured |
| 21st.dev | Component search and retrieval | Free account supports 2 component-code retrievals per day; paid plan is not needed if we stay within that allowance |
| Penpot | Read and edit the active design file through Penpot's official MCP | Open source/local option; hosted remote availability depends on the Penpot account/deployment |
| Lunacy | Inspect selected layers, variables, components and assets in the running Lunacy desktop app | Free desktop app; local MCP, no paid API key |
| Context7 | Retrieve current library documentation and code examples | Public remote MCP; anonymous use has low rate limits |

21st.dev's free tier requires a free account/API token for most MCP clients. Set `API_KEY_21ST` in the environment used to launch the MCP client. Do not purchase Builder or AI credits. Its search/browsing is free and the free account currently includes 2 code retrievals daily. See [21st.dev MCP docs](https://docs.21st.dev/mcp) and [pricing/limits](https://mcp.21st.dev/pricing).

Penpot and Lunacy setup is optional and documented in [DESIGN-TOOLS.md](DESIGN-TOOLS.md). Penpot's project entry reads a complete URL from `PENPOT_MCP_URL`; do not commit the URL because it contains an access key. Lunacy supplies its own server configuration from the running app; copy its entry instead of guessing a local port or endpoint.

Context7 is configured at `https://mcp.context7.com/mcp`. Anonymous access is available with lower rate limits; optional authentication raises limits depending on its plan. Do not add a paid plan or API-credit dependency. See [Context7 installation](https://context7.com/docs/installation) and [MCP client guidance](https://context7.com/docs/resources/all-clients).

The connected ChatGPT Figma app is a separate design integration, not a project MCP server. Its availability and feature limits depend on the user's Figma/ChatGPT accounts.

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

### Animation choice

- Use Motion (package `motion`, imports from `motion/react`) for React component transitions, layout animation and gestures. Motion is MIT-licensed and free.
- Use GSAP for complex timelines and scroll choreography. Its full toolset, including formerly paid plugins, is now free.
- Do not animate the same element with both engines. Respect `prefers-reduced-motion`.
- Use CSS transitions for simple hover/focus states.

Do not install animation dependencies until the app framework is selected.

## 4. Automated repository checks

The repository contains GitHub Actions workflows for:

| Workflow | Trigger | Purpose | Current state |
|---|---|---|---|
| Repository validation | Every push, pull request, manual | Checks MCP JSON, env placeholders, `.gitignore`, local Markdown links, installer syntax and whitespace | Runs now via `scripts/validate_repo.py` |
| Quality checks | Push, pull request, manual | Markdown lint; optional npm dependency audit, lint, typecheck, test and build | Markdown runs now; Node.js checks wait for a package manifest and lockfile |
| CodeQL | Push, pull request, weekly schedule | Static security analysis for JavaScript/TypeScript | Skips until JS/TS source files exist |
| Secret scan | Push, pull request, weekly schedule | Gitleaks scans Git history for accidentally committed credentials | Runs now |
| Browser tests | Push, pull request, manual | Playwright Chromium tests | Skips until package manifest, lockfile and Playwright config exist |
| Accessibility audit | Manual | Pa11y CI audit against a supplied public URL | Runs when a target URL is provided |
| Lighthouse audit | Manual | Performance, accessibility, best-practices and SEO report | Runs when a target URL is provided; report stored as a short-retention artifact |
| GitHub Pages deploy | Manual | Deploys the `site/` directory | Waits for `site/index.html` and Pages configuration |

The repository also has a Python-based validator at `scripts/validate_repo.py`; it checks the repository-owned MCP and environment configuration, not whether remote MCP endpoints are reachable. Keep this validation workflow and script when editing `.mcp.json`, `.env.example`, `.gitignore`, or Markdown links.

The public repository uses standard GitHub-hosted runners. The workflows do not call paid AI APIs or paid external scanning services. Lighthouse and accessibility audits target public URLs; do not put credentials or private URLs into workflow inputs.

### Running manual audits from GitHub on mobile

1. Open the repository's **Actions** tab.
2. Select **Lighthouse audit** or **Accessibility audit**.
3. Choose **Run workflow**.
4. Enter the public website URL and start the workflow.
5. Open the run to see the logs or download the Lighthouse HTML artifact.

These manual audits become useful once the site is deployed.

### GitHub Pages setup

When the website is ready, open **Settings → Pages** and set the build/deployment source to **GitHub Actions**. The included deployment workflow expects the built static site in `site/` and an `index.html` at its root. No custom domain is required.

### Dependency updates

Dependabot currently checks GitHub Actions weekly. The npm updater is intentionally disabled because this repository has no `package.json`; leaving it enabled produces a failed update job (`/package.json not found`). Add the appropriate Dependabot ecosystem only after selecting the application's package manager and committing its manifest and lockfile. The Node.js CI job runs `npm audit --audit-level=high` only when an npm project and `package-lock.json` are present.

## 5. Strix without API spending

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

## 6. What is free and what has limits?

- Free/open source: GSAP, Motion, shadcn/ui, public React Bits components, UI/UX Pro Max basic, Taste, Vercel agent skills, Playwright, Pa11y, Lighthouse, Gitleaks, CodeQL for public repositories, Dependabot, Strix software and Ollama.
- Free with usage limits: 21st.dev component retrieval (2/day on its free account) and Context7 anonymous requests.
- Penpot is open source; use its local MCP option when remote MCP is unavailable.
- Lunacy provides a free single-user desktop option; keep use within its free license.
- No paid React Bits Pro license, 21st.dev subscription, Strix API key, hosted LLM, or AI credits should be purchased.
- Normal internet/data usage, local electricity, and computer storage are not included in software pricing.

## 7. Pending app scaffold

This repository currently has no `package.json`, React app, `components.json`, or deployment target. Do not install React, Next.js, Tailwind, Motion, GSAP, React Bits components, or Watermelon components until the framework and actual site requirements are selected.

Once the scaffold exists:

1. Initialize shadcn/ui.
2. Add free Watermelon UI components only when they solve a real requirement.
3. Copy/install public React Bits components selectively.
4. Add Motion and/or GSAP only where required.
5. Export Haikei SVG assets and commit them to the project.
