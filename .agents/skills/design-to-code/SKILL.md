---
name: design-to-code
description: Use when implementing, reviewing, or documenting a website UI based on a Penpot or Lunacy design file, design tokens, component library, or exported assets.
---

# Design-to-code workflow

Use this skill when the task depends on a visual design source. Read the repository's `AGENTS.md` and `docs/DESIGN-TOOLS.md` first.

## 1. Establish the source of truth

- Ask which source file is authoritative only when the conversation does not already establish it.
- Use the connected Penpot or Lunacy MCP server when available.
- Do not assume Penpot and Lunacy contain synchronized copies of the same design.
- If no MCP connection exists, work from supplied screenshots, exported assets, design specs, or explicit descriptions. State which evidence you used.

## 2. Inspect before implementing

Inspect the relevant page/artboard and its hierarchy. Record:

- Frame dimensions and intended responsive breakpoints.
- Layout method, constraints, alignment, and spacing.
- Color variables, typography styles, radii, borders, shadows, and effects.
- Reusable components, variants, states, and naming conventions.
- Image, icon, and illustration assets, including export formats and licenses.
- Interaction states, transitions, keyboard behavior, and reduced-motion expectations.

Do not infer missing states or responsive layouts as facts. Mark those decisions as implementation assumptions.

## 3. Create a design handoff

Summarize the design as:

- Semantic token map (for example, surface, text, border, accent, spacing, radius, and type roles).
- Component inventory and variant map.
- Page structure and responsive behavior.
- Asset list with source paths and intended use.
- Interaction and accessibility requirements.
- Any unresolved visual ambiguities.

Prefer existing repository conventions over importing a second design system.

## 4. Implement

- Build semantic, responsive HTML and composable components.
- Use the project's established primitive layer first; prefer shadcn/ui when the project has adopted it.
- Reuse design tokens rather than scattering raw values throughout the code.
- Import only the assets and packages required by the task.
- Inspect third-party component code, dependencies, accessibility, license, and responsive behavior before adopting it.
- Do not introduce paid packages, Pro-only assets, API credits, or hosted inference.
- Do not add a framework or build stack before the project scaffold has been selected.

## 5. Validate

- Compare the implementation to the selected source at relevant viewport sizes.
- Check responsive reflow, text wrapping, spacing, typography, contrast, focus visibility, keyboard access, and reduced-motion behavior.
- Run the repository's available checks; do not claim tests passed unless they were run.
- List any deliberate deviations from the source and explain why they were necessary.

## 6. Protect the design source and credentials

- Do not edit or delete source design elements unless explicitly asked.
- Confirm before broad or destructive design-file changes.
- Treat Penpot MCP URLs/keys as secrets. Never commit them, print them in logs, or put them in generated documentation.
- Use the user's selected file/page as the boundary for inspection and changes.
