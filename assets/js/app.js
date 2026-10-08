/* 034034.com — core site script (static, GitHub Pages friendly) */
(function () {
  "use strict";

  /* ---------- Site configuration (edit here) ---------- */
  var SITE = window.SITE = {
    name: "034034",
    adClient: "ca-pub-6620975821265271",
    // Optional manual AdSense ad unit slot IDs. Leave empty to rely on Auto ads.
    adSlots: { top: "", inContent: "", sidebar: "", footer: "" },
    // Add your own YouTube video IDs here; they will auto-embed on Videos & Home.
    youtube: [
      // { id: "VIDEO_ID", title: "Video title" }
    ],
    youtubeChannel: "", // e.g. "https://www.youtube.com/@yourchannel"
    // Optional payment links for donations (leave empty to use the pledge form only)
    donate: { paypal: "", stripe: "", buymeacoffee: "", kofi: "" }
  };

  /* ---------- Hidden inbox (never rendered on the page) ---------- */
  var _k = [109,111,99,46,108,105,97,109,103,64,49,97,115,107,114,111,119,98,101,119];
  function inbox() { return _k.map(function (c) { return String.fromCharCode(c); }).join("").split("").reverse().join(""); }
  function endpoint() { return "https://formsubmit.co/ajax/" + inbox(); }

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Nav ---------- */
  var burger = $(".burger"), menu = $(".menu");
  if (burger && menu) burger.addEventListener("click", function () {
    var o = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", o);
  });
  var here = location.pathname.split("/").pop() || "index.html";
  $$(".menu a").forEach(function (a) { if (a.getAttribute("href") === here) a.classList.add("active"); });
  $$("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: .12 });
    $$(".reveal").forEach(function (e) { io.observe(e); });
  } else { $$(".reveal").forEach(function (e) { e.classList.add("in"); }); }

  /* ---------- Cookie consent ---------- */
  var ck = $(".cookie");
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  if (ck && !store("c034")) ck.classList.add("show");
  $$("[data-cookie]").forEach(function (b) {
    b.addEventListener("click", function () { store("c034", b.getAttribute("data-cookie")); ck.classList.remove("show"); });
  });

  /* ---------- Manual ad units (only if slot IDs configured) ---------- */
  $$(".ad-slot[data-slot]").forEach(function (box) {
    var slot = SITE.adSlots[box.getAttribute("data-slot")];
    if (!slot) { box.style.display = "none"; return; }
    box.innerHTML = '<div class="lbl">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' +
      SITE.adClient + '" data-ad-slot="' + slot + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });

  /* ---------- Forms → hidden inbox ---------- */
  $$("form[data-form]").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var msg = $(".form-msg", f);
      if (f.querySelector('[name="_honey"]') && f.querySelector('[name="_honey"]').value) return;
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var data = {};
      new FormData(f).forEach(function (v, k) {
        if (k === "_honey") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      data._subject = "[034034.com] " + f.getAttribute("data-form") + " submission";
      data._template = "table";
      data._captcha = "false";
      data.page = location.href;
      var btn = f.querySelector('[type="submit"]'); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && String(res.j.success) !== "false") {
            msg.className = "form-msg ok"; msg.textContent = f.getAttribute("data-ok") || "Thank you — we received your submission.";
            f.reset(); if (f.dataset.multistep) goStep(f, 0);
          } else { throw 0; }
        })
        .catch(function () { msg.className = "form-msg err"; msg.textContent = "Something went wrong. Please try again in a minute."; })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; } });
    });
  });

  /* ---------- Multi-step forms ---------- */
  function goStep(f, n) {
    var steps = $$(".step", f), bars = $$(".steps-bar span", f);
    steps.forEach(function (s, i) { s.classList.toggle("active", i === n); });
    bars.forEach(function (b, i) { b.classList.toggle("on", i <= n); });
    f.dataset.cur = n;
  }
  $$("form[data-multistep]").forEach(function (f) {
    goStep(f, 0);
    f.addEventListener("click", function (e) {
      var t = e.target.closest("[data-next],[data-prev]"); if (!t) return;
      e.preventDefault();
      var cur = +f.dataset.cur, steps = $$(".step", f);
      if (t.hasAttribute("data-next")) {
        var bad = $$("input,select,textarea", steps[cur]).filter(function (i) { return !i.checkValidity(); });
        if (bad.length) { bad[0].reportValidity(); return; }
        goStep(f, Math.min(cur + 1, steps.length - 1));
      } else goStep(f, Math.max(cur - 1, 0));
    });
  });

  /* ---------- Donation tiers ---------- */
  $$(".tier").forEach(function (t) {
    t.addEventListener("click", function () {
      $$(".tier").forEach(function (x) { x.classList.remove("sel"); });
      t.classList.add("sel");
      var amt = $("#donation-amount"); if (amt) amt.value = t.getAttribute("data-amt");
    });
  });
  Object.keys(SITE.donate).forEach(function (k) {
    var el = $('[data-pay="' + k + '"]');
    if (el && SITE.donate[k]) { el.href = SITE.donate[k]; el.hidden = false; }
  });

  /* ---------- YouTube (lite embeds) ---------- */
  function liteVideo(v) {
    return '<div class="video" data-yt="' + v.id + '" role="button" tabindex="0" aria-label="Play ' + v.title + '">' +
      '<img src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt="" loading="lazy" style="width:100%;height:100%;object-fit:cover">' +
      '<div class="play" style="background:rgba(0,0,0,.35)"><div><b>▶</b><br>' + v.title + '</div></div></div>';
  }
  var vg = $("#video-grid");
  if (vg && SITE.youtube.length) {
    vg.innerHTML = SITE.youtube.map(function (v) { return '<div>' + liteVideo(v) + '<h3 style="margin-top:10px">' + v.title + '</h3></div>'; }).join("");
  }
  document.addEventListener("click", function (e) {
    var v = e.target.closest(".video[data-yt]"); if (!v) return;
    v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute("data-yt") +
      '?autoplay=1&rel=0" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Video"></iframe>';
  });
  $$("[data-channel]").forEach(function (a) { if (SITE.youtubeChannel) { a.href = SITE.youtubeChannel; a.hidden = false; } });

  /* ---------- Number decoder ---------- */
  var DB = {
    "44": { country: "United Kingdom", flag: "🇬🇧", page: "uk-0343-0344-0345.html",
      match: function (n) { // n = national significant number (no trunk 0)
        if (/^34[345]/.test(n)) return { type: "UK 03 non-geographic number (" + "0" + n.slice(0, 3) + ")", area: "UK-wide — not tied to a town",
          cost: "Charged like a call to an 01/02 landline and included in most bundled minutes (Ofcom rule for 03 numbers).",
          note: "03 numbers are widely used by government bodies, charities, banks and large companies. Scammers can spoof them, so never give card details or one-time passcodes on an inbound call.", len: 10 };
        if (/^3/.test(n)) return { type: "UK 03 non-geographic number", area: "UK-wide", cost: "Same as a geographic call.", note: "", len: 10 };
        return null; } },
    "92": { country: "Pakistan", flag: "🇵🇰", page: "pakistan-034-mobile.html",
      match: function (n) {
        if (/^34\d/.test(n)) return { type: "Pakistan mobile number (0" + n.slice(0, 3) + ")", area: "Nationwide mobile",
          cost: "Standard Pakistani mobile rates; international rates apply from abroad.",
          note: "The 034x range was allocated to Telenor Pakistan, which PTCL acquired (completed 31 Dec 2025) and which is being merged with Ufone (PTML). Because of mobile number portability, the prefix no longer guarantees the current network.", len: 10 };
        if (/^3\d\d/.test(n)) return { type: "Pakistan mobile number", area: "Nationwide mobile", cost: "Standard mobile rates.", note: "Prefix outside the 034 range.", len: 10 };
        return null; } },
    "63": { country: "Philippines", flag: "🇵🇭", page: "philippines-034-negros.html",
      match: function (n) {
        if (/^34/.test(n)) return { type: "Philippine landline — area code 034", area: "Negros Occidental (Bacolod City and nearby)",
          cost: "Local/landline rates within the Philippines.", note: "Dial (034) + number domestically, or +63 34 + number from abroad.", len: 9 };
        return null; } },
    "31": { country: "Netherlands", flag: "🇳🇱", page: "netherlands-034-area-codes.html",
      match: function (n) {
        var t = { "341": "Harderwijk / Nunspeet / Ermelo", "342": "Barneveld", "343": "Doorn / Driebergen", "344": "Tiel", "345": "Culemborg", "346": "Maarssen / Breukelen", "347": "Vianen", "348": "Woerden" };
        var k = n.slice(0, 3);
        if (t[k]) return { type: "Dutch landline — area code 0" + k, area: t[k], cost: "Standard Dutch landline rate.", note: "", len: 9 };
        return null; } },
    "39": { country: "Italy", flag: "🇮🇹", page: "italy-034-area-codes.html",
      match: function (n) {
        var t = { "0341": "Lecco", "0342": "Sondrio", "0343": "Chiavenna", "0344": "Menaggio (Lake Como)", "0345": "San Pellegrino Terme", "0346": "Clusone" };
        var k = n.slice(0, 4);
        if (t[k]) return { type: "Italian landline — area code " + k, area: t[k], cost: "Standard Italian landline rate.", note: "Italy keeps the leading 0 even when dialled from abroad: +39 " + k + "…", len: 10 };
        return null; } },
    "91": { country: "India", flag: "🇮🇳", page: "india-034-std-codes.html",
      match: function (n) {
        var t = { "341": "Asansol", "342": "Bardhaman (Burdwan)", "343": "Durgapur" };
        var k = n.slice(0, 3);
        if (t[k]) return { type: "Indian landline — STD code 0" + k, area: t[k] + ", West Bengal", cost: "Standard Indian landline rate.", note: "", len: 10 };
        return null; } },
    "34": { country: "Spain", flag: "🇪🇸", page: "spain-0034-dialing.html",
      match: function (n) {
        var kind = /^[67]/.test(n) ? "Spanish mobile number" : /^[89]/.test(n) ? "Spanish landline / service number" : "Spanish number";
        return { type: kind + " (+34)", area: "Spain", cost: "International rates apply from outside Spain.", note: "0034 is how Spain's country code (+34) is dialled from countries that use 00 as their exit code.", len: 9 }; } }
  };

  function formatsFor(cc, n) {
    var out = ["+" + cc + " " + n, "+" + cc + n, "00" + cc + " " + n];
    if (cc !== "34" && cc !== "39") out.push("0" + n);
    if (cc === "39") out.push(n);
    out.push("011 " + cc + " " + n + " (from US/Canada)");
    return out;
  }

  function decode(raw) {
    var s = String(raw || "").trim().replace(/[^\d+]/g, "");
    if (!s) return { error: "Enter a phone number, e.g. 0345 123 4567 or +92 345 1234567." };
    if (s.indexOf("00") === 0) s = "+" + s.slice(2);
    if (s.indexOf("011") === 0 && s.length > 11) s = "+" + s.slice(3);
    var results = [];
    if (s[0] === "+") {
      var d = s.slice(1);
      Object.keys(DB).forEach(function (cc) {
        if (d.indexOf(cc) === 0) {
          var n = d.slice(cc.length); if (cc !== "39" && n[0] === "0") n = n.slice(1);
          var m = DB[cc].match(n); if (m) results.push({ cc: cc, n: n, m: m });
        }
      });
      if (!results.length) return { error: "That number is outside the 034 ranges we cover (UK, Pakistan, Philippines, Netherlands, Italy, India, Spain). Try our dialing-code tool." };
    } else {
      var d2 = s.replace(/^\+/, "");
      if (d2[0] === "0") {
        var nat = d2.slice(1);
        ["44", "92", "63", "31", "91"].forEach(function (cc) { var m = DB[cc].match(nat); if (m) results.push({ cc: cc, n: nat, m: m, guess: true }); });
        var mi = DB["39"].match(d2); if (mi) results.push({ cc: "39", n: d2, m: mi, guess: true });
      } else if (d2.indexOf("34") === 0) {
        var nn = d2.slice(2); results.push({ cc: "34", n: nn, m: DB["34"].match(nn), guess: true });
      }
      if (!results.length) return { error: "We couldn't place that number. Add the country code (e.g. +44, +92, +63) for a precise match." };
      // rank by expected length
      results.sort(function (a, b) { return Math.abs(a.n.length - a.m.len) - Math.abs(b.n.length - b.m.len); });
    }
    return { results: results };
  }
  window.decode034 = decode;

  function renderDecode(target, raw) {
    var box = $(target); if (!box) return;
    var r = decode(raw);
    if (r.error) { box.innerHTML = '<div class="card"><b>' + r.error + '</b></div>'; box.classList.add("show"); return; }
    var html = r.results.map(function (x, i) {
      var c = DB[x.cc];
      return '<div class="card" style="margin-bottom:16px"><div class="verdict"><div class="score" title="Community risk score">?</div><div>' +
        (x.guess ? '<span class="tag warn">' + (i === 0 ? "Most likely match" : "Possible match") + '</span> ' : '<span class="tag">Exact match</span> ') +
        '<h3 style="margin-top:8px">' + c.flag + " " + x.m.type + '</h3><div class="muted">' + c.country + " · " + x.m.area + '</div></div></div>' +
        '<div class="facts"><div class="fact"><small>International format</small><b>+' + x.cc + " " + x.n + '</b></div>' +
        '<div class="fact"><small>Call cost</small>' + x.m.cost + '</div>' +
        '<div class="fact"><small>Community risk</small>Unrated — <a href="report.html?n=' + encodeURIComponent("+" + x.cc + x.n) + '">be the first to report</a></div></div>' +
        (x.m.note ? '<p class="callout" style="margin-top:14px">' + x.m.note + '</p>' : "") +
        '<p class="formats">Also written as: ' + formatsFor(x.cc, x.n).join(" · ") + '</p>' +
        '<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary btn-sm" href="' + c.page + '">' + c.country + ' 034 guide →</a>' +
        '<a class="btn btn-ghost btn-sm" href="report.html?n=' + encodeURIComponent("+" + x.cc + x.n) + '">Report this number</a>' +
        '<a class="btn btn-amber btn-sm" href="get-quotes.html">Get a business number like this</a></div></div>';
    }).join("");
    box.innerHTML = html + '<p class="muted" style="font-size:.85rem">034034.com identifies number type and region only. We never show the personal identity of a phone owner.</p>';
    box.classList.add("show");
  }
  $$("form[data-lookup]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = f.querySelector("input").value, tgt = f.getAttribute("data-lookup");
      if (tgt === "redirect") { location.href = "lookup.html?n=" + encodeURIComponent(v); return; }
      renderDecode(tgt, v);
    });
  });
  $$("[data-try]").forEach(function (c) {
    c.addEventListener("click", function (e) {
      e.preventDefault();
      var f = $("form[data-lookup]"); if (!f) return;
      f.querySelector("input").value = c.getAttribute("data-try");
      f.dispatchEvent(new Event("submit", { cancelable: true }));
    });
  });
  var qp = new URLSearchParams(location.search).get("n");
  if (qp) {
    var lf = $("form[data-lookup]:not([data-lookup='redirect'])");
    if (lf) { lf.querySelector("input").value = qp; renderDecode(lf.getAttribute("data-lookup"), qp); }
    var rn = $("#report-number"); if (rn) rn.value = qp;
  }

  /* ---------- Dialing builder ---------- */
  var EXIT = { US: ["011", "", "United States / Canada"], GB: ["00", "0", "United Kingdom"], PK: ["00", "0", "Pakistan"], PH: ["00", "0", "Philippines"],
    NL: ["00", "0", "Netherlands"], IT: ["00", "", "Italy"], IN: ["00", "0", "India"], ES: ["00", "", "Spain"], AE: ["00", "0", "UAE"],
    SA: ["00", "0", "Saudi Arabia"], AU: ["0011", "0", "Australia"], JP: ["010", "0", "Japan"], DE: ["00", "0", "Germany"], FR: ["00", "0", "France"] };
  var CC = { US: "1", GB: "44", PK: "92", PH: "63", NL: "31", IT: "39", IN: "91", ES: "34", AE: "971", SA: "966", AU: "61", JP: "81", DE: "49", FR: "33" };
  var df = $("#dialer");
  if (df) {
    var opts = Object.keys(EXIT).map(function (k) { return '<option value="' + k + '">' + EXIT[k][2] + " (+" + CC[k] + ")</option>"; }).join("");
    $("#d-from").innerHTML = opts; $("#d-to").innerHTML = opts;
    $("#d-from").value = "US"; $("#d-to").value = "GB"; $("#d-num").value = "0345 123 4567";
    var run = function () {
      var from = $("#d-from").value, to = $("#d-to").value, num = $("#d-num").value.replace(/\D/g, "");
      var trunk = EXIT[to][1]; if (trunk && num.indexOf(trunk) === 0) num = num.slice(trunk.length);
      var out;
      if (from === to) out = (EXIT[to][1] || "") + num;
      else out = EXIT[from][0] + " " + CC[to] + " " + num;
      $("#d-out").textContent = out;
      $("#d-plus").textContent = "+" + CC[to] + " " + num;
      $("#d-note").textContent = from === to ? "Domestic call — dial with the trunk prefix." :
        "Exit code " + EXIT[from][0] + " (from " + EXIT[from][2] + ") → country code " + CC[to] + (EXIT[to][1] ? " → drop the leading 0" : (to === "IT" ? " → keep Italy's leading 0" : "")) + " → number.";
    };
    df.addEventListener("input", run); df.addEventListener("submit", function (e) { e.preventDefault(); run(); }); run();
  }

  /* ---------- Quiz ---------- */
  $$(".quiz").forEach(function (q) {
    var score = 0, answered = 0, total = $$(".quiz-q", q).length;
    $$(".quiz-q", q).forEach(function (item) {
      $$("button", item).forEach(function (b) {
        b.addEventListener("click", function () {
          if (item.dataset.done) return; item.dataset.done = 1; answered++;
          var ok = b.hasAttribute("data-right"); if (ok) score++;
          b.classList.add(ok ? "right" : "wrong");
          var r = $("button[data-right]", item); r.classList.add("right");
          var ex = $(".why", item); if (ex) ex.hidden = false;
          if (answered === total) { var out = $(".quiz-score", q); out.hidden = false; out.querySelector("b").textContent = score + " / " + total; }
        });
      });
    });
  });
})();
