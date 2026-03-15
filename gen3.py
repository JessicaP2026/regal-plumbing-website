import json, os, random

OUT = r"C:\Users\Nick\Projects\regal-plumbing-website\elementor-templates"
os.makedirs(OUT, exist_ok=True)

used_ids = set()
def uid():
    while True:
        i = ''.join(random.choices('0123456789abcdef', k=8))
        if i not in used_ids:
            used_ids.add(i)
            return i

SCHEMA = "{\"@context\":\"https://schema.org\",\"@type\":\"Plumber\",\"name\":\"Regal Plumbing & Rooter\",\"address\":{\"@type\":\"PostalAddress\",\"streetAddress\":\"2141 E Philadelphia St Suite R\",\"addressLocality\":\"Ontario\",\"addressRegion\":\"CA\",\"postalCode\":\"91761\"},\"telephone\":\"+19096004561\",\"openingHours\":\"Mo-Sa 07:00-19:00\",\"areaServed\":\"Inland Empire CA\"}"

EMERGENCY_BAR = """<style>.emergency-bar{background:#2D2D2D;color:#fff;text-align:center;padding:9px 16px;font-size:13.5px;font-weight:600;font-family:'Open Sans',sans-serif;letter-spacing:.3px}.emergency-bar a{color:#fca5a5;text-decoration:underline;text-underline-offset:2px}</style>
<div class="emergency-bar">24/7 Emergency Service Available - Call <a href="tel:9096004561">(909) 600-4561</a></div>"""

def header_html(active=""):
    nav_links = [("/","Home"),("/services/","Services"),("/about/","About"),("/service-area/","Service Area"),("/contact/","Contact")]
    nav_items = ""
    for href, label in nav_links:
        cls = ' class="active"' if label == active else ""
        nav_items += f'<a href="{href}"{cls}>{label}</a>\n      '
    return f"""<style>.site-header{{background:#fff;box-shadow:0 2px 12px rgba(0,0,0,.10)}}.header-inner{{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;gap:24px;height:72px}}.logo{{display:flex;align-items:center;gap:12px;flex-shrink:0}}.site-nav{{display:flex;align-items:center;gap:6px}}.site-nav a{{font-family:'Oswald',sans-serif;font-weight:500;font-size:14px;letter-spacing:1.2px;text-transform:uppercase;color:#2D2D2D;padding:8px 12px;border-radius:4px;text-decoration:none;transition:color .2s,background .2s}}.site-nav a:hover,.site-nav a.active{{color:#B91C1C;background:#FEF2F2}}.header-right{{display:flex;align-items:center;gap:14px;flex-shrink:0}}.header-phone{{font-family:'Oswald',sans-serif;font-weight:600;font-size:16px;color:#1E3A6E;letter-spacing:.5px;text-decoration:none}}.btn-red{{display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;border:2px solid #B91C1C;text-decoration:none}}@media(max-width:640px){{.site-nav{{display:none}}}}</style>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Open+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<header class="site-header">
  <div class="header-inner">
    <a href="/" class="logo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumbing-logo.png" alt="Regal Plumbing and Rooter logo" style="height:56px;width:auto;" /></a>
    <nav class="site-nav">
      {nav_items}</nav>
    <div class="header-right">
      <a href="tel:9096004561" class="header-phone">(909) 600-4561</a>
      <a href="tel:9096004561" class="btn-red">Call Now</a>
    </div>
  </div>
</header>"""

FOOTER = """<style>.site-footer{background:#2D2D2D;color:#fff;padding:64px 24px 0}.footer-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.6fr 1fr 1fr 1.3fr;gap:48px;padding-bottom:48px;border-bottom:1px solid rgba(255,255,255,.10)}.footer-logo-name{font-family:'Oswald',sans-serif;font-weight:700;font-size:18px;color:#fff;letter-spacing:1px;text-transform:uppercase;margin-bottom:6px}.footer-tagline{font-size:13px;color:#9CA3AF;margin-bottom:16px;line-height:1.6}.footer-license{display:inline-block;background:rgba(185,28,28,.2);border:1px solid rgba(185,28,28,.4);color:#fca5a5;font-size:11.5px;font-family:'Oswald',sans-serif;letter-spacing:1px;padding:4px 10px;border-radius:3px}.footer-col h4{font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:18px;padding-bottom:10px;border-bottom:2px solid #B91C1C;display:inline-block}.footer-links{list-style:none;display:flex;flex-direction:column;gap:9px;padding:0}.footer-links a{font-size:13.5px;color:#9CA3AF;text-decoration:none;display:flex;align-items:center;gap:6px}.footer-links a::before{content:"\u203a";color:#B91C1C;font-size:16px}.footer-contact-list{list-style:none;display:flex;flex-direction:column;gap:12px;padding:0}.footer-contact-list li{display:flex;gap:10px;font-size:13.5px;color:#9CA3AF;line-height:1.5}.footer-contact-list a{color:#9CA3AF;text-decoration:none}.footer-bottom{max-width:1200px;margin:0 auto;padding:18px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}.footer-bottom-text{font-size:12.5px;color:#6B7280}.footer-bottom-links{display:flex;gap:20px}.footer-bottom-links a{font-size:12.5px;color:#6B7280;text-decoration:none}@media(max-width:900px){.footer-inner{grid-template-columns:1fr 1fr;gap:32px}}@media(max-width:640px){.footer-inner{grid-template-columns:1fr;gap:28px}.footer-bottom{flex-direction:column;text-align:center}}</style>
<footer class="site-footer">
  <div class="footer-inner">
    <div><div class="footer-logo-name">Regal Plumbing &amp; Rooter</div><p class="footer-tagline">Honest, professional plumbing &amp; rooter services for the Inland Empire &amp; San Gabriel Valley.</p><span class="footer-license">CA License #1097482</span></div>
    <div class="footer-col"><h4>Services</h4><ul class="footer-links"><li><a href="/emergency-plumbing/">Emergency Plumbing</a></li><li><a href="/drain-cleaning/">Drain Cleaning</a></li><li><a href="/sewer-line-repair/">Sewer Line Repair</a></li><li><a href="/water-heater-services/">Water Heater Services</a></li><li><a href="/slab-leak-detection/">Slab Leak Detection</a></li><li><a href="/hydrojetting/">Hydrojetting</a></li><li><a href="/gas-leak-detection/">Gas Leak Detection</a></li><li><a href="/water-filtration/">Water Filtration</a></li></ul></div>
    <div class="footer-col"><h4>Service Area</h4><ul class="footer-links"><li><a href="/service-area/ontario-ca/">Ontario</a></li><li><a href="/service-area/rancho-cucamonga-ca/">Rancho Cucamonga</a></li><li><a href="/service-area/fontana-ca/">Fontana</a></li><li><a href="/service-area/pomona-ca/">Pomona</a></li><li><a href="/service-area/chino-ca/">Chino</a></li><li><a href="/service-area/corona-ca/">Corona</a></li><li><a href="/service-area/upland-ca/">Upland</a></li><li><a href="/service-area/west-covina-ca/">West Covina</a></li></ul></div>
    <div class="footer-col"><h4>Contact Us</h4><ul class="footer-contact-list"><li><span>📍</span><span>2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</span></li><li><span>📞</span><a href="tel:9096004561">(909) 600-4561</a></li><li><span>✉️</span><a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></li><li><span>🕐</span><span>24/7 Emergency<br>Mon–Sat: 7am–7pm</span></li></ul></div>
  </div>
  <div class="footer-bottom"><span class="footer-bottom-text">© 2025 Regal Plumbing &amp; Rooter. All Rights Reserved. CA License #1097482</span><div class="footer-bottom-links"><a href="/privacy-policy/">Privacy Policy</a><a href="/terms-of-service/">Terms of Service</a><a href="/sitemap/">Sitemap</a></div></div>
</footer>"""

