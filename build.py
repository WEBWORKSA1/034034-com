#!/usr/bin/env python3
"""034034.com static site generator.
Run:  python3 build.py   → writes every .html page, sitemap.xml into the repo root.
All pages share one layout (top inquiry bar, header, footer, AdSense, consent bar).
"""
import datetime, os

DOMAIN = "https://034034.com/"
AD_CLIENT = "ca-pub-6620975821265271"
TODAY = datetime.date.today().isoformat()
INQUIRY = "https://web.works/contact"

NAV = [("lookup.html", "Number Lookup"), ("prefixes.html", "034 Prefixes"), ("dialing-codes.html", "Dialing Tool"),
       ("scam-safety.html", "Scam Safety"), ("report.html", "Report"), ("get-quotes.html", "Business Numbers"),
       ("videos.html", "Videos")]

def layout(fn, title, desc, body, schema=""):
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{'' if fn=='index.html' else fn}">
<meta property="og:type" content="website"><meta property="og:site_name" content="034034.com">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{'' if fn=='index.html' else fn}"><meta property="og:image" content="{DOMAIN}assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1530">
<meta name="google-adsense-account" content="{AD_CLIENT}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={AD_CLIENT}" crossorigin="anonymous"></script>
{schema}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="{INQUIRY}" target="_blank" rel="noopener">contact here</a></div>
<header class="header"><div class="container nav">
<a class="logo" href="index.html" aria-label="034034 home"><span class="badge">034</span>034034</a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
<nav class="menu" aria-label="Main">{nav}<a class="btn btn-amber btn-sm" href="support.html">Support ♥</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="container">
<div class="fgrid">
<div><a class="logo" href="index.html" style="color:#fff"><span class="badge" style="background:#fff;color:#0b1530">034</span>034034</a>
<p style="margin-top:12px">The independent guide to every phone number that starts with 034 — who uses them, what they cost, and how to stay safe.</p>
<a class="btn btn-amber btn-sm" href="{INQUIRY}" target="_blank" rel="noopener">Buy / sponsor this domain</a></div>
<div><h4>Tools</h4><ul><li><a href="lookup.html">Number lookup</a></li><li><a href="dialing-codes.html">Dialing tool</a></li><li><a href="report.html">Report a number</a></li><li><a href="scam-safety.html#quiz">Scam quiz</a></li><li><a href="number-meaning.html">Meaning of 034034</a></li></ul></div>
<div><h4>034 Prefixes</h4><ul><li><a href="uk-0343-0344-0345.html">UK 0343 / 0344 / 0345</a></li><li><a href="pakistan-034-mobile.html">Pakistan 034x mobile</a></li><li><a href="philippines-034-negros.html">Philippines 034</a></li><li><a href="netherlands-034-area-codes.html">Netherlands 034x</a></li><li><a href="italy-034-area-codes.html">Italy 034x</a></li><li><a href="india-034-std-codes.html">India 034x</a></li><li><a href="spain-0034-dialing.html">Spain 0034</a></li></ul></div>
<div><h4>Business</h4><ul><li><a href="get-quotes.html">Get phone-system quotes</a></li><li><a href="get-quotes.html#claim">Claim your number</a></li><li><a href="advertise.html">Advertise</a></li><li><a href="contests.html">Contests &amp; prizes</a></li><li><a href="careers.html">Careers</a></li></ul></div>
<div><h4>About</h4><ul><li><a href="about.html">About</a></li><li><a href="support.html">Donate</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="disclaimer.html">Disclaimer &amp; trademarks</a></li></ul></div>
</div>
<div class="legal-strip">© <span data-year></span> 034034.com. All rights reserved. “034034” is used as a descriptive numeric domain name; no trademark rights in the number are claimed. 034034.com is independent and not affiliated with any telecom operator, regulator or government. Third-party names and marks belong to their owners. <a href="disclaimer.html">Full trademark &amp; copyright disclosure</a>.</div>
</div></footer>
<div class="cookie" role="dialog" aria-label="Cookie consent"><p>We use cookies for analytics and to show ads (Google AdSense). See our <a href="privacy.html">privacy policy</a>.</p><button class="btn btn-primary btn-sm" data-cookie="all">Accept</button><button class="btn btn-ghost btn-sm" data-cookie="essential">Essential only</button></div>
<script src="assets/js/app.js" defer></script>
</body>
</html>
"""

def ad(slot="inContent"):
    return f'<div class="container ad-slot" data-slot="{slot}"></div>'

def hp():
    return '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'

def faq(items):
    html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    import json
    sch = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, f'<script type="application/ld+json">{json.dumps(sch)}</script>'

def lead_cta():
    return """<section><div class="container"><div class="lead-box reveal">
<div><span class="tag" style="background:rgba(255,255,255,.12);color:#fff">Free · No obligation</span>
<h2 style="margin-top:12px">Want your own 0345, 03 or local business number?</h2>
<p style="color:#c9d4f2">Tell us your team size and needs once. We match you with business phone and VoIP providers and send tailored quotes — usually within one business day.</p>
<ul class="list-check" style="color:#e6ecff"><li>Virtual 03 / 034x numbers, local numbers in 6 countries</li><li>Call forwarding, AI receptionist, call recording</li><li>Port your existing number at no cost to you</li></ul></div>
<div class="card"><form data-form="Quick quote" data-ok="Thanks! Your quote request is in — expect a reply within 1 business day.">
<label for="qq-n">Name</label><input id="qq-n" name="name" required autocomplete="name">
<label for="qq-e">Business email</label><input id="qq-e" name="email" type="email" required autocomplete="email">
<div class="row"><div><label for="qq-u">Users</label><select id="qq-u" name="users" required><option value="">Select</option><option>1–4</option><option>5–19</option><option>20–99</option><option>100+</option></select></div>
<div><label for="qq-c">Country</label><select id="qq-c" name="country" required><option value="">Select</option><option>United Kingdom</option><option>Pakistan</option><option>Philippines</option><option>India</option><option>Netherlands</option><option>Italy</option><option>Spain</option><option>Other</option></select></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about quotes. No spam.</label>
""" + hp() + """<button class="btn btn-primary" type="submit" style="width:100%">Get my free quotes →</button><div class="form-msg" role="status"></div>
<p class="muted" style="font-size:.8rem;margin:10px 0 0">Prefer the detailed version? <a href="get-quotes.html">4-step quote wizard</a></p></form></div>
</div></div></section>"""

def support_strip():
    return """<section class="section-alt"><div class="container grid g2" style="align-items:center">
<div><h2>Keep 034034 free for everyone</h2><p class="muted">Reader support pays for hosting, moderation, translations, new tools, marketing, hiring contributors and contest prizes.</p></div>
<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end"><a class="btn btn-amber" href="support.html">Donate ♥</a><a class="btn btn-ghost" href="contests.html">Enter the contest</a><a class="btn btn-ghost" href="advertise.html">Sponsor</a></div>
</div></section>"""

def page_hero(title, lead, crumbs=None, extra=""):
    c = ""
    if crumbs:
        c = '<div class="crumbs"><a href="index.html">Home</a> › ' + " › ".join(crumbs) + "</div>"
    return f'<section class="page-hero section-alt"><div class="container">{c}<h1>{title}</h1><p class="lead muted">{lead}</p>{extra}</div></section>'

def lookup_form(target="#result", big=False):
    return f'''<form class="searchbox" data-lookup="{target}" role="search"><input name="n" inputmode="tel" placeholder="Enter any 034 number e.g. 0345 123 4567" aria-label="Phone number" required><button class="btn btn-primary" type="submit">Check</button></form>'''

PAGES = {}

# ---------------- HOME ----------------
home_faq, home_faq_schema = faq([
    ("Who is calling me from an 0345 or 0344 number?", "In the UK, 0343, 0344 and 0345 are 03 non-geographic numbers used mostly by government services, banks, utilities and charities. Enter the full number in our lookup to see its type, and check community reports before you share any details."),
    ("Is an 0345 number free to call?", "Not free, but cheap: Ofcom rules say 03 numbers cost no more than calls to normal 01/02 landlines and are included in inclusive minutes."),
    ("Which network is 0345 in Pakistan?", "The 034x mobile range was allocated to Telenor Pakistan, now owned by PTCL and merging with Ufone. Because numbers can be ported, the prefix alone no longer proves the current network."),
    ("Where is area code 034 in the Philippines?", "034 is the landline area code for Negros Occidental, including Bacolod City."),
    ("Does 034034.com show who owns a number?", "No. We identify number type, region and costs, and host community scam reports. We never publish the personal identity of a phone subscriber."),
])
PAGES["index.html"] = ("034034 — Who Called Me From 034? Free 034 Number Lookup & Scam Checker",
 "Free lookup for every phone number starting with 034: UK 0343/0344/0345, Pakistan 034x mobiles, Philippines 034, Netherlands, Italy, India and Spain 0034. Report scam calls, dial correctly, get business numbers.",
 f"""<section class="hero"><div class="container">
