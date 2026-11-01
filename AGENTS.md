# Website development instructions

## Project state

This repository is being prepared as a website project. Do not assume a framework, package manager, or application structure until the project scaffold is selected and committed.

## Zero-cost requirement

- Do not add paid services, subscriptions, API-credit dependencies, paid templates, or paid component licenses.
- Prefer free and open-source tools, local execution, and free tiers with explicit usage limits.
- Never trigger paid model APIs or hosted scans. Ask before introducing any service that could incur charges.
- Use public/free React Bits components only; do not depend on React Bits Pro.
- For 21st.dev, stay within its free allowance; component retrieval is limited on the free account.
- Strix must use a local Ollama model by default, not a paid LLM API.
- Do not run cloud CI security scans that require paid inference.

## Design and implementation

- Start each page or feature with a clear information hierarchy, responsive layout plan, and accessible interaction model.
- Build a coherent design system first: semantic color tokens, type scale, spacing, radii, elevation, and motion rules.
- Prefer custom, purposeful composition over generic template layouts.
- Use semantic HTML, keyboard-accessible controls, visible focus states, reduced-motion support, and responsive behavior.
- Keep components composable and source-owned. Add only dependencies required by the selected implementation.
- Prefer shadcn/ui as the base primitive layer; use React Bits, Watermelon UI, Motion Primitives, and 21st.dev as selective source libraries.
- Use GSAP for complex timelines and scroll choreography. Use Motion for React component transitions and layout animation. Avoid running two animation engines on the same element.
- Use Haikei for bespoke SVG backgrounds when a page needs them; commit exported assets rather than relying on a runtime generator.

## Design application integrations

- Penpot is the preferred open-source design source. When its MCP is connected, inspect the active file/page, layers, components, variables, typography, spacing, and exported assets before implementation.
- Lunacy is an optional desktop design source. Use its MCP only when the native app is running and the user has selected the relevant document or objects.
- Figma may be used through the connected ChatGPT Figma app when available; this is separate from project MCP configuration and is not a Figma MCP server.
- Treat the design file selected by the user as the source of truth for visual specifications. Do not silently combine Penpot, Lunacy, or Figma files or assume they contain the same design.
- Translate design values into project-owned semantic tokens and reusable components; do not copy demo styling or create a parallel design system.
- If an MCP connection is unavailable, state the limitation and work from user-provided exports, screenshots, or specifications instead.
- Read `.agents/skills/design-to-code/SKILL.md` before substantial design-to-code work.
- Keep all MCP URLs, access tokens, and keys out of commits, logs, screenshots, and generated documentation.

## Agent workflow


- Read relevant skill instructions before applying a specialist workflow.
- Use Vercel's `react-best-practices` skill when implementing React and `web-design-guidelines` for UX, accessibility, and visual review.
- Use UI/UX Pro Max for design-system and UX guidance; Taste for art direction and visual QA; GSAP skills for advanced GSAP implementation; 21st.dev and Watermelon MCPs for source-backed component discovery; Context7 for current library documentation when available.
- Inspect a component's source, dependencies, accessibility, license, and responsive behavior before adding it.
- Adapt imported components to project tokens. Do not leave demo colors or unrelated dependencies in production.
- Run type checks, lint, tests, and a production build when those scripts exist.
- Use browser-based visual checks for important responsive states.

## Repository automation


- Keep CI workflows least-privileged; grant only the permissions a job needs.
- Pin external GitHub Actions to reviewed major versions and allow Dependabot to keep them updated.
- Never introduce AI security scans, hosted LLM calls, paid Actions, or services that can incur charges.
- Keep manual audits scoped to public URLs; never pass secrets or authenticated URLs as workflow inputs.

## Security

- Never commit API keys, tokens, passwords, customer data, or environment files.
- Run Strix only against this repository or targets the owner has explicitly authorized.
- Treat security findings as actionable evidence; verify the affected code and retest fixes.

## Source-of-truth rule

The repository's design tokens and existing components take precedence over imported library defaults. Prefer editing a copied component over introducing a second competing design system.
