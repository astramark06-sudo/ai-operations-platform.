# Unified website toolchain — one coordinated system

**Status:** Operating architecture for this repository
**Contract version:** 1.0.0
**Scope:** Design, component discovery, implementation, animation, browser exploration, QA and security

## 1. What “one body” means

The tools do not become one application or automatically call each other merely because their names appear in configuration. They become one coordinated system when they share:

1. **One orchestrator:** the repository's unified-web-engineering skill selects specialists and orders their work.
2. **One memory:** GitHub stores the feature handoff, decisions, component provenance, motion ownership and test evidence.
3. **One design system:** every component and asset maps to the same approved token contract.
4. **One motion ownership map:** each animated target has one animation engine owner.
5. **One set of gates:** a tool's output is not accepted until the next stage validates it.

The system deliberately does not run every tool on every task. The orchestrator selects only the organs needed and records whether each connection was truly available.

## 2. The organism

**Workflow:** User brief → Unified orchestrator → UI/UX Pro Max → Taste → one selected design source → component discovery → shadcn primitive foundation + approved source-library additions → implementation → Motion/GSAP/CSS ownership → Haikei assets → local/staging preview → Alibaba Page Agent exploration → Playwright regression tests → Strix authorized security review → GitHub CI, accessibility and Lighthouse gates → reviewed release.

Feedback from visual review, browser exploration, tests and security returns to the orchestrator and implementation stage. This is a workflow, not a claim that every service is currently live or connected.

## 3. Organs and boundaries

| Organ | Tool | Owns | Must not do |
|---|---|---|---|
| Brain / coordinator | Unified orchestration skill | Planning, handoffs, contract updates, conflict resolution and gates | Pretend disconnected tools are live |
| Product intelligence | UI/UX Pro Max | Product-aware UX structure, token proposal and accessibility guidance | Silently override the selected design source |
| Art direction / visual cortex | Taste | Distinctive visual direction, browser review and prioritized visual corrections | Create a competing token system |
| Design memory / sensory input | One of Penpot, Figma or Lunacy | Authoritative frames, variables, components and assets | Treat unsynchronized files as equally authoritative |
| Primitive skeleton | shadcn/ui | Default accessible primitives and registry workflow | Become a separate visual theme |
| Component scouts | 21st.dev, Watermelon UI, React Bits through Manus, Motion Primitives | Search and compare candidate components and blocks | Install everything found or bypass licence review |
| Visual page editors | Puck, GrapesJS, Webstudio, Onlook | Build editable pages/sites visually; choose by output ownership and deployment model | Create a second source of truth beside the chosen design file |
| Low-code app builders | Appsmith, Budibase, ToolJet | Visually compose internal tools, dashboards and operational apps | Treat them as the default for public marketing sites or ignore AGPL/GPL obligations |
| Code-first admin frameworks | Refine, React Admin | Build custom data-centric admin/B2B applications | Combine both frameworks in one app without a concrete boundary |
| Interactive UI systems | Magic UI, daisyUI, Flowbite React, Chakra UI, MUI, Headless UI, Floating UI | Source animated components, coherent component systems, accessible primitives and positioning behavior | Mix multiple global design systems or confuse a positioning engine with a component library |
| Workflow and canvas editors | React Flow, Rete.js, Excalidraw | Build node graphs, programmable flows, diagrams and whiteboards | Use a freeform canvas where a structured workflow graph is required |
| Dynamic layout and drag/drop | React Grid Layout, dnd-kit, FormKit Drag and Drop, React Resizable Panels | Create draggable dashboards, sortable lists, split panes and editable workspaces | Ship drag-only interactions without keyboard alternatives or responsive fallbacks |
| CSS and motion specialists | Open Props, CSS Doodle, React Spring, Anime.js | Supply CSS tokens, generative visual effects and alternative animation models | Introduce competing token systems or multiple animation owners on the same target |
| Application framework alternatives | Next.js, SvelteKit, Nuxt | Select a full application framework after product and rendering requirements are known | Stack multiple frameworks in one app |
| Primitive alternatives | Base UI, Radix UI, React Aria, Mantine | Fill a documented primitive/accessibility gap or deliberately select a full UI system | Mix multiple primitive foundations or global themes in one component family |
| Component memory | Storybook + its MCP addon | Record reusable components, variants, states and implementation guidance | Replace the selected product design file |
| Versioned skill bridge | TanStack Intent | Load package-maintained skills that match installed TanStack versions | Install unrelated or unreviewed agent instructions |
| Continuous audits | Lighthouse CI, Pa11y CI | Check performance budgets and multi-route accessibility during CI | Treat automated scores as a complete UX or accessibility review |
| Editorial content | Payload CMS | Supply a Next.js-native structured content backend and admin when required | Add a CMS to a static site or before hosting/database decisions |
| Documentation quality | CSpell | Catch terminology and spelling errors across code/docs | Block work over unreviewed product names or a missing vocabulary list |
| Browser instrumentation | Playwright MCP, Chrome DevTools MCP | Agent inspection, console/network diagnostics and performance traces | Replace deterministic tests or expose personal browser profiles |
| Data and forms | TanStack Query/Table, React Hook Form, Zod, MSW, Zustand | Real remote data, complex forms, schemas, realistic network tests and shared client state | Add dependencies before their acceptance criteria exist |
| Accessibility and test organs | Vitest, React Testing Library, axe-core | Unit/component tests and automated WCAG/ARIA checks | Claim automated scans prove full accessibility |
| Visual/asset specialists | Lucide, Tabler, Recharts, SVGO, Sharp, dotLottie | Consistent icons/charts, optimized exports and authored vector animation | Mix icon/chart systems without reason or treat animation-player licence as asset licence |
| 3D and scroll specialists | Three.js, React Three Fiber, Drei, Lenis | Explicit 3D scenes and justified scroll-led experiences | Add GPU-heavy or smooth-scroll dependencies by default |
| Build and framework candidates | Vite, Astro, Starlight | Select a suitable app/content/docs build model | Choose a framework before requirements are defined |
| Backend and analytics candidates | Supabase, Appwrite, Umami | Real backend or privacy-conscious product metrics | Confuse open-source software with free hosted infrastructure |
| Code and supply-chain quality | Biome, Knip, OSV-Scanner, Trivy, OWASP ZAP | Hygiene, dead-code/dependency checks, dependency/SBOM and authorized DAST scanning | Run duplicate overlapping scanners on every change or scan unauthorized targets |
| Motion component organ | Motion for React | React state transitions, gestures, layout and enter/exit | Co-own a DOM target with GSAP |
| Timeline organ | GSAP | Complex timelines, scroll choreography, SVG morphs and sequencing | Replace Motion for routine React state transitions |
| Motion tissue library | Motion Primitives | Copy-in Motion-based components where stack-compatible | Add a second motion runtime unnecessarily |
| Visual materials | Haikei | Export original SVG/PNG assets | Become a runtime service dependency |
| Reflexes / exploratory browser | Alibaba Page Agent | Natural-language exploration of local/staging pages | Replace Playwright or operate on production accounts without scope |
| Immune system | Strix with local Ollama | Authorized security probing, findings and retest evidence | Run against unapproved targets or paid inference |
| Memory and release control | GitHub and CI | Versioned contracts, pull requests, repeatable tests and evidence | Treat setup-detection jobs as app test coverage |