<span class="eyebrow">034 · 0034 · +34 · 0345 · +63 34 · +92 34x</span>
<h1>Got a call from a <span style="color:#f5a524">034</span> number?<br>Find out what it is in seconds.</h1>
<p class="lead">One free tool for every number starting with 034 — across 7 countries. See the number type, region and call cost, read community reports, and learn how to stay safe.</p>
<form class="searchbox" data-lookup="redirect" role="search"><input name="n" inputmode="tel" placeholder="e.g. 0345 123 4567 or +92 345 1234567" aria-label="Phone number" required><button class="btn btn-primary" type="submit">Check number</button></form>
<div class="chips"><a class="chip" href="lookup.html?n=03450000000">0345 (UK)</a><a class="chip" href="lookup.html?n=%2B923451234567">+92 345 (PK)</a><a class="chip" href="lookup.html?n=%2B63344330000">+63 34 (PH)</a><a class="chip" href="lookup.html?n=%2B31341000000">+31 341 (NL)</a><a class="chip" href="lookup.html?n=%2B390341000000">+39 0341 (IT)</a><a class="chip" href="lookup.html?n=0034600000000">0034 (ES)</a></div>
<div class="kpis"><div class="kpi"><b>7</b><span>countries covered</span></div><div class="kpi"><b>30+</b><span>034 prefixes decoded</span></div><div class="kpi"><b>0</b><span>personal data exposed</span></div><div class="kpi"><b>100%</b><span>free to use</span></div></div>
<div class="bignum">034034</div></div></section>
{ad("top")}
<section><div class="container">
<h2 class="reveal">Every 034 number, explained</h2><p class="muted reveal">“034” means something different in each country. Pick yours.</p>
<div class="grid g3">
<a class="card reveal" href="uk-0343-0344-0345.html"><div class="icon">🇬🇧</div><h3>UK 0343 · 0344 · 0345</h3><p class="muted">Non-geographic 03 numbers used by HMRC-style services, banks, utilities and charities. Priced like a landline.</p><span class="tag">Most searched</span></a>
<a class="card reveal" href="pakistan-034-mobile.html"><div class="icon">🇵🇰</div><h3>Pakistan 0340–0349</h3><p class="muted">Mobile range of Telenor Pakistan — now owned by PTCL and merging with Ufone. What it means for you.</p><span class="tag warn">Changed 2026</span></a>
<a class="card reveal" href="philippines-034-negros.html"><div class="icon">🇵🇭</div><h3>Philippines (034)</h3><p class="muted">Landline area code for Negros Occidental and Bacolod City — the “City of Smiles”.</p></a>
<a class="card reveal" href="netherlands-034-area-codes.html"><div class="icon">🇳🇱</div><h3>Netherlands 0341–0348</h3><p class="muted">Area codes for Harderwijk, Barneveld, Tiel, Culemborg, Woerden and more.</p></a>
<a class="card reveal" href="italy-034-area-codes.html"><div class="icon">🇮🇹</div><h3>Italy 0341–0346</h3><p class="muted">Lecco, Sondrio, Lake Como and the Bergamo valleys.</p></a>
<a class="card reveal" href="spain-0034-dialing.html"><div class="icon">🇪🇸</div><h3>Spain 0034 / +34</h3><p class="muted">How to call Spain — and why a “0034” call can be a missed-call scam.</p></a>
</div><p style="margin-top:18px"><a href="india-034-std-codes.html">Also: India STD 0341 Asansol · 0342 Bardhaman · 0343 Durgapur →</a></p></div></section>
<section class="section-alt"><div class="container grid g4">
<a class="card reveal" href="lookup.html"><div class="icon">🔎</div><h3>Number lookup</h3><p class="muted">Decode any 034 number: type, region, formats, cost.</p></a>
<a class="card reveal" href="report.html"><div class="icon">🚩</div><h3>Report a caller</h3><p class="muted">Warn others about scam, spam or silent calls.</p></a>
<a class="card reveal" href="dialing-codes.html"><div class="icon">🌍</div><h3>Dialing tool</h3><p class="muted">Exactly what to dial, from anywhere to anywhere.</p></a>
<a class="card reveal" href="scam-safety.html#quiz"><div class="icon">🧠</div><h3>Scam IQ quiz</h3><p class="muted">Can you spot a phone scam? 6 questions.</p></a>
</div></section>
{lead_cta()}
{ad("inContent")}
<section><div class="container grid g2">
<div class="reveal"><h2>Top phone scams hitting 034 numbers right now</h2>
<ul class="list-check"><li><b>Bank “fraud team” calls</b> spoofing a real 0345 number, asking you to move money to a “safe account”.</li>
<li><b>Prize & benefit scams</b> on Pakistani 034x mobiles promising lucky-draw winnings or government cash in exchange for a code.</li>
<li><b>One-ring “Wangiri” calls</b> from unfamiliar international codes, hoping you call back at premium rates.</li>
<li><b>Delivery and customs texts</b> with links to fake payment pages.</li></ul>
<a class="btn btn-primary" href="scam-safety.html">Full safety guide</a></div>
<div class="card reveal"><h3>Report a number in 30 seconds</h3><p class="muted">Your report helps thousands of people decide whether to pick up.</p>
<form action="report.html" method="get"><label for="hr">Phone number</label><input id="hr" name="n" placeholder="+44 345 …" required><button class="btn btn-amber" style="margin-top:12px;width:100%">Start report →</button></form></div>
</div></section>
<section class="section-alt"><div class="container"><h2>034 Video Guides</h2><p class="muted">Short explainers on spotting scam calls and dialing internationally.</p>
<div class="grid g3" id="video-grid">
<a class="card" href="videos.html"><div class="icon">▶</div><h3>How to spot a bank impersonation call</h3><p class="muted">Watch on our Videos page.</p></a>
<a class="card" href="videos.html"><div class="icon">▶</div><h3>0345 numbers: cost & who uses them</h3><p class="muted">Watch on our Videos page.</p></a>
<a class="card" href="videos.html"><div class="icon">▶</div><h3>Calling Pakistan, the Philippines & Spain</h3><p class="muted">Watch on our Videos page.</p></a>
</div></div></section>
<section><div class="container prose"><h2>Frequently asked questions</h2>{home_faq}<p><a href="number-meaning.html">Curious about the number 034034 itself? Culture, numerology & meaning →</a></p></div></section>
{support_strip()}
""", home_faq_schema + '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"034034","url":"https://034034.com/","potentialAction":{"@type":"SearchAction","target":"https://034034.com/lookup.html?n={number}","query-input":"required name=number"}}</script>')

# ---------------- LOOKUP ----------------
PAGES["lookup.html"] = ("034 Number Lookup — Decode Any 034, 0034, 0345 or +92 34x Number | 034034",
 "Free reverse lookup for numbers starting with 034. Identify number type, country, region, formats and call cost. UK, Pakistan, Philippines, Netherlands, Italy, India, Spain.",
 page_hero("034 Number Lookup", "Type any number in any format — with or without the country code. We'll tell you what kind of number it is, where it's from and what it costs to call back.", ["Number lookup"],
   lookup_form() + '<div class="chips" style="margin-top:6px"><a class="chip" style="color:var(--ink);border-color:var(--line);background:var(--bg)" href="#" data-try="0345 300 0000">0345 300 0000</a><a class="chip" style="color:var(--ink);border-color:var(--line);background:var(--bg)" href="#" data-try="+92 345 1234567">+92 345 1234567</a><a class="chip" style="color:var(--ink);border-color:var(--line);background:var(--bg)" href="#" data-try="(034) 433 0000">(034) 433 0000</a><a class="chip" style="color:var(--ink);border-color:var(--line);background:var(--bg)" href="#" data-try="0034 612 345 678">0034 612 345 678</a></div><div id="result" class="result" aria-live="polite"></div>') +
 ad("top") + """<section><div class="container grid g3">
<div class="card"><h3>What we show</h3><ul class="list-check"><li>Number type (mobile, landline, non-geographic)</li><li>Country & region</li><li>All the ways it's written</li><li>Call-back cost rules</li><li>Community risk reports</li></ul></div>
<div class="card"><h3>What we never show</h3><ul class="list-check"><li>Subscriber names or addresses</li><li>CNIC, ID or SIM-owner data</li><li>Leaked or scraped databases</li></ul><p class="muted">Sites offering “SIM owner details” often use leaked data — avoid them.</p></div>
<div class="card"><h3>Next steps</h3><p><a href="report.html">Report the number</a> if it was spam, read our <a href="scam-safety.html">scam guide</a>, or <a href="dialing-codes.html">build the right dial string</a> to call back.</p></div>
</div></section>""" + lead_cta() + support_strip())

# ---------------- PREFIX HUB PAGES ----------------
def prefix_page(fn, h1, title, desc, intro, table_head, rows, sections, faqs, crumbs):
    th = "".join(f"<th>{h}</th>" for h in table_head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    fh, fs = faq(faqs)
    secs = "".join(f'<h2>{h}</h2>{b}' for h, b in sections)
    body = page_hero(h1, intro, ['<a href="prefixes.html">034 Prefixes</a>', crumbs], lookup_form() + '<div id="result" class="result" aria-live="polite"></div>') + ad("top") + f"""