def cta_html(heading, subtext):
    return f"""<style>.cta-section{{background:#B91C1C;padding:64px 24px;text-align:center;position:relative;overflow:hidden}}.cta-section::before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent,transparent 8px,rgba(0,0,0,.04) 8px,rgba(0,0,0,.04) 10px)}}.cta-inner{{position:relative;z-index:2;max-width:700px;margin:0 auto}}.cta-inner h2{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,4vw,42px);color:#fff;letter-spacing:1px;text-transform:uppercase;margin-bottom:12px}}.cta-sub{{font-size:16px;color:rgba(255,255,255,.85);margin-bottom:24px}}.cta-phone{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,5vw,50px);color:#fff;letter-spacing:2px;margin-bottom:28px;display:block;text-decoration:none}}.btn-white-red{{display:inline-flex;align-items:center;padding:14px 32px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;background:#fff;color:#B91C1C;border:2px solid #fff;text-decoration:none}}</style>
<section class="cta-section"><div class="cta-inner"><h2>{heading}</h2><p class="cta-sub">{subtext}</p><a href="tel:9096004561" class="cta-phone">(909) 600-4561</a><br><a href="tel:9096004561" class="btn-white-red">📞 Call Now</a></div></section>"""

def img_hero_html(img_src, img_alt, breadcrumb_items, badge, h1, sub):
    bc = ""
    for label, href in breadcrumb_items:
        if href:
            bc += f'<a href="{href}" style="color:#9CA3AF;text-decoration:none">{label}</a><span style="color:#4B5563"> › </span>'
        else:
            bc += f'<span style="color:#fca5a5">{label}</span>'
    badge_html = f'<span style="display:inline-block;background:#B91C1C;color:#fff;font-family:Oswald,sans-serif;font-weight:600;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;padding:5px 14px;border-radius:3px;margin-bottom:16px">{badge}</span>' if badge else ""
    return f"""<style>.svc-hero{{position:relative;overflow:hidden;min-height:320px;display:flex;align-items:center}}.svc-hero-bg{{position:absolute;inset:0}}.svc-hero-bg img{{width:100%;height:100%;object-fit:cover}}.svc-hero-overlay{{position:absolute;inset:0;background:linear-gradient(105deg,rgba(0,0,0,.85) 0%,rgba(30,58,110,.65) 60%,rgba(185,28,28,.25) 100%)}}.svc-hero-inner{{position:relative;z-index:2;max-width:1200px;margin:0 auto;padding:72px 24px;width:100%}}.breadcrumb{{display:flex;align-items:center;gap:6px;font-size:13px;color:#9CA3AF;margin-bottom:14px;flex-wrap:wrap}}.svc-hero h1{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,52px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}.svc-hero-sub{{font-size:17px;color:#D1D5DB;max-width:600px;line-height:1.6}}</style>
<div class="svc-hero"><div class="svc-hero-bg"><img src="{img_src}" alt="{img_alt}" loading="eager" /></div><div class="svc-hero-overlay"></div><div class="svc-hero-inner"><div class="breadcrumb">{bc}</div>{badge_html}<h1>{h1}</h1><p class="svc-hero-sub">{sub}</p></div></div>"""

def svc_overview(eyebrow, h2, body_paras, features, img_src, img_alt, btn_label, btn_href):
    features_html = "".join(f"<li>{f}</li>" for f in features)
    btn = f'<a href="{btn_href}" style="display:inline-flex;align-items:center;padding:12px 24px;border-radius:4px;font-family:Oswald,sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;text-decoration:none">{btn_label}</a>'
    paras = "".join(f'<p style="font-size:15.5px;color:#4B5563;line-height:1.8;margin-bottom:18px">{p}</p>' for p in body_paras)
    return f"""<style>.ov-section{{background:#fff;padding:80px 24px}}.ov-inner{{max-width:1200px;margin:0 auto}}.ov-grid{{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}}.ov-photo{{border-radius:10px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.15)}}.ov-photo img{{width:100%;height:420px;object-fit:cover;display:block}}.feat-list{{list-style:none;margin:0 0 28px;display:flex;flex-direction:column;gap:10px;padding:0}}.feat-list li{{display:flex;align-items:flex-start;gap:10px;font-size:15px;color:#2D2D2D}}.feat-list li::before{{content:"✓";color:#B91C1C;font-weight:700;flex-shrink:0;margin-top:1px}}@media(max-width:900px){{.ov-grid{{grid-template-columns:1fr;gap:40px}}}}</style>
<section class="ov-section"><div class="ov-inner"><div class="ov-grid">
  <div>
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:8px">{eyebrow}</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(24px,3vw,38px);color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px;line-height:1.15">{h2}</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0 24px"></div>
    {paras}<ul class="feat-list">{features_html}</ul>{btn}
  </div>
  <div class="ov-photo"><img src="{img_src}" alt="{img_alt}" loading="lazy" /></div>
</div></div></section>"""

