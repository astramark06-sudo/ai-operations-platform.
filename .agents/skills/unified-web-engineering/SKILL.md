---
name: unified-web-engineering
description: Coordinate product UX, art direction, design sources, component discovery, implementation, animation, browser exploration, testing and security as one contract-driven workflow. Use before substantial website, page or component design and implementation tasks.
---

# Unified web engineering

You are the coordinator for the repository's website toolchain. Make specialists share one decision record; do not call every available tool.

## Mandatory context

Read:

1. AGENTS.md
2. docs/architecture/UNIFIED-TOOLCHAIN.md
3. docs/contracts/toolchain.registry.json
4. The relevant feature contract copied from docs/contracts/ui-handoff.template.json, if one exists
5. docs/DEVELOPMENT-TOOLKIT.md when selecting or connecting tools

For design-to-code tasks, also read .agents/skills/design-to-code/SKILL.md. For React tasks, apply Vercel React best practices when loaded. Apply specialist skills only when relevant.

## Start-of-task connection check

Before relying on a tool:

- Check whether the current agent/client has actually loaded the relevant skill or can invoke the configured MCP server.
- Treat an entry in .mcp.json as configuration, not proof of connectivity.
- Record unavailable tools as not-available-in-this-client and continue with an explicit fallback.
- Never say a skill, MCP, Manus integration, Page Agent or Strix is connected unless the current client confirms it.
- Never expose or write credentials to the feature contract, logs or Git.

## Orchestration sequence

### 1. Scope

Extract the user outcome, audience, feature boundary, constraints and acceptance criteria. Ask only for a missing decision that blocks implementation. Do not invent a product concept or framework.

### 2. Create or resume the shared contract

Copy docs/contracts/ui-handoff.template.json to a feature-specific JSON file. If one already exists, read and update it instead of creating a competing document.

Record the feature ID, authoritative design source, pending questions, tool availability and next stage. The feature contract is shared memory across clients and sessions.

### 3. Design intelligence

- Use UI/UX Pro Max to propose information architecture, layout, UX patterns, color, typography and accessibility.
- Use Taste to challenge generic choices, develop art direction and later critique browser output.
- Reconcile their output into one token proposal. Do not retain competing palettes or type scales.
- If a skill is unavailable, state that and apply the repository's checklist; do not simulate a tool run.
- When a selected TanStack library publishes version-matched skills, consider TanStack Intent to load only the relevant package guidance. Review its permission and guidance diff before committing.

### 4. Design source

Select exactly one authoritative source per feature: Penpot, Figma or Lunacy. Inspect its relevant page, hierarchy, variables, components, assets, responsive rules and interaction states.

If the source cannot be inspected, work from supplied screenshots/specifications and mark every inference in the contract.

### 5. Component discovery

- Start with shadcn for semantic accessible primitives.
- Use Watermelon UI and 21st.dev to discover and compare candidates.
- Use React Bits through Manus when that client is available.
- Use Motion Primitives only when compatible with the selected React/Tailwind stack.
- Consider Base UI, Radix or React Aria when the selected primitive foundation does not fit; treat Mantine as an alternative complete design system, not an add-on.
- Use Storybook when reusable component variants need an inspectable catalogue and the app scaffold can support it.
- Evaluate visual authoring tools by output type: Puck for React page composition, GrapesJS for HTML/CSS builder workflows, Webstudio for a full visual website builder, and Onlook for editing a codebase visually. Select one when visual editing is a real product requirement; preserve a single source of truth.
- For internal application builders, choose Appsmith, Budibase or ToolJet for low-code visual construction, or Refine/React Admin for code-first React admin apps. Review GPL/AGPL deployment obligations and managed-service pricing.
- For workflow/diagram UI, choose React Flow for interactive graphs, Rete.js for programmable dataflow, and Excalidraw for freeform canvas/whiteboards.
- For dynamic layouts, choose React Grid Layout for dashboard widgets, dnd-kit or FormKit Drag and Drop for sortable interactions, and React Resizable Panels for split workspaces. Include keyboard operation, touch behavior, persistence rules and mobile fallbacks.
- Magic UI, daisyUI, Flowbite React, Chakra UI and MUI are component-system options; Headless UI provides unstyled accessible controls and Floating UI provides positioning. Do not combine several global systems.
- Open Props and CSS Doodle are optional CSS tools. Next.js, SvelteKit and Nuxt are alternative app frameworks; select one only after requirements are defined.
- Shortlist before retrieving source, especially with 21st.dev's limited free retrievals.
- Inspect each candidate's licence, third-party notices, dependencies, accessibility, responsive behavior and state handling.
- Record selected components and rejected alternatives in the contract.

