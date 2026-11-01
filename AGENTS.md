# Website development instructions

## Project state
This repository is being prepared as a website project. Do not assume a framework, package manager, or application structure until the project scaffold is selected and committed.

## Design and implementation
- Start each page or feature with a clear information hierarchy, responsive layout plan, and accessible interaction model.
- Build a coherent design system first: semantic color tokens, type scale, spacing, radii, elevation, and motion rules.
- Prefer custom, purposeful composition over generic template layouts.
- Use semantic HTML, keyboard-accessible controls, visible focus states, reduced-motion support, and responsive behavior.
- Keep components composable and source-owned. Add only dependencies required by the selected implementation.
- Do not combine multiple component libraries for the same primitive. Prefer shadcn/ui as the base primitive layer; use React Bits, Watermelon UI, Motion Primitives, and 21st.dev as selective source libraries.
- Use GSAP for complex timelines and scroll choreography. Use Motion (the current Framer Motion successor) for React component transitions and layout animation. Avoid running two animation engines on the same element.
- Use Haikei for bespoke SVG backgrounds when a page needs them; commit exported assets rather than relying on a runtime generator.

## Agent workflow
- Read relevant skill instructions before applying a specialist workflow.
- Use UI/UX Pro Max for design-system and UX guidance; Taste for art direction and visual QA; GSAP skills for advanced GSAP implementation; 21st.dev and Watermelon MCPs for source-backed component discovery.
- Inspect a component's source, dependencies, accessibility, license, and responsive behavior before adding it.
- Adapt imported components to project tokens. Do not leave demo colors or unrelated dependencies in production.
- Run type checks, lint, tests, and a production build when those scripts exist.
- Use browser-based visual checks for important responsive states.

## Security
- Never commit API keys, tokens, passwords, customer data, or environment files.
- Use GitHub Actions Secrets for CI credentials.
- Run Strix only against this repository or targets the owner has explicitly authorized. Do not add live production URLs to automated scans without explicit scope approval.
- Treat security findings as actionable evidence; verify affected code and retest fixes.

## Source-of-truth rule
The repository's design tokens and existing components take precedence over imported library defaults. Prefer editing a copied component over introducing a second competing design system.