def covers_section(title, cards):
    cards_html = ""
    for icon, ctitle, desc in cards:
        cards_html += f'<div style="background:#fff;border-radius:8px;padding:28px 24px;border-top:3px solid #B91C1C;box-shadow:0 2px 12px rgba(0,0,0,.06)"><div style="font-size:28px;margin-bottom:14px">{icon}</div><div style="font-family:Oswald,sans-serif;font-weight:600;font-size:16px;text-transform:uppercase;letter-spacing:.5px;color:#2D2D2D;margin-bottom:8px">{ctitle}</div><p style="font-size:14px;color:#6B7280;line-height:1.7">{desc}</p></div>'
    return f"""<style>.cov-section{{background:#F3F4F6;padding:80px 24px}}.cov-inner{{max-width:1200px;margin:0 auto}}.cov-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:48px}}@media(max-width:900px){{.cov-grid{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:640px){{.cov-grid{{grid-template-columns:1fr}}}}</style>
<section class="cov-section"><div class="cov-inner">
  <div style="text-align:center"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">What We Cover</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">{title}</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div class="cov-grid">{cards_html}</div>
</div></section>"""

def why_section_html():
    return """<style>.why-sec{background:#1E3A6E;padding:80px 24px}.why-sec-inner{max-width:1200px;margin:0 auto}.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:48px}.why-card{text-align:center;padding:32px 24px}.why-icon{font-size:36px;display:block;margin-bottom:16px}.why-title{font-family:'Oswald',sans-serif;font-weight:600;font-size:18px;color:#fff;text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px}.why-desc{font-size:14px;color:#93C5FD;line-height:1.7}@media(max-width:640px){.why-grid{grid-template-columns:1fr}}</style>
<section class="why-sec"><div class="why-sec-inner">
  <div style="text-align:center"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#fca5a5;margin-bottom:10px">Our Promise</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);color:#fff;text-transform:uppercase;letter-spacing:.5px">Why Choose Regal?</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div class="why-grid">
    <div class="why-card"><span class="why-icon">💰</span><div class="why-title">Honest Pricing</div><p class="why-desc">Upfront, transparent quotes before any work begins. No hidden fees, no surprises.</p></div>
    <div class="why-card"><span class="why-icon">⚡</span><div class="why-title">Fast Response</div><p class="why-desc">24/7 availability for emergencies. We arrive quickly and work efficiently.</p></div>
    <div class="why-card"><span class="why-icon">🔧</span><div class="why-title">Quality Workmanship</div><p class="why-desc">Every job backed by our commitment to premium craftsmanship and lasting results.</p></div>
  </div>
</div></section>"""

OTHER_SERVICES = """<style>.other-svcs{background:#fff;padding:80px 24px}.other-svcs-inner{max-width:1200px;margin:0 auto}.other-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:48px}.other-card{background:#F3F4F6;border:1px solid #E5E7EB;border-radius:8px;padding:22px 20px;text-decoration:none;display:block;transition:box-shadow .2s,border-color .2s}.other-card:hover{box-shadow:0 4px 20px rgba(0,0,0,.10);border-color:#B91C1C}.other-name{font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;text-transform:uppercase;letter-spacing:.5px;color:#2D2D2D;margin-bottom:6px}.other-desc{font-size:13px;color:#6B7280;line-height:1.6;margin-bottom:12px}.other-link{font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#B91C1C}@media(max-width:900px){.other-grid{grid-template-columns:repeat(2,1fr)}}</style>
<section class="other-svcs"><div class="other-svcs-inner">
  <div style="text-align:center"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Explore</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Other Services We Offer</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div class="other-grid">
    <a href="/emergency-plumbing/" class="other-card"><div class="other-name">Emergency Plumbing</div><p class="other-desc">24/7 rapid-response for burst pipes, major leaks, and sewage backups.</p><span class="other-link">Learn More →</span></a>
    <a href="/drain-cleaning/" class="other-card"><div class="other-name">Drain Cleaning</div><p class="other-desc">Professional clearing of kitchen, bathroom, and main sewer line blockages.</p><span class="other-link">Learn More →</span></a>
    <a href="/sewer-line-repair/" class="other-card"><div class="other-name">Sewer Line Repair</div><p class="other-desc">Camera inspection, trenchless repair, and full sewer line replacement.</p><span class="other-link">Learn More →</span></a>
    <a href="/water-heater-services/" class="other-card"><div class="other-name">Water Heater Services</div><p class="other-desc">Installation and repair of tank, tankless, and heat pump water heaters.</p><span class="other-link">Learn More →</span></a>
    <a href="/slab-leak-detection/" class="other-card"><div class="other-name">Slab Leak Detection</div><p class="other-desc">Electronic leak detection beneath concrete slabs with minimal disruption.</p><span class="other-link">Learn More →</span></a>
    <a href="/hydrojetting/" class="other-card"><div class="other-name">Hydrojetting</div><p class="other-desc">High-pressure water jetting to scour pipe walls and restore full flow.</p><span class="other-link">Learn More →</span></a>
    <a href="/gas-leak-detection/" class="other-card"><div class="other-name">Gas Leak Detection</div><p class="other-desc">Licensed gas line detection, repair, and pressure testing for safety.</p><span class="other-link">Learn More →</span></a>
    <a href="/water-filtration/" class="other-card"><div class="other-name">Water Filtration</div><p class="other-desc">Whole-home softeners, reverse osmosis, and filtration systems installed.</p><span class="other-link">Learn More →</span></a>
  </div>
</div></section>"""

def make_container(html_content, bg_color="#FFFFFF"):
    return {
        "id": uid(), "elType": "container",
        "settings": {"content_width":"full","background_background":"classic","background_color":bg_color,"padding":{"top":"0","right":"0","bottom":"0","left":"0","unit":"px","isLinked":False}},
        "elements": [{"id":uid(),"elType":"widget","widgetType":"html","settings":{"html":html_content},"elements":[]}]
    }

def make_page(title, seo_title, seo_desc, sections_html):
    content = [make_container(html, bg) for html, bg in sections_html]
    return {
        "version":"0.4","title":title,"type":"page","content":content,
        "page_settings":{
            "post_title":title,"template":"elementor_canvas","_elementor_template_type":"page",
            "rank_math_title":seo_title,"rank_math_description":seo_desc,
            "rank_math_og_title":seo_title,"rank_math_og_description":seo_desc,
            "rank_math_schema_pro_markup":SCHEMA,"_elementor_edit_mode":"builder"
        }
    }