<section><div class="container"><div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>
<p class="muted" style="font-size:.85rem;margin-top:8px">Data checked {TODAY}. Spotted an error? <a href="contact.html">Tell us</a>.</p></div></section>
<section class="section-alt"><div class="container prose">{secs}{ad("inContent")}<h2>FAQ</h2>{fh}</div></section>""" + lead_cta() + support_strip()
    PAGES[fn] = (title, desc, body, fs)

prefix_page("uk-0343-0344-0345.html", "UK 0343, 0344 &amp; 0345 numbers",
 "0345, 0344 & 0343 Numbers: Who's Calling, Cost & Scam Check | 034034",
 "Everything about UK 034x numbers: who uses 0343, 0344 and 0345, what they cost from mobiles and landlines, and how to spot spoofed scam calls.",
 "03 numbers are the UK's “national rate” numbers. The 034x block — 0343, 0344 and 0345 — is one of the most common sets of numbers used by large organisations.",
 ["Prefix", "Type", "Typical users", "Cost to call"],
 [["0343", "03 non-geographic", "Councils, charities, service providers", "Same as 01/02 landline"],
  ["0344", "03 non-geographic", "Utilities, insurers, retailers, public bodies", "Same as 01/02 landline"],
  ["0345", "03 non-geographic", "Banks, government departments, large companies", "Same as 01/02 landline"]],
 [("Why organisations use 0345", "<p>An 03 number gives one national number that callers can reach at normal landline prices, and calls count towards inclusive minutes. Because revenue sharing is not allowed on 03 numbers, the organisation does not profit from your call — which is why many public services moved from 0845/0870 to 0345/0344.</p>"),
  ("Is a call from 0345 safe?", "<p>Most 0345 calls are legitimate, but caller ID can be faked. Criminals often spoof a bank's real 0345 number. If a caller asks you to move money, read out a one-time passcode or install remote-access software, hang up and call the number on the back of your card. In the UK you can forward scam texts to <b>7726</b>, call <b>159</b> to reach your bank safely, and report fraud to Action Fraud.</p>"),
  ("Get your own 0345 number", "<p>Virtual 0345/0344 numbers can route to any mobile or landline, start from a few pounds a month, and look established to customers. <a href='get-quotes.html'>Compare providers in one form →</a></p>")],
 [("Is 0345 a free number?", "No. 0800 and 0808 are free; 0345 costs the same as a normal landline call and is usually inside bundled minutes."),
  ("Is 0345 the same as 0845?", "No. 0845 numbers can carry a service charge; 0345 cannot. Many organisations migrated from 0845 to 0345 for that reason."),
  ("Can I find out who owns an 0345 number?", "Business 03 numbers are usually published by the organisation itself. Search the full number, check our community reports, and never trust caller ID alone.")],
 "UK 034x")

prefix_page("pakistan-034-mobile.html", "Pakistan 034x mobile numbers (0340–0349)",
 "0345 / 034x Pakistan Number: Which Network? Telenor, PTCL & Ufone Explained | 034034",
 "What 0340–0349 numbers mean in Pakistan after PTCL's acquisition of Telenor Pakistan and the merger with Ufone. Network, portability, scam warnings and how to call.",
 "The 034x series is one of Pakistan's best-known mobile ranges — the Telenor Pakistan range, whose head office was even named “345”. In 2025–26 that network changed hands.",
 ["Range", "Originally allocated to", "2026 status", "International format"],
 [["0340 – 0349", "Telenor Pakistan", "PTCL completed acquisition 31 Dec 2025; court-approved merger with Ufone (PTML) July 2026", "+92 34x xxxxxxx"],
  ["Ported numbers", "Any operator", "Mobile number portability — prefix ≠ network", "+92 3xx xxxxxxx"]],
 [("What changed in 2026", "<p>PTCL completed its purchase of Telenor Pakistan at the end of 2025, and in July 2026 the Islamabad High Court approved its merger with Ufone (PTML). The Telenor brand is being phased out, but existing 034x numbers continue to work.</p>"),
  ("Common scams on 034x numbers", "<p>Watch for calls and SMS claiming you've won a lucky draw or a government cash programme, fake “bank verification” calls asking for OTPs, and fraudsters posing as courier or customs staff. No legitimate bank or programme asks for your PIN or OTP. Report fraudulent SIMs and calls to the PTA through its official complaint channels, and to the FIA cybercrime wing for fraud.</p>"),
  ("Avoid “SIM owner details” sites", "<p>Sites that promise the owner's name and CNIC for any 034x number usually rely on leaked databases. Using them is risky and can be illegal. 034034.com never shows personal subscriber data.</p>"),
  ("Calling a 034x number from abroad", "<p>Drop the leading 0 and add +92: 0345 1234567 becomes <span class='mono'>+92 345 1234567</span>. From the US/Canada dial 011 92 345…; from the UK or Gulf dial 00 92 345…</p>")],
 [("Which company is 0345 in Pakistan?", "0345 was Telenor Pakistan's flagship code. Telenor Pakistan is now owned by PTCL and is being merged into Ufone (PTML). Ported numbers may be on any network."),
  ("Is Telenor still working in Pakistan?", "Existing Telenor numbers keep working while the merged company integrates the networks and phases out the brand."),
  ("How do I check a 034x number's owner?", "Lawful options are limited to the network's own services and law enforcement. Use our lookup for type and region, and report scam numbers.")],
 "Pakistan 034x")

prefix_page("philippines-034-negros.html", "Philippines area code 034 — Negros Occidental",
 "Area Code 034 Philippines: Bacolod & Negros Occidental Landlines | 034034",
 "Area code 034 covers Bacolod City and Negros Occidental. How to dial (034) numbers locally and from abroad, and how to check unknown calls.",
 "If a Philippine landline starts with (034), it's in Negros Occidental — home of Bacolod City, the MassKara Festival and much of the country's sugar industry.",
 ["Area code", "Province / city", "From abroad", "Domestic"],
 [["034", "Bacolod City, Negros Occidental (incl. Silay, Talisay, Kabankalan, San Carlos)", "+63 34 + number", "(034) + number"]],
 [("Why 034 matters", "<p>Bacolod is a major BPO and call-centre hub in the Visayas, so calls from (034) numbers may come from customer-service operations serving international clients — as well as local businesses, hospitals and government offices.</p>"),
  ("Spotting scam calls in the Philippines", "<p>Be wary of callers claiming to be from banks, e-wallets or couriers who ask for OTPs or MPINs. Report scam calls and texts through your network and the national telecom regulator's channels, and to the CICC hotline for cyber fraud.</p>")],
 [("What area code is Bacolod?", "Bacolod City and the rest of Negros Occidental use area code 034."),
  ("How do I call Bacolod from the US?", "Dial 011 63 34 followed by the local number.")],
 "Philippines 034")

prefix_page("netherlands-034-area-codes.html", "Netherlands 034x area codes",
 "Netnummer 0341–0348: Harderwijk, Barneveld, Tiel, Culemborg, Woerden | 034034",
 "Dutch area codes 0341 to 0348 explained: which towns they cover, how to dial them from abroad, and how to check an unknown Dutch caller.",
 "In the Netherlands the 034x netnummers cover a belt of towns in Gelderland and Utrecht — from Harderwijk on the Veluwe to Woerden in the Green Heart.",
 ["Area code", "Main places", "From abroad"],
 [["0341", "Harderwijk, Nunspeet, Ermelo", "+31 341 …"], ["0342", "Barneveld", "+31 342 …"], ["0343", "Doorn, Driebergen", "+31 343 …"],
  ["0344", "Tiel", "+31 344 …"], ["0345", "Culemborg", "+31 345 …"], ["0346", "Maarssen, Breukelen", "+31 346 …"],
  ["0347", "Vianen", "+31 347 …"], ["0348", "Woerden", "+31 348 …"]],
 [("Dialing tips", "<p>Dutch numbers have 10 digits domestically. From abroad, drop the leading 0: 0344 123456 becomes +31 344 123456.</p>"),
  ("Unknown caller?", "<p>Spoofed Dutch landline numbers are used in fake bank-helpdesk scams. Banks never ask you to transfer money to a “safe account”. Hang up and call your bank directly.</p>")],
 [("Which town is 0345?", "In the Netherlands, 0345 is Culemborg. (In the UK, 0345 is a non-geographic number; in Pakistan, a mobile prefix.)")],
 "Netherlands 034x")

prefix_page("italy-034-area-codes.html", "Italy 034x prefissi",
 "Prefisso 0341, 0342, 0344, 0345: Lecco, Sondrio, Lago di Como | 034034",
 "Italian area codes 0341–0346: Lecco, Sondrio, Chiavenna, Menaggio, San Pellegrino Terme and Clusone. How to dial them from abroad.",
 "Italy's 034x prefixes cover Lombardy's lakes and Alpine valleys — Lecco and Lake Como, Valtellina, and the valleys above Bergamo.",
 ["Prefix", "Area", "From abroad"],
 [["0341", "Lecco", "+39 0341 …"], ["0342", "Sondrio (Valtellina)", "+39 0342 …"], ["0343", "Chiavenna", "+39 0343 …"],
  ["0344", "Menaggio (Lake Como)", "+39 0344 …"], ["0345", "San Pellegrino Terme", "+39 0345 …"], ["0346", "Clusone", "+39 0346 …"]],
 [("Keep the zero", "<p>Unlike most countries, Italy keeps the leading 0 of landline numbers when dialled internationally: +39 0341 …, not +39 341 ….</p>")],
 [("What is prefix 0341?", "0341 is the area code for Lecco, on the south-eastern arm of Lake Como.")],
 "Italy 034x")

prefix_page("india-034-std-codes.html", "India STD codes 0341, 0342, 0343",
 "STD Code 0341 Asansol, 0342 Bardhaman, 0343 Durgapur | 034034",
 "India's 034x STD codes for West Bengal's industrial belt: Asansol, Bardhaman and Durgapur. How to dial them, plus scam-call safety tips.",
 "In India, 034x STD codes cover West Bengal's steel-and-coal belt along the Grand Trunk Road.",
 ["STD code", "City", "From abroad"],
 [["0341", "Asansol", "+91 341 …"], ["0342", "Bardhaman (Burdwan)", "+91 342 …"], ["0343", "Durgapur", "+91 343 …"]],
 [("Scam safety in India", "<p>Fraud callers impersonate banks, courier firms, telecom regulators and police (“digital arrest” scams). No agency arrests anyone over a video call. Report fraud on the national cybercrime helpline 1930 or cybercrime.gov.in, and suspected fraud calls via the Sanchar Saathi Chakshu facility.</p>")],
 [("Which city has STD code 0343?", "Durgapur, West Bengal.")],
 "India 034x")

prefix_page("spain-0034-dialing.html", "Spain 0034 / +34",
 "0034 Country Code: Calling Spain, Spanish Numbers & Missed-Call Scams | 034034",
 "0034 is how you dial Spain (+34) from most countries. Learn Spanish number formats, mobile vs landline, and how to handle unknown +34 calls.",
 "If your phone shows 0034 or +34, the call is from Spain — or from someone spoofing a Spanish number.",
 ["Starts with", "Type", "Example"],
 [["+34 6 / +34 7", "Mobile", "+34 612 345 678"], ["+34 9 / +34 8", "Landline", "+34 912 345 678 (Madrid)"], ["+34 90x", "Shared-cost / premium", "Check before calling"]],
 [("Dialing Spain", "<p>Spanish numbers have 9 digits with no trunk 0. From the UK or Pakistan dial 00 34 + 9 digits; from the US/Canada dial 011 34 + 9 digits.</p>"),
  ("One-ring calls from +34", "<p>A single ring from an unknown international number may be a “Wangiri” scam designed to make you call back a costly line. If you don't know anyone in Spain, don't call back.</p>")],
 [("What country is 0034?", "Spain. 00 is the international exit code used in most of Europe, Asia and Africa, and 34 is Spain's country code.")],
 "Spain 0034")

# ---------------- PREFIX INDEX ----------------
PAGES["prefixes.html"] = ("All 034 Phone Prefixes Worldwide — Country by Country | 034034",
 "Directory of every phone prefix starting with 034: UK 0343/0344/0345, Pakistan 0340–0349, Philippines 034, Netherlands 0341–0348, Italy 0341–0346, India 0341–0343, Spain 0034.",
 page_hero("The 034 prefix directory", "Seven countries, one sequence of digits. Here's every place “034” shows up on a phone screen.", ["034 Prefixes"]) + ad("top") + """
