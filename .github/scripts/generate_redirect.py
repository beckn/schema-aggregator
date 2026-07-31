#!/usr/bin/env python3
"""
Writes a root index.html that redirects to the schema browser, so GitHub
Pages' root URL lands somewhere useful instead of 404ing.

Reads the target from the SCHEMA_BROWSER_URL env var (backed by the
`SCHEMA_BROWSER_URL` repository Actions variable) rather than hardcoding
it, so the target can change without a code edit -- just update the
variable and re-run this workflow.
"""

import html
import os
import sys

REPO_ROOT = os.getcwd()

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting to the schema browser</title>
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
<script>window.location.replace("{js_url}");</script>
</head>
<body>
<p>Redirecting to the <a href="{url}">schema browser</a>.</p>
</body>
</html>
"""


def main():
    url = os.environ.get("SCHEMA_BROWSER_URL", "").strip()
    if not url:
        print(
            "SCHEMA_BROWSER_URL is not set -- refusing to publish a broken redirect. "
            "Set the 'SCHEMA_BROWSER_URL' repository variable (Settings -> Secrets and "
            "variables -> Actions -> Variables) and re-run this workflow.",
            file=sys.stderr,
        )
        sys.exit(1)

    escaped = html.escape(url, quote=True)
    js_escaped = url.replace("\\", "\\\\").replace('"', '\\"')

    content = TEMPLATE.format(url=escaped, js_url=js_escaped)
    with open(os.path.join(REPO_ROOT, "index.html"), "w") as f:
        f.write(content)

    print(f"Wrote index.html redirecting to {url}")


if __name__ == "__main__":
    main()
