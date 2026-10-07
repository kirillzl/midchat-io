#!/usr/bin/env python3
"""Generate the midchat.io static site pages. Run from sites/midchat.io/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOMAIN = "midchat.io"
BASE = f"https://{DOMAIN}"
SUPPORT_EMAIL = "support@midchat.io"
PRIVACY_EMAIL = "privacy@midchat.io"
PUBLISHER = "Midchat"
HOST_NAME = "GitHub Pages"
HOST_PRIVACY = "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement"
RETENTION = "12 months after the support request is closed"
PUBLICATION_DATE = "6 October 2026"
DRAFT_BANNER = (
    '<p class="draft-banner"><strong>Live site — legal review recommended.</strong> '
    "Not legal advice; have privacy and terms reviewed for your jurisdiction.</p>"
)

PLUGINS = [
    {
        "slug": "billfast",
        "name": "BillFast",
        "tagline": "Notes in. Invoice out.",
        "short": "Notes to invoice PDF",
        "color": "#003DBC",
        "color_dark": "#8CA7E0",
        "icon": "billfast.png",
        "kind": "skills-only",
        "submit": "Submit skills-only now",
        "blurb": (
            "Paste notes, hours, or a timesheet into ChatGPT. BillFast turns them into a clean, "
            "tax-ready invoice — exact totals, VAT per rate, English or German."
        ),
        "bullets": [
            ("From messy notes to line items", "Workshop prep 4h, workshop 6h becomes a proper table."),
            ("Asks, never guesses", "Missing rate, tax number, or IBAN? One checklist. No made-up numbers."),
            ("Exact math", "Net, VAT per rate, discounts, total — to the cent."),
            ("English or German", "Invoice or Rechnung, your choice."),
            ("Draft-safe", "Missing fields stay as visible [PLACEHOLDER] on a DRAFT."),
        ],
        "steps": [
            "Paste notes, hours, or upload a timesheet CSV.",
            "Confirm the draft table and totals.",
            "Download the invoice (PDF where ChatGPT can run code, print-ready otherwise).",
        ],
        "prompts": [
            "Create an invoice from these notes",
            "Turn this timesheet into an invoice with 19% VAT",
            "Generate an invoice PDF for this client",
            "Rechnung auf Deutsch mit 19 % MwSt",
        ],
        "example": (
            "Acme GmbH · 12 h × €110 · 19 % VAT · due in 14 days<br>"
            "<strong>Net €1,320.00 · VAT €250.80 · Total €1,570.80</strong>"
        ),
        "limitations": [
            "PDF file only where ChatGPT can run code; otherwise print-ready invoice in chat.",
            "No memory across chats — client defaults aren't saved between conversations.",
            "Does not send invoices, take payments, or connect to accounting/banking tools.",
            "Human-readable invoice, not XRechnung/ZUGFeRD e-invoice.",
            "Not tax advice — does not choose your VAT rate or tax status.",
        ],
        "privacy_extra": (
            "When you use BillFast you may paste or upload work notes, hours, timesheets (e.g. CSV), "
            "and invoice details such as names, addresses, VAT IDs/tax numbers, and bank details (IBAN). "
            "BillFast's instructions tell ChatGPT to structure that into line items, calculate totals and VAT, "
            "and produce an invoice (PDF/HTML where ChatGPT can run code, otherwise a print-ready text block). "
            "BillFast does <strong>not</strong> send invoices, contact clients, take payments, or connect to accounting or banking tools."
        ),
        "future_mcp": (
            "We may later offer a separate hosted version (e.g. “BillFast Pro”) that renders invoice PDFs "
            "on our own server. That is not part of BillFast today. If it launches, it will have its own "
            "listing and this policy will be updated before launch."
        ),
        "terms_what": (
            "BillFast helps you turn notes, hours, or timesheets into a draft invoice: it structures line items, "
            "asks for missing details, computes totals and VAT from the figures you give, and renders a one-page "
            "invoice in English or German."
        ),
        "terms_you": [
            "BillFast produces <strong>drafts</strong>. Check every invoice — amounts, tax rates, invoice numbers, dates, names, addresses, VAT IDs, bank details — before you send it.",
            "BillFast does <strong>not</strong> provide tax, legal, or accounting advice and does not decide your tax status or VAT rate.",
            "BillFast produces a human-readable invoice, <strong>not</strong> a structured e-invoice (e.g. XRechnung/ZUGFeRD).",
            "BillFast does not send invoices, collect payments, or file anything with authorities.",
        ],
        "support_how": (
            "<ol>"
            "<li>Reads your notes and proposes line items.</li>"
            "<li>Asks for anything missing (rates, tax rate, invoice number, addresses, bank details) in one checklist.</li>"
            "<li>Shows a draft table for you to confirm.</li>"
            "<li>Calculates net, VAT per rate, discounts, and total to the cent.</li>"
            "<li>Renders the invoice in English or German.</li>"
            "</ol>"
            "<p>It <strong>never invents</strong> amounts, hours, tax rates, invoice numbers, VAT IDs, IBANs, or addresses. "
            "Missing fields stay as visible placeholders like <code>[IBAN]</code> and the invoice is marked <strong>DRAFT</strong>.</p>"
        ),
        "troubleshoot": [
            ("No PDF appeared", "Ask “render it as a PDF file”. If code execution isn't available, use the print-ready version."),
            ("Totals look wrong", "Ask “show the math”. BillFast rounds per line, then tax per rate group."),
            ("Keeps asking questions", "Deliberate for required fields. Say “make it a DRAFT with placeholders” to proceed."),
            ("Didn't activate", "Mention BillFast directly or start with “Create an invoice from…”."),
        ],
    },
    {
        "slug": "friday-pack",
        "name": "Friday Pack",
        "tagline": "Raw notes → client-ready Friday status.",
        "short": "Weekly client status packs",
        "color": "#E38217",
        "color_dark": "#F2C696",
        "icon": "friday-pack.png",
        "kind": "skills-only",
        "submit": "Submit skills-only now",
        "blurb": (
            "Paste bullets, notes, or a metrics CSV. Get a short client email plus a one-pager with wins, "
            "progress, blockers, risks, and next steps. Tone: direct, no fluff."
        ),
        "bullets": [
            ("Email + one-pager", "Client-ready copy and a structured status in one pass."),
            ("Wins, risks, next steps", "The sections stakeholders actually read."),
            ("Never invents metrics", "Asks when owners, dates, or numbers are missing."),
            ("No auto-send", "You copy and send yourself."),
        ],
        "steps": [
            "Paste this week's notes, bullets, or metrics.",
            "Confirm audience, tone, and anything missing.",
            "Copy the email draft and one-pager into your tools.",
        ],
        "prompts": [
            "Write a weekly status report for the client from these notes",
            "Turn this update into a client email",
            "Friday status report — include risks and next steps",
        ],
        "example": (
            "Subject: Week of Oct 6 — Acme redesign<br>"
            "Wins · Progress · Blockers · Risks · Next steps — then a 5-line email."
        ),
        "limitations": [
            "Does not invent metrics, owners, or dates.",
            "Does not send email or post to Slack.",
            "No memory across chats.",
            "Skills-only — no external integrations.",
        ],
        "privacy_extra": (
            "When you use Friday Pack you may paste project notes, client names, metrics, and stakeholder details. "
            "Processing stays inside ChatGPT. Friday Pack does not send email or post messages."
        ),
        "future_mcp": "No hosted MCP version is planned for Friday Pack.",
        "terms_what": (
            "Friday Pack drafts weekly client status packs: a short email and a one-pager with wins, progress, "
            "blockers, risks, and next steps from notes or metrics you provide."
        ),
        "terms_you": [
            "Outputs are <strong>drafts</strong>. Verify facts, names, and metrics before sending to a client.",
            "Friday Pack does not provide project-management or legal advice.",
            "Friday Pack does not send messages on your behalf.",
        ],
        "support_how": (
            "<ol>"
            "<li>Structures your notes into wins, progress, blockers, risks, and next steps.</li>"
            "<li>Asks once for missing owners, dates, or metrics.</li>"
            "<li>Produces a client email draft and a one-pager.</li>"
            "</ol>"
        ),
        "troubleshoot": [
            ("Invented a metric", "That shouldn't happen — ask it to remove invented numbers and flag gaps."),
            ("Wrong tone", "Say “more direct / more formal / shorter”."),
            ("Didn't activate", "Start with “Friday status report” or “weekly client update”."),
        ],
    },
    {
        "slug": "action-loop",
        "name": "Action Loop",
        "tagline": "Meeting dump → owners, deadlines, follow-ups.",
        "short": "Meeting notes to next steps",
        "color": "#3B3FBC",
        "color_dark": "#A6A8E0",
        "icon": "action-loop.png",
        "kind": "skills-only",
        "submit": "Submit skills-only now",
        "blurb": (
            "Paste meeting notes or a transcript. Get a table of owner / action / due date / source quote, "
            "plus draft Slack or email follow-ups you send yourself."
        ),
        "bullets": [
            ("Action table", "Owner, action, due date, and a source quote for each item."),
            ("Flags ambiguity", "Missing owners and vague commitments stay visible."),
            ("Draft follow-ups", "Slack or email text ready to paste."),
            ("No auto-send", "You stay in control of every message."),
        ],
        "steps": [
            "Paste notes or a transcript.",
            "Review the action table and ambiguity flags.",
            "Copy follow-ups into Slack, email, or your tracker.",
        ],
        "prompts": [
            "Extract action items from this meeting",
            "Turn this transcript into next steps",
            "Draft follow-ups from this call",
        ],
        "example": (
            "Owner · Action · Due · Quote<br>"
            "Alex · Send revised quote · Fri · “I'll send the quote by Friday”"
        ),
        "limitations": [
            "Does not invent owners or deadlines.",
            "Does not auto-send messages or create calendar events.",
            "No memory across chats.",
            "Skills-only — no CRM or calendar integrations.",
        ],
        "privacy_extra": (
            "When you use Action Loop you may paste meeting notes, transcripts, names, and commitments. "
            "Processing stays inside ChatGPT. Action Loop does not send messages or create calendar events."
        ),
        "future_mcp": "No hosted MCP version is planned for Action Loop.",
        "terms_what": (
            "Action Loop extracts action items from meeting notes or transcripts into a table with owners and "
            "due dates, and drafts follow-up messages for you to send."
        ),
        "terms_you": [
            "Outputs are <strong>drafts</strong>. Verify owners, deadlines, and wording before acting.",
            "Action Loop does not create calendar events or send messages.",
            "Don't paste transcripts you aren't allowed to process.",
        ],
        "support_how": (
            "<ol>"
            "<li>Extracts commitments with owner / action / due / source quote.</li>"
            "<li>Flags missing owners and vague language.</li>"
            "<li>Drafts follow-up Slack or email text.</li>"
            "</ol>"
        ),
        "troubleshoot": [
            ("Wrong owner", "Correct it in chat; Action Loop should not invent names."),
            ("No due dates", "It leaves due blank when the transcript doesn't say — that's intentional."),
            ("Didn't activate", "Start with “extract action items from this meeting”."),
        ],
    },
    {
        "slug": "expense-sheet",
        "name": "Expense Sheet",
        "tagline": "Receipts in. Expense sheet out.",
        "short": "Receipts to expense sheet",
        "color": "#8331E5",
        "color_dark": "#C7A2F3",
        "icon": "expense-sheet.png",
        "kind": "skills-only (verify first)",
        "submit": "Private-test receipts before Directory submit",
        "blurb": (
            "Attach receipt photos or PDFs. Get one row per receipt with date, merchant, gross, VAT, net, "
            "currency, and category — plus a review list before export."
        ),
        "bullets": [
            ("One row per receipt", "Date, merchant, gross, VAT rate/amount, net, currency, category."),
            ("Review before export", "Unreadable fields, uncertain categories, possible duplicates."),
            ("CSV or Excel", "Standard or German semicolon CSV; Excel where ChatGPT can run code."),
            ("Never estimates amounts", "Unreadable values stay empty and flagged."),
        ],
        "steps": [
            "Attach receipt photos or PDFs.",
            "Review the table and flags.",
            "Export CSV or Excel (or copy-paste CSV if no code execution).",
        ],
        "prompts": [
            "Turn these receipts into a spreadsheet",
            "Expense report from these photos",
            "Prepare these expenses for my accountant as CSV",
        ],
        "example": (
            "12 receipts → review table → totals by category → "
            "<code>expenses.csv</code> ready for your bookkeeper."
        ),
        "limitations": [
            "Receipt values are read by ChatGPT vision in this version — verify before filing (not a dedicated OCR engine).",
            "Unreadable amounts stay empty and flagged, never estimated.",
            "Downloadable file only where ChatGPT can run code; otherwise copy-paste CSV.",
            "Does not sync to accounting software, submit claims, produce DATEV, or advise on deductibility.",
        ],
        "privacy_extra": (
            "When you use Expense Sheet you may upload receipt photos or PDFs that can include merchant names, "
            "amounts, VAT, card fragments, and addresses. Processing stays inside ChatGPT for the skills-only "
            "version. Expense Sheet does not sync to accounting tools or submit claims."
        ),
        "future_mcp": (
            "A future hosted version may use a dedicated OCR engine. That is not part of Expense Sheet today. "
            "If it launches, it will be a separate listing and this policy will be updated before launch "
            "(EU hosting, no training on your receipts, short retention for generated files)."
        ),
        "terms_what": (
            "Expense Sheet organizes receipt photos or PDFs into an expense spreadsheet with categories, "
            "VAT split, and export to CSV or Excel."
        ),
        "terms_you": [
            "Outputs are for your review. Verify every amount and category before filing or claiming.",
            "Expense Sheet does not advise on tax deductibility or produce DATEV imports.",
            "Receipt reading in this version uses ChatGPT vision — treat values as unverified until you check them.",
        ],
        "support_how": (
            "<ol>"
            "<li>Reads each receipt into a structured row.</li>"
            "<li>Assigns one of 8 categories; flags uncertain ones.</li>"
            "<li>Shows a review list (unreadable fields, duplicates).</li>"
            "<li>Exports CSV (standard or DE) or Excel where possible.</li>"
            "</ol>"
        ),
        "troubleshoot": [
            ("Wrong amount", "Correct in chat; never trust unverified vision reads for filing."),
            ("Empty fields", "Intentional when unreadable — re-photo or type the value."),
            ("No Excel file", "Ask for CSV, or use copy-paste if code execution isn't available."),
        ],
    },
    {
        "slug": "pdf-to-sheets",
        "name": "PDF → Sheets",
        "tagline": "PDF tables → Excel or CSV.",
        "short": "PDF tables to Excel or CSV",
        "color": "#058578",
        "color_dark": "#8EC8C2",
        "icon": "pdf-to-sheets.png",
        "kind": "hold for MCP",
        "submit": "Do not submit skills-only — burns the Directory name before MCP",
        "blurb": (
            "Attach a PDF. Get every table in source order with cleaned headers, ISO dates, plain decimals, "
            "a preview, and a totals check. Multi-page tables are stitched."
        ),
        "bullets": [
            ("All tables, in order", "Stitched multi-page tables, repeated headers removed."),
            ("Clean types", "ISO dates, plain-decimal amounts, cleaned headers."),
            ("Honest gaps", "Unreadable cells stay empty and flagged — never guessed."),
            ("Excel or CSV", "Download where available; otherwise copy-paste CSV."),
        ],
        "steps": [
            "Attach the PDF and say Excel or CSV.",
            "Review the preview and totals check.",
            "Download or copy the export.",
        ],
        "prompts": [
            "Convert this PDF to Excel",
            "Extract the tables from this PDF as CSV",
            "Turn this bank statement PDF into a spreadsheet",
        ],
        "example": (
            "Bank statement PDF → 3 tables stitched → "
            "<code>statement.xlsx</code> with ISO dates and plain amounts."
        ),
        "limitations": [
            "Skills-only version: text PDFs OK; scanned PDFs without a text layer are reported, not OCR'd.",
            "Unreadable cells left empty and flagged.",
            "Downloadable file only where ChatGPT can run code.",
            "Does not edit/merge PDFs, convert to Word, or give tax/accounting advice.",
            "Public Directory listing is planned only with the hosted MCP server — do not submit skills-only.",
        ],
        "privacy_extra": (
            "When you use PDF → Sheets you may upload PDFs that contain bank statements, invoices, or reports. "
            "In the current skills-only package, processing stays inside ChatGPT. "
            "A future hosted MCP version will download PDFs from ChatGPT, process them in memory on an EU server, "
            "<strong>not store</strong> the source PDF, and delete generated exports within 24 hours. "
            "That hosted version is not live yet; when it is, this policy will be updated before launch."
        ),
        "future_mcp": (
            "Planned MCP endpoint: <code>https://mcp.midchat.io/mcp</code> (not live). "
            "EU hosting, one instance, no OCR vendor in the first MCP release unless separately disclosed. "
            "Submitting a skills-only Directory listing first would prevent adding MCP to the same listing — "
            "so PDF → Sheets will launch publicly only with MCP."
        ),
        "terms_what": (
            "PDF → Sheets extracts tables from PDFs into Excel or CSV, with multi-page stitching, "
            "type normalization, and honest flags for unreadable cells."
        ),
        "terms_you": [
            "Outputs are for your review. Verify extracted numbers before relying on them.",
            "PDF → Sheets does not give tax or accounting advice.",
            "Don't upload documents you aren't allowed to process.",
            "The skills-only package is for private testing; the public listing is planned with MCP.",
        ],
        "support_how": (
            "<ol>"
            "<li>Detects tables in source order.</li>"
            "<li>Stitches multi-page tables and removes repeated headers.</li>"
            "<li>Normalizes dates and amounts; shows a preview and totals check.</li>"
            "<li>Exports Excel or CSV (or chat CSV fallback).</li>"
            "</ol>"
            "<p><strong>Scanned PDFs:</strong> without a text layer, the skills-only version reports that "
            "OCR isn't available rather than guessing.</p>"
        ),
        "troubleshoot": [
            ("No tables found", "Confirm the PDF has a text layer; scans need the future MCP/OCR path."),
            ("Wrong columns", "Ask to re-detect with a bank-statement or invoice-lines preset."),
            ("No Excel file", "Ask for CSV, or wait for the hosted MCP export links."),
        ],
    },
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def head(title: str, description: str, accent: str = "#0f172a") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · Midchat</title>
<meta name="description" content="{esc(description)}">
<link rel="stylesheet" href="/css/site.css">
<style>:root {{ --accent: {accent}; }}</style>
</head>
<body>
"""