<section><div class="container"><div class="table-wrap"><table><thead><tr><th>Country</th><th>034 prefixes</th><th>Number type</th><th>Guide</th></tr></thead><tbody>
<tr><td>🇬🇧 United Kingdom</td><td class="mono">0343, 0344, 0345</td><td>Non-geographic (03)</td><td><a href="uk-0343-0344-0345.html">Open</a></td></tr>
<tr><td>🇵🇰 Pakistan</td><td class="mono">0340–0349</td><td>Mobile</td><td><a href="pakistan-034-mobile.html">Open</a></td></tr>
<tr><td>🇵🇭 Philippines</td><td class="mono">(034)</td><td>Landline — Negros Occidental</td><td><a href="philippines-034-negros.html">Open</a></td></tr>
<tr><td>🇳🇱 Netherlands</td><td class="mono">0341–0348</td><td>Landline area codes</td><td><a href="netherlands-034-area-codes.html">Open</a></td></tr>
<tr><td>🇮🇹 Italy</td><td class="mono">0341–0346</td><td>Landline area codes</td><td><a href="italy-034-area-codes.html">Open</a></td></tr>
<tr><td>🇮🇳 India</td><td class="mono">0341–0343</td><td>Landline STD codes</td><td><a href="india-034-std-codes.html">Open</a></td></tr>
<tr><td>🇪🇸 Spain</td><td class="mono">0034 / +34</td><td>Country code</td><td><a href="spain-0034-dialing.html">Open</a></td></tr>
</tbody></table></div></div></section>""" + lead_cta() + support_strip())

# ---------------- DIALING ----------------
PAGES["dialing-codes.html"] = ("International Dialing Tool — How to Call Any 034 Number | 034034",
 "Build the exact dial string to call the UK, Pakistan, Philippines, Netherlands, Italy, India or Spain from 14 countries. Exit codes, country codes and trunk-zero rules.",
 page_hero("International dialing tool", "Pick where you're calling from and to, paste the number, and get the exact digits to dial.", ["Dialing tool"]) + f"""
<section><div class="container grid g2">
<div class="card"><form id="dialer"><div class="row"><div><label for="d-from">Calling from</label><select id="d-from"></select></div><div><label for="d-to">Calling to</label><select id="d-to"></select></div></div>
<label for="d-num">Number (as written locally)</label><input id="d-num" inputmode="tel"></form></div>
<div class="card" style="background:linear-gradient(160deg,var(--hero1),var(--hero2));color:#fff"><small style="color:#c9d4f2">DIAL THIS</small><div id="d-out" class="mono" style="font-size:2rem;font-weight:800;margin:6px 0"></div>
<small style="color:#c9d4f2">ON A MOBILE YOU CAN ALSO USE</small><div id="d-plus" class="mono" style="font-size:1.3rem"></div><p id="d-note" style="color:#c9d4f2;margin-top:12px"></p></div>
</div></section>{ad("inContent")}
<section class="section-alt"><div class="container prose"><h2>Three rules that fix 90% of failed international calls</h2>
<ol><li><b>Exit code first</b> — 00 in most of the world, 011 from the US & Canada, 0011 from Australia, 010 from Japan. On a mobile, “+” replaces it.</li>
<li><b>Country code next</b> — 44 UK, 92 Pakistan, 63 Philippines, 31 Netherlands, 39 Italy, 91 India, 34 Spain.</li>
<li><b>Drop the trunk 0</b> — except Italy, which keeps it.</li></ol>
<p>Calling family abroad often? Business and VoIP plans can cut per-minute international rates sharply — <a href="get-quotes.html">compare quotes</a>.</p></div></section>""" + support_strip())

# ---------------- SCAM SAFETY ----------------
quiz_items = [
 ("A caller from your bank's real 0345 number says your account is under attack and asks you to move money to a “safe account”. What do you do?",
  ["Move the money quickly", "Hang up and call the number on your card", "Give them a one-time passcode to verify"], 1,
  "Banks never ask you to move money to a safe account. Caller ID can be spoofed."),
 ("You get one ring from +34 at 3am. You don't know anyone in Spain.", ["Call back to check", "Ignore it", "Text them your name"], 1,
  "One-ring (Wangiri) calls bait you into calling back premium-rate lines."),
 ("An SMS from a 034x mobile says you've won a lucky draw and must pay a small “tax” to claim it.", ["Pay the small fee", "Report and delete", "Send your ID to verify"], 1,
  "Genuine prizes never require upfront fees."),
 ("Is an 0345 number more expensive than calling an 01 number?", ["Yes, it's premium rate", "No, it costs the same", "It's always free"], 1,
  "Ofcom rules cap 03 numbers at geographic rates."),
 ("A “police officer” on video call says you're under “digital arrest”.", ["Stay on the call", "Hang up — it's a scam", "Transfer bail money"], 1,
  "No genuine law-enforcement agency arrests people over a video call."),
 ("A courier text asks you to pay £1.45 redelivery via a link.", ["Pay — it's tiny", "Check directly on the courier's official site", "Reply STOP"], 1,
  "Tiny fees are used to harvest card details."),
]
qhtml = ""
for i, (q, opts, r, why) in enumerate(quiz_items):
    bs = "".join(f'<button type="button"{" data-right" if j == r else ""}>{o}</button>' for j, o in enumerate(opts))
    qhtml += f'<div class="quiz-q card"><b>{i+1}. {q}</b><div class="ans">{bs}</div><p class="why muted" hidden style="margin-top:10px">{why}</p></div>'
PAGES["scam-safety.html"] = ("Phone Scam Safety Guide + Scam IQ Quiz — 0345, +92, +63, 0034 | 034034",
 "How to spot and report phone scams: bank impersonation, prize scams, Wangiri one-ring calls, digital-arrest calls. Country-by-country reporting links and a free quiz.",
 page_hero("Phone scam safety", "The five scripts fraudsters use most — and the official places to report them in each country.", ["Scam safety"]) + ad("top") + f"""
