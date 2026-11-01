# Contributing

The repository is currently a tooling starter. The application framework and product requirements have not been selected yet.

## Before proposing changes

1. Read [AGENTS.md](AGENTS.md) and [the development toolkit](docs/DEVELOPMENT-TOOLKIT.md).
2. Keep every required tool and service free to use. Do not add paid API calls, subscriptions, paid assets, or paid hosting.
3. Prefer small, focused pull requests.
4. Check the license and dependencies of copied components before including them.

## Development conventions

- Use semantic HTML and accessible interaction patterns.
- Support narrow mobile layouts, keyboard navigation, visible focus, and reduced motion.
- Keep design tokens and shared components consistent.
- Use the package manager and framework already selected by the project. The current CI template expects npm and a committed package-lock.json; update the workflow deliberately if the project adopts another package manager.
- Never commit .env files, access tokens, passwords, private data, build output, or dependency folders.

## Checks

The repository runs Markdown linting, optional Node.js checks, dependency review, secret scanning, and CodeQL when applicable. Playwright tests run after a Playwright configuration is added.

Before requesting review, run the checks relevant to the files you changed and describe any checks you could not run.

## Pull requests

Include:

- What changed and why.
- Screenshots for visible UI changes.
- Accessibility and responsive behavior considered.
- Tests and build checks performed.
- Any new dependency, its purpose, and license.
