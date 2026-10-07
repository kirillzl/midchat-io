# Midchat.io — URL map for plugin.json listing fields

**Domain:** `midchat.io` (GitHub Pages, repo `kirillzl/midchat-io`)  
**Status:** HTTPS live + Enforce HTTPS (2026-10-07). Publisher brand **Midchat**. Impressum / personal address **not published** (publisher choice).

Every listing URL must be **HTTPS**, publicly reachable without login, ≤1024 chars, and identify the same publisher as your verified OpenAI developer identity.

Emails: `support@midchat.io` · `privacy@midchat.io`  
Publisher: Midchat (midchat.io)  
Planned MCP (Vela only, **not live**): `https://mcp.midchat.io/mcp`

---

## Suite pages

| Page | URL |
| --- | --- |
| Home | `https://midchat.io/` |
| Suite privacy | `https://midchat.io/privacy/` |
| Suite terms | `https://midchat.io/terms/` |
| Suite support | `https://midchat.io/support/` |

---

## Per-plugin listing URLs → `extensions.com.openai.interface`

### Mizar (`mizar/plugin.json`) — submit skills-only after pages live

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/mizar/` |
| `supportURL` | `https://midchat.io/mizar/support/` |
| `privacyPolicyURL` | `https://midchat.io/mizar/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/mizar/terms/` |
| `homepage` (root) | `https://midchat.io/mizar/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Lyra (`lyra/plugin.json`) — submit skills-only

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/lyra/` |
| `supportURL` | `https://midchat.io/lyra/support/` |
| `privacyPolicyURL` | `https://midchat.io/lyra/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/lyra/terms/` |
| `homepage` | `https://midchat.io/lyra/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Kaus (`kaus/plugin.json`) — submit skills-only

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/kaus/` |
| `supportURL` | `https://midchat.io/kaus/support/` |
| `privacyPolicyURL` | `https://midchat.io/kaus/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/kaus/terms/` |
| `homepage` | `https://midchat.io/kaus/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Alcor (`alcor/plugin.json`) — private-test first

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/alcor/` |
| `supportURL` | `https://midchat.io/alcor/support/` |
| `privacyPolicyURL` | `https://midchat.io/alcor/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/alcor/terms/` |
| `homepage` | `https://midchat.io/alcor/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Vela (`vela/plugin.json`) — **do not Directory-submit skills-only**

Wire the four site URLs into `plugin.json` for when you build the **MCP release ZIP** (via `build_with_mcp_zip.py --release`). Keep skills-only `dist/vela.zip` **without** `mcp.json`.

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/vela/` |
| `supportURL` | `https://midchat.io/vela/support/` |
| `privacyPolicyURL` | `https://midchat.io/vela/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/vela/terms/` |
| `homepage` | `https://midchat.io/vela/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

**MCP server URL (next-steps / release ZIP only — not in skills-only package):**

| Field | URL |
| --- | --- |
| `mcp.json` server URL | `https://mcp.midchat.io/mcp` |
| Health check (once deployed) | `https://mcp.midchat.io/health` |

---

## Apply to all packages

```bash
cd /workspace/chatgpt-plugins
python3 sites/midchat.io/apply_all_urls.py
# or override:
python3 sites/midchat.io/apply_all_urls.py --domain midchat.io --email support@midchat.io
```

Patches all five `plugin.json` files (backup → `plugin.json.bak`), rebuilds skills-only `dist/<name>.zip` via `tools/build_dist.py` (**excludes** `.mcp.json` / `mcp.json` / `mcp-server/` / `submit-prep/`). Vela stays skills-only without MCP.

---

## Trailing slashes

This static pack uses directory `index.html` URLs with trailing slashes (`/mizar/`). Most static hosts redirect both forms; prefer the trailing-slash form in manifests for consistency with this pack.