<section><div class="container grid g3">
<div class="card"><div class="icon">🏦</div><h3>Bank impersonation</h3><p class="muted">Spoofed 0345 or bank numbers, “safe account” transfers, OTP requests.</p></div>
<div class="card"><div class="icon">🎁</div><h3>Prize &amp; benefit scams</h3><p class="muted">Lucky draws, fake government cash, “fees” to release winnings.</p></div>
<div class="card"><div class="icon">📞</div><h3>Wangiri one-ring</h3><p class="muted">Missed calls from unfamiliar codes like +34 to bait call-backs.</p></div>
<div class="card"><div class="icon">👮</div><h3>Authority impersonation</h3><p class="muted">Fake police, tax or customs officers; “digital arrest”.</p></div>
<div class="card"><div class="icon">📦</div><h3>Delivery texts</h3><p class="muted">Tiny redelivery fees that steal card details.</p></div>
<div class="card"><div class="icon">💼</div><h3>Job &amp; investment offers</h3><p class="muted">Task-based “earn from home” and crypto schemes.</p></div>
</div></section>
<section class="section-alt"><div class="container"><h2>Where to report — official channels</h2><div class="table-wrap"><table><thead><tr><th>Country</th><th>Report to</th></tr></thead><tbody>
<tr><td>🇬🇧 UK</td><td>Forward scam texts to 7726 · Call 159 to reach your bank · <a href="https://www.actionfraud.police.uk/" rel="noopener" target="_blank">Action Fraud</a> (England, Wales, NI) / Police Scotland</td></tr>
<tr><td>🇵🇰 Pakistan</td><td><a href="https://www.pta.gov.pk/" rel="noopener" target="_blank">PTA</a> complaint channels · FIA Cybercrime Wing</td></tr>
<tr><td>🇵🇭 Philippines</td><td>Your network operator · <a href="https://cicc.gov.ph/" rel="noopener" target="_blank">CICC</a> hotline 1326</td></tr>
<tr><td>🇮🇳 India</td><td>Cybercrime helpline 1930 · <a href="https://cybercrime.gov.in/" rel="noopener" target="_blank">cybercrime.gov.in</a> · <a href="https://sancharsaathi.gov.in/" rel="noopener" target="_blank">Sanchar Saathi</a></td></tr>
<tr><td>🇳🇱 Netherlands</td><td><a href="https://www.fraudehelpdesk.nl/" rel="noopener" target="_blank">Fraudehelpdesk</a> · Police</td></tr>
<tr><td>🇮🇹 Italy</td><td><a href="https://www.commissariatodips.it/" rel="noopener" target="_blank">Polizia Postale</a></td></tr>
<tr><td>🇪🇸 Spain</td><td><a href="https://www.incibe.es/" rel="noopener" target="_blank">INCIBE</a> helpline 017</td></tr>
</tbody></table></div><p class="muted" style="font-size:.85rem;margin-top:8px">Always verify official contact details on the agency's own website.</p></div></section>
{ad("inContent")}
<section id="quiz"><div class="container prose"><h2>Scam IQ quiz</h2><p class="muted">Six real-world scenarios. Tap an answer.</p><div class="quiz">{qhtml}<div class="quiz-score card" hidden><h3>Your score: <b></b></h3><p>Share the quiz with someone who'd benefit — and <a href="contests.html">enter our monthly Scam-Spotter contest</a>.</p></div></div></div></section>
<section class="section-alt"><div class="container grid g2"><div><h2>Get the free scam-safety checklist</h2><p class="muted">A one-page printable for parents, grandparents and staff, plus monthly alerts about new 034 scams.</p></div>
<div class="card"><form data-form="Newsletter / checklist" data-ok="You're in! The checklist is on its way.">
<label for="nl-e">Email</label><input id="nl-e" name="email" type="email" required><label for="nl-c">Country</label><select id="nl-c" name="country"><option>United Kingdom</option><option>Pakistan</option><option>Philippines</option><option>India</option><option>Other</option></select>
<label class="check"><input type="checkbox" name="consent" value="yes" required> Send me scam alerts. Unsubscribe any time.</label>{hp()}
<button class="btn btn-primary" type="submit">Send me the checklist</button><div class="form-msg" role="status"></div></form></div></div></section>""" + lead_cta())

# ---------------- REPORT ----------------
PAGES["report.html"] = ("Report a Scam or Spam Call — 034 Numbers | 034034",
 "Report a spam, scam or nuisance call from any 034 number. Help others decide whether to answer. Moderated, anonymous, free.",
 page_hero("Report a number", "Tell the community what happened. Reports are moderated before publishing, and you can stay anonymous.", ["Report"]) + f"""
<section><div class="container grid g2">
<div class="card"><form data-form="Number report" data-ok="Thank you — your report has been received and will be reviewed by a moderator.">
<label for="report-number">Phone number</label><input id="report-number" name="number" required inputmode="tel" placeholder="+44 345 …">
<label>How risky was the call?</label><div class="opts">
<label class="opt"><input type="radio" name="rating" value="Safe" required> 🟢 Safe / legitimate</label>
<label class="opt"><input type="radio" name="rating" value="Annoying"> 🟡 Annoying / spam</label>
<label class="opt"><input type="radio" name="rating" value="Dangerous"> 🔴 Dangerous / scam</label></div>
<label for="r-type">Call type</label><select id="r-type" name="call_type" required><option value="">Select</option><option>Bank / payment impersonation</option><option>Prize / lottery / benefit</option><option>Sales / telemarketing</option><option>Survey</option><option>Debt collection</option><option>Silent call</option><option>One-ring / Wangiri</option><option>Robocall / recorded message</option><option>SMS / WhatsApp spam</option><option>Delivery / customs</option><option>Legitimate organisation</option><option>Other</option></select>
<label for="r-caller">Caller claimed to be (optional)</label><input id="r-caller" name="claimed_caller" placeholder="e.g. 'my bank', 'courier'">
<label for="r-msg">What happened?</label><textarea id="r-msg" name="details" required placeholder="Describe the call. Don't include your own personal data."></textarea>
<div class="row"><div><label for="r-nick">Nickname (public)</label><input id="r-nick" name="nickname"></div><div><label for="r-mail">Email for follow-up (private, optional)</label><input id="r-mail" name="email" type="email"></div></div>
<label class="check"><input type="checkbox" name="agree" value="yes" required> My report is truthful and contains no one's private personal information.</label>{hp()}
<button class="btn btn-primary" type="submit">Submit report</button><div class="form-msg" role="status"></div></form></div>
<div><div class="card"><h3>Reporting guidelines</h3><ul class="list-check"><li>Describe the call, not the person</li><li>No names, addresses or ID numbers</li><li>No threats or abuse</li><li>Businesses can reply to reports</li></ul></div>
<div class="card" style="margin-top:20px"><h3>Is this your business number?</h3><p class="muted">Claim it to add your verified company name, reply to reports and get a “Verified” badge.</p><a class="btn btn-amber" href="get-quotes.html#claim">Claim your number</a></div>
<div class="card" style="margin-top:20px"><h3>Want a report removed?</h3><p class="muted">Use the <a href="contact.html?topic=removal">removal request form</a>. We review every request.</p></div></div>
</div></section>""" + ad("inContent") + support_strip())

# ---------------- LEAD GEN ----------------
PAGES["get-quotes.html"] = ("Business Phone Numbers & VoIP Quotes — 0345, 03 & Local Numbers | 034034",
 "Get free, no-obligation quotes for business phone systems, virtual 0345/03 numbers, local numbers in the UK, Pakistan, Philippines, India and more. 4-step form, answers within 1 business day.",
 page_hero("Get business phone quotes", "Virtual numbers, cloud phone systems, call centres and AI receptionists — compared for you. Free, no obligation, one form.", ["Business numbers"],
   '<div class="trust" style="color:var(--muted)"><span>✓ Free for businesses</span><span>✓ Replies within 1 business day</span><span>✓ No contracts required</span><span>✓ Keep your existing number</span></div>') + f"""