Do not add a component because it exists. Add it because it serves an acceptance criterion.

For application behavior, select only the needed specialist: TanStack Query for remote state, TanStack Table for complex grids, React Hook Form for complex forms, Zod for runtime boundary validation, Zustand for justified shared client state, and MSW for deterministic network mocks. Recharts is an option for real data visualization, not decoration. Mock state must remain clearly separate from persistence.

### 6. Implementation and motion ownership

Implement approved project tokens before page-level polish. Adapt adopted source to those tokens.

Assign one animation owner per animated DOM target:

- CSS: simple hover/focus or local transitions.
- Motion, package motion and imports from motion/react: React state transitions, gestures, layout and enter/exit.
- GSAP: complex timelines, scroll choreography and coordinated multi-element sequences.

Motion for React is the successor to Framer Motion. Do not add both packages to a new project. Do not let GSAP and Motion animate the same target/properties. Record owners in motion_ownership.

React Spring and Anime.js are optional alternative animation engines, not defaults. Use them only when their spring/timeline model materially fits better than Motion/GSAP/CSS; preserve one owner per animated target. Use Open Props only through the project token contract.\n\nUse Haikei only for asset generation. Export, optimize and commit original assets; SVGO can optimize SVG exports and Sharp can generate raster variants when needed. dotLottie Web is an optional player for individually licensed authored animation files. Do not create runtime dependencies on the Haikei editor. Three.js/React Three Fiber/Drei and Lenis are specialist options only when explicit 3D/scroll requirements justify their performance and accessibility cost.

### 7. Browser feedback

Use Alibaba Page Agent or Playwright MCP for optional agent-driven exploration on a local/staging preview with approved scope. Select one for a given exploration pass. Chrome DevTools MCP is a separate diagnostic option for console, network and performance traces; isolate browser profiles.

Use Storybook as an optional isolated component/variant catalogue when the app has sufficient reusable components. Use Vitest and React Testing Library for unit/component tests when the selected app stack supports them. Integrate axe-core into browser/component tests for automated accessibility regression checks, but retain manual keyboard and assistive-technology review.

Use Playwright for deterministic regression tests. When several routes exist, Pa11y CI can cover a defined URL list/sitemap and Lighthouse CI can enforce performance budgets against a stable preview. CSpell may enforce terminology quality for substantial documentation. Use Taste for visual QA. Convert findings into explicit defects and update the shared contract.

### 8. Security and release

Use Strix only for authorized repository/staging scope, preferably with local Ollama and Docker. Consider Payload CMS only when structured editorial content, roles and an admin workflow require a Next.js backend; it is not a static-site default. Do not run against production or third-party targets without explicit authorization. Do not run paid hosted inference or add Strix to cloud CI.

Require applicable GitHub CI, accessibility, performance, regression and security gates. Consider OSV-Scanner for dependency advisories, Trivy for filesystem/container/SBOM/license scanning, and OWASP ZAP for a safe, explicitly authorized staging DAST scan. Do not run overlapping scanners without a clear purpose. Treat missing or skipped app-specific checks honestly.

## Conflict priority

Resolve disagreements in this order:

1. User's explicit requirements and constraints.
2. The feature's selected authoritative design source.
3. The accepted project design-token contract.
4. Existing project-owned components and accessibility rules.
5. shadcn primitive baseline.
6. Approved source-library candidates.
7. Specialist tool preferences.

A later tool may recommend changes, but it cannot silently invalidate an approved contract. Propose the change, record its reason, and update dependent artifacts together.

## Session handoff

Before ending a substantial task, update:

- feature stage and next stage
- selected design direction and tokens
- component provenance and dependency decisions
- motion owners
- data/mock/backend truth
- tool runs and connection failures
- unresolved defects and test evidence

Another client must be able to resume from the contract and GitHub files without hidden chat memory.