def nav(active: str = "") -> str:
    items = [
        ("/", "Home", "home"),
        ("/billfast/", "BillFast", "billfast"),
        ("/friday-pack/", "Friday Pack", "friday-pack"),
        ("/action-loop/", "Action Loop", "action-loop"),
        ("/expense-sheet/", "Expense Sheet", "expense-sheet"),
        ("/pdf-to-sheets/", "PDF → Sheets", "pdf-to-sheets"),
        ("/support/", "Support", "support"),
    ]
    links = []
    for href, label, key in items:
        cls = ' class="active"' if key == active else ""
        links.append(f'<a href="{href}"{cls}>{esc(label)}</a>')
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="/">midchat<span>.io</span></a>
    <nav class="nav">{"".join(links)}</nav>
  </div>
</header>
"""


def footer() -> str:
    return f"""<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <strong>Midchat</strong> — ChatGPT plugins for mid-conversation work.<br>
      Published by {PUBLISHER} · {DOMAIN}
    </div>
    <div class="footer-links">
      <a href="/privacy/">Privacy</a>
      <a href="/terms/">Terms</a>
      <a href="/support/">Support</a>
      <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>
    </div>
  </div>
  <div class="wrap footer-note">
    Published by Midchat · {DOMAIN}. Legal review of privacy/terms recommended. Not legal advice.
  </div>