def save(filename, data):
    path = os.path.join(OUT, filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {filename}")

# ── 11. HYDROJETTING ──────────────────────────────────────────────────────────
hj_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/hydro-jetting-roof-rancho-cucamonga-ca.webp",
    "hydrojetting drain cleaning service Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Hydrojetting",None)],
    "High-Pressure Cleaning",
    "Hydrojetting",
    "High-pressure water jetting to clear roots, grease, and scale from drain and sewer lines throughout Southern California"
)
hj_overview = svc_overview(
    "The Most Effective Drain Cleaning",
    "Professional Hydrojetting Service",
    ["When snaking isn't enough, hydrojetting is the most effective method for clearing stubborn grease, scale, and root intrusion from drain and sewer lines. Using water at up to 4,000 PSI, hydrojetting scours pipe walls clean and restores full pipe capacity — ideal for commercial properties and recurring residential blockages."],
    ["Clears grease, scale, and hardened buildup","Removes tree root intrusion","Ideal for commercial kitchens and restaurants","Scours pipe walls — not just pokes a hole","Extends the life of your plumbing system","Combines well with camera inspection"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/hydro-jetting-roof-rancho-cucamonga-ca.webp",
    "hydrojetting drain cleaning service Inland Empire CA",
    "Get a Free Quote",
    "/contact/"
)
hj_covers = covers_section("When Hydrojetting Is the Right Choice", [
    ("🏢","Commercial Properties","Restaurants, food service, and commercial kitchens generate heavy grease loads that quickly coat pipe walls. Hydrojetting is the industry standard for these applications."),
    ("🌳","Root Intrusion","Tree roots that have infiltrated sewer lines can be shredded and flushed clear with hydrojetting — far more effective than snaking alone."),
    ("🔄","Recurring Blockages","If you're calling for drain cleaning every few months, hydrojetting provides a thorough deep clean that lasts far longer than mechanical snaking."),
])

save("hydrojetting.json", make_page(
    "Hydrojetting Service | Regal Plumbing & Rooter",
    "Hydrojetting Service | Regal Plumbing & Rooter",
    "Professional hydrojetting drain cleaning in the Inland Empire. High-pressure water jetting clears roots, grease & buildup. Call (909) 600-4561.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html("Services"),"#FFFFFF"),(hj_hero,"#111827"),(hj_overview,"#FFFFFF"),(hj_covers,"#F3F4F6"),(why_section_html(),"#1E3A6E"),(OTHER_SERVICES,"#FFFFFF"),(cta_html("Ready for a Deep Clean?","Hydrojetting removes what snaking can't — call now for a free quote"),"#B91C1C"),(FOOTER,"#2D2D2D")]
))

# ── 12. GAS LEAK DETECTION ────────────────────────────────────────────────────
gl_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/camera-inspection-drain-cleaning-san-bernardino-ca.webp",
    "gas leak detection Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Gas Leak Detection",None)],
    "Safety Critical — Call Immediately",
    "Gas Leak Detection",
    "Licensed gas leak detection and repair for the Inland Empire — safe, fast, and available 24/7 for emergencies"
)
gl_overview = svc_overview(
    "Safety First",
    "Professional Gas Leak Detection & Repair",
    ["A gas leak is a serious safety emergency. If you smell gas, leave the building immediately and call 911 first. Then call us. Our licensed plumbers perform precise gas leak detection and repair, ensuring your home or business is safe before restoring service. Never ignore a suspected gas leak."],
    ["Electronic gas leak detection equipment","Gas line repair and re-piping","Pressure testing after repair","Licensed for natural gas and propane systems","24/7 emergency availability","Post-repair safety verification"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/camera-inspection-drain-cleaning-san-bernardino-ca.webp",
    "gas leak detection Inland Empire CA",
    "📞 Call Now — (909) 600-4561",
    "tel:9096004561"
)
gl_covers = covers_section("Gas Leak Services We Provide", [
    ("🔍","Electronic Detection","We use advanced gas detection equipment to precisely locate leaks in gas supply lines — inside walls, under slabs, or in the yard."),
    ("🔧","Gas Line Repair","Once located, our licensed plumbers make the necessary repairs or replacements to restore safe, leak-free gas service to your home or business."),
    ("✅","Pressure Testing","After every gas leak repair, we perform thorough pressure testing to verify the entire system is sealed and safe before restoring gas service."),
])

save("gas-leak-detection.json", make_page(
    "Gas Leak Detection & Repair | Regal Plumbing & Rooter",
    "Gas Leak Detection & Repair | Regal Plumbing & Rooter",
    "Safe, fast gas leak detection and repair in the Inland Empire. Licensed & insured. Available 24/7 for emergencies. Call (909) 600-4561.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html("Services"),"#FFFFFF"),(gl_hero,"#111827"),(gl_overview,"#FFFFFF"),(gl_covers,"#F3F4F6"),(why_section_html(),"#1E3A6E"),(OTHER_SERVICES,"#FFFFFF"),(cta_html("Smell Gas? Get Out and Call Now","Leave the building, call 911, then call us — we respond immediately to gas emergencies"),"#B91C1C"),(FOOTER,"#2D2D2D")]
))

# ── 13. WATER FILTRATION ──────────────────────────────────────────────────────
wf_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-replacement-copper-ontario-ca.webp",
    "water filtration copper pipe installation Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Water Filtration",None)],
    "Cleaner, Softer Water",
    "Water Filtration & Softeners",
    "Whole-home water filtration and softener systems for the Inland Empire — clean, soft water from every tap"
)
wf_overview = svc_overview(
    "Protect Your Home & Family",
    "Water Filtration & Softener Installation",
    ["Southern California water is notoriously hard. Mineral buildup damages appliances, leaves residue on fixtures, and affects the taste and quality of your water. We install whole-home water softeners, under-sink filters, and reverse osmosis systems to give you cleaner, softer water throughout your home."],
    ["Whole-home water softener installation","Under-sink reverse osmosis systems","Carbon filtration and UV purification","Filter cartridge replacement service","Water quality testing available","Reduces scale buildup on appliances and pipes"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/copper-pipe-installation-chino-ca.webp",
    "water filtration copper pipe installation Inland Empire CA",
    "Get a Free Quote",
    "/contact/"
)
wf_covers = covers_section("Water Filtration Systems We Install", [
    ("💧","Whole-Home Softeners","Ion-exchange water softeners treat all water entering your home — protecting your water heater, pipes, appliances, and fixtures from hard water scale."),
    ("🔬","Reverse Osmosis","Under-sink RO systems deliver ultra-pure drinking water by removing minerals, chlorine, heavy metals, and contaminants at the point of use."),
    ("☀️","UV Purification","UV purification systems neutralize bacteria and microorganisms in your water supply, providing an additional layer of safety for your family."),
])

save("water-filtration.json", make_page(
    "Water Filtration & Softeners | Regal Plumbing & Rooter",
    "Water Filtration & Softeners | Regal Plumbing & Rooter",
    "Whole-home water filtration and softener systems in the Inland Empire. Clean, soft water for your home. Licensed & local. Call (909) 600-4561.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html("Services"),"#FFFFFF"),(wf_hero,"#111827"),(wf_overview,"#FFFFFF"),(wf_covers,"#F3F4F6"),(why_section_html(),"#1E3A6E"),(OTHER_SERVICES,"#FFFFFF"),(cta_html("Ready for Cleaner Water?","Call for a free water quality consultation — licensed installation available"),"#B91C1C"),(FOOTER,"#2D2D2D")]
))

# ── CITY PAGE TEMPLATE ────────────────────────────────────────────────────────
def city_hero(city, state="CA"):
    return f"""<style>.city-hero{{background:#1E3A6E;position:relative;overflow:hidden;padding:64px 24px}}.city-hero::before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent,transparent 2px,rgba(255,255,255,.015) 2px,rgba(255,255,255,.015) 4px)}}.city-hero-inner{{position:relative;z-index:2;max-width:1200px;margin:0 auto}}.breadcrumb{{display:flex;align-items:center;gap:6px;font-size:13px;color:#93C5FD;margin-bottom:14px;flex-wrap:wrap}}.breadcrumb a{{color:#93C5FD;text-decoration:none}}.city-hero h1{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}.city-hero-sub{{font-size:16px;color:#93C5FD;max-width:580px}}</style>
<div class="city-hero"><div class="city-hero-inner">
  <div class="breadcrumb"><a href="/">Home</a><span style="color:rgba(255,255,255,.3)"> › </span><a href="/service-area/">Service Area</a><span style="color:rgba(255,255,255,.3)"> › </span><span style="color:rgba(255,255,255,.7)">{city} {state}</span></div>
  <h1>Plumber in {city}, {state}</h1>
  <p class="city-hero-sub">Licensed, local plumbing services for {city} homeowners and businesses — available 24/7 for emergencies and same-day scheduled work.</p>
</div></div>"""

def city_trust_bar():
    return """<style>.trust-bar{background:#F3F4F6;border-top:3px solid #B91C1C;border-bottom:1px solid #E5E7EB}.trust-bar-inner{max-width:1200px;margin:0 auto;display:flex;align-items:stretch}.trust-item{flex:1;display:flex;align-items:center;gap:12px;padding:18px 24px;border-right:1px solid #E5E7EB}.trust-item:last-child{border-right:none}.trust-icon{font-size:22px}.trust-label{font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px;line-height:1.2}.trust-label span{display:block;font-family:'Open Sans',sans-serif;font-weight:400;font-size:12px;color:#6B7280;text-transform:none;letter-spacing:0}@media(max-width:900px){.trust-bar-inner{flex-wrap:wrap}.trust-item{border-right:none;border-bottom:1px solid #E5E7EB;min-width:50%}}</style>
<div class="trust-bar"><div class="trust-bar-inner">
  <div class="trust-item"><span class="trust-icon">⏰</span><div class="trust-label">24/7 Emergency<span>Always Available</span></div></div>
  <div class="trust-item"><span class="trust-icon">👨‍👩‍👧</span><div class="trust-label">Family Owned<span>Community Focused</span></div></div>
  <div class="trust-item"><span class="trust-icon">✅</span><div class="trust-label">CA Licensed #1097482<span>Fully Insured</span></div></div>
  <div class="trust-item"><span class="trust-icon">⭐</span><div class="trust-label">4+ Years Experience<span>Proven Track Record</span></div></div>
  <div class="trust-item"><span class="trust-icon">📍</span><div class="trust-label">32+ Cities Served<span>Southern California</span></div></div>
</div></div>"""

def city_services(city):
    return f"""<style>.city-svcs{{background:#F3F4F6;padding:80px 24px}}.city-svcs-inner{{max-width:1200px;margin:0 auto}}.city-svc-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:48px}}.city-svc-card{{background:#fff;border-radius:8px;overflow:hidden;border:1px solid #E5E7EB;text-decoration:none;display:block;transition:box-shadow .25s,transform .25s}}.city-svc-card:hover{{box-shadow:0 8px 32px rgba(0,0,0,.10);transform:translateY(-4px)}}.city-svc-photo{{height:140px;overflow:hidden}}.city-svc-photo img{{width:100%;height:100%;object-fit:cover}}.city-svc-body{{padding:18px}}.city-svc-name{{font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;text-transform:uppercase;letter-spacing:.5px;color:#2D2D2D;margin-bottom:6px}}.city-svc-desc{{font-size:13px;color:#6B7280;line-height:1.6;margin-bottom:12px}}.city-svc-link{{font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#B91C1C}}@media(max-width:900px){{.city-svc-grid{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:640px){{.city-svc-grid{{grid-template-columns:1fr}}}}</style>
<section class="city-svcs"><div class="city-svcs-inner">
  <div style="text-align:center;margin-bottom:0">
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">What We Do</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Plumbing Services in {city}, CA</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
    <p style="font-size:15px;color:#6B7280;max-width:520px;margin:16px auto 0;line-height:1.65">Full-service plumbing for every situation — from routine maintenance to major repairs throughout {city}.</p>
  </div>
  <div class="city-svc-grid">
    <a href="/emergency-plumbing/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-repair-service-truck-inland-empire.webp" alt="Emergency Plumbing {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Emergency Plumbing</div><p class="city-svc-desc">24/7 rapid response for burst pipes, sewage backups, and major leaks in {city}.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/drain-cleaning/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/drain-cleaning-shower-upland-ca.webp" alt="Drain Cleaning {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Drain Cleaning</div><p class="city-svc-desc">Professional clearing of kitchen, bathroom, and main sewer lines in {city}.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/sewer-line-repair/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-line-repair-excavation-fontana-ca.webp" alt="Sewer Line Repair {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Sewer Line Repair</div><p class="city-svc-desc">Camera inspection and trenchless sewer repair options for {city} properties.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/water-heater-services/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sink-faucet-installation-ontario-ca.webp" alt="Water Heater Services {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Water Heater Services</div><p class="city-svc-desc">Tank and tankless water heater installation and repair throughout {city}.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/slab-leak-detection/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-repair-leak-detection-chino-hills-ca.webp" alt="Slab Leak Detection {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Slab Leak Detection</div><p class="city-svc-desc">Electronic slab leak detection with minimal disruption for {city} homes.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/hydrojetting/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/hydro-jetting-roof-rancho-cucamonga-ca.webp" alt="Hydrojetting {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Hydrojetting</div><p class="city-svc-desc">High-pressure hydrojetting clears scale, grease, and roots in {city} pipes.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/gas-leak-detection/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/camera-inspection-drain-cleaning-san-bernardino-ca.webp" alt="Gas Leak Detection {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Gas Leak Detection</div><p class="city-svc-desc">Licensed gas leak detection and repair for {city} homes and businesses.</p><span class="city-svc-link">Learn More →</span></div></a>
    <a href="/water-filtration/" class="city-svc-card"><div class="city-svc-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/copper-pipe-installation-chino-ca.webp" alt="Water Filtration {city} CA" loading="lazy" /></div><div class="city-svc-body"><div class="city-svc-name">Water Filtration</div><p class="city-svc-desc">Whole-home softeners and reverse osmosis systems for {city} residents.</p><span class="city-svc-link">Learn More →</span></div></a>
  </div>
</div></section>"""

def city_why(city, why1_title, why1_desc, why2_title, why2_desc, why3_title, why3_desc):
    return f"""<style>.city-why{{background:#1E3A6E;padding:80px 24px}}.city-why-inner{{max-width:1200px;margin:0 auto}}.city-why-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:48px}}.city-why-card{{text-align:center;padding:32px 24px}}.city-why-icon{{font-size:36px;display:block;margin-bottom:16px}}.city-why-title{{font-family:'Oswald',sans-serif;font-weight:600;font-size:18px;color:#fff;text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px}}.city-why-desc{{font-size:14px;color:#93C5FD;line-height:1.7}}@media(max-width:640px){{.city-why-grid{{grid-template-columns:1fr}}}}</style>
<section class="city-why"><div class="city-why-inner">
  <div style="text-align:center"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#fca5a5;margin-bottom:10px">Our Promise</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);color:#fff;text-transform:uppercase;letter-spacing:.5px">Why {city} Residents Choose Regal</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div class="city-why-grid">
    <div class="city-why-card"><span class="city-why-icon">📍</span><div class="city-why-title">{why1_title}</div><p class="city-why-desc">{why1_desc}</p></div>
    <div class="city-why-card"><span class="city-why-icon">🔧</span><div class="city-why-title">{why2_title}</div><p class="city-why-desc">{why2_desc}</p></div>
    <div class="city-why-card"><span class="city-why-icon">✅</span><div class="city-why-title">{why3_title}</div><p class="city-why-desc">{why3_desc}</p></div>
  </div>
</div></section>"""

def city_seo(city, para1, para2, para3):
    return f"""<style>.city-seo{{background:#fff;padding:80px 24px}}.city-seo-inner{{max-width:860px;margin:0 auto}}.seo-body{{font-size:15.5px;color:#4B5563;line-height:1.85}}.seo-body p{{margin-bottom:18px}}.seo-body strong{{color:#2D2D2D}}</style>
<section class="city-seo"><div class="city-seo-inner">
  <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Local Expertise</div>
  <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Trusted Plumber in {city} CA</h2>
  <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0 28px"></div>
  <div class="seo-body"><p>{para1}</p><p>{para2}</p><p>{para3}</p></div>
</div></section>"""

def city_faq(city, faqs):
    faq_items = ""
    for i, (q, a) in enumerate(faqs, 1):
        faq_items += f"""<div style="border:1px solid #E5E7EB;border-radius:8px;overflow:hidden;margin-bottom:12px"><details><summary style="padding:20px 24px;font-family:'Oswald',sans-serif;font-weight:600;font-size:16px;color:#2D2D2D;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center">{q}<span style="color:#B91C1C;font-size:20px;flex-shrink:0">+</span></summary><div style="padding:0 24px 20px;font-size:15px;color:#4B5563;line-height:1.7">{a}</div></details></div>"""
    return f"""<style>.faq-section{{background:#F3F4F6;padding:80px 24px}}.faq-inner{{max-width:860px;margin:0 auto}}</style>
<section class="faq-section"><div class="faq-inner">
  <div style="text-align:center;margin-bottom:48px">
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Common Questions</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">{city} Plumbing FAQs</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
  </div>
  {faq_items}
</div></section>"""

def make_city_page(filename, title, seo_title, seo_desc, city, map_embed_src,
                   map_intro_p1, map_intro_p2,
                   why1_title, why1_desc, why2_title, why2_desc, why3_title, why3_desc,
                   seo_p1, seo_p2, seo_p3, faqs):
    map_section = f"""<style>.map-section{{background:#fff;padding:80px 24px}}.map-inner{{max-width:1200px;margin:0 auto}}.map-layout{{display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:start}}.map-embed{{border-radius:8px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.12);height:420px}}.map-embed iframe{{width:100%;height:100%;border:0;display:block}}@media(max-width:900px){{.map-layout{{grid-template-columns:1fr}}}}</style>
<section class="map-section"><div class="map-inner"><div class="map-layout">
  <div class="map-embed"><iframe src="{map_embed_src}" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Plumber in {city} CA"></iframe></div>
  <div>
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Your Local Plumber</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Serving All of {city}, CA</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0"></div>
    <p style="font-size:15.5px;color:#4B5563;line-height:1.8;margin-top:20px;margin-bottom:16px">{map_intro_p1}</p>
    <p style="font-size:15.5px;color:#4B5563;line-height:1.8;margin-bottom:16px">{map_intro_p2}</p>
  </div>
</div></div></section>"""
    sections = [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Service Area"), "#FFFFFF"),
        (city_hero(city), "#1E3A6E"),
        (map_section, "#FFFFFF"),
        (city_trust_bar(), "#F3F4F6"),
        (city_services(city), "#F3F4F6"),
        (city_why(city, why1_title, why1_desc, why2_title, why2_desc, why3_title, why3_desc), "#1E3A6E"),
        (city_seo(city, seo_p1, seo_p2, seo_p3), "#FFFFFF"),
        (city_faq(city, faqs), "#F3F4F6"),
        (cta_html(f"Need a Plumber in {city}? Call Now", f"Licensed, local, available 24/7 — serving all of {city}, CA"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
    save(filename, make_page(title, seo_title, seo_desc, sections))

# ── 14. ONTARIO CA ────────────────────────────────────────────────────────────
make_city_page(
    "ontario-ca.json",
    "Plumber in Ontario CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Plumber in Ontario CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Need a plumber in Ontario CA? Licensed, local, available 24/7. Emergency plumbing, drain cleaning, slab leak repair & more. Call (909) 600-4561.",
    "Ontario",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.6509!3d34.0633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Ontario, CA is one of the Inland Empire's fastest-growing cities, home to neighborhoods like Ontario Ranch, Gramercy, Creekside, and the bustling corridor near Ontario International Airport. As the region expands, plumbing demands have grown alongside it — from brand-new subdivisions facing high water pressure issues to older homes near downtown contending with aging cast iron pipes and galvanized supply lines.",
    "Regal Plumbing &amp; Rooter is based right here in Ontario at 2141 E Philadelphia St, Suite R — which means we respond faster than anyone else when emergencies strike. Whether you're dealing with a slab leak in Ontario Ranch, a clogged main sewer near Gramercy, or a failed water heater near the airport corridor, our licensed technicians are on the road within the hour.",
    "Based in Ontario","Our shop is in Ontario at 2141 E Philadelphia St. When you call, we're already nearby — reaching most Ontario locations in under an hour.",
    "Ontario Experts","We know Ontario's soil conditions, water quality challenges, and infrastructure age across neighborhoods like Ontario Ranch, Gramercy, and Creekside.",
    "Licensed &amp; Insured","CA License #1097482. Every Ontario job is covered by full liability insurance, and every quote is upfront with no hidden fees.",
    "When you need a reliable <strong>plumber in Ontario CA</strong>, Regal Plumbing &amp; Rooter is your local choice. Based in Ontario, we understand the specific plumbing challenges homeowners face throughout this growing city. From the sprawling <strong>Ontario Ranch</strong> master-planned community to the established <strong>Gramercy</strong> and <strong>Creekside</strong> neighborhoods, we've seen and solved every type of plumbing problem Ontario has to offer.",
    "As your trusted <strong>emergency plumber Ontario CA</strong>, our team is on call around the clock. Whether it's a slab leak beneath a concrete foundation in an older Ontario home, a broken water main along Euclid Avenue, or a sewage backup in a commercial property — we dispatch fast and arrive with the tools to fix it right.",
    "<strong>Drain cleaning Ontario CA</strong> is one of our most frequent services. Ontario's water supply carries heavy mineral content from the local groundwater system, which accelerates scale buildup inside pipes. We use professional snaking and high-pressure hydrojetting to restore full function — not a temporary fix, but a lasting clear that protects your pipes long-term.",
    [
        ("How fast can Regal Plumbing get to my Ontario, CA home?", "Because we're based in Ontario at 2141 E Philadelphia St, our technicians can typically reach most parts of Ontario within 45–60 minutes of your call. For plumbing emergencies, we prioritize the fastest possible dispatch — including nights and weekends."),
        ("Do you serve all neighborhoods in Ontario, CA?", "Yes — we serve all of Ontario, including Ontario Ranch, Gramercy, Creekside, the Airport District, downtown Ontario, and every area in between. No part of the city is outside our service range."),
        ("What are the most common plumbing problems in Ontario, CA?", "The most frequent calls we get from Ontario residents involve slab leaks — especially in older neighborhoods where copper pipes sit in calcium-heavy soil — drain blockages from hard water buildup, and water heater failures. We handle all of these daily."),
        ("Is emergency plumbing service available on weekends in Ontario?", "Absolutely. Our emergency plumbing line is staffed 24 hours a day, 7 days a week — including weekends and holidays. Call (909) 600-4561 any time and a real person will answer."),
    ]
)

# ── 15. RANCHO CUCAMONGA ──────────────────────────────────────────────────────
make_city_page(
    "rancho-cucamonga-ca.json",
    "Plumber in Rancho Cucamonga CA — 24/7 Service | Regal Plumbing & Rooter",
    "Plumber in Rancho Cucamonga CA — 24/7 Service | Regal Plumbing & Rooter",
    "Need a plumber in Rancho Cucamonga CA? Licensed, local, available 24/7. Emergency plumbing, drain cleaning & more. Call (909) 600-4561.",
    "Rancho Cucamonga",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.5931!3d34.1064!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Rancho Cucamonga is one of the Inland Empire's most affluent and rapidly growing cities, home to well-established neighborhoods like Etiwanda, Alta Loma, Deer Creek, and newer communities near Haven Avenue. The combination of older custom homes and newer construction creates diverse plumbing needs across the city.",
    "Regal Plumbing &amp; Rooter serves all of Rancho Cucamonga with the same commitment to quality and fast response that has made us a trusted name in the Inland Empire. From the hillside estates near the foothills to homes near the 210 freeway corridor, our technicians are on call 24/7 for emergency and scheduled work.",
    "Fast to Rancho Cucamonga","Stationed in nearby Ontario, our technicians reach Rancho Cucamonga quickly — most service calls arrive within 60 minutes, emergencies faster.",
    "Local Knowledge","We understand Rancho Cucamonga's plumbing landscape — older Etiwanda pipes, hillside pressure issues, and hard water buildup common throughout the city.",
    "Licensed &amp; Insured","CA License #1097482. Fully insured for every job in Rancho Cucamonga. Upfront pricing, no surprises.",
    "When you need a <strong>plumber in Rancho Cucamonga CA</strong>, Regal Plumbing &amp; Rooter delivers reliable service backed by local knowledge. We serve every neighborhood in Rancho Cucamonga — from the custom homes of <strong>Etiwanda Estates</strong> and <strong>Alta Loma</strong> to the newer subdivisions south of Foothill Boulevard.",
    "Our <strong>emergency plumber Rancho Cucamonga</strong> service is available around the clock. Older hillside homes in Rancho Cucamonga can experience unique pressure-related pipe stress, while newer homes near Haven Avenue may deal with defective fixtures or expansion issues. Our licensed team handles it all.",
    "<strong>Drain cleaning Rancho Cucamonga</strong> is a frequent service need given the city's hard water. Scale buildup in kitchen and shower drains is common. We use professional-grade snaking and hydrojetting to clear blockages completely and prevent costly backups.",
    [
        ("Do you serve all of Rancho Cucamonga?", "Yes — we cover all of Rancho Cucamonga including Etiwanda, Alta Loma, Deer Creek, and all areas from Foothill Blvd to the 210 freeway."),
        ("How quickly can you respond to a plumbing emergency in Rancho Cucamonga?", "Our technicians are based in nearby Ontario and typically reach Rancho Cucamonga within 45–60 minutes of your call. Emergency calls are prioritized for fastest dispatch."),
        ("Do you handle both old and new homes in Rancho Cucamonga?", "Absolutely. We're experienced with older custom homes in Alta Loma and Etiwanda as well as newer construction throughout the city. Each property type has unique plumbing considerations we're well-equipped to handle."),
    ]
)

# ── 16. FONTANA ───────────────────────────────────────────────────────────────
make_city_page(
    "fontana-ca.json",
    "Plumber in Fontana CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Plumber in Fontana CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Need a plumber in Fontana CA? Licensed, local, available 24/7. Emergency plumbing, drain cleaning, slab leak repair & more. Call (909) 600-4561.",
    "Fontana",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.435!3d34.092!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Fontana is one of the largest cities in San Bernardino County, with a diverse mix of older residential neighborhoods near the historic town center and growing communities on the city's east and north sides. Many of Fontana's established neighborhoods have aging cast iron sewer lines and galvanized water pipes that are reaching the end of their service life.",
    "Regal Plumbing &amp; Rooter serves all of Fontana with the quick response times and expert plumbing service that the Inland Empire has come to depend on. From the older homes near Sierra Avenue to newer developments near Fontana Ranch, our licensed technicians handle every plumbing challenge with skill and transparency.",
    "Fontana Coverage","We serve all of Fontana — from the historic core near Sierra Avenue to the growing communities in North Fontana and Fontana Ranch.",
    "Aging Pipe Experts","Many Fontana homes have aging sewer and supply lines. We specialize in camera inspection, trenchless repair, and pipe replacement throughout Fontana.",
    "Licensed &amp; Insured","CA License #1097482. Fully licensed for all plumbing work in Fontana. Upfront quotes, no hidden fees.",
    "When you need a reliable <strong>plumber in Fontana CA</strong>, Regal Plumbing &amp; Rooter is the local choice. We serve all of Fontana — from the established neighborhoods near <strong>Sierra Avenue</strong> to the growing residential areas in <strong>North Fontana</strong> and beyond the 210 freeway.",
    "Our <strong>sewer line repair Fontana</strong> service is one of our most in-demand because Fontana has a large stock of older homes with clay and cast iron sewer laterals that are prone to cracking and root intrusion. We use camera inspection to diagnose the problem accurately, then offer trenchless repair options to minimize disruption.",
    "<strong>Emergency plumber Fontana</strong> calls are answered 24/7. Whether it's a burst pipe at 2am or a sewage backup on a Sunday afternoon, our team is dispatched promptly. We carry the tools to handle virtually any plumbing emergency on the first visit.",
    [
        ("Do you serve all neighborhoods in Fontana, CA?", "Yes — we cover all of Fontana including the historic core, North Fontana, Fontana Ranch, and all areas from the 10 freeway to the foothills."),
        ("What plumbing issues are most common in Fontana?", "Fontana's older neighborhoods frequently experience sewer line problems due to aging clay pipes, root intrusion, and ground shifting. Drain blockages from hard water scale and water heater failures are also very common."),
        ("Can you repair old cast iron pipes in Fontana homes?", "Yes — we work with cast iron and galvanized steel pipes frequently in Fontana. Depending on the extent of corrosion, we may recommend spot repair, sectional replacement, or full re-piping."),
    ]
)

# ── 17. POMONA ────────────────────────────────────────────────────────────────
make_city_page(
    "pomona-ca.json",
    "Plumber in Pomona CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Plumber in Pomona CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Need a plumber in Pomona CA? Licensed, local, available 24/7. Emergency plumbing, drain cleaning, slab leak repair & more. Call (909) 600-4561.",
    "Pomona",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.75!3d34.055!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Pomona is a historic city at the junction of the Inland Empire and the San Gabriel Valley, with a rich legacy of early 20th-century homes and an increasingly diverse residential landscape. Many of Pomona's older neighborhoods feature original cast iron and galvanized plumbing that has reached or exceeded its service life, creating frequent need for repair and replacement.",
    "Regal Plumbing &amp; Rooter serves all of Pomona with licensed, professional plumbing services and 24/7 emergency availability. Whether you're in a historic craftsman near downtown Pomona or a newer home in the Phillips Ranch area, our team brings the same expertise and honest pricing to every job.",
    "Pomona Coverage","We serve all of Pomona — from historic downtown neighborhoods to Phillips Ranch and every area in between.",
    "Old Pipe Specialists","Pomona's historic homes often have original plumbing. We specialize in diagnosing and replacing aging cast iron, galvanized, and clay systems.",
    "Licensed &amp; Insured","CA License #1097482. Fully licensed for all plumbing work in Pomona. Upfront pricing, always transparent.",
    "When you need a <strong>plumber in Pomona CA</strong>, Regal Plumbing &amp; Rooter provides fast, expert service throughout this historic city. We work in all of Pomona's neighborhoods — from the century-old craftsman homes near <strong>downtown Pomona</strong> to the newer construction in <strong>Phillips Ranch</strong>.",
    "Our <strong>drain cleaning Pomona</strong> service addresses the heavy buildup common in Pomona's aging pipe infrastructure. Galvanized and cast iron pipes develop significant interior scale over decades, restricting flow and eventually failing. We clear blockages and advise on long-term solutions including pipe lining and replacement.",
    "<strong>Slab leak Pomona</strong> detection is another common service request. Many of Pomona's slab-on-grade homes from the 1950s–1970s have copper supply lines embedded in calcium-heavy concrete that eventually corrode and fail. Our electronic detection equipment pinpoints leaks precisely without unnecessary excavation.",
    [
        ("Do you serve all of Pomona, CA?", "Yes — we serve all of Pomona including downtown, Phillips Ranch, Ganesha Hills, and every neighborhood throughout the city."),
        ("What are the most common plumbing problems in Pomona?", "Pomona's older housing stock means we frequently deal with galvanized pipe corrosion, root-invaded clay sewer lines, and slab leaks in homes built before 1980. Water heater replacements and main line clearing are also very common."),
        ("Can you replace old galvanized pipes in a Pomona home?", "Yes — we perform full and partial re-pipes using modern copper or PEX piping. We'll inspect your system and provide a transparent estimate for the scope of work needed."),
    ]
)

print("Pages 11-17 done.")
