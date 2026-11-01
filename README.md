# Website Creation

Repository for building the website and its supporting development workflow.

## Cost policy

This project has a strict zero-spend requirement. Use free/open-source tools, free public-repository GitHub Actions, and GitHub Pages. Do not introduce paid subscriptions, paid model APIs, paid hosting, paid assets, or paid component licenses.

## Current repository setup

- Agent skills: Motion, GSAP, Taste, Vercel React best practices, Vercel web design guidelines, 21st.dev, UI/UX Pro Max and the repository's design-to-code skill.
- MCP configuration: shadcn, Watermelon UI, optional 21st.dev, Context7 and optional Penpot.
- Design workflow: Penpot is the preferred open-source design source; Lunacy is documented as an optional desktop design source.
- Quality: Markdown lint and optional Node.js dependency audit, lint, typecheck, test and build jobs.
- Security: CodeQL for JavaScript/TypeScript when present, Gitleaks history scans and npm audit when a Node.js app exists.
- Browser and UX: conditional Playwright tests, manual Pa11y accessibility audit and manual Lighthouse audit.
- Deployment: manual GitHub Pages workflow for a built static site in `site/`.
- Dependency maintenance: weekly Dependabot updates for npm and GitHub Actions.

See [docs/DEVELOPMENT-TOOLKIT.md](docs/DEVELOPMENT-TOOLKIT.md) for workflow behavior and limits. See [docs/DESIGN-TOOLS.md](docs/DESIGN-TOOLS.md) for Penpot and Lunacy setup.

## Mobile-first workflow

Repository changes can be managed through GitHub's website or connected GitHub integration. The local agent installer is optional and requires a compatible coding environment; it has not been run on Android. MCP configuration in this repository does not automatically connect servers to ChatGPT's Android app.

## Project state

The repository is still a tooling starter. No frontend framework, application scaffold, package manifest or website content has been selected. App-specific CI checks and deployment remain dormant until the corresponding source/configuration exists.

Coding agents must read [AGENTS.md](AGENTS.md) before making changes.
