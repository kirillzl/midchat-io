# midchat.io — public site pack

Static HTML for the Midchat ChatGPT plugin suite. **Live on GitHub Pages** (`kirillzl/midchat-io`). HTTP serving; HTTPS cert may still be provisioning.

## Local preview

```bash
cd sites/midchat.io
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## Layout

- `/` — suite landing  
- `/billfast/`, `/friday-pack/`, `/action-loop/`, `/expense-sheet/`, `/pdf-to-sheets/` — each with `privacy/`, `terms/`, `support/`  
- `/privacy`, `/terms`, `/support` — suite-level  
- `css/site.css` — shared styles (plugin brand accents)  
- `assets/*.png` — plugin icons  
- `MANIFEST-URLS.md` — exact HTTPS URLs for `plugin.json`  
- `apply_all_urls.py` — patch all five manifests + rebuild `dist/*.zip`  
- `_build_site.py` — regenerate HTML from content (optional)

## Publisher / contacts

- Brand: **Midchat** (no personal name on the site)  
- `support@midchat.io`, `privacy@midchat.io`  
- Hosting: GitHub Pages  
- Impressum: not published (publisher choice)

## Before Directory submit

1. Confirm **HTTPS** works on midchat.io and turn on Enforce HTTPS in GitHub Pages settings.  
2. Legal pass on privacy/terms if needed.  
3. Run `python3 sites/midchat.io/apply_all_urls.py` → smoke-test plugins → Directory submit order: BillFast → Friday Pack → Action Loop; hold PDF → Sheets for MCP; private-test Expense Sheet.  
4. Later: deploy MCP at `https://mcp.midchat.io/mcp` (see `dist/pdf-to-sheets-mcp-next-steps.md`).

Zip of this pack: `dist/midchat-io-site.zip`.