### Repository status versus live connection

- Project configuration currently includes shadcn, 21st.dev, Watermelon UI, Penpot (environment placeholder) and Context7 in .mcp.json.
- The installer script prepares Motion, GSAP, Taste, Vercel skills, 21st.dev skills and UI/UX Pro Max. This does not prove those skills are loaded in every client.
- React Bits is a source library the owner reports using through Manus; it is not a project MCP server.
- Motion Primitives and Haikei are component/asset sources, not MCP servers in this configuration.
- Alibaba Page Agent is optional browser-side exploration with an optional beta MCP/extension; it is not configured here.
- Strix is documented as a local-only security option; it is not installed or running.
- The repository has no application scaffold or package manifest. Runtime packages remain intentionally uninstalled.

## 4. The shared nervous system: one feature contract

For every substantial page or feature, copy [the UI handoff template](../contracts/ui-handoff.template.json) to a feature-specific file, for example docs/contracts/features/dashboard.json.

That file is the common language between all tools. It records:

- The user outcome and testable acceptance criteria.
- Exactly one authoritative design file for the feature.
- Approved semantic tokens and responsive breakpoints.
- Each adopted component, its origin, licence review, third-party notices, dependencies and accessibility review.
- The single motion owner for each target.
- Data source and persistence truth, including mock versus real integrations.
- Tool runs, decisions, defects and the next handoff.

Do not rely on chat history to synchronize work across Manus, ChatGPT, another coding agent or a future session. Read the current feature contract first and write decisions back to GitHub.

