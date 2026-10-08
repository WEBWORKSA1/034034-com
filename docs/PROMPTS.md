# 034034.com — Phase-wise Build Prompts

Use these prompts in order with any AI builder (or Claude) to rebuild, extend or clone this site. Each phase is self-contained. Global constraints apply to every phase.

## Global constraints (paste at the top of every phase)
```
Project: 034034.com — "The 034 Number Intelligence Hub". Static HTML/CSS/vanilla JS only, hostable free on GitHub Pages (repo WEBWORKSA1/034034-com). No server code, no build step required at runtime.
- Every page top: a bar reading "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" linking to https://web.works/contact.
- All forms send to ONE inbox via FormSubmit AJAX. The address must never appear in HTML, text or visible JS strings — store it as reversed char codes and assemble it only at submit time. Include a honeypot field on every form.
- Google AdSense client ca-pub-6620975821265271: auto-ads script in <head>, ads.txt at root, optional manual slots configured in one JS config object.
- Mobile-first, responsive, light/dark via prefers-color-scheme, WCAG AA contrast, skip link, semantic HTML.
- SEO: unique title/description, canonical to https://034034.com/, OpenGraph, FAQPage + WebSite SearchAction JSON-LD, sitemap.xml, robots.txt.
- Never show personal subscriber identity for any number. Trademark/copyright disclosure in footer and on disclaimer.html.
```

## Phase 1 — Foundation & design system
```
Create assets/css/style.css with tokens (navy #0b1530 hero, brand blue #0f62fe, teal #00b3a4, amber #f5a524), fonts Space Grotesk (headings), Inter (body), JetBrains Mono (numbers). Components: sticky header with burger menu, hero with big search box and example chips, cards, tags, KPI strip, tables, form controls, option tiles, multi-step bar, donation tiers, ad-slot wrapper, lite YouTube embed, quiz, FAQ details, cookie bar, footer grid, reveal-on-scroll. Create build.py that renders all pages from one shared layout (top inquiry bar, header, footer with legal strip, cookie consent) and writes sitemap.xml.
```

## Phase 2 — Number intelligence engine
```
In assets/js/app.js build decode(number): normalise any input (spaces, brackets, 00, 011, +). Country rules: UK +44 34[345] (03 non-geographic, Ofcom cost rule); Pakistan +92 34x (Telenor range, PTCL/Ufone 2026 status, portability caveat); Philippines +63 34 (Negros Occidental/Bacolod); Netherlands +31 341–348 (town table); Italy +39 0341–0346 (keep leading 0); India +91 341–343; Spain +34 (mobile 6/7, landline 8/9). National-format input returns ranked candidate matches. Render result cards: match confidence, type, region, international format, cost, community risk "Unrated – report", alternate formats, CTAs (country guide, report, get a business number). Support ?n= deep links.
```

## Phase 3 — Content hubs (programmatic SEO)
```
Generate prefixes.html directory plus 7 country hubs: uk-0343-0344-0345, pakistan-034-mobile, philippines-034-negros, netherlands-034-area-codes, italy-034-area-codes, india-034-std-codes, spain-0034-dialing. Each: hero with embedded lookup, data table, "data checked" date, explainer sections, scam warnings with official reporting channels, FAQ with JSON-LD, lead CTA, donation strip, two ad slots. Add number-meaning.html (numerology, East Asian 3/4 symbolism, telecom economics).
```

## Phase 4 — Tools & engagement
```
dialing-codes.html: live from/to dial builder for 14 countries (exit codes, trunk-zero rules, Italy exception) with "+" format. scam-safety.html: 6 scam archetypes, country reporting table, 6-question Scam IQ quiz with explanations and score, newsletter/checklist capture form. report.html: rating (safe/annoying/dangerous), 12 call types, claimed caller, details, nickname, private email, truthfulness consent; prefill from ?n=.
```

## Phase 5 — Lead generation (primary revenue)
```
get-quotes.html: 4-step wizard — (1) users band 1-4/5-19/20-99/100+, country, industry (2) needs checkboxes: virtual 0345/03, local numbers abroad, cloud PBX, forwarding, AI receptionist, contact centre, CRM, porting, bulk SMS/WhatsApp (3) timeframe, current provider, budget (4) name, company, business email, phone, best time, required contact consent + optional marketing consent. Progress bar, per-step validation, trust bullets. Add "Claim your business number" form with free/verified/featured plans. Reusable quick-quote block (name, email, users, country, consent) on home, lookup, hub and safety pages.
```

## Phase 6 — Monetisation & community funding
```
AdSense: auto ads + config-driven manual slots (top, inContent, sidebar, footer) that stay hidden until slot IDs are set. YouTube: config array of video IDs rendered as click-to-load nocookie embeds on home and videos.html; channel subscribe button. support.html: donation tiers $5/$25/$100/$500, amount, frequency, allocation (operations, promotions & marketing, hiring, contests & prizes), pledge form, optional PayPal/Stripe/BMC/Ko-fi buttons from config, allocation table. contests.html: monthly Scam-Spotter Challenge with prizes, rules, entry form, sponsor CTA. careers.html: 6 remote roles + application form. advertise.html: 8 packages incl. domain acquisition, media-kit form.
```

## Phase 7 — Trust, legal & compliance
```
about.html, contact.html (topic select incl. removal request & domain purchase, ?topic= prefill), privacy.html (AdSense cookies, Google ad settings link, lead sharing with consent, form processor), terms.html, disclaimer.html (trademark disclosure: "034034" descriptive numeric domain, no trademark claimed, not affiliated with Ofcom/PTA/PTCL/Ufone/Telenor/NTC/TRAI or banks; copyright notice; affiliate disclosure), 404.html with lookup. Cookie consent bar stored in localStorage.
```

## Phase 8 — Deploy & launch
```
Add .nojekyll, ads.txt, robots.txt, manifest.webmanifest, SVG favicon and OG image. Push to WEBWORKSA1/034034-com (main). Enable GitHub Pages (Settings → Pages → Deploy from branch → main / root). Point 034034.com DNS (A records 185.199.108-111.153, CNAME www → webworksa1.github.io), then add the custom domain in Pages settings and enforce HTTPS. Submit sitemap to Google Search Console, apply site in AdSense, send one test form to activate FormSubmit.
```

## Phase 9 — Growth roadmap
```
1) Generate sub-range pages (0345-0, 0345-3 … and PK 0340–0349 each). 2) Translate hubs to Urdu, Tagalog, Dutch, Italian, Spanish with hreflang. 3) Move reports to a free backend (Supabase / Giscus) and publish moderated reports per number. 4) Monthly scam-alert articles with author + date. 5) YouTube Shorts per prefix. 6) Sell verified listings and lead partnerships (CPL).
```