</footer>
</body>
</html>
"""


def page(title, description, body, active="", accent="#0f172a"):
    return head(title, description, accent) + nav(active) + f'<main class="wrap">\n{body}\n</main>\n' + footer()


# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = """/* Midchat.io — shared site styles */
:root {
  --bg: #f8fafc;
  --ink: #0f172a;
  --muted: #475569;
  --line: #e2e8f0;
  --card: #ffffff;
  --accent: #0f172a;
  --radius: 14px;
  --shadow: 0 1px 2px rgba(15,23,42,.06), 0 8px 24px rgba(15,23,42,.06);
  font-family: "Inter", ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  line-height: 1.55; font-size: 17px;
}
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 3px; }
a:hover { opacity: .85; }
.wrap { max-width: 960px; margin: 0 auto; padding: 0 1.25rem; }
.site-header {
  position: sticky; top: 0; z-index: 20;
  background: rgba(248,250,252,.9); backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}
.header-inner {
  display: flex; align-items: center; justify-content: space-between;
  gap: 1rem; min-height: 64px; flex-wrap: wrap; padding-top: .5rem; padding-bottom: .5rem;
}
.logo {
  font-weight: 800; font-size: 1.15rem; letter-spacing: -.02em;
  color: var(--ink); text-decoration: none;
}
.logo span { color: var(--muted); font-weight: 600; }
.nav { display: flex; flex-wrap: wrap; gap: .65rem 1rem; font-size: .92rem; }
.nav a { color: var(--muted); text-decoration: none; }
.nav a.active, .nav a:hover { color: var(--ink); }
main.wrap { padding-top: 2.5rem; padding-bottom: 4rem; }
.hero { margin-bottom: 2.5rem; }
.hero h1 {
  font-size: clamp(2rem, 4vw, 2.75rem); line-height: 1.15;
  letter-spacing: -.03em; margin: 0 0 .75rem;
}
.hero .lede { font-size: 1.15rem; color: var(--muted); max-width: 42rem; }
.badge {
  display: inline-block; font-size: .75rem; font-weight: 700;
  letter-spacing: .04em; text-transform: uppercase;
  padding: .25rem .55rem; border-radius: 999px;
  background: color-mix(in srgb, var(--accent) 12%, white);
  color: var(--accent); margin-bottom: .75rem;
}
.grid {
  display: grid; gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}