<section><div class="container grid g2" style="align-items:start">
<div class="card"><form data-form="Business phone quote (detailed)" data-multistep="1" data-ok="Done! Your request is in — matched providers will contact you within 1 business day.">
<div class="steps-bar"><span></span><span></span><span></span><span></span></div>
<div class="step"><h3>1. About your business</h3>
<label>How many people need phones?</label><div class="opts">
<label class="opt"><input type="radio" name="users" value="1-4" required> 1–4</label><label class="opt"><input type="radio" name="users" value="5-19"> 5–19</label>
<label class="opt"><input type="radio" name="users" value="20-99"> 20–99</label><label class="opt"><input type="radio" name="users" value="100+"> 100+</label></div>
<label for="gq-country">Where are you based?</label><select id="gq-country" name="country" required><option value="">Select</option><option>United Kingdom</option><option>Pakistan</option><option>Philippines</option><option>India</option><option>Netherlands</option><option>Italy</option><option>Spain</option><option>United States</option><option>Canada</option><option>UAE</option><option>Other</option></select>
<label for="gq-ind">Industry</label><select id="gq-ind" name="industry"><option>Retail / e-commerce</option><option>Professional services</option><option>Healthcare</option><option>Real estate</option><option>BPO / call centre</option><option>Education</option><option>Charity / non-profit</option><option>Other</option></select></div>
<div class="step"><h3>2. What do you need?</h3><div class="opts">
<label class="opt"><input type="checkbox" name="needs" value="Virtual 03/0345 number"> Virtual 0345 / 03 number</label>
<label class="opt"><input type="checkbox" name="needs" value="Local numbers"> Local numbers abroad</label>
<label class="opt"><input type="checkbox" name="needs" value="Cloud phone system"> Cloud phone system (VoIP)</label>
<label class="opt"><input type="checkbox" name="needs" value="Call forwarding"> Call forwarding to mobile</label>
<label class="opt"><input type="checkbox" name="needs" value="AI receptionist"> AI receptionist / IVR</label>
<label class="opt"><input type="checkbox" name="needs" value="Contact centre"> Contact centre</label>
<label class="opt"><input type="checkbox" name="needs" value="CRM integration"> CRM integration</label>
<label class="opt"><input type="checkbox" name="needs" value="Port number"> Port my existing number</label>
<label class="opt"><input type="checkbox" name="needs" value="Bulk SMS / WhatsApp"> Bulk SMS / WhatsApp API</label></div></div>
<div class="step"><h3>3. Timing &amp; budget</h3>
<label for="gq-time">When do you want to switch?</label><select id="gq-time" name="timeframe" required><option value="">Select</option><option>ASAP</option><option>Within 1 month</option><option>1–3 months</option><option>Just researching</option></select>
<label for="gq-prov">Current provider (optional)</label><input id="gq-prov" name="current_provider">
<label for="gq-bud">Monthly budget per user</label><select id="gq-bud" name="budget"><option>Under $15</option><option>$15–30</option><option>$30–50</option><option>$50+</option><option>Not sure</option></select></div>
<div class="step"><h3>4. Where should we send quotes?</h3>
<div class="row"><div><label for="gq-name">Full name</label><input id="gq-name" name="name" required autocomplete="name"></div><div><label for="gq-co">Company</label><input id="gq-co" name="company" required autocomplete="organization"></div></div>
<div class="row"><div><label for="gq-mail">Business email</label><input id="gq-mail" name="email" type="email" required autocomplete="email"></div><div><label for="gq-tel">Phone</label><input id="gq-tel" name="phone" type="tel" required autocomplete="tel"></div></div>
<label for="gq-best">Best time to contact</label><select id="gq-best" name="best_time"><option>Morning</option><option>Afternoon</option><option>Evening</option><option>Email only</option></select>
<label class="check"><input type="checkbox" name="consent_contact" value="yes" required> I agree that 034034.com and up to 3 matched providers may contact me about my request.</label>
<label class="check"><input type="checkbox" name="consent_marketing" value="yes"> Send me occasional offers and guides (optional).</label>{hp()}</div>
<div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" data-next>Next →</button></div>
<button class="btn btn-amber" type="submit" style="width:100%;margin-top:12px">Get my free quotes</button>
<div class="form-msg" role="status"></div></form></div>
<div><div class="card"><h3>Why businesses choose 034 numbers</h3><ul class="list-check"><li><b>0345 in the UK</b>: nationally recognised, landline-priced for callers</li><li><b>Local presence</b> in Pakistan, the Philippines, India, Spain</li><li><b>Work from anywhere</b> — calls ring on your app or mobile</li><li><b>Typical cost</b>: cloud phone plans commonly start around $15–30 per user/month</li></ul></div>
<div class="card" style="margin-top:20px"><h3>How it works</h3><ol><li>Complete the 4-step form (60 seconds)</li><li>We match you with suitable providers</li><li>Compare quotes &amp; choose — or don't</li></ol></div></div>
</div></section>
<section id="claim" class="section-alt"><div class="container grid g2"><div><h2>Claim your business number</h2><p class="muted">Own an 0343/0344/0345 number or a 034 line in another country? Verify it to show your company name to people who look it up, reply to reports and turn callers into customers.</p>
<ul class="list-check"><li>Verified badge on lookups</li><li>Respond publicly to reports</li><li>Add opening hours and a link</li></ul></div>
<div class="card"><form data-form="Claim business number" data-ok="Thanks — we'll verify your number and be in touch.">
<label for="cl-n">Number</label><input id="cl-n" name="number" required><label for="cl-co">Company name</label><input id="cl-co" name="company" required>
<label for="cl-w">Website</label><input id="cl-w" name="website" type="url" placeholder="https://"><label for="cl-e">Work email</label><input id="cl-e" name="email" type="email" required>
<label for="cl-p">Plan</label><select id="cl-p" name="plan"><option>Free basic listing</option><option>Verified listing (paid)</option><option>Featured listing + reply tools (paid)</option></select>{hp()}
<button class="btn btn-primary" type="submit" style="margin-top:12px">Claim number</button><div class="form-msg" role="status"></div></form></div></div></section>
{ad("inContent")}""" + support_strip())

# ---------------- VIDEOS ----------------
PAGES["videos.html"] = ("034 Video Guides — Scam Calls, 0345 Numbers & International Dialing | 034034",
 "Watch short video guides on spotting phone scams, understanding 0345 and 03 numbers, and calling Pakistan, the Philippines and Spain.",
 page_hero("Video guides", "Short, practical videos. New episodes added regularly.", ["Videos"], '<a class="btn btn-primary" data-channel hidden target="_blank" rel="noopener">Subscribe on YouTube</a>') + ad("top") + """
<section><div class="container"><div class="grid g3" id="video-grid">
<div class="card"><div class="video"><div class="play"><div><b>▶</b><br>Spot a bank impersonation call</div></div></div><h3 style="margin-top:12px">Spot a bank impersonation call</h3><p class="muted">Coming soon.</p></div>
<div class="card"><div class="video"><div class="play"><div><b>▶</b><br>0345 numbers explained</div></div></div><h3 style="margin-top:12px">0345 numbers explained</h3><p class="muted">Coming soon.</p></div>
<div class="card"><div class="video"><div class="play"><div><b>▶</b><br>Call Pakistan, PH &amp; Spain</div></div></div><h3 style="margin-top:12px">Calling Pakistan, the Philippines &amp; Spain</h3><p class="muted">Coming soon.</p></div>
</div></div></section>
<section class="section-alt"><div class="container grid g2"><div><h2>Make a video with us</h2><p class="muted">Creators, fraud-prevention experts and brands: pitch a collaboration or sponsor an episode.</p></div><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-amber" href="advertise.html">Sponsor an episode</a><a class="btn btn-ghost" href="careers.html">Join as a creator</a></div></div></section>""" + support_strip())

# ---------------- SUPPORT / DONATE ----------------
PAGES["support.html"] = ("Support 034034 — Donate to Keep Scam Protection Free | 034034",
 "Donate to 034034.com to fund free scam-call tools, moderation, translations, marketing, contributors and contest prizes.",
 page_hero("Support 034034", "Every contribution keeps the tools free, ad-light and independent.", ["Support"]) + f"""
<section><div class="container grid g2" style="align-items:start">
<div class="card"><h3>Choose an amount (USD)</h3><div class="tiers">
<div class="tier" data-amt="5"><b>$5</b>Supporter<br><small class="muted">Covers 1 day of hosting & tools</small></div>
<div class="tier sel" data-amt="25"><b>$25</b>Protector<br><small class="muted">Funds a translated scam guide</small></div>
<div class="tier" data-amt="100"><b>$100</b>Champion<br><small class="muted">Adds to the contest prize pool</small></div>
<div class="tier" data-amt="500"><b>$500</b>Sponsor<br><small class="muted">Name on our sponsors wall</small></div></div>
<form data-form="Donation pledge" data-ok="Thank you! We'll send secure payment instructions to your email shortly." style="margin-top:16px">
<div class="row"><div><label for="donation-amount">Amount (USD)</label><input id="donation-amount" name="amount" type="number" min="1" value="25" required></div>
<div><label for="d-freq">Frequency</label><select id="d-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<label for="d-use">Direct my gift to</label><select id="d-use" name="allocation"><option>Where it's needed most</option><option>Ongoing operations &amp; hosting</option><option>Promotions &amp; marketing</option><option>Hiring writers, translators &amp; moderators</option><option>Contests &amp; prizes</option></select>
<div class="row"><div><label for="d-name">Name</label><input id="d-name" name="name" required></div><div><label for="d-mail">Email</label><input id="d-mail" name="email" type="email" required></div></div>
<label for="d-msg">Message (optional)</label><textarea id="d-msg" name="message" style="min-height:80px"></textarea>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> List my name on the supporters wall</label>{hp()}
<button class="btn btn-amber" type="submit" style="width:100%">Pledge my support ♥</button><div class="form-msg" role="status"></div></form>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:14px"><a class="btn btn-ghost btn-sm" data-pay="paypal" hidden target="_blank" rel="noopener">PayPal</a><a class="btn btn-ghost btn-sm" data-pay="stripe" hidden target="_blank" rel="noopener">Card (Stripe)</a><a class="btn btn-ghost btn-sm" data-pay="buymeacoffee" hidden target="_blank" rel="noopener">Buy Me a Coffee</a><a class="btn btn-ghost btn-sm" data-pay="kofi" hidden target="_blank" rel="noopener">Ko-fi</a></div></div>
<div><div class="card"><h3>Where your money goes</h3><div class="table-wrap"><table><tbody>
<tr><td>Operations, hosting &amp; tools</td><td>35%</td></tr><tr><td>Hiring writers, translators, moderators</td><td>30%</td></tr><tr><td>Promotion &amp; awareness campaigns</td><td>20%</td></tr><tr><td>Contests &amp; prizes</td><td>15%</td></tr></tbody></table></div></div>
<div class="card" style="margin-top:20px"><h3>Corporate sponsorship</h3><p class="muted">Banks, telecoms and security firms can sponsor scam-awareness campaigns in the UK, Pakistan, the Philippines and India.</p><a class="btn btn-primary" href="advertise.html">See sponsor packages</a></div></div>
</div></section>""")

