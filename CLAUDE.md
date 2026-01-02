# Personal Site

A minimal personal website built with Astro.

## Structure

```
src/
├── content/
│   └── blog/          # Blog posts as Markdown files
├── layouts/
│   └── BaseLayout.astro   # Shared page wrapper (nav, head, etc.)
├── pages/
│   ├── index.astro    # Homepage
│   ├── about.astro    # About page
│   └── blog/
│       ├── index.astro    # Blog listing (reverse chronological)
│       └── [slug].astro   # Individual post template
public/
├── styles/
│   └── global.css     # All styling lives here
└── images/            # Static images
```

## Common tasks

**Add a new blog post:**
Create a `.md` file in `src/content/blog/` with this frontmatter:
```yaml
---
title: "Post title"
date: 2026-01-15
description: "Optional short description"
---
```

**Add a new static page:**
Create a `.astro` file in `src/pages/`. Use `BaseLayout` for consistency:
```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Page Title">
  <h1>Page Title</h1>
  <p>Content here.</p>
</BaseLayout>
```
Then add a link in `src/layouts/BaseLayout.astro` nav if needed.

**Change styling:**
All styles are in `public/styles/global.css`. The file uses CSS custom properties (tokens) at the top for colors, fonts, and spacing.

**Add images:**
Put images in `public/images/` and reference them as `/images/filename.jpg` in Markdown or Astro files.

## Development

```bash
npm install      # First time only
npm run dev      # Start dev server at localhost:4321
npm run build    # Build for production
```

## Deployment

Pushes to `main` trigger GitHub Actions to deploy to GitHub Pages. Before first deploy:
1. Update `astro.config.mjs` with your GitHub username and repo name
2. In repo Settings → Pages, set source to "GitHub Actions"

## Design notes

The aesthetic is intentionally minimal—warm off-white background, restrained typography, no unnecessary decoration. When making changes, preserve this restraint. Avoid adding social icons, badges, or visual clutter.