.card {
  background: var(--card); border: 1px solid var(--line);
  border-radius: var(--radius); padding: 1.25rem; box-shadow: var(--shadow);
}
.card h2, .card h3 { margin-top: 0; letter-spacing: -.02em; }
.plugin-card { border-top: 4px solid var(--accent); }
.plugin-card .icon {
  width: 56px; height: 56px; border-radius: 12px; display: block; margin-bottom: .75rem;
}
.plugin-card .meta { color: var(--muted); font-size: .9rem; margin: .35rem 0 1rem; }
.btn {
  display: inline-block; background: var(--accent); color: #fff !important;
  padding: .65rem 1rem; border-radius: 10px; text-decoration: none; font-weight: 600;
}
.btn.secondary {
  background: transparent; color: var(--accent) !important;
  border: 1px solid color-mix(in srgb, var(--accent) 40%, var(--line));
}
.btn-row { display: flex; flex-wrap: wrap; gap: .75rem; margin: 1.25rem 0; }
.section { margin: 2.5rem 0; }
.section h2 { letter-spacing: -.02em; margin-bottom: .75rem; }
.bullets { list-style: none; padding: 0; margin: 0; }
.bullets li {
  padding: 1rem 0; border-bottom: 1px solid var(--line);
}
.bullets li:last-child { border-bottom: 0; }
.bullets strong { display: block; margin-bottom: .2rem; }
.steps { counter-reset: step; list-style: none; padding: 0; }
.steps li {
  counter-increment: step; position: relative;
  padding: .85rem 0 .85rem 2.75rem; border-bottom: 1px solid var(--line);
}
.steps li::before {
  content: counter(step); position: absolute; left: 0; top: .85rem;
  width: 1.85rem; height: 1.85rem; border-radius: 999px;
  background: var(--accent); color: #fff; font-weight: 700; font-size: .9rem;
  display: grid; place-items: center;
}
.prompt-list { display: flex; flex-wrap: wrap; gap: .5rem; }
.prompt-list code {
  background: #fff; border: 1px solid var(--line); border-radius: 999px;
  padding: .4rem .75rem; font-size: .9rem;
}
.example {
  background: #0f172a; color: #e2e8f0; border-radius: var(--radius);
  padding: 1.25rem; font-size: 1rem;
}
.draft-banner {
  background: #fff7ed; border: 1px solid #fdba74; color: #9a3412;
  padding: .85rem 1rem; border-radius: 10px; margin: 0 0 1.5rem;
}
.legal h2 { margin-top: 2rem; font-size: 1.25rem; }
.legal table { width: 100%; border-collapse: collapse; font-size: .95rem; }
.legal th, .legal td {
  border: 1px solid var(--line); padding: .6rem .7rem; text-align: left; vertical-align: top;
}
.legal th { background: #f1f5f9; }
.muted { color: var(--muted); }
.site-footer {
  border-top: 1px solid var(--line); background: #fff;
  padding: 2rem 0 1.5rem; font-size: .92rem; color: var(--muted);
}
.footer-inner {
  display: flex; justify-content: space-between; gap: 1.5rem; flex-wrap: wrap;
}
.footer-links { display: flex; flex-wrap: wrap; gap: .75rem 1.1rem; }
.footer-links a { color: var(--muted); text-decoration: none; }
.footer-links a:hover { color: var(--ink); }
.footer-note { margin-top: 1rem; font-size: .8rem; opacity: .8; }
.plugin-hero {
  display: grid; gap: 1.5rem; align-items: center;
  grid-template-columns: 88px 1fr;
}
.plugin-hero img {
  width: 88px; height: 88px; border-radius: 20px;
  box-shadow: var(--shadow); background: #fff;
}
@media (max-width: 640px) {
  .plugin-hero { grid-template-columns: 1fr; }
  .nav { font-size: .85rem; }
}
"""

write(ROOT / "css" / "site.css", CSS)


# ── Suite landing ────────────────────────────────────────────────────────────
cards = []
for p in PLUGINS:
    cards.append(f"""
    <article class="card plugin-card" style="--accent:{p['color']}">
      <img class="icon" src="/assets/{p['icon']}" alt="{esc(p['name'])} icon" width="56" height="56">
      <h3><a href="/{p['slug']}/" style="color:inherit;text-decoration:none">{esc(p['name'])}</a></h3>
      <p class="meta">{esc(p['short'])} · {esc(p['kind'])}</p>
      <p>{esc(p['blurb'])}</p>
      <p><a href="/{p['slug']}/">Learn more →</a></p>
    </article>""")

suite_body = f"""
{DRAFT_BANNER}
<section class="hero">
  <span class="badge">ChatGPT plugins</span>
  <h1>Work that finishes in the chat.</h1>
  <p class="lede">
    Midchat is a suite of ChatGPT plugins for freelancers and operators —
    invoices, Friday status, meeting actions, expenses, and PDF tables —
    built to be recommended mid-conversation, not buried in a marketplace.
  </p>
  <div class="btn-row">
    <a class="btn" href="/support/">Support</a>
    <a class="btn secondary" href="/privacy/">Privacy</a>
  </div>
</section>

<section class="section">
  <h2>The five plugins</h2>
  <div class="grid">{"".join(cards)}</div>
</section>

<section class="section">
  <h2>Publisher</h2>
  <p class="muted">
    Built and published by <strong>{PUBLISHER}</strong> ({DOMAIN}).
    Contact: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> ·
    Privacy: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>
  </p>
  <p class="muted">
    Skills-only plugins run inside ChatGPT and have no Midchat server.
    PDF → Sheets will add a hosted MCP endpoint at
    <code>https://mcp.midchat.io/mcp</code> before public Directory listing (not live yet).
  </p>
</section>
"""
write(ROOT / "index.html", page(
    "Midchat", "ChatGPT plugins for invoices, weekly status, meeting actions, expenses, and PDF tables.",
    suite_body, active="home"
))


# ── Per-plugin pages ─────────────────────────────────────────────────────────
def plugin_landing(p: dict) -> str:
    bullets = "".join(
        f"<li><strong>{esc(t)}</strong>{esc(d)}</li>" for t, d in p["bullets"]
    )
    steps = "".join(f"<li>{esc(s)}</li>" for s in p["steps"])
    prompts = "".join(f"<code>{esc(x)}</code>" for x in p["prompts"])
    limits = "".join(f"<li>{esc(x)}</li>" for x in p["limitations"])
    return f"""
{DRAFT_BANNER}
<section class="hero plugin-hero" style="--accent:{p['color']}">
  <img src="/assets/{p['icon']}" alt="{esc(p['name'])} icon" width="88" height="88">
  <div>
    <span class="badge">{esc(p['kind'])}</span>
    <h1>{esc(p['name'])}</h1>
    <p class="lede">{esc(p['tagline'])}</p>
    <p>{esc(p['blurb'])}</p>
    <div class="btn-row">
      <a class="btn" href="#try">Try saying</a>
      <a class="btn secondary" href="/{p['slug']}/support/">Support</a>
    </div>
    <p class="muted" style="font-size:.9rem">{esc(p['submit'])}. Directory link added after approval.</p>
  </div>
</section>

<section class="section">
  <h2>Why it exists</h2>
  <ul class="bullets">{bullets}</ul>
</section>

<section class="section">
  <h2>How it works</h2>
  <ol class="steps">{steps}</ol>
</section>

<section class="section" id="try">
  <h2>Try saying</h2>
  <div class="prompt-list">{prompts}</div>
</section>

<section class="section">
  <h2>Example</h2>
  <div class="example">{p['example']}</div>
</section>

<section class="section">
  <h2>Good to know</h2>
  <ul>{limits}</ul>
  <p class="muted">
    Free. Runs inside ChatGPT for the skills-only package.
    See <a href="/{p['slug']}/privacy/">Privacy</a> ·
    <a href="/{p['slug']}/terms/">Terms</a> ·
    <a href="/{p['slug']}/support/">Support</a>.
  </p>
</section>
"""


def plugin_privacy(p: dict) -> str:
    return f"""
{DRAFT_BANNER}
<article class="legal">
  <h1>{esc(p['name'])} — Privacy Policy</h1>
  <p class="muted">Last updated: {PUBLICATION_DATE}</p>

  <h2>Who we are</h2>
  <p>
    {esc(p['name'])} is a plugin for ChatGPT published by <strong>{PUBLISHER}</strong>
    (“we”, “us”).
    Privacy contact: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.
  </p>

  <h2>The short version</h2>
  <ul>
    <li>{esc(p['name'])}’s public package today is primarily <strong>skills-only</strong>: instructions and small scripts that run <strong>inside ChatGPT</strong>.</li>
    <li>For skills-only use, Midchat has <strong>no server that receives your chat content</strong>. We do not see the files or text you process with the plugin.</li>
    <li>Your conversation and uploads are processed by <strong>OpenAI</strong> under OpenAI’s terms and privacy policy: <a href="https://openai.com/policies/privacy-policy">openai.com/policies/privacy-policy</a>.</li>
    <li>We only process personal data if <strong>you contact us</strong> (support/privacy email) or visit this website.</li>
  </ul>

  <h2>What {esc(p['name'])} does with your data inside ChatGPT</h2>
  <p>{p['privacy_extra']}</p>
  <p>
    Whether chats and files are stored, for how long, and whether they are used to improve OpenAI’s models
    is governed by <strong>your ChatGPT account settings and OpenAI’s policies</strong>, not by us.
    Tip: only share data the task actually needs.
  </p>

  <h2>Data we do process (outside ChatGPT)</h2>
  <table>
    <thead><tr><th>Situation</th><th>Data</th><th>Purpose</th><th>Legal basis (GDPR)</th><th>Retention</th></tr></thead>
    <tbody>
      <tr>
        <td>You email support or privacy</td>
        <td>email address, name, message, attachments</td>
        <td>answer your request</td>
        <td>Art. 6(1)(b) or (f)</td>
        <td>{RETENTION}</td>
      </tr>
      <tr>
        <td>You visit our website</td>
        <td>technical data processed by our hosting provider (e.g. IP, browser, time)</td>
        <td>deliver and secure the site</td>
        <td>Art. 6(1)(f)</td>
        <td>per hosting provider: {HOST_NAME} — {HOST_PRIVACY}</td>
      </tr>
    </tbody>
  </table>
  <p>
    OpenAI may make aggregated plugin metrics available to us as publisher.
    We do not receive your conversation content through the skills-only plugin.
    We do not sell personal data or use it for advertising.
    [ADJUST if your site host or analytics sets cookies.]
  </p>
  <p><strong>Please don’t email real invoices, bank statements, or full receipts</strong> unless needed; blur sensitive values.</p>

  <h2>Your rights (EU/EEA)</h2>
  <p>
    For data we hold (e.g. support emails) you have rights of access, rectification, erasure, restriction,
    portability, and objection (Art. 15–21 GDPR). Contact <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.
    For ChatGPT conversation data, exercise rights with OpenAI — we cannot access or delete it.
    You may also complain to a data protection supervisory authority, in particular in the EU member state
    where you live or work.
  </p>

  <h2>Future hosted / MCP version</h2>
  <p>{p['future_mcp']}</p>

  <h2>Changes</h2>
  <p>We’ll update this page when the product changes and adjust the “Last updated” date.</p>

  <p class="muted">
    Suite privacy overview: <a href="/privacy/">/privacy</a> ·
    Terms: <a href="/{p['slug']}/terms/">/{p['slug']}/terms</a> ·
    Support: <a href="/{p['slug']}/support/">/{p['slug']}/support</a>
  </p>
</article>
"""


def plugin_terms(p: dict) -> str:
    you = "".join(f"<li>{x}</li>" for x in p["terms_you"])
    return f"""
{DRAFT_BANNER}
<article class="legal">
  <h1>{esc(p['name'])} — Terms of Use</h1>
  <p class="muted">Last updated: {PUBLICATION_DATE}</p>
  <p>
    These terms apply to {esc(p['name'])}, a ChatGPT plugin published by
    <strong>{PUBLISHER}</strong> (“we”).
    Your use of ChatGPT itself is governed by OpenAI’s terms.
  </p>

  <h2>1. What {esc(p['name'])} is</h2>
  <p>{p['terms_what']}</p>

  <h2>2. Free of charge</h2>
  <p>{esc(p['name'])} is currently provided free of charge. We may change or discontinue it at any time.</p>

  <h2>3. You are responsible for outputs</h2>
  <ul>{you}</ul>

  <h2>4. Acceptable use</h2>
  <p>
    Use {esc(p['name'])} only for lawful purposes. Don’t use it to create false or fraudulent documents,
    or to process personal data you aren’t allowed to process. OpenAI’s usage policies apply.
  </p>

  <h2>5. Your content</h2>
  <p>
    You keep all rights to your inputs and outputs. For skills-only use we don’t receive them
    (see the <a href="/{p['slug']}/privacy/">Privacy Policy</a>).
  </p>

  <h2>6. No warranty</h2>
  <p>
    {esc(p['name'])} is provided “as is”. Outputs are generated by an AI system and may contain errors.
    We don’t guarantee availability, accuracy, or fitness for a particular purpose.
  </p>

  <h2>7. Liability</h2>
  <p>
    We are liable without limitation for intent and gross negligence, for injury to life, body, or health,
    and where mandatory law (e.g. German Product Liability Act) requires. For slight negligence, we are
    liable only for breach of essential obligations and limited to typical, foreseeable damage. Otherwise,
    liability is excluded. Since the plugin is free, statutory liability privileges for gratuitous services
    (e.g. §§ 521, 599 BGB analogously) may apply. [HAVE REVIEWED]
  </p>

  <h2>8. Changes</h2>
  <p>We may update these terms; the “Last updated” date shows the current version. Continued use after changes means you accept them.</p>

  <h2>9. Law</h2>
  <p>
    German law applies, excluding the UN CISG. If you are a consumer in the EU, mandatory consumer
    protection of your country of residence remains unaffected.
  </p>

  <h2>Contact</h2>
  <p><a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></p>
</article>
"""


def plugin_support(p: dict) -> str:
    rows = "".join(
        f"<tr><td>{esc(prob)}</td><td>{esc(fix)}</td></tr>" for prob, fix in p["troubleshoot"]
    )
    prompts = "".join(f"<li><code>{esc(x)}</code></li>" for x in p["prompts"])
    limits = "".join(f"<li>{esc(x)}</li>" for x in p["limitations"])
    return f"""
{DRAFT_BANNER}
<article class="legal">
  <h1>{esc(p['name'])} — Support</h1>
  <p>
    Contact: <a href="mailto:{SUPPORT_EMAIL}"><strong>{SUPPORT_EMAIL}</strong></a>
    · Typical response: within 3 business days
    · Languages: English, Deutsch
  </p>

  <h2>What {esc(p['name'])} does</h2>
  <p>{esc(p['blurb'])}</p>
  {p['support_how']}

  <h2>How to use it</h2>
  <p>Install from the ChatGPT Plugin Directory (link after approval), then try:</p>
  <ul>{prompts}</ul>

  <h2>Limitations</h2>
  <ul>{limits}</ul>

  <h2>Troubleshooting</h2>
  <table>
    <thead><tr><th>Problem</th><th>Try</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>

  <h2>Contact &amp; reporting problems</h2>
  <p>
    Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a> with: what you asked, what happened,
    what you expected, and a screenshot (<strong>blur real names, addresses, bank details, and receipt totals</strong>).
  </p>
  <p class="muted">
    Privacy: <a href="/{p['slug']}/privacy/">/{p['slug']}/privacy</a> ·
    Terms: <a href="/{p['slug']}/terms/">/{p['slug']}/terms</a> ·
    Suite support: <a href="/support/">/support</a>
  </p>
</article>
"""


for p in PLUGINS:
    slug = p["slug"]
    write(ROOT / slug / "index.html", page(
        p["name"], p["blurb"], plugin_landing(p), active=slug, accent=p["color"]
    ))
    write(ROOT / slug / "privacy" / "index.html", page(
        f"{p['name']} Privacy", f"Privacy policy for {p['name']}.",
        plugin_privacy(p), active=slug, accent=p["color"]
    ))
    write(ROOT / slug / "terms" / "index.html", page(
        f"{p['name']} Terms", f"Terms of use for {p['name']}.",
        plugin_terms(p), active=slug, accent=p["color"]
    ))
    write(ROOT / slug / "support" / "index.html", page(
        f"{p['name']} Support", f"Support for {p['name']}.",
        plugin_support(p), active=slug, accent=p["color"]
    ))


# ── Suite-level privacy / terms / support ────────────────────────────────────
plugin_privacy_links = "".join(
    f'<li><a href="/{p["slug"]}/privacy/">{esc(p["name"])} privacy</a></li>' for p in PLUGINS
)
plugin_terms_links = "".join(
    f'<li><a href="/{p["slug"]}/terms/">{esc(p["name"])} terms</a></li>' for p in PLUGINS
)
plugin_support_links = "".join(
    f'<li><a href="/{p["slug"]}/support/"><strong>{esc(p["name"])}</strong></a> — {esc(p["short"])}</li>'
    for p in PLUGINS
)

suite_privacy = f"""
{DRAFT_BANNER}
<article class="legal">
  <h1>Midchat — Privacy Policy (suite)</h1>
  <p class="muted">Last updated: {PUBLICATION_DATE}</p>
  <p>
    This page covers the Midchat website ({DOMAIN}) and how we handle data when you contact us.
    Each ChatGPT plugin also has its own privacy page describing that product:
  </p>
  <ul>{plugin_privacy_links}</ul>

  <h2>Who we are</h2>
  <p>
    Published by <strong>{PUBLISHER}</strong>.
    Privacy: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a> ·
    Support: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.
  </p>

  <h2>Website</h2>
  <p>
    This is a static informational site. Our hosting provider ({HOST_NAME}) may process technical data
    (IP address, browser, time) to deliver and secure the site — see {HOST_PRIVACY}.
    We do not intend to set advertising cookies. [ADJUST if you add analytics.]
  </p>

  <h2>Skills-only plugins</h2>
  <p>
    BillFast, Friday Pack, Action Loop, and Expense Sheet (skills-only) run inside ChatGPT.
    Midchat does not receive your chat content through those packages. See each plugin privacy page
    and OpenAI’s privacy policy.
  </p>

  <h2>PDF → Sheets MCP (planned)</h2>
  <p>
    A hosted MCP server is planned at <code>https://mcp.midchat.io/mcp</code> (not live).
    When live, privacy for that product will describe EU processing, no storage of source PDFs,
    and deletion of generated exports within 24 hours — updated <em>before</em> launch.
  </p>

  <h2>Your rights</h2>
  <p>
    GDPR rights for data we hold: contact {PRIVACY_EMAIL}.
    You may also complain to a data protection supervisory authority in the EU member state where you live or work.
  </p>
</article>
"""
write(ROOT / "privacy" / "index.html", page(
    "Privacy", "Midchat suite privacy policy.", suite_privacy, active="support"
))

suite_terms = f"""
{DRAFT_BANNER}
<article class="legal">
  <h1>Midchat — Terms of Use (suite)</h1>
  <p class="muted">Last updated: {PUBLICATION_DATE}</p>
  <p>
    These suite terms cover use of the Midchat website. Each plugin has its own terms:
  </p>
  <ul>{plugin_terms_links}</ul>
  <p>
    Published by <strong>{PUBLISHER}</strong>.
    ChatGPT use is governed by OpenAI. German law applies; EU consumer protections unaffected.
    Contact: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.
  </p>
  <h2>Website</h2>
  <p>
    The site is informational and provided “as is”. Plugin availability depends on OpenAI’s Directory
    and review process. We may change or remove pages at any time.
  </p>
  <h2>No professional advice</h2>
  <p>
    Nothing on this site or in the plugins is tax, legal, accounting, or medical advice.
  </p>
</article>
"""
write(ROOT / "terms" / "index.html", page(
    "Terms", "Midchat suite terms of use.", suite_terms, active="support"
))

suite_support = f"""
{DRAFT_BANNER}
<article class="legal">
  <h1>Midchat — Support</h1>
  <p>
    <a href="mailto:{SUPPORT_EMAIL}"><strong>{SUPPORT_EMAIL}</strong></a>
    · within 3 business days · English / Deutsch
  </p>
  <p>Pick the plugin you’re using:</p>
  <ul>{plugin_support_links}</ul>
  <h2>Publisher</h2>
  <p>
    {PUBLISHER} · {DOMAIN}.
    Privacy questions: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.
  </p>
  <h2>Before you email</h2>
  <ul>
    <li>Blur real client names, IBANs, and receipt totals in screenshots.</li>
    <li>Include the plugin name, what you asked, what happened, and what you expected.</li>
  </ul>
</article>
"""
write(ROOT / "support" / "index.html", page(
    "Support", "Midchat support hub.", suite_support, active="support"
))

print("DONE", len(list(ROOT.rglob("*.html"))), "html files")
