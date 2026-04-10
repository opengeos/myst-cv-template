---
title: "Getting Started with MyST Markdown for Academic Websites"
date: 2026-04-01
authors:
  - name: Jane Doe
    email: jane.doe@example.com
description: A guide to building academic websites with MyST Markdown, including CV PDF generation, blog support, and automated deployment.
tags:
  - MyST Markdown
  - GitHub Pages
  - Academic Website
keywords:
  - MyST Markdown
  - GitHub Pages
  - Academic Website
  - CV PDF
---

# Getting Started with MyST Markdown for Academic Websites

Building an academic website can be time-consuming, but [MyST Markdown](https://mystmd.org) makes it straightforward. This template provides everything you need to get started: a clean layout, automatic CV PDF generation, blog support with RSS feeds, and automated deployment via GitHub Actions.

## Why MyST Markdown?

MyST Markdown extends standard Markdown with features that are particularly useful for academic and technical content:

- **Rich content**: grids, cards, dropdowns, tables, and more
- **Citations and references**: BibTeX support built in
- **Code execution**: integrate Jupyter notebooks directly
- **Multiple output formats**: HTML, PDF, and more from the same source

## Quick Start

1. Click **Use this template** on GitHub to create a new repository
2. Update `myst.yml` with your site title and information
3. Replace placeholder content in `pages/` with your own
4. Push to GitHub to trigger automated builds

## CV PDF Generation

One of the key features of this template is automatic CV generation. The `generate_cv.py` script reads your website's markdown files and generates a professional PDF using [Typst](https://typst.app/) and the [modern-cv](https://typst.app/universe/package/modern-cv/) package. This means your CV stays in sync with your website content automatically.

## Blog Support

The template includes a blog system with:

- Individual post pages in the `blog/` directory
- RSS and Atom feed generation via `generate_rss.py`
- Optional Giscus comments (GitHub-backed)

## Deployment

Pushes to `main` automatically build and deploy your site to GitHub Pages. Pull requests get preview deployments via Netlify.

## Learn More

- [MyST Markdown documentation](https://mystmd.org)
- [Typst documentation](https://typst.app/docs)
- [GitHub Pages documentation](https://docs.github.com/en/pages)