# ---------------- CONTESTS ----------------
PAGES["contests.html"] = ("Scam-Spotter Contest — Win Prizes for Scam Awareness | 034034",
 "Enter the monthly 034034 Scam-Spotter Challenge: share a scam-awareness tip, video or poster and win prizes. Sponsors welcome.",
 page_hero("Scam-Spotter Challenge", "Monthly contest. Teach people to spot phone scams — win prizes and get featured.", ["Contests"]) + f"""
<section><div class="container grid g3">
<div class="card"><div class="icon">🏆</div><h3>1st prize</h3><p class="muted">Cash or gift-card prize + featured on our homepage &amp; YouTube.</p></div>
<div class="card"><div class="icon">🥈</div><h3>Runners-up</h3><p class="muted">Gift cards + certificate + backlink to your profile.</p></div>
<div class="card"><div class="icon">🎓</div><h3>Student category</h3><p class="muted">Separate prize for school &amp; university entries.</p></div></div></section>
<section class="section-alt"><div class="container grid g2" style="align-items:start">
<div class="prose"><h2>How to enter</h2><ol><li>Create an original tip, short video, poster or story about a phone scam.</li><li>Submit the link below before the last day of the month.</li><li>Winners are chosen by judges on originality, accuracy and reach.</li></ol>
<h3>Rules (summary)</h3><ul><li>Free to enter; open where legally permitted; no purchase necessary.</li><li>Entries must be your original work and contain no one's personal data.</li><li>Prize values and availability depend on sponsorship for that month and are announced on this page.</li><li>By entering you grant 034034.com a non-exclusive licence to display your entry with credit.</li></ul>
<h3>Sponsor a month</h3><p>Put your brand behind a prize pool. <a href="advertise.html">Sponsorship options →</a></p></div>
<div class="card"><form data-form="Contest entry" data-ok="Entry received — good luck! Winners are announced at the start of each month.">
<div class="row"><div><label for="c-n">Name</label><input id="c-n" name="name" required></div><div><label for="c-e">Email</label><input id="c-e" name="email" type="email" required></div></div>
<label for="c-cat">Category</label><select id="c-cat" name="category"><option>Tip / article</option><option>Short video</option><option>Poster / graphic</option><option>Student</option></select>
<label for="c-l">Link to your entry</label><input id="c-l" name="entry_link" type="url" required placeholder="https://">
<label for="c-d">Describe your entry</label><textarea id="c-d" name="description" required></textarea>
<label for="c-ct">Country</label><input id="c-ct" name="country">
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I accept the contest rules and confirm the entry is my original work.</label>{hp()}
<button class="btn btn-amber" type="submit">Submit entry</button><div class="form-msg" role="status"></div></form></div>
</div></section>""" + ad("inContent") + support_strip())

# ---------------- CAREERS ----------------
roles = [("Content writer (Urdu/English)", "Write scam alerts and guides for Pakistani readers.", "Remote · Freelance"),
         ("Content writer (Tagalog/English)", "Cover Philippine scam trends and dialing guides.", "Remote · Freelance"),
         ("Community moderator", "Review number reports and keep the community safe.", "Remote · Part-time"),
         ("Video creator / editor", "Produce short scam-awareness videos for YouTube & Shorts.", "Remote · Per project"),
         ("SEO &amp; growth specialist", "Grow organic traffic across 7 country hubs.", "Remote · Contract"),
         ("Partnerships &amp; ad sales", "Sell sponsorships to telecom, fintech and security brands.", "Remote · Commission")]
rh = "".join(f'<div class="card"><span class="tag">{t}</span><h3 style="margin-top:10px">{n}</h3><p class="muted">{d}</p><a href="#apply" class="btn btn-ghost btn-sm">Apply</a></div>' for n, d, t in roles)
ropts = "".join(f"<option>{n}</option>" for n, _, _ in roles)
PAGES["careers.html"] = ("Careers at 034034 — Writers, Moderators, Video Creators | 034034",
 "Join 034034.com: remote roles for writers (Urdu, Tagalog), moderators, video creators, SEO specialists and partnership managers.",
 page_hero("Work with us", "We're a remote-first team fighting phone scams in seven countries. Talent welcome from anywhere.", ["Careers"]) + f"""
<section><div class="container grid g3">{rh}</div></section>
<section id="apply" class="section-alt"><div class="container grid g2" style="align-items:start"><div><h2>Apply or send a general application</h2><p class="muted">Tell us about yourself and link to your work. We reply to every applicant.</p></div>
<div class="card"><form data-form="Job application" data-ok="Application received — thank you! We'll be in touch.">
<label for="j-role">Role</label><select id="j-role" name="role" required>{ropts}<option>General application</option></select>
<div class="row"><div><label for="j-n">Name</label><input id="j-n" name="name" required></div><div><label for="j-e">Email</label><input id="j-e" name="email" type="email" required></div></div>
<div class="row"><div><label for="j-c">Country / time zone</label><input id="j-c" name="location"></div><div><label for="j-l">Languages</label><input id="j-l" name="languages"></div></div>
<label for="j-p">Portfolio / CV link</label><input id="j-p" name="portfolio" type="url" required placeholder="https://">
<label for="j-m">Why you?</label><textarea id="j-m" name="message" required></textarea>{hp()}
<button class="btn btn-primary" type="submit">Send application</button><div class="form-msg" role="status"></div></form></div></div></section>""")

# ---------------- ADVERTISE ----------------
PAGES["advertise.html"] = ("Advertise & Sponsor on 034034 — Reach Phone Users in 7 Countries | 034034",
 "Advertising, sponsorship and partnership packages on 034034.com: sponsored scam-alert campaigns, prefix-page sponsorship, video sponsorship, contest prizes and lead partnerships.",
 page_hero("Advertise, sponsor &amp; partner", "Reach people at the exact moment they're checking a number — in the UK, Pakistan, the Philippines, India and Europe.", ["Advertise"],
   f'<a class="btn btn-amber" href="{INQUIRY}" target="_blank" rel="noopener">Talk about the domain / partnership</a>') + f"""
<section><div class="container grid g4">
<div class="card"><h3>Prefix-page sponsor</h3><p class="muted">Own a country hub (e.g. UK 0345 or Pakistan 034x) with a native banner and logo.</p></div>
<div class="card"><h3>Scam-alert campaign</h3><p class="muted">Co-branded awareness series for banks, telecoms and fintechs.</p></div>
<div class="card"><h3>Video sponsorship</h3><p class="muted">Integrated mention in our YouTube guides.</p></div>
<div class="card"><h3>Contest prize partner</h3><p class="muted">Fund a monthly prize pool and get featured.</p></div>
<div class="card"><h3>Lead partnership</h3><p class="muted">Receive qualified business-phone and VoIP leads (CPL or rev-share).</p></div>
<div class="card"><h3>Verified listings</h3><p class="muted">Bulk verification for organisations with many 03 numbers.</p></div>
<div class="card"><h3>Newsletter slot</h3><p class="muted">Sponsor our monthly scam-alert email.</p></div>
<div class="card"><h3>Domain acquisition</h3><p class="muted">034034.com may be available. <a href="{INQUIRY}" target="_blank" rel="noopener">Enquire</a>.</p></div>
</div></section>
<section class="section-alt"><div class="container grid g2" style="align-items:start"><div><h2>Request the media kit</h2><p class="muted">Audience breakdown, available placements and rates.</p></div>
<div class="card"><form data-form="Advertising / sponsorship inquiry" data-ok="Thanks — the media kit is on its way.">
<div class="row"><div><label for="a-n">Name</label><input id="a-n" name="name" required></div><div><label for="a-c">Company</label><input id="a-c" name="company" required></div></div>
<label for="a-e">Work email</label><input id="a-e" name="email" type="email" required>
<label for="a-t">Interested in</label><select id="a-t" name="interest"><option>Sponsorship</option><option>Advertising</option><option>Partnership</option><option>Lead partnership</option><option>Domain / website acquisition</option></select>
<label for="a-b">Budget</label><select id="a-b" name="budget"><option>Under $1,000</option><option>$1,000–5,000</option><option>$5,000–25,000</option><option>$25,000+</option></select>
<label for="a-m">Message</label><textarea id="a-m" name="message"></textarea>{hp()}
<button class="btn btn-primary" type="submit">Request media kit</button><div class="form-msg" role="status"></div></form></div></div></section>""")

# ---------------- CONTACT ----------------
PAGES["contact.html"] = ("Contact 034034 | 034034",
 "Contact the 034034.com team: general questions, report removal requests, corrections, press and partnerships.",
 page_hero("Contact us", "We read every message. For domain, sponsorship, advertising or partnership enquiries you can also use our dedicated contact page.", ["Contact"],
   f'<a class="btn btn-amber" href="{INQUIRY}" target="_blank" rel="noopener">Domain / sponsorship / partnership enquiries</a>') + f"""
<section><div class="container grid g2" style="align-items:start">
<div class="card"><form data-form="Contact" data-ok="Message sent — we'll reply as soon as possible.">
<label for="ct-t">Topic</label><select id="ct-t" name="topic" required><option value="general">General question</option><option value="removal">Report / data removal request</option><option value="correction">Correction</option><option value="press">Press</option><option value="partnership">Partnership</option><option value="domain">Domain / website purchase</option></select>
<div class="row"><div><label for="ct-n">Name</label><input id="ct-n" name="name" required></div><div><label for="ct-e">Email</label><input id="ct-e" name="email" type="email" required></div></div>
<label for="ct-num">Related phone number (optional)</label><input id="ct-num" name="number">
<label for="ct-m">Message</label><textarea id="ct-m" name="message" required></textarea>{hp()}
<button class="btn btn-primary" type="submit">Send message</button><div class="form-msg" role="status"></div></form></div>
<div class="card"><h3>Removal requests</h3><p class="muted">If a report mentions your number unfairly, choose “Report / data removal request”, include the number and explain why. We aim to review requests within 7 days.</p>
<h3>Response times</h3><p class="muted">General: 2–3 business days · Business & partnerships: 1 business day.</p></div>
</div></section>
<script>(function(){{var t=new URLSearchParams(location.search).get("topic");if(t){{var s=document.getElementById("ct-t");if(s)s.value=t;}}}})();</script>""")

