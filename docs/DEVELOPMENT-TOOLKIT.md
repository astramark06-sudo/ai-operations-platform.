# Website development toolkit

This project has a strict zero-spend requirement. The toolkit uses free/open-source software and optional free tiers. It does not require a paid subscription, paid model API, paid component license, paid hosting plan or AI credits.

The repository currently has no application scaffold, so frontend dependencies will be selected after the website requirements and framework are chosen. The CI workflows are designed to skip app-specific checks until the corresponding scaffold exists.

## 1. Agent skills

Run from the repository root in a compatible coding-agent environment:

```bash
bash scripts/setup-agent-toolkit.sh
```

| Tool / skill | Purpose | Cost |
|---|---|---|
| [Motion AI kit](https://motion.dev/docs/react) | Motion for React documentation and agent tooling | Free/open source |
| [GSAP skills](https://github.com/greensock/gsap-skills) | Timelines, ScrollTrigger, React integration and performance | Free; full GSAP toolset |
| [Taste](https://github.com/Leonxlnx/taste-skill) | Art direction, layout, typography and browser-based visual QA | Free; no API key |
| [Vercel React best practices](https://github.com/vercel-labs/agent-skills) | React performance, rendering, data fetching and bundle-size guidance | Open source |
| [Vercel web design guidelines](https://github.com/vercel-labs/agent-skills) | UX, accessibility, responsive behavior and interface review checklist | Open source |
| [21st.dev skills](https://github.com/21st-dev/skill) | Discover and adapt component patterns | Free skill; service has free-tier limits |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design systems, styles, palettes, typography and UX patterns | Open-source basic version |

Taste requires Node.js 22+ and Chrome, Edge or Chromium for its browser inspection script. It does not need API keys.

The installer is intended for a compatible coding-agent environment. It has not been run on the user's Android device, and adding it to GitHub does not install skills into ChatGPT itself.

## 2. MCP integrations

Project configuration is in [.mcp.json](../.mcp.json). MCP availability depends on the client: GitHub repository configuration does not automatically connect a server to the ChatGPT Android app.

| Server | Purpose | Cost / limit |
|---|---|---|
| shadcn | Search and install components from public shadcn-compatible registries | Free/open source |
| Watermelon UI | Search its component, block, dashboard and template catalog | Public MCP endpoint; no key configured |
| 21st.dev | Component search and retrieval | Free account has a limited daily code-retrieval allowance |
| Context7 | Retrieve current library documentation and code examples from upstream docs | Public endpoint; usable without a key at lower rate limits |

21st.dev's free tier requires a free account/API token for most MCP clients. Set `API_KEY_21ST` only in a compatible client's environment. Do not purchase Builder or AI credits. See [21st.dev MCP docs](https://docs.21st.dev/mcp) and [pricing/limits](https://mcp.21st.dev/pricing).

Context7 is configured at `https://mcp.context7.com/mcp`. It can be used without an API key, subject to lower anonymous rate limits. A key is optional and should only be used with a free allowance. See [Context7 MCP documentation](https://context7.com/docs).

The project MCP format may need translation for clients that do not support Claude Code-style `.mcp.json`.

## 3. Component and visual libraries

Use these as source libraries, not as a reason to install every package.

| Resource | Use | Cost guidance |
|---|---|---|
| [React Bits](https://www.reactbits.dev/) | Animated React components, text effects, backgrounds and micro-interactions | Use public open-source components; avoid Pro |
| [Watermelon UI](https://ui.watermelon.sh/) | React components, blocks, dashboards and templates | Use free/public components |
| [Motion Primitives](https://motion-primitives.com/) | Reusable motion-focused React components | Use free source components |
| [21st.dev](https://21st.dev/) | Component marketplace and retrieval | Free tier only |
| [shadcn/ui](https://ui.shadcn.com/) | Base component primitives and registry workflow | Free/open source |
| [Haikei](https://haikei.app/) | Generate/export SVG backgrounds | Use free exports; do not buy assets |
| [Alibaba Page Agent](https://github.com/alibaba/page-agent) | Browser-side natural-language interaction with existing pages | Open-source project; optional |

React Bits' repository is MIT + Commons Clause and describes the components as free for personal and commercial use. Still inspect individual third-party notices when using adapted effects. [Source](https://github.com/DavidHDev/react-bits).

### Animation choice

- Use Motion (package `motion`, imports from `motion/react`) for React component transitions, layout animation and gestures. Motion is MIT-licensed and free.
- Use GSAP for complex timelines and scroll choreography. Its full toolset is free.
- Do not animate the same element with both engines. Respect `prefers-reduced-motion`.
- Use CSS transitions for simple hover/focus states.

Do not install animation dependencies until the app framework is selected.

## 4. Automated repository checks

The repository contains GitHub Actions workflows for:

| Workflow | Trigger | Purpose | Current state |
|---|---|---|---|
| Quality checks | Push, pull request, manual | Markdown lint; optional npm lint, typecheck, test and build scripts | Markdown check runs now; Node checks wait for a package manifest and lockfile |
| CodeQL | Push, pull request, weekly schedule | Static security analysis for JavaScript/TypeScript | Skips until JS/TS source files exist |
| npm audit | Push, pull request, manual | Audits locked npm dependencies and fails on high-severity vulnerabilities | Runs when an npm package manifest and lockfile exist |
| Secret scan | Push, pull request, weekly schedule | Gitleaks scans Git history for accidentally committed credentials | Runs now |
| Browser tests | Push, pull request, manual | Playwright Chromium tests | Skips until package manifest, lockfile and Playwright config exist |
| Accessibility audit | Manual | Pa11y CI audit against a supplied public URL | Runs when a target URL is provided |
| Lighthouse audit | Manual | Performance, accessibility, best-practices and SEO report | Runs when a target URL is provided; report stored as a short-retention artifact |
| GitHub Pages deploy | Manual | Deploys the `site/` directory | Waits for `site/index.html` and Pages configuration |

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

Dependabot is configured to check npm dependencies and GitHub Actions weekly. It will not create npm update pull requests until an npm project exists. The Node.js CI job also runs `npm audit --audit-level=high` once a package manifest and lockfile are present.

## 5. Strix without API spending

Strix is open source. It can use a local model through Ollama, so no paid LLM API key is required. This avoids API charges but requires a separate computer, local compute, disk space, Docker and model downloads. A large model may not run well on modest hardware.

Strix is therefore **not part of the mobile-only workflow**. Do not assume it can run in ChatGPT or on the Android device.

For a computer that can handle local inference, see [Strix's Ollama setup](https://github.com/usestrix/strix/blob/main/docs/llm-providers/local.mdx). Do not use the removed GitHub Actions Strix workflow; cloud CI scans with hosted LLM inference could create charges. Only test this repository or systems you are authorized to assess.

## 6. What is free and what has limits?

- Free/open source: GSAP, Motion, shadcn/ui, public React Bits components, UI/UX Pro Max basic, Taste, Vercel agent skills, Playwright, Pa11y, Lighthouse, Gitleaks, CodeQL for public repositories, Dependabot and Context7 anonymous access.
- Free with limits: 21st.dev component retrieval and optional authenticated Context7 usage.
- Hosting: GitHub Pages for a static website in this public repository.
- Avoid: React Bits Pro, 21st.dev paid plans, Strix API inference, hosted LLMs, paid templates, paid assets and paid hosting.
- Ordinary internet/data use and storage remain practical requirements.

## 7. Pending application scaffold

This repository currently has no `package.json`, React app, `components.json`, `site/index.html` or deployment target. Do not install React, Next.js, Tailwind, Motion, GSAP, React Bits components or Watermelon components until the framework and site requirements are selected.

Once the scaffold exists:

1. Select the framework and package manager deliberately.
2. Initialize shadcn/ui if it fits the design.
3. Add free Watermelon UI components only when they solve a real requirement.
4. Copy/install public React Bits components selectively.
5. Add Motion and/or GSAP only where required.
6. Add Playwright configuration and meaningful browser tests.
7. Export Haikei SVG assets and commit them to the project.
8. Build into `site/` or update the Pages workflow to match the selected framework's output directory.

## 8. Design sources: Penpot and Lunacy

The repository also includes a design-to-code skill at [`.agents/skills/design-to-code/SKILL.md`](../.agents/skills/design-to-code/SKILL.md) and setup instructions in [`docs/DESIGN-TOOLS.md`](DESIGN-TOOLS.md).

- **Penpot:** preferred open-source design source. The optional MCP entry reads `PENPOT_MCP_URL` from the environment. The complete URL contains a private key; keep it out of commits and logs.
- **Lunacy:** optional free desktop design source. Its native application provides a local MCP configuration; copy the configuration from the running app rather than guessing an endpoint.
- Inspect only the user-selected file/page. Treat the selected design as the source of truth, and translate its styles into reusable project-owned tokens.
- These design MCPs require a compatible desktop or hosted MCP client. They do not become active inside ChatGPT's Android app merely because they are listed in this repository.
