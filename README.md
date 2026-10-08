# 034034.com — The 034 Number Intelligence Hub

Free lookup, scam reporting and dialing tools for every phone number starting with **034** — UK 0343/0344/0345, Pakistan 034x mobiles, Philippines (034), Netherlands 034x, Italy 034x, India 034x and Spain 0034 — with a business-phone lead engine, AdSense, YouTube, donations, contests and careers.

Static HTML/CSS/JS. Runs on the GitHub Pages free plan.

## Structure
- `build.py` — generates all 26 pages + `sitemap.xml` from one layout. Edit content there, then `python3 build.py`.
- `assets/js/app.js` — config (`SITE` object: AdSense slots, YouTube IDs, donation links), number decoder, forms, dialer, quiz.
- `assets/css/style.css` — design system.
- `docs/RESEARCH.md` — research, concept decision, competitor audit.
- `docs/PROMPTS.md` — phase-wise build prompts.

## Launch checklist
1. **GitHub Pages:** Settings → Pages → Deploy from a branch → `main` / `(root)`.
2. **Custom domain:** DNS A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `www` CNAME → `webworksa1.github.io`. Then enter `034034.com` in Pages settings and tick *Enforce HTTPS*.
3. **Forms:** submit any form once on the live site and click the activation link FormSubmit sends to the inbox.
4. **AdSense:** add the site in AdSense (`ads.txt` included). Optional manual slots: fill `SITE.adSlots` in `app.js`.
5. **YouTube:** add video IDs to `SITE.youtube` and your channel URL to `SITE.youtubeChannel`.
6. **Donations:** add PayPal / Stripe / Buy Me a Coffee / Ko-fi links to `SITE.donate` (pledge form works without them).
7. Submit `sitemap.xml` in Google Search Console.

## Legal
“034034” is used as a descriptive numeric domain; no trademark rights are claimed. Not affiliated with any telecom operator, regulator or bank. See `disclaimer.html`.