# ---------------- MEANING ----------------
PAGES["number-meaning.html"] = ("Meaning of 034034 — Culture, Numerology & Why 034 Matters | 034034",
 "What the number 034034 means across cultures: Chinese and Japanese number symbolism of 3 and 4, numerology, mirrored repetition, and 034's role in telecoms and the economy.",
 page_hero("The meaning of 034034", "A repeating six-digit sequence that sits at the crossroads of numerology, superstition and the world's phone networks.", ["Meaning of 034034"]) + ad("top") + f"""
<section><div class="container prose">
<h2>Numerology</h2><p>Add the digits: 0+3+4+0+3+4 = 14, and 1+4 = <b>5</b>. In Western numerology 5 is the number of change, freedom and movement. The building blocks pair <b>3</b> (creativity, communication) with <b>4</b> (structure, stability), and the zero is read as potential — “communication built on a solid foundation”, said twice for emphasis.</p>
<h2>Repetition and memorability</h2><p>Repeated patterns (“ABCABC”) are among the easiest numbers to remember, which is why repeating sequences are prized in phone numbers, licence plates and domain names. A six-digit repeat like 034034 is recalled from just three digits.</p>
<h2>East Asian symbolism</h2><p>In Mandarin, 4 (<i>sì</i>) sounds like “death” (<i>sǐ</i>) and 3 (<i>sān</i>) is often linked to “life” (<i>shēng</i>), so “34” can be read as “life and death” — a weighty, double-edged pairing. In Japanese, 4 can be read <i>shi</i>, also a homophone for death, and many buildings skip fourth floors. Numbers containing 4 tend to be cheaper in East Asian markets for plates and phone numbers.</p>
<h2>In telecoms and the economy</h2><ul>
<li><b>UK:</b> 0343/0344/0345 are national-rate 03 numbers used by banks, government and charities — part of a UK-wide shift away from costly 08 numbers.</li>
<li><b>Pakistan:</b> 034x is the mobile range of Telenor Pakistan — one of the country's largest networks, now part of a PTCL–Ufone consolidation.</li>
<li><b>Philippines:</b> (034) is Negros Occidental, a sugar and BPO economy centred on Bacolod.</li>
<li><b>Netherlands, Italy, India:</b> 034x area codes cover regional towns from Harderwijk to Lecco to Asansol.</li>
<li><b>Spain:</b> 0034 is the international way to dial +34.</li></ul>
<h2>In sport, science &amp; culture</h2><p>34 is the ninth Fibonacci number, the atomic number of selenium, and a common squad number. 0.34 appears often as a probability or ratio — and “034” is a frequent product and model code.</p>
<div class="callout">034034.com is a neutral informational site. It does not claim any trademark in the number 034034 or its parts.</div>
<p><a class="btn btn-primary" href="lookup.html">Check a 034 number now</a></p>
</div></section>""" + support_strip())

# ---------------- ABOUT ----------------
PAGES["about.html"] = ("About 034034 — Independent 034 Number Intelligence | 034034",
 "034034.com is an independent, privacy-first guide to phone numbers starting with 034 across seven countries.",
 page_hero("About 034034", "Independent, privacy-first, and focused on one thing: helping people understand the numbers that call them.", ["About"]) + """
<section><div class="container grid g3">
<div class="card"><h3>Our mission</h3><p class="muted">Cut phone fraud by giving everyone a fast, free way to understand a 034 number before they answer or call back.</p></div>
<div class="card"><h3>Our principles</h3><ul class="list-check"><li>No personal subscriber data, ever</li><li>Official sources first</li><li>Moderated community reports</li><li>Clear labelling of ads &amp; sponsors</li></ul></div>
<div class="card"><h3>How we make money</h3><p class="muted">Display ads (Google AdSense), sponsorships, business-phone referrals, verified listings and reader donations. Editorial content is never for sale.</p></div>
</div></section>""" + support_strip())

# ---------------- LEGAL ----------------
def legal(fn, title, h1, html):
    PAGES[fn] = (title + " | 034034", title + " for 034034.com.", page_hero(h1, f"Last updated {TODAY}.", [h1]) + f'<section><div class="container prose">{html}</div></section>')

legal("privacy.html", "Privacy Policy", "Privacy policy", """
<p>034034.com (“we”) respects your privacy. This policy explains what we collect and why.</p>
<h2>What we collect</h2><ul><li><b>Lookups:</b> numbers you type are processed in your browser and are not stored by us.</li><li><b>Forms:</b> when you submit a form (report, quote, contact, donation pledge, contest, job application) we receive the details you enter, via a third-party form-delivery service.</li><li><b>Cookies:</b> we and our partners (including Google) use cookies for ads, measurement and preferences.</li></ul>
<h2>Advertising</h2><p>We use Google AdSense. Google and its partners use cookies to serve ads based on your visits to this and other sites. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> and learn more at <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener">How Google uses information from sites that use its services</a>. Visitors in the EEA, UK and Switzerland are shown a consent choice.</p>
<h2>Lead forms</h2><p>If you request quotes, we share your details only with up to three matched providers, for that purpose, and only with your consent.</p>
<h2>Embedded content</h2><p>Videos load from YouTube in privacy-enhanced mode only after you press play.</p>
<h2>Your rights</h2><p>You may request access, correction or deletion of data you sent us via our <a href="contact.html">contact form</a>. We keep form submissions only as long as needed.</p>
<h2>Children</h2><p>The site is not directed at children under 13.</p>""")
legal("terms.html", "Terms of Use", "Terms of use", """
<p>By using 034034.com you agree to these terms.</p>
<h2>Information only</h2><p>Lookups describe number types and regions using public numbering plans. They are not a guarantee of who is calling. Caller ID can be spoofed.</p>
<h2>Community reports</h2><p>Reports reflect users' opinions. You must not post personal data, defamatory statements or abuse. We may edit or remove any content.</p>
<h2>Contests</h2><p>Each contest is governed by the rules published on the <a href="contests.html">contests page</a>. Void where prohibited.</p>
<h2>Donations</h2><p>Donations support site operations and are not tax-deductible unless stated otherwise. Pledges are confirmed by email before any payment.</p>
<h2>Liability</h2><p>The site is provided “as is”. To the extent permitted by law we are not liable for losses arising from use of the site.</p>
<h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>""")
legal("disclaimer.html", "Disclaimer, Trademark & Copyright Disclosure", "Disclaimer &amp; trademarks", """
<h2>Trademark disclosure</h2><p>“034034” is used on this website solely as a descriptive numeric domain name and as a reference to telephone numbering. 034034.com does not claim trademark rights in the number 034034, the sequence “034”, or any telephone prefix, and does not intend to suggest any connection to any person or company that may use those digits.</p>
<p>034034.com is <b>independent</b> and is <b>not affiliated with, endorsed by or sponsored by</b> any telecom operator, regulator or government body, including Ofcom, PTA, PTCL, Ufone, Telenor, NTC, TRAI, or any bank. All company names, product names, logos and trademarks mentioned are the property of their respective owners and are used for identification and informational purposes only (nominative use).</p>
<h2>Copyright</h2><p>Original text, design, code and graphics on this site are © 034034.com. Numbering-plan facts are public information. Third-party content, if any, is used with permission or under applicable exceptions and is credited. If you believe your copyright has been infringed, please use our <a href="contact.html">contact form</a> with details and we will respond promptly.</p>
<h2>No professional advice</h2><p>Content is general information, not legal, financial or security advice. In an emergency or if you have lost money, contact your bank and local police immediately.</p>
<h2>Affiliate &amp; advertising disclosure</h2><p>We may earn a fee when you request quotes or follow certain links, and we display ads. This never affects our safety guidance.</p>""")

# ---------------- 404 ----------------
PAGES["404.html"] = ("Page not found | 034034", "Page not found.",
 page_hero("404 — number not in service", "The page you dialled doesn't exist. Try a lookup instead.", None, lookup_form("redirect")))


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    for fn, val in PAGES.items():
        title, desc, body = val[0], val[1], val[2]
        schema = val[3] if len(val) > 3 else ""
        with open(os.path.join(root, fn), "w", encoding="utf-8") as f:
            f.write(layout(fn, title, desc, body, schema))
    urls = "".join(f"<url><loc>{DOMAIN}{'' if fn=='index.html' else fn}</loc><lastmod>{TODAY}</lastmod></url>\n"
                   for fn in PAGES if fn != "404.html")
    with open(os.path.join(root, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print(f"Built {len(PAGES)} pages")

if __name__ == "__main__":
    main()
