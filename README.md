# midchat.io — public site pack

Static HTML for the Midchat ChatGPT plugin suite. **Domain not registered by this build. Not deployed.**

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

## Placeholders to fill before publish

- `[PUBLISHER NAME]` (privacy/terms)  
- `[DATE OF PUBLICATION]`  
- `[HOSTING PROVIDER …]` + privacy link  
- Legal review of privacy and terms (not legal advice)

Contacts already set: `support@midchat.io`, `privacy@midchat.io`.

## Before going live

1. Register **midchat.io** (and optionally email / Google Workspace for the two inboxes).  
2. Point DNS to a static host (Cloudflare Pages, Netlify, Vercel, or similar) in an EU-friendly setup if possible.  
3. Fill placeholders → legal pass → deploy this folder as the site root.  
4. Open every URL in a private window (HTTPS, no login).  
5. Run `python3 sites/midchat.io/apply_all_urls.py` (if not already) → smoke-test plugins → Directory submit order: BillFast → Friday Pack → Action Loop; hold PDF → Sheets for MCP; private-test Expense Sheet.  
6. Later: deploy MCP at `https://mcp.midchat.io/mcp` (see `dist/pdf-to-sheets-mcp-next-steps.md`).

Zip of this pack: `dist/midchat-io-site.zip`.
