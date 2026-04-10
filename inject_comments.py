#!/usr/bin/env python3
"""Inject Giscus comment widget into blog post HTML files after MyST build.

Before using this script, set up Giscus for your repository:
1. Visit https://giscus.app to configure Giscus
2. Update the data-repo, data-repo-id, data-category, and data-category-id below
3. Enable GitHub Discussions on your repository

Usage: python inject_comments.py
"""

from pathlib import Path

# TODO: Update these values with your Giscus configuration from https://giscus.app
GISCUS_SNIPPET = """
<script>
(function() {
  function getGiscusTheme() {
    var theme = document.documentElement.getAttribute('data-theme');
    if (!theme) {
      theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    return (theme === 'dark') ? 'dark' : 'light';
  }

  function initGiscus() {
    // Find the article content area to append comments inside it
    var article = document.querySelector('article') || document.querySelector('main');
    if (!article) return false;

    // Don't duplicate
    if (document.getElementById('giscus-comments')) return true;

    var container = document.createElement('div');
    container.id = 'giscus-comments';
    container.style.cssText = 'margin: 2rem 0; color: var(--color-text, inherit);';
    container.innerHTML = '<h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: inherit;">Comments</h2>';
    article.appendChild(container);

    var s = document.createElement('script');
    s.src = 'https://giscus.app/client.js';
    s.setAttribute('data-repo', 'username/repo');           // TODO: Update
    s.setAttribute('data-repo-id', 'R_XXXXXXXXXX');         // TODO: Update
    s.setAttribute('data-category', 'General');              // TODO: Update
    s.setAttribute('data-category-id', 'DIC_XXXXXXXXXX');   // TODO: Update
    s.setAttribute('data-mapping', 'url');
    s.setAttribute('data-strict', '0');
    s.setAttribute('data-reactions-enabled', '1');
    s.setAttribute('data-emit-metadata', '0');
    s.setAttribute('data-input-position', 'bottom');
    s.setAttribute('data-theme', getGiscusTheme());
    s.setAttribute('data-lang', 'en');
    s.setAttribute('crossorigin', 'anonymous');
    s.async = true;
    container.appendChild(s);
    return true;
  }

  // Retry until React has finished rendering the article content
  var attempts = 0;
  var timer = setInterval(function() {
    attempts++;
    if (initGiscus() || attempts > 50) clearInterval(timer);
  }, 200);

  // Update Giscus theme when the site theme toggles
  var observer = new MutationObserver(function() {
    var iframe = document.querySelector('iframe.giscus-frame');
    if (iframe) {
      iframe.contentWindow.postMessage(
        { giscus: { setConfig: { theme: getGiscusTheme() } } },
        'https://giscus.app'
      );
    }
  });
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
})();
</script>
"""


def main():
    """Inject Giscus comments into blog post HTML files."""
    build_dir = Path(__file__).parent / "_build" / "html"
    blog_dir = build_dir / "blog"

    if not blog_dir.exists():
        print(f"No blog directory found at {blog_dir}")
        return

    count = 0
    for html_file in blog_dir.rglob("*.html"):
        content = html_file.read_text(encoding="utf-8")
        if "giscus-comments" in content:
            continue
        # Insert before closing </body> tag
        if "</body>" in content:
            content = content.replace("</body>", f"{GISCUS_SNIPPET}\n</body>")
            html_file.write_text(content, encoding="utf-8")
            count += 1
            print(f"Injected comments into {html_file.name}")

    print(f"Done. Injected comments into {count} file(s).")


if __name__ == "__main__":
    main()
