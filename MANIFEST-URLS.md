# Midchat.io — URL map for plugin.json listing fields

**Domain chosen:** `midchat.io`  
**Status:** Site pack built under `sites/midchat.io/`. Domain is **not registered by this build**. Pages are **not deployed**. Do not upload Directory ZIPs until pages are live on HTTPS and placeholders in privacy and terms are filled + legally reviewed.

Every listing URL must be **HTTPS**, publicly reachable without login, ≤1024 chars, and identify the same publisher as your verified OpenAI developer identity.

Emails: `support@midchat.io` · `privacy@midchat.io`  
Publisher: Midchat (midchat.io)  
Planned MCP (PDF → Sheets only, **not live**): `https://mcp.midchat.io/mcp`

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

### BillFast (`billfast/plugin.json`) — submit skills-only after pages live

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/billfast/` |
| `supportURL` | `https://midchat.io/billfast/support/` |
| `privacyPolicyURL` | `https://midchat.io/billfast/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/billfast/terms/` |
| `homepage` (root) | `https://midchat.io/billfast/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Friday Pack (`friday-pack/plugin.json`) — submit skills-only

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/friday-pack/` |
| `supportURL` | `https://midchat.io/friday-pack/support/` |
| `privacyPolicyURL` | `https://midchat.io/friday-pack/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/friday-pack/terms/` |
| `homepage` | `https://midchat.io/friday-pack/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Action Loop (`action-loop/plugin.json`) — submit skills-only

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/action-loop/` |
| `supportURL` | `https://midchat.io/action-loop/support/` |
| `privacyPolicyURL` | `https://midchat.io/action-loop/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/action-loop/terms/` |
| `homepage` | `https://midchat.io/action-loop/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### Expense Sheet (`expense-sheet/plugin.json`) — private-test first

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/expense-sheet/` |
| `supportURL` | `https://midchat.io/expense-sheet/support/` |
| `privacyPolicyURL` | `https://midchat.io/expense-sheet/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/expense-sheet/terms/` |
| `homepage` | `https://midchat.io/expense-sheet/` |
| `author.url` | `https://midchat.io/` |
| `author.email` | `support@midchat.io` |

### PDF → Sheets (`pdf-to-sheets/plugin.json`) — **do not Directory-submit skills-only**

Wire the four site URLs into `plugin.json` for when you build the **MCP release ZIP** (via `build_with_mcp_zip.py --release`). Keep skills-only `dist/pdf-to-sheets.zip` **without** `mcp.json`.

| JSON field | URL |
| --- | --- |
| `websiteURL` | `https://midchat.io/pdf-to-sheets/` |
| `supportURL` | `https://midchat.io/pdf-to-sheets/support/` |
| `privacyPolicyURL` | `https://midchat.io/pdf-to-sheets/privacy/` |
| `termsOfServiceURL` | `https://midchat.io/pdf-to-sheets/terms/` |
| `homepage` | `https://midchat.io/pdf-to-sheets/` |
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

Patches all five `plugin.json` files (backup → `plugin.json.bak`), rebuilds skills-only `dist/<name>.zip` via `tools/build_dist.py` (**excludes** `.mcp.json` / `mcp.json` / `mcp-server/` / `submit-prep/`). PDF → Sheets stays skills-only without MCP.

---

## Trailing slashes

This static pack uses directory `index.html` URLs with trailing slashes (`/billfast/`). Most static hosts redirect both forms; prefer the trailing-slash form in manifests for consistency with this pack.
