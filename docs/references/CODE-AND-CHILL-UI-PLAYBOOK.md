# Code and Chill — UI reference playbook

**Research date:** 2026-11-03  
**Primary source:** https://codeandchill.store/  
**Purpose:** Public-source design and interaction research for original implementations in this repository.

## Source and reuse boundaries

The public store exposes catalogue names, product briefs, selected demo previews, advertised technology stacks, selected ZIP manifests, version histories and bundle prices. It does not expose a public AI prompt library in the pages examined. Prompts below are original prompts synthesized from public product briefs; they are not represented as the seller's prompts.

Do not copy proprietary code, paid ZIP contents, illustrations, exact page compositions, brand names, or marketing copy. Treat these products as references for design principles and interaction patterns only. The repository's zero-spend rule still applies: do not add paid templates, paid components, paid subscriptions or paid assets.

The full 2026-11-03 research files are provided separately in the conversation as a Markdown report and structured JSON catalogue. The public catalogue is changing; re-check the store before relying on prices or counts.

## Store structure and advertised terms

- [New releases](https://codeandchill.store/new)
- [Components](https://codeandchill.store/components)
- [Collections](https://codeandchill.store/collections)
- [Templates](https://codeandchill.store/templates/cirrel) (example product page)

The seller advertises one-time payments, lifetime updates, unlimited client projects, Polar checkout and a 14-day refund if a product does not work like its demo. These are seller claims, not independently verified contract terms.

The collections page advertises 114 templates ($4,628), 71 dashboards ($3,946) and 43 business dashboards ($2,496). Smaller bundles include 26 buttons ($77), 10 upload/download components ($34), seven navigation bars ($27), seven OTP/verification components ($30), nine shop templates ($410), seven SaaS/analytics dashboards ($333), and 21 finance dashboards ($1,214). The page's “35% off” header does not match the varying discounts shown beside individual bundles; use each displayed price rather than the headline sale percentage.

## Design system patterns worth learning

### Frosted-glass surfaces

Observed product directions include smoked navy/blue, warm rose/apricot, milky day, smoked night and image-backed glass. The useful pattern is layered material—not maximum blur everywhere:

1. Ambient background layer with controlled light forms or replaceable photography.
2. Main translucent application surface.
3. Elevated cards with subtly brighter edges and restrained shadows.
4. Solid or near-solid controls for dense data, forms and important actions.
5. Separate tokens for light and dark themes; remember user preference.

Legibility must take priority over the glass effect. Do not place dense tables or small text over highly variable photography without an adequate scrim or solid surface.

### Navigation and application shell

- Sidebar folds into a stable icon rail.
- Text labels fade while the rail narrows.
- Icons glide into place and retain a clear active-state marker.
- The content region changes width with the sidebar instead of jumping.
- Global search/command menu is available through Cmd+K.
- Notifications, help, profile and sign-in surfaces remain predictable.
- Phone and tablet layouts need a different navigation strategy, not a scaled-down desktop sidebar.

### Data-heavy dashboard composition

The product briefs repeatedly use a consistent information hierarchy:

- Small KPI cards at the top.
- One primary chart with meaningful date-range controls.
- A secondary queue, activity feed or alert panel.
- Dense tables/lists below, with filtering, sorting and bulk actions.
- A goal/ring indicator for a single high-level target.
- Contextual detail drawers rather than navigating away for every item.
- CSV export and clearly labelled comparison periods.

Filters should update the underlying data and all related chart/table outputs, not merely the selected control label.

### Motion and state transitions

Observed concepts include fluid toggles, physical upload progress, paper-plane send actions, delivery/checkout metaphors, animated OTP completion, drag-and-drop pipelines, morphing charts, room-aware photo transitions and scroll-driven product storytelling.

Engineering principles to carry forward:

- Animate meaningful state changes; avoid decoration with no feedback value.
- Use opacity and transforms for routine transitions where possible.
- Interpolate chart data while preserving axis/label clarity.
- Coordinate sidebar and content movement.
- Tie upload/download progress to measured bytes, never an arbitrary timer.
- Provide undo for reversible actions and confirmation for destructive/security-sensitive actions.
- Support keyboard, touch, visible focus and `prefers-reduced-motion`.
- Make animations interruptible and never delay an essential action.

## Six high-value product references

These summaries are based on public product descriptions. All six products are advertised as React/Vite/TypeScript/CSS/GSAP templates with sample data; they are not production backends.

### Cirrel — commerce operations

[Product page](https://codeandchill.store/templates/cirrel)

Frosted iPhone-style shop admin with light/dark themes. Its advertised surface includes overview KPIs, orders, a draggable packing board, catalogue and stock, analytics, customers, P&L/payouts, invoices, discounts, chat, email, settings and help. The chart changes among 7-day, 30-day, 6-month and 12-month periods. The sidebar collapses to icons; Cmd+K searches across the app. Demo data is browser-stored and must be replaced with a real store API.

Published manifest indicates a conventional separation into app shell, actions, finder, motion, router, store, page components and shared charts/format/icons. Page-specific styles cover analytics, apps, chats, customers, dashboard, discounts, email, finances, help, invoices, orders, products and settings. Version notes dated 2026-11-02 mention smoother sidebar folding and dark-by-default behavior.

### Lumelle — D2C and wholesale shop admin

[Product page](https://codeandchill.store/templates/lumelle)

Warm rose/apricot frosted glass with a bright edge treatment. Advertised modules include orders, product grid/list, inventory thresholds, customer segments, analytics, campaigns, automations, discounts, gift cards, storefront preview, point-of-sale till and wholesale deal board. The till flow includes basket, codes, card/cash, change and an on-screen receipt. Date ranges change the sales chart and sidebar folds into icons. Demo data is browser-stored; real store, payments and server integration are required.

The published manifest separates page styles and includes reusable chart, format, icon, kit and overlay modules. A 2026-11-02 update changes the default theme to dark while remembering the user's choice.

### Nimbra — SaaS revenue and retention

[Product page](https://codeandchill.store/templates/nimbra)

Frosted navy over blue light, with light mode and adjustable glass strength. Advertised modules include MRR by plan, new/churned revenue, NRR, trial-to-paid funnels, cohort retention, reports, rule-based insights, account health, segments, activity, integrations, automations, campaigns, teams and billing. Its question box uses keyword rules, not an AI model. Demo data is browser-stored; billing/product data and a server must be connected.

Its manifest separates pages for accounts, activity, automations, billing, campaigns, cohorts, funnels, insights, integrations, overview, reports, segments, settings, teams and users, plus shared shell/motion/store/UI modules.

### Nestra — smart-home control

[Product page](https://codeandchill.store/templates/nestra)

Frosted glass over room photographs, with a milky day theme and smoked night theme. Advertised pages cover home, rooms, devices, climate, energy, security, scenes, automations, media, family, settings and help. Interactions include a draggable thermostat dial, weekly heating schedule, room-aware backgrounds, energy charts, device sheets, PIN alarm, guest access and music queue. Demo data only; no real devices or backend. The voice card uses preset replies, not a connected voice-AI system.

### Halvo — room-based smart home

[Product page](https://codeandchill.store/templates/halvo)

Room photo backgrounds, tick-ring thermostat with half-degree increments, day/week/month/year energy views, device search/filter/detail sheets, weekly heating plan, air quality, solar/battery, cameras, locks, scenes with undo, routines, room-based music and family/guest controls. Demo data only; a real hub, devices and server are needed.

### Sorvo — creator studio

[Product page](https://codeandchill.store/templates/sorvo)

Frosted panels over selectable photo wallpapers, with adjustable blur. Advertised modules include channel overview, videos/Shorts/playlists, audience analytics, hourly/day heatmap, retention curve, upload calendar, drag-and-drop pipeline, earnings by source, payouts, sponsorship pipeline, comment moderation, memberships, merch and fulfilment. The retention curve is inspectable by pointer position. Demo data and browser persistence only; real platform data and authentication are required.

## Component ideas from the catalogue

The indexed components catalogue includes patterns such as:

- Liquid/glass toggles and tab markers.
- Stretching or electrically jumping navigation indicators.
- Search icon expanding into a search field.
- Send button folding into a paper plane.
- Upload button whose arrow becomes a liquid level.
- Download outline/fill becoming the progress indicator.
- Cart/checkout actions that transform into a bag, parcel or vehicle.
- OTP fields that fold, spin, seal or unlock on completion.
- Password-strength controls with an expressive growth metaphor.
- Search, volume, mood and spice sliders with visual feedback.
- 3D team/product cards and swipeable galleries.
- Playful 404 pages and seasonal/interactive scenes.

The catalogue is useful as a source of interaction concepts; implement original, accessible variants rather than copying a paid component.

## Original prompts for implementation

These are reusable prompts derived from the observed public design briefs.

### 1. Frosted-glass design system

> Design an original production-oriented web application for [product]. Use restrained frosted glass: an ambient background, translucent panels with controlled blur, thin edge highlights, subtle depth and strong readable contrast. Define semantic tokens for colour, typography, spacing, radius, borders, shadows, blur and motion before building pages. Provide light and dark themes with saved preference. Use solid surfaces for dense tables and forms. Support mobile, tablet and desktop. Do not copy any existing site's branding, copy, exact layout, illustration or assets.

### 2. Commerce operations dashboard

> Build an original commerce admin for [store type]. Include overview KPIs, date-filtered sales chart, order queue, low-stock alerts, best sellers, orders with filters/bulk actions, fulfilment board, returns, product catalogue and inventory thresholds, customers/segments, finance, invoices, discounts, campaigns, messages, storefront preview, settings and help. Make all filters update real local demo data. Add CSV export, undo for reversible actions, collapsible sidebar, command search and responsive navigation. Mark sample data; isolate store/payment/server adapters. Use React and TypeScript; use GSAP only for coordinated timelines.

### 3. SaaS revenue analytics

> Build a SaaS metrics console with MRR by plan, new/churned revenue, NRR, conversion funnel, cohort retention, account health, segments, activity, report builder, integrations, automation rules, campaigns, teams and billing. Filters must change data. Define units and comparison periods. Do not label keyword rules as AI. Clearly label demo data and create integration boundaries for billing and product analytics. Use a refined frosted-navy theme with a usable light mode.

### 4. Smart-home controller

> Design an original smart-home app for one household. Include room-aware overview, device catalogue and control sheets, climate dial, weekly heating schedule, energy/solar/battery, security, scenes, automations, media, household and settings. Support pointer, touch and keyboard for every control. Show connectivity and last-seen state. Confirm or provide undo for sensitive actions. Mark mock devices until a real hub/API is connected.

### 5. Creator studio

> Build a creator studio with content library, per-video detail drawer, audience analytics, inspectable retention curve, heatmap, publishing calendar, drag-and-drop pipeline, revenue by source, payouts, sponsors, comments moderation, memberships, merch and order fulfilment. Clearly separate sample metrics from platform integrations and authentication. Use an editorial frosted-glass visual system with accessible data density.

### 6. Meaningful micro-interaction

> Design one original [control/action] interaction. Specify idle, hover/focus, pressed, pending/progress, success and error states. Animation must explain state, not decorate it. Tie visual progress to the real operation. Include keyboard, touch, disabled, error-recovery and reduced-motion behavior, plus text status and focus management. Use CSS/SVG/Canvas only where justified.

### 7. Upload/download control

> Create an upload/download control that reflects measured bytes. Include queued, transferring, paused, completed, cancelled and failed states. Announce progress accessibly, expose byte count and percentage, support retry/cancel, prevent double submission and show a clear result. On reduced-motion or low-power devices, use a simple progress bar with identical information. Never fake progress using a timer.

### 8. OTP verification

> Build accessible one-time-code verification with [N] digits. Support paste, auto-advance, backspace, keyboard navigation, screen-reader announcements, mobile autofill and resend behavior. Validate through the supplied callback/API. Provide pending, invalid, expired and success states. Do not expose codes in logs or analytics. Include a reduced-motion path.

### 9. Scroll-driven landing page

> Create an original editorial landing page for [product] with a strong hero, concise value proposition, product visual, proof, use cases and clear conversion action. Use scroll motion only to explain the product story. Avoid scroll-jacking, autoplay audio and excessive parallax. Preserve semantic structure, keyboard navigation, reduced-motion behavior and mobile performance. Create original copy and imagery.

### 10. UI-reference-to-implementation

> Analyze the supplied UI reference and extract principles only: information architecture, components, design tokens, responsive behavior, state machines, motion triggers, accessibility, data contracts and tests. Do not reproduce the brand, exact composition, copy, illustration or proprietary assets. Implement an original version in [framework] with separated page, data, shared UI and motion layers. Label observed facts, inferred behavior and unresolved decisions.

### 11. Design and motion audit

> Audit this interface for hierarchy, contrast on glass, visible focus, keyboard/touch operation, reduced motion, chart readability, loading/empty/error states, responsive overflow, layout shifts and performance. Prioritize evidence-backed fixes. Reduce large blur regions and perpetual animations. Ensure filters update dependent charts and tables together.

### 12. Sample-data/backend handoff

> Classify every displayed value or interaction as static sample, browser-persisted state, deterministic local behavior, API-backed data or real-time data. Mark demo values. Create typed adapters for [commerce/billing/devices/messaging/analytics/auth]. Never claim an external action succeeded before the adapter confirms it. Add loading, stale, error and empty states, validation and tests. Preserve the UI while replacing sample stores with real adapters.

## Implementation rules for this repository

1. This reference does not select the project's framework or product concept. Follow the repository's existing decision process.
2. Use free/open-source implementations only. Do not buy the referenced components or templates.
3. Build one interaction at a time and test it.
4. Keep sample data and integrations separate.
5. Test keyboard, touch, reduced motion, responsive layouts, empty/error/loading states and performance.
6. Prefer CSS for simple transitions; use GSAP for complex timelines; do not run two animation engines on the same element.
7. Keep large blur/filter regions limited to avoid GPU and text-rendering costs.

## Public source index

- https://codeandchill.store/
- https://codeandchill.store/new
- https://codeandchill.store/components
- https://codeandchill.store/collections
- https://codeandchill.store/templates/cirrel
- https://codeandchill.store/templates/lumelle
- https://codeandchill.store/templates/nimbra
- https://codeandchill.store/templates/nestra
- https://codeandchill.store/templates/halvo
- https://codeandchill.store/templates/sorvo
