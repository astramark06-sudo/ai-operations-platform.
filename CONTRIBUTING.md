# Contributing

The repository is currently a tooling starter. The application framework and product requirements have not been selected yet.

## Before proposing changes

1. Read [AGENTS.md](AGENTS.md), [the development toolkit](docs/DEVELOPMENT-TOOLKIT.md), and the [design-to-code skill](.agents/skills/design-to-code/SKILL.md) when working from a visual reference.
2. Keep every required tool and service free to use. Do not add paid API calls, subscriptions, paid assets, or paid hosting.
3. Prefer small, focused pull requests.
4. Check the license and dependencies of copied components before including them.
5. Do not overwrite an existing Penpot, Lunacy, or Figma design source unless the task explicitly requires it.

## Development conventions

- Use semantic HTML and accessible interaction patterns.
- Support narrow mobile layouts, keyboard navigation, visible focus, and reduced motion.
- Keep design tokens and shared components consistent with the selected design source.
- The current Node.js CI template is npm-specific and requires a committed `package-lock.json`. Enable it only if npm is selected; configure the matching install, audit, and Dependabot behavior deliberately if another package manager is selected.
- Never commit `.env` files, access tokens, passwords, private data, build output, or dependency folders.

## Checks

The repository runs Markdown linting, optional Node.js dependency auditing, CodeQL when supported source exists, Gitleaks history scanning, and conditional Playwright tests.

Before requesting review, run the checks relevant to the files you changed and describe any checks you could not run.

## Pull requests

Include what changed and why, screenshots for visible UI changes, the design file/page used as the source of truth, accessibility and responsive behavior considered, tests/build checks performed, and any new dependency with its purpose and license.