The machine-readable tool catalogue is [toolchain.registry.json](../contracts/toolchain.registry.json). It defines each tool's organ, repository status, responsibility, inputs, outputs and handoff destination.

## 5. Exact stage sequence

### Stage 0 — Brief and scope

The orchestrator owns the user outcome, audience, feature boundary, constraints and acceptance tests. Output: a feature brief with explicit unknowns. Do not invent product scope.

### Stage 1 — Product UX and design system proposal

**UI/UX Pro Max** proposes information architecture, UX patterns, palette, typography, interaction and accessibility.

**Taste** challenges generic choices and defines art direction. It reviews the initial proposal rather than generating an unrelated competing design system.

Output: one candidate direction and a list of decisions still needing resolution.

### Stage 2 — Authoritative design inspection

Select one source for the feature: Penpot, Figma or Lunacy. Inspect the relevant frame, layout constraints, variables, components, assets, responsive behavior and interactions. If no live connection exists, use supplied exports/specifications and mark inferences as assumptions.

Output: token evidence, component map, asset list and unresolved questions.

### Stage 3 — Component discovery and adoption

1. Search shadcn first for the accessible primitive baseline.
2. Search Watermelon UI and 21st.dev for alternatives and composed blocks.
3. Search React Bits through Manus when available for expressive effects.
4. Search Motion Primitives for Motion-based interactions that fit the selected React/Tailwind stack.
5. Consider Base UI, Radix or React Aria only where the selected shadcn primitive does not fit; Mantine is a complete-system alternative, not an additive theme.
6. Use Storybook when the project has enough reusable components to need isolated stories, variants and component documentation.
7. Compare candidates; do not merge several implementations of the same pattern.

Before adoption, inspect source, licence, third-party notices, dependencies, accessibility, responsive behavior, keyboard behavior and mobile fallback. Record the winning candidate. The 21st.dev free account currently allows two code retrievals per day; search first and retrieve only after shortlisting.

Output: a reviewed component inventory, not a pile of unfiltered snippets.

### Stage 4 — Implementation, state and motion ownership

Implement approved tokens and components in project-owned source. Adapt imported code to the contract. Select supporting libraries only when a feature needs their capability:

- TanStack Query for remote/server state; TanStack Table for complex data grids.
- React Hook Form for complex forms; Zod for runtime schemas shared across boundaries.
- Zustand only when shared client state outgrows local React state/context.
- Mock Service Worker for realistic network-level tests; never present mocked data as real persistence.
- Recharts only when the product needs actual data visualization.
- Keep simple forms, static tables, local state and hand-authored CSS dependency-free where possible.

- **CSS** owns simple hover/focus and local transitions.
- **Motion for React** owns React component state transitions, gestures, layout and presence transitions.
- **GSAP** owns complex timelines, scroll narratives and coordinated multi-element sequences.
- Each DOM target has only one animation owner. If a component contains independent animated sub-elements, record each target separately.

### Stage 5 — Visual materials

Use Haikei only when a generated background or vector is needed. Export approved assets, optimize them and commit them under the project's asset directory with any required attribution. Do not load the Haikei editor at runtime.

### Stage 6 — Browser exploration, component and accessibility tests

**Alibaba Page Agent** or **Playwright MCP** may explore the running local/staging page with natural-language actions and report interaction gaps. Choose one for each exploration pass; neither replaces repeatable assertions.

**Chrome DevTools MCP** is an optional browser diagnostics organ for console/network/performance traces. Use isolated browser profiles; it can inspect the full browser context.

**Storybook** provides isolated component stories and state/variant references once the component system warrants it. The Storybook MCP addon exposes those component facts to compatible agents.

**Playwright** encodes repeatable journeys and assertions. **Vitest + React Testing Library** cover unit and component behavior where a React/Vite stack is chosen. **axe-core** can run inside tests for automated accessibility regression checks; retain manual keyboard and assistive-technology review. **Taste** reviews mobile, tablet and desktop visuals. The orchestrator converts accepted findings into explicit implementation tasks.

### Stage 7 — Security and release gates

**Strix** runs only after the repository or staging target exists and scope is explicitly authorized. Prefer local Ollama plus Docker; collect evidence, fix verified findings and retest. Do not run it in cloud CI or introduce hosted paid inference.

