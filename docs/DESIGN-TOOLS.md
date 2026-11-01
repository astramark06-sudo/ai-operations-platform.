# Design tools: Penpot and Lunacy

Penpot and Lunacy are optional design applications for the website workflow. Their MCP servers let an MCP-capable coding agent inspect a real design instead of relying only on screenshots or manual descriptions.

Do not install both simply for the sake of adding dependencies. Use the application that holds the current design file. Keep this repository's zero-spend policy: no paid plugin, paid API, or hosted inference requirement.

## Penpot

Penpot is the preferred open-source design source. Its MCP integration can inspect and modify the active Penpot design file, including its pages, layers, components, styles, and design tokens.

### Hosted remote MCP

1. Open Penpot and go to **Your account → Integrations → MCP Server**.
2. Enable the MCP server. Generate an MCP key if Penpot asks for one.
3. Copy the complete server URL shown by Penpot. The URL includes the user token; treat the entire URL as a password.
4. Set the `PENPOT_MCP_URL` environment variable to that exact URL before launching the MCP client. The project-level `.mcp.json` already contains the optional `penpot` entry.
5. Restart or reload the MCP client and connect to the active Penpot file.

For a Bash session, you can set it directly without committing it:

```bash
export PENPOT_MCP_URL='PASTE_THE_COMPLETE_URL_COPIED_FROM_PENPOT'
```

If you keep it in a local `.env` file, load that file into the same shell before starting the MCP client:

```bash
set -a
source .env
set +a
```

Do not put the key in `.mcp.json`, source code, GitHub Actions, screenshots, issue comments, or commits. The `.env` file is ignored by Git.

Remote MCP availability depends on the Penpot deployment/account. If the Integrations page does not offer it, use the local option below.

### Local MCP server

Requirements: Node.js 20 or later, a local browser, and a machine that can run Penpot and the MCP process.

1. Start Penpot's local MCP package in a terminal and keep it running:

   ```bash
   npx -y @penpot/mcp@latest
   ```

2. Open a Penpot design file in the browser.
3. In Penpot, choose **Plugins → Load from URL** and enter `http://localhost:4400/manifest.json`.
4. Run the Penpot MCP plugin and select **Connect to MCP server**. Keep the plugin UI open while the agent is using it.
5. Set `PENPOT_MCP_URL=http://localhost:4401/mcp` in the environment used to launch the MCP client.

The local server's default MCP endpoint is `http://localhost:4401/mcp`. If the browser blocks local network access, allow the connection for Penpot or use a browser that permits the local connection. Start with a read-only request, such as listing pages or reading the selected frame, before asking the agent to edit a design.

Official references:
- [Penpot MCP documentation](https://help.penpot.app/mcp/)
- [Penpot MCP source and local setup](https://github.com/penpot/penpot/tree/develop/mcp)

## Lunacy

Lunacy is an optional free desktop design application for Windows, macOS, and Linux. Its MCP server runs locally alongside the native Lunacy app. It can provide access to selected design objects, color variables, components, properties, images, and other assets.

1. Install and open the native Lunacy desktop app on the same computer as the MCP-capable coding client.
2. Open the document and select the relevant artboard, layers, or objects.
3. In Lunacy, choose **AI → Model Context Protocol → MCP Server Enabled**.
4. Choose **AI → Model Context Protocol → Copy MCP Servers File** for the complete configuration, or **Copy MCP Server Entry** to copy only Lunacy's entry.
5. Merge the copied Lunacy entry into the existing `mcpServers` object in this repository's `.mcp.json`. Preserve the existing shadcn, 21st.dev, Watermelon, and Penpot entries. Do not replace the whole file with the copied Lunacy configuration.
6. Restart/reload the MCP client and keep Lunacy running while the integration is in use.

Lunacy generates the connection settings for the installed app. Use the copied configuration verbatim; do not guess a port, command, or URL.

Official references:
- [Lunacy MCP / LLM integration](https://lunacy.docs.icons8.com/mcp/)
- [Lunacy downloads](https://icons8.com/lunacy-download)
- [Lunacy system requirements](https://lunacy.docs.icons8.com/sysreq/)

## Figma through ChatGPT

Figma is an optional separate design source when the Figma app is connected to the current ChatGPT session.

- Use the connected Figma app to inspect or work with the design file the user selects.
- Treat the selected Figma file as authoritative only for that task; do not assume it is synchronized with Penpot or Lunacy.
- The ChatGPT Figma app connection is not a project MCP server and does not add a `figma` entry to `.mcp.json`.
- Figma account plans and feature limits are separate from this repository's zero-cost requirement. Do not assume paid-only features are available.

## Design-to-code workflow

When either integration is connected:

1. Confirm which application and file are authoritative for this task.
2. Inspect the selected page or artboard, hierarchy, reusable components, color and typography variables, spacing, constraints, and responsive variants.
3. Record the design system as semantic project tokens. Reuse existing repository tokens if they already match.
4. Map repeated visual patterns to reusable components before implementing individual screens.
5. Export only the assets needed by the implementation. Keep original filenames and attribution/license information where applicable.
6. Implement responsive behavior rather than copying one fixed canvas size. Preserve keyboard behavior, focus states, contrast, and reduced-motion support.
7. Compare the implementation against the reference at the important viewport sizes. Correct layout and token mismatches before adding decorative effects.
8. Do not modify the source design file unless the user asks for design edits. Ask for confirmation before destructive or broad multi-page changes.

## Device and client limitation

These integrations are not installed by committing files to GitHub. Penpot's local plugin/server workflow and Lunacy's MCP server need a computer running the relevant app; Lunacy's documented MCP server is part of its native desktop application. The `.mcp.json` file is for compatible coding clients and does not add custom MCP servers to the ChatGPT mobile app. With a phone-only setup, the repository can hold the configuration and workflow instructions, but the live local design integrations cannot be started from the GitHub repository or from GitHub Actions.
