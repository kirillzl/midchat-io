# midchat.io — public site pack

Static HTML for the Midchat ChatGPT plugin suite. **Live on GitHub Pages** (`kirillzl/midchat-io`). HTTPS + Enforce HTTPS enabled.

## Local preview

```bash
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## Layout

- `/` — suite landing  
- `/mizar/`, `/lyra/`, `/kaus/`, `/alcor/`, `/vela/` — each with `privacy/`, `terms/`, `support/`  
- `/privacy`, `/terms`, `/support` — suite-level  
- `css/site.css` — shared styles (light, dark, and plugin accents)  
- `js/config.js` — ChatGPT directory links (empty until each app is listed)  
- `js/site.js` — theme toggle, menu, click-to-play demos  
- `assets/*.png` — plugin icons  
- `MANIFEST-URLS.md` — exact HTTPS URLs for `plugin.json`  
- `apply_all_urls.py` — patch all five manifests + rebuild `dist/*.zip`  
- `_build_site.py` — retired; it would overwrite the current pages. Edit HTML directly.

## ChatGPT links

The apps are in review, so every call to action says “Coming soon to ChatGPT” and offers the demo. When an app is in the directory, set its full https URL in `js/config.js` (`window.MIDCHAT_LINKS`). That is the only switch. Empty string keeps the coming-soon label; a URL turns it into “Open in ChatGPT”.

## Publisher / contacts

- Brand: **Midchat** (no personal name on the site)  
- `support@midchat.io`, `privacy@midchat.io`  
- Hosting: GitHub Pages  
- Impressum: not published (publisher choice)

## Before Directory submit

1. ✅ HTTPS + Enforce HTTPS confirmed.  
2. Legal pass on privacy/terms if needed.  
3. Run `python3 sites/midchat.io/apply_all_urls.py` → smoke-test plugins → Directory submit order: Mizar → Lyra → Kaus; hold Vela for MCP; private-test Alcor.  
4. Later: deploy MCP at `https://mcp.midchat.io/mcp` (see `dist/vela-mcp-next-steps.md`).

Zip of this pack: `dist/midchat-io-site.zip`.