GitHub CI remains the release gate: repository validation, Markdown lint, secret scanning, CodeQL when source exists, Playwright when the app exists, accessibility and Lighthouse audits against an authorized public HTTPS deployment. For multi-route apps, Pa11y CI can scan a fixed URL list or sitemap; Lighthouse CI can enforce repeatable performance budgets. CSpell can check documentation terminology. These are candidates, not added workflow jobs yet. Consider OSV-Scanner for dependency advisories, Trivy for SBOM/container/filesystem/license coverage, and OWASP ZAP for an explicitly authorized staging DAST pass. Keep scanners complementary and scoped. A skipped application test is not a passing application test.

## 6. Conflict-resolution rules

1. **Design source beats library defaults.** Project tokens and the selected design file outrank imported colors, spacing and typography.
2. **shadcn is the current primitive baseline.** Base UI, Radix and React Aria are alternative/underlying primitive choices; Mantine is a complete-system alternative. Select one foundation per component family and do not create parallel global themes.
3. **One animation owner per target.** CSS, Motion and GSAP cannot compete for the same target/properties.
4. **Do not duplicate Motion under two package names.** Motion for React was previously Framer Motion. For a new app, use package motion and imports from motion/react. Use legacy framer-motion only if a selected dependency requires it; do not add both without a documented compatibility reason.
5. **Source ownership and licence are mandatory.** No paid/pro-only assets or components. Verify current component-specific licence and notices before copying source.
6. **Real operation beats decorative feedback.** Upload progress, payment success, deletion and form submission must be driven by actual state/API results.
7. **Exploration is not proof.** Page Agent and Taste can find issues; Playwright and CI provide repeatable checks.
8. **Security is scoped.** Strix, ZAP, Trivy and other scanners must never target an unapproved system.
9. **One icon and chart convention per product.** Choose Lucide or Tabler, and choose one charting library for each visualization layer.
10. **No duplicate quality tools.** Choose Biome or ESLint plus Prettier for overlapping formatting/linting responsibilities.
11. **Open source is not free infrastructure.** Supabase, Appwrite and Umami self-hosting requires compute and maintenance; managed free tiers have quotas. Do not activate without an explicit data/backend need and cost boundary.

## 7. Client and machine boundaries

- A compatible coding agent must load the repository's Agent Skills. The installer requires a compatible Node/browser environment; it does not install skills into ChatGPT Android automatically.
- .mcp.json is consumed only by compatible clients. It does not connect its servers to Manus or ChatGPT merely by existing in GitHub.
- Each client must configure its own supported MCP endpoints and credentials. Clients synchronize through committed contracts and pull requests.
- Taste browser inspection needs a compatible Node/browser environment.
- Strix needs a local machine, Docker and an available model runtime. A phone-only GitHub workflow cannot run it.
- Page Agent needs its own model/runtime. Do not use the public demo LLM endpoint for production or confidential pages.
- Never commit API keys, Penpot tokenized URLs or local runtime secrets.

## 8. Definition of synchronized

A feature is synchronized only when:

- A single feature contract exists and has no unresolved design-source conflict.
- UI/UX Pro Max and Taste outputs are reconciled into one design direction.
- Every adopted component has provenance, licence/dependency and accessibility review recorded.
- Important tokens are implemented from the same contract.
- Every animated target has one named owner.
- Mock data and real integrations are explicitly distinguished.
- Responsive, keyboard, focus, reduced-motion, loading, empty and error states are covered.
- Browser exploration findings have been triaged.
- Repeatable tests and security/quality gates have evidence.
- The GitHub PR contains contract and implementation together.

## 9. Official references

- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Taste skill](https://github.com/Leonxlnx/taste-skill)
- [GSAP AI skills](https://github.com/greensock/gsap-skills)
- [Motion for React](https://motion.dev/docs/react)
- [shadcn MCP](https://ui.shadcn.com/docs/mcp)
- [21st.dev MCP](https://docs.21st.dev/mcp)
- [Watermelon MCP](https://ui.watermelon.sh/developers/mcp)
- [React Bits](https://reactbits.dev/)
- [Motion Primitives](https://motion-primitives.com/docs)
- [Haikei free exports](https://haikei.app/pricing/)
- [Alibaba Page Agent](https://github.com/alibaba/page-agent)
- [Strix open-source security agent](https://www.strix.ai/open-source-pentesting)
- [Expanded web tool ecosystem catalogue](../references/EXPANDED-WEB-TOOL-ECOSYSTEM.md)
- [Machine-readable tool registry](../contracts/toolchain.registry.json)
- [Code and Chill UI playbook](../references/CODE-AND-CHILL-UI-PLAYBOOK.md)
