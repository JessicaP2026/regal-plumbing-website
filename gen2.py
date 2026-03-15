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
    <div>
      <div class="footer-logo-name">Regal Plumbing &amp; Rooter</div>
      <p class="footer-tagline">Honest, professional plumbing &amp; rooter services for the Inland Empire &amp; San Gabriel Valley.</p>
      <span class="footer-license">CA License #1097482</span>
    </div>
    <div class="footer-col"><h4>Services</h4><ul class="footer-links">
      <li><a href="/emergency-plumbing/">Emergency Plumbing</a></li>
      <li><a href="/drain-cleaning/">Drain Cleaning</a></li>
      <li><a href="/sewer-line-repair/">Sewer Line Repair</a></li>
      <li><a href="/water-heater-services/">Water Heater Services</a></li>
      <li><a href="/slab-leak-detection/">Slab Leak Detection</a></li>
      <li><a href="/hydrojetting/">Hydrojetting</a></li>
      <li><a href="/gas-leak-detection/">Gas Leak Detection</a></li>
      <li><a href="/water-filtration/">Water Filtration</a></li>
    </ul></div>
    <div class="footer-col"><h4>Service Area</h4><ul class="footer-links">
      <li><a href="/service-area/ontario-ca/">Ontario</a></li>
      <li><a href="/service-area/rancho-cucamonga-ca/">Rancho Cucamonga</a></li>
      <li><a href="/service-area/fontana-ca/">Fontana</a></li>
      <li><a href="/service-area/pomona-ca/">Pomona</a></li>
      <li><a href="/service-area/chino-ca/">Chino</a></li>
      <li><a href="/service-area/corona-ca/">Corona</a></li>
      <li><a href="/service-area/upland-ca/">Upland</a></li>
      <li><a href="/service-area/west-covina-ca/">West Covina</a></li>
    </ul></div>
    <div class="footer-col"><h4>Contact Us</h4><ul class="footer-contact-list">
      <li><span>📍</span><span>2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</span></li>
      <li><span>📞</span><a href="tel:9096004561">(909) 600-4561</a></li>
      <li><span>✉️</span><a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></li>
      <li><span>🕐</span><span>24/7 Emergency<br>Mon–Sat: 7am–7pm</span></li>
    </ul></div>
  </div>
  <div class="footer-bottom">
    <span class="footer-bottom-text">© 2025 Regal Plumbing &amp; Rooter. All Rights Reserved. CA License #1097482</span>
    <div class="footer-bottom-links">
      <a href="/privacy-policy/">Privacy Policy</a>
      <a href="/terms-of-service/">Terms of Service</a>
      <a href="/sitemap/">Sitemap</a>
    </div>
  </div>
</footer>"""

def cta_html(heading, subtext):
    return f"""<style>.cta-section{{background:#B91C1C;padding:64px 24px;text-align:center;position:relative;overflow:hidden}}.cta-section::before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent,transparent 8px,rgba(0,0,0,.04) 8px,rgba(0,0,0,.04) 10px)}}.cta-inner{{position:relative;z-index:2;max-width:700px;margin:0 auto}}.cta-inner h2{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,4vw,42px);color:#fff;letter-spacing:1px;text-transform:uppercase;margin-bottom:12px}}.cta-sub{{font-size:16px;color:rgba(255,255,255,.85);margin-bottom:24px}}.cta-phone{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,5vw,50px);color:#fff;letter-spacing:2px;margin-bottom:28px;display:block;text-decoration:none}}.btn-white-red{{display:inline-flex;align-items:center;padding:14px 32px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;background:#fff;color:#B91C1C;border:2px solid #fff;text-decoration:none}}</style>
<section class="cta-section"><div class="cta-inner"><h2>{heading}</h2><p class="cta-sub">{subtext}</p><a href="tel:9096004561" class="cta-phone">(909) 600-4561</a><br><a href="tel:9096004561" class="btn-white-red">📞 Call Now</a></div></section>"""

def navy_hero_html(breadcrumb_items, h1, sub):
    bc = ""
    for i, (label, href) in enumerate(breadcrumb_items):
        if href:
            bc += f'<a href="{href}">{label}</a><span style="color:#4B5563"> › </span>'
        else:
            bc += f'<span style="color:#fca5a5">{label}</span>'
    return f"""<style>.page-hero{{background:#1E3A6E;position:relative;overflow:hidden;padding:64px 24px}}.page-hero::before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent,transparent 2px,rgba(255,255,255,.015) 2px,rgba(255,255,255,.015) 4px)}}.page-hero-inner{{position:relative;z-index:2;max-width:1200px;margin:0 auto}}.breadcrumb{{display:flex;align-items:center;gap:6px;font-size:13px;color:#93C5FD;margin-bottom:14px;flex-wrap:wrap}}.breadcrumb a{{color:#93C5FD;text-decoration:none}}.page-hero h1{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}.page-hero-sub{{font-size:16px;color:#93C5FD;max-width:580px}}</style>
<div class="page-hero"><div class="page-hero-inner"><div class="breadcrumb">{bc}</div><h1>{h1}</h1><p class="page-hero-sub">{sub}</p></div></div>"""

def dark_hero_html(breadcrumb_items, h1, sub):
    bc = ""
    for label, href in breadcrumb_items:
        if href:
            bc += f'<a href="{href}" style="color:#9CA3AF;text-decoration:none">{label}</a><span style="color:#4B5563"> › </span>'
        else:
            bc += f'<span style="color:#fca5a5">{label}</span>'
    return f"""<style>.page-hero{{background:#111827;position:relative;overflow:hidden;padding:64px 24px}}.page-hero-bg{{position:absolute;inset:0;background:linear-gradient(135deg,rgba(30,58,110,.7) 0%,rgba(0,0,0,.8) 70%)}}.page-hero-inner{{position:relative;z-index:2;max-width:1200px;margin:0 auto}}.breadcrumb{{display:flex;align-items:center;gap:6px;font-size:13px;color:#9CA3AF;margin-bottom:14px;flex-wrap:wrap}}.page-hero h1{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}.page-hero-sub{{font-size:16px;color:#D1D5DB;max-width:540px}}</style>
<div class="page-hero"><div class="page-hero-bg"></div><div class="page-hero-inner"><div class="breadcrumb">{bc}</div><h1>{h1}</h1><p class="page-hero-sub">{sub}</p></div></div>"""

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

def why_section_html(bg="#1E3A6E"):
    return f"""<style>.why-sec{{background:{bg};padding:80px 24px}}.why-sec-inner{{max-width:1200px;margin:0 auto}}.why-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:48px}}.why-card{{text-align:center;padding:32px 24px}}.why-icon{{font-size:36px;display:block;margin-bottom:16px}}.why-title{{font-family:'Oswald',sans-serif;font-weight:600;font-size:18px;color:#fff;text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px}}.why-desc{{font-size:14px;color:#93C5FD;line-height:1.7}}@media(max-width:640px){{.why-grid{{grid-template-columns:1fr}}}}</style>
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
        "id": uid(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "background_background": "classic",
            "background_color": bg_color,
            "padding": {"top":"0","right":"0","bottom":"0","left":"0","unit":"px","isLinked":False}
        },
        "elements": [{"id":uid(),"elType":"widget","widgetType":"html","settings":{"html":html_content},"elements":[]}]
    }

def make_page(title, seo_title, seo_desc, sections_html):
    content = [make_container(html, bg) for html, bg in sections_html]
    return {
        "version": "0.4",
        "title": title,
        "type": "page",
        "content": content,
        "page_settings": {
            "post_title": title,
            "template": "elementor_canvas",
            "_elementor_template_type": "page",
            "rank_math_title": seo_title,
            "rank_math_description": seo_desc,
            "rank_math_og_title": seo_title,
            "rank_math_og_description": seo_desc,
            "rank_math_schema_pro_markup": SCHEMA,
            "_elementor_edit_mode": "builder"
        }
    }

def save(filename, data):
    path = os.path.join(OUT, filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {filename}")

# ── 4. SERVICES ───────────────────────────────────────────────────────────────
services_hero = dark_hero_html(
    [("Home","/"),("Services",None)],
    "Plumbing Services",
    "Comprehensive residential and commercial plumbing solutions — available 24/7 across Southern California."
)

services_list = """<style>
.svc-list-section{background:#F3F4F6;padding:80px 24px}
.svc-list-inner{max-width:1200px;margin:0 auto}
.svcs-list{display:flex;flex-direction:column;gap:56px}
.svc-detail{display:grid;grid-template-columns:1fr 1.8fr;gap:48px;align-items:start;padding:40px;background:#fff;border:1px solid #E5E7EB;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,.04)}
.svc-detail.alt{grid-template-columns:1.8fr 1fr}
.svc-detail.alt .svc-visual{order:2}.svc-detail.alt .svc-content{order:1}
.svc-visual{border-radius:8px;overflow:hidden;min-height:260px;position:relative}
.svc-visual img{width:100%;height:100%;min-height:260px;object-fit:cover;display:block}
.svc-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.55) 0%,transparent 50%)}
.svc-label{position:absolute;bottom:14px;left:14px;font-family:'Oswald',sans-serif;font-weight:700;font-size:15px;color:#fff;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;padding:4px 10px;border-radius:3px}
.svc-name{font-family:'Oswald',sans-serif;font-weight:700;font-size:24px;color:#2D2D2D;letter-spacing:.5px;margin-bottom:6px}
.svc-tag{display:inline-block;background:#FEF2F2;color:#B91C1C;font-family:'Oswald',sans-serif;font-weight:500;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;padding:3px 10px;border-radius:2px;margin-bottom:14px}
.svc-desc{font-size:15px;color:#4B5563;line-height:1.75;margin-bottom:20px}
.svc-features{list-style:none;display:flex;flex-direction:column;gap:8px;margin-bottom:24px;padding:0}
.svc-features li{display:flex;align-items:flex-start;gap:10px;font-size:14px;color:#374151}
.svc-features li::before{content:'✓';width:20px;height:20px;background:#B91C1C;color:#fff;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;margin-top:1px}
.btn-red-svc{display:inline-flex;align-items:center;padding:10px 22px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;border:2px solid #B91C1C;text-decoration:none;margin-right:12px}
.btn-outline-red{display:inline-flex;align-items:center;padding:10px 22px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:transparent;color:#B91C1C;border:2px solid #B91C1C;text-decoration:none}
@media(max-width:900px){.svc-detail,.svc-detail.alt{grid-template-columns:1fr}.svc-detail.alt .svc-visual,.svc-detail.alt .svc-content{order:0}}
</style>
<section class="svc-list-section"><div class="svc-list-inner">
  <div style="text-align:center;margin-bottom:52px">
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Full Service Plumbing</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Everything We Offer</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
    <p style="font-size:16px;color:#6B7280;max-width:520px;margin:16px auto 0;line-height:1.65;">From emergency repairs to planned installations — our licensed technicians handle it all.</p>
  </div>
  <div class="svcs-list">
    <div class="svc-detail">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-repair-leak-detection-chino-hills-ca.webp" alt="24/7 emergency plumber Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Emergency Plumbing</div></div>
      <div class="svc-content"><div class="svc-name">Emergency Plumbing</div><span class="svc-tag">24/7 Available</span><p class="svc-desc">Plumbing emergencies don't wait for business hours, and neither do we. Regal Plumbing &amp; Rooter provides rapid-response emergency plumbing services around the clock. Whether it's a burst pipe, severe water leak, or overflowing fixture — our team mobilizes fast to minimize damage.</p><ul class="svc-features"><li>Rapid response — typically on-site within the hour</li><li>Burst pipe repair and water shut-off</li><li>Severe clog and overflow emergencies</li><li>24/7 availability, including holidays</li></ul><a href="tel:9096004561" class="btn-red-svc">📞 Call for Emergency Service</a></div>
    </div>
    <div class="svc-detail alt">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/drain-cleaning-shower-upland-ca.webp" alt="drain cleaning service Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Drain Cleaning</div></div>
      <div class="svc-content"><div class="svc-name">Drain Cleaning</div><span class="svc-tag">Residential &amp; Commercial</span><p class="svc-desc">Slow or blocked drains are more than an inconvenience. Our drain cleaning services clear everything from minor kitchen clogs to severe main line blockages, using professional-grade equipment to restore full flow.</p><ul class="svc-features"><li>Kitchen and bathroom drain clearing</li><li>Main sewer line snaking</li><li>Floor drain and utility sink cleaning</li><li>Preventative maintenance plans available</li></ul><a href="/drain-cleaning/" class="btn-outline-red">Learn More →</a></div>
    </div>
    <div class="svc-detail">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-line-repair-excavation-fontana-ca.webp" alt="sewer line repair excavation Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Sewer Line Repair</div></div>
      <div class="svc-content"><div class="svc-name">Sewer Line Repair</div><span class="svc-tag">Expert Diagnosis</span><p class="svc-desc">Sewer line problems can cause serious damage if left untreated. We use camera inspection technology to accurately diagnose issues — root intrusion, cracks, bellied pipes — then provide the most cost-effective repair solution.</p><ul class="svc-features"><li>Camera video inspection and diagnosis</li><li>Pipe bursting and trenchless repair</li><li>Root intrusion removal</li><li>Full sewer line replacement when needed</li></ul><a href="/sewer-line-repair/" class="btn-outline-red">Learn More →</a></div>
    </div>
    <div class="svc-detail alt">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sink-faucet-installation-ontario-ca.webp" alt="water heater installation Ontario CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Water Heater Services</div></div>
      <div class="svc-content"><div class="svc-name">Water Heater Install &amp; Repair</div><span class="svc-tag">All Types &amp; Brands</span><p class="svc-desc">No hot water? We install and repair all types of water heaters — traditional tank units, tankless systems, and hybrid heat pump models. Our technicians can help you choose the right system for your household's needs and budget.</p><ul class="svc-features"><li>Traditional tank water heater install &amp; repair</li><li>Tankless water heater installation</li><li>Heat pump water heater systems</li><li>Anode rod replacement and flushing</li></ul><a href="/water-heater-services/" class="btn-outline-red">Learn More →</a></div>
    </div>
    <div class="svc-detail">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/leak-repair-wall-open-ontario-ca.webp" alt="slab leak detection pipe repair Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Slab Leak Detection</div></div>
      <div class="svc-content"><div class="svc-name">Slab Leak Detection</div><span class="svc-tag">Non-Invasive Technology</span><p class="svc-desc">Slab leaks are among the most damaging plumbing problems a homeowner can face. We use electronic detection equipment to precisely locate leaks beneath your concrete slab without unnecessary excavation.</p><ul class="svc-features"><li>Electronic leak detection — no guesswork</li><li>Spot repair and re-routing options</li><li>Epoxy pipe lining (non-invasive)</li><li>Post-repair pressure testing</li></ul><a href="/slab-leak-detection/" class="btn-outline-red">Learn More →</a></div>
    </div>
    <div class="svc-detail alt">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/hydro-jetting-roof-rancho-cucamonga-ca.webp" alt="hydrojetting drain cleaning service Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Hydrojetting</div></div>
      <div class="svc-content"><div class="svc-name">Hydrojetting</div><span class="svc-tag">High-Pressure Cleaning</span><p class="svc-desc">When snaking isn't enough, hydrojetting is the most effective method for clearing stubborn grease, scale, and root intrusion. Using water at up to 4,000 PSI, hydrojetting scours pipe walls clean and restores full pipe capacity.</p><ul class="svc-features"><li>Clears grease, scale, and hardened buildup</li><li>Removes tree root intrusion</li><li>Ideal for commercial kitchens and restaurants</li><li>Extends the life of your plumbing system</li></ul><a href="/hydrojetting/" class="btn-outline-red">Learn More →</a></div>
    </div>
    <div class="svc-detail">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/camera-inspection-drain-cleaning-san-bernardino-ca.webp" alt="gas leak detection Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Gas Leak Detection</div></div>
      <div class="svc-content"><div class="svc-name">Gas Leak Detection</div><span class="svc-tag">Safety Critical · Call Immediately</span><p class="svc-desc">A gas leak is a serious safety emergency. If you smell gas, leave the building immediately and call 911 first. Then call us. Our licensed plumbers perform precise gas leak detection and repair, ensuring your home is safe before restoring service.</p><ul class="svc-features"><li>Electronic gas leak detection equipment</li><li>Gas line repair and re-piping</li><li>Pressure testing after repair</li><li>Licensed for natural gas and propane systems</li></ul><a href="tel:9096004561" class="btn-red-svc">📞 Call Now — Safety Emergency</a></div>
    </div>
    <div class="svc-detail alt">
      <div class="svc-visual"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-replacement-copper-ontario-ca.webp" alt="water filtration copper pipe installation Inland Empire CA" loading="lazy" /><div class="svc-overlay"></div><div class="svc-label">Water Filtration</div></div>
      <div class="svc-content"><div class="svc-name">Water Filtration &amp; Softeners</div><span class="svc-tag">Cleaner, Softer Water</span><p class="svc-desc">Southern California water is notoriously hard. Mineral buildup damages appliances and affects water quality. We install whole-home water softeners, under-sink filters, and reverse osmosis systems to give you cleaner, softer water.</p><ul class="svc-features"><li>Whole-home water softener installation</li><li>Under-sink reverse osmosis systems</li><li>Carbon filtration and UV purification</li><li>Filter cartridge replacement service</li></ul><a href="/water-filtration/" class="btn-outline-red">Learn More →</a></div>
    </div>
  </div>
</div></section>"""

save("services.json", make_page(
    "Plumbing Services | Regal Plumbing & Rooter",
    "Plumbing Services | Regal Plumbing & Rooter",
    "Emergency plumbing, drain cleaning, water heater repair, slab leak detection & more. Licensed 24/7 plumbers in the Inland Empire. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Services"), "#FFFFFF"),
        (services_hero, "#111827"),
        (services_list, "#F3F4F6"),
        (why_section_html("#2D2D2D"), "#2D2D2D"),
        (cta_html("Ready to Get Started?", "Call now for a free quote or immediate emergency service"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 5. SERVICE AREA ───────────────────────────────────────────────────────────
sa_hero = navy_hero_html(
    [("Home","/"),("Service Area",None)],
    "Plumbing Services Across Southern California",
    "Serving 32+ cities in the Inland Empire and San Gabriel Valley — fast, local plumbers available 24/7."
)

sa_map = """<style>
.map-section{background:#fff;padding:80px 24px}
.map-inner{max-width:1200px;margin:0 auto}
.map-layout{display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:start}
.map-embed{border-radius:8px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.12);height:420px}
.map-embed iframe{width:100%;height:100%;border:0;display:block}
.map-stats{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:28px}
.map-stat{background:#F3F4F6;border-left:4px solid #B91C1C;border-radius:4px;padding:14px 18px}
.map-stat-num{font-family:'Oswald',sans-serif;font-weight:700;font-size:28px;color:#B91C1C;line-height:1}
.map-stat-label{font-size:12px;color:#6B7280;text-transform:uppercase;letter-spacing:.5px;margin-top:3px}
@media(max-width:900px){.map-layout{grid-template-columns:1fr}}
</style>
<section class="map-section"><div class="map-inner"><div class="map-layout">
  <div class="map-embed"><iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d422147!2d-117.55!3d34.0!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Regal Plumbing Service Area"></iframe></div>
  <div>
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Our Coverage</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Your Local Plumbing Experts</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0"></div>
    <p style="font-size:15.5px;color:#4B5563;line-height:1.8;margin-bottom:16px">Regal Plumbing &amp; Rooter is based in Ontario, CA and serves a wide coverage area spanning the Inland Empire and San Gabriel Valley. Whether you're in Rancho Cucamonga, Pomona, Chino Hills, or anywhere in between — we have a technician near you.</p>
    <p style="font-size:15.5px;color:#4B5563;line-height:1.8;margin-bottom:16px">Our service area covers everything from emergency plumbing and drain cleaning to slab leak detection and water heater installation across 32 cities in Southern California.</p>
    <div class="map-stats">
      <div class="map-stat"><div class="map-stat-num">32+</div><div class="map-stat-label">Cities Covered</div></div>
      <div class="map-stat"><div class="map-stat-num">24/7</div><div class="map-stat-label">Emergency Service</div></div>
      <div class="map-stat"><div class="map-stat-num">60min</div><div class="map-stat-label">Avg. Response Time</div></div>
      <div class="map-stat"><div class="map-stat-num">500+</div><div class="map-stat-label">Jobs Completed</div></div>
    </div>
  </div>
</div></div></section>"""

sa_cities = """<style>
.cities-section{background:#F3F4F6;padding:80px 24px}
.cities-inner{max-width:1200px;margin:0 auto}
.cities-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0}
.city-card{background:#fff;border:1px solid #E5E7EB;padding:14px 18px;display:flex;align-items:center;gap:10px}
.city-dot{width:8px;height:8px;background:#B91C1C;border-radius:50%;flex-shrink:0}
.city-name{font-family:'Oswald',sans-serif;font-weight:500;font-size:15px;color:#2D2D2D;letter-spacing:.3px}
@media(max-width:900px){.cities-grid{grid-template-columns:repeat(2,1fr)}}
</style>
<section class="cities-section"><div class="cities-inner">
  <div style="text-align:center;margin-bottom:48px">
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Full Coverage List</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Cities We Serve</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
    <p style="font-size:15px;color:#6B7280;max-width:500px;margin:16px auto 0;line-height:1.65">Don't see your city? Call us — our service area is always expanding.</p>
  </div>
  <div class="cities-grid">
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Azusa</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Bloomington</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Brea</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Charter Oak</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Chino</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Chino Hills</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Citrus</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Claremont</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Colton</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Corona</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Covina</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Diamond Bar</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Eastvale</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Fontana</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Glendora</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Highgrove</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Jurupa Valley</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">La Verne</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Loma Linda</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Mira Loma</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Montclair</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Muscoy</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Norco</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Ontario</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Pomona</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Rancho Cucamonga</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Rowland Heights</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">San Dimas</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Upland</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Walnut</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">West Covina</div></div>
    <div class="city-card"><div class="city-dot"></div><div class="city-name">Yorba Linda</div></div>
  </div>
</div></section>"""

sa_seo = """<style>.seo-section{background:#fff;padding:80px 24px}.seo-inner{max-width:860px;margin:0 auto}.seo-body{font-size:15.5px;color:#4B5563;line-height:1.85}.seo-body p{margin-bottom:18px}.seo-body strong{color:#2D2D2D}</style>
<section class="seo-section"><div class="seo-inner">
  <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Fast, Local Plumbing</div>
  <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Fast, Local Plumbing You Can Count On</h2>
  <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0 28px"></div>
  <div class="seo-body">
    <p>When a plumbing problem strikes, the last thing you want is to wait hours for a technician from across the county. That's why <strong>Regal Plumbing &amp; Rooter</strong> built our team around fast, local response — with technicians positioned throughout the <strong>Inland Empire and San Gabriel Valley</strong> to reach you quickly, whether you're in <strong>Rancho Cucamonga, Fontana, Ontario, Pomona</strong>, or any of the 32 cities we serve.</p>
    <p>Our services cover the full range of residential and commercial plumbing needs across Southern California. From <strong>24/7 emergency plumbing</strong> and <strong>drain cleaning</strong> to <strong>slab leak detection</strong>, <strong>water heater installation</strong>, and <strong>hydrojetting</strong> — we bring expert, licensed service directly to your door.</p>
    <p>As a <strong>family-owned, CA licensed business (License #1097482)</strong>, we're deeply invested in the communities we serve. We know the plumbing challenges specific to Southern California — hard water buildup, aging infrastructure, and the unique demands of high-density residential areas.</p>
    <p>Need a plumber near you? <strong>Call (909) 600-4561</strong> — we're available 24 hours a day, 7 days a week, for emergencies and scheduled service alike.</p>
  </div>
</div></section>"""

save("service-area.json", make_page(
    "Plumbing Service Area | Regal Plumbing & Rooter",
    "Plumbing Service Area | Regal Plumbing & Rooter",
    "Regal Plumbing serves 32+ cities in the Inland Empire including Ontario, Rancho Cucamonga, Fontana, Pomona & more. Available 24/7. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Service Area"), "#FFFFFF"),
        (sa_hero, "#1E3A6E"),
        (sa_map, "#FFFFFF"),
        (sa_cities, "#F3F4F6"),
        (sa_seo, "#FFFFFF"),
        (cta_html("Need a Plumber in Your Area? We're Ready Now", "Available 24/7 for emergency and scheduled service across 32+ cities"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── helper: service page overview section ─────────────────────────────────────
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
    {paras}
    <ul class="feat-list">{features_html}</ul>
    {btn}
  </div>
  <div class="ov-photo"><img src="{img_src}" alt="{img_alt}" loading="lazy" /></div>
</div></div></section>"""

def covers_section(title, cards):
    cards_html = ""
    for icon, ctitle, desc in cards:
        cards_html += f'<div style="background:#fff;border-radius:8px;padding:28px 24px;border-top:3px solid #B91C1C;box-shadow:0 2px 12px rgba(0,0,0,.06)"><div style="font-size:28px;margin-bottom:14px">{icon}</div><div style="font-family:Oswald,sans-serif;font-weight:600;font-size:16px;text-transform:uppercase;letter-spacing:.5px;color:#2D2D2D;margin-bottom:8px">{ctitle}</div><p style="font-size:14px;color:#6B7280;line-height:1.7">{desc}</p></div>'
    return f"""<style>.cov-section{{background:#F3F4F6;padding:80px 24px}}.cov-inner{{max-width:1200px;margin:0 auto}}.cov-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:48px}}@media(max-width:900px){{.cov-grid{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:640px){{.cov-grid{{grid-template-columns:1fr}}}}</style>
<section class="cov-section"><div class="cov-inner">
  <div style="text-align:center">
    <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">What We Cover</div>
    <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">{title}</h2>
    <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
  </div>
  <div class="cov-grid">{cards_html}</div>
</div></section>"""

# ── 6. EMERGENCY PLUMBING ─────────────────────────────────────────────────────
ep_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-repair-leak-detection-chino-hills-ca.webp",
    "24/7 emergency plumber Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Emergency Plumbing",None)],
    "24/7 Available",
    "Emergency Plumbing",
    "Rapid-response emergency plumbing for the Inland Empire — we're on call around the clock"
)
ep_overview = svc_overview(
    "When Every Minute Counts",
    "24/7 Emergency Plumbing Response",
    ["When a plumbing emergency strikes — a burst pipe, major leak, or sewage backup — every minute matters. Regal Plumbing &amp; Rooter provides rapid-response emergency service around the clock, 365 days a year. We mobilize fast, arrive with the right equipment, and get the problem under control before it causes serious damage to your home or property."],
    ["Typically on-site within the hour","Burst pipe detection and emergency shutoff","Sewage backup and overflow response","Major leak control and repair","24/7 availability including holidays","Upfront pricing even in emergencies"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-repair-service-truck-inland-empire.webp",
    "Emergency plumbing response Inland Empire",
    "📞 Call Now — (909) 600-4561",
    "tel:9096004561"
)
ep_covers = covers_section("Emergency Services We Provide", [
    ("💥","Burst Pipes","Immediate shutoff and repair of burst or frozen pipes before water damage spreads to walls, floors, and structural elements."),
    ("🚿","Sewage Backups","Emergency response to sewage backups and overflow situations that require immediate containment and clearance."),
    ("💧","Major Leaks","Rapid detection and repair of active leaks — under sinks, behind walls, or at the main line — stopping damage fast."),
])

save("emergency-plumbing.json", make_page(
    "Emergency Plumber | 24/7 Service | Regal Plumbing & Rooter",
    "Emergency Plumber | 24/7 Service | Regal Plumbing & Rooter",
    "24/7 emergency plumber in the Inland Empire. Fast response, licensed & insured. Burst pipes, flooding, gas leaks & more. Call (909) 600-4561 now.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Services"), "#FFFFFF"),
        (ep_hero, "#111827"),
        (ep_overview, "#FFFFFF"),
        (ep_covers, "#F3F4F6"),
        (why_section_html(), "#1E3A6E"),
        (OTHER_SERVICES, "#FFFFFF"),
        (cta_html("Plumbing Emergency? Call Right Now", "Our emergency team is standing by 24/7 — including weekends and holidays"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 7. DRAIN CLEANING ─────────────────────────────────────────────────────────
dc_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/drain-cleaning-shower-upland-ca.webp",
    "drain cleaning service Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Drain Cleaning",None)],
    "Residential & Commercial",
    "Drain Cleaning",
    "Professional drain clearing for kitchen, bathroom, and main sewer line blockages throughout Southern California"
)
dc_overview = svc_overview(
    "Restore Full Flow",
    "Professional Drain Cleaning Service",
    ["Slow or blocked drains are more than an inconvenience — they can signal deeper plumbing issues and lead to pipe damage or backups if left untreated. Regal Plumbing &amp; Rooter uses professional-grade equipment to clear everything from minor bathroom clogs to severe main line blockages, restoring full flow and preventing future buildup."],
    ["Kitchen drain and grease trap clearing","Bathroom sink, tub, and shower drain cleaning","Main sewer line snaking and clearing","Floor drain and utility sink service","Camera inspection to diagnose root causes","Preventative maintenance plans available"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/drain-cleaning-bathtub-rialto-ca.webp",
    "drain cleaning service Inland Empire CA",
    "Get a Free Quote",
    "/contact/"
)
dc_covers = covers_section("Drain Types We Service", [
    ("🍳","Kitchen Drains","Clear grease, food buildup, and soap scum that accumulates in kitchen sink drains. We also service garbage disposals and grease traps."),
    ("🛁","Bathroom Drains","Remove hair, soap residue, and debris from tub, shower, and sink drains. Fast clearing with minimal disruption."),
    ("🔩","Main Sewer Line","Professional snaking and clearing of main line blockages before they cause sewage backup. Camera inspection available."),
])

save("drain-cleaning.json", make_page(
    "Drain Cleaning Service | Regal Plumbing & Rooter",
    "Drain Cleaning Service | Regal Plumbing & Rooter",
    "Professional drain cleaning in the Inland Empire. Hydrojetting, snake service, same-day available. Licensed & local. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Services"), "#FFFFFF"),
        (dc_hero, "#111827"),
        (dc_overview, "#FFFFFF"),
        (dc_covers, "#F3F4F6"),
        (why_section_html(), "#1E3A6E"),
        (OTHER_SERVICES, "#FFFFFF"),
        (cta_html("Ready for Clear Drains?", "Call for a free quote — same-day service often available"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 8. SEWER LINE REPAIR ──────────────────────────────────────────────────────
sl_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-line-repair-excavation-fontana-ca.webp",
    "sewer line repair excavation Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Sewer Line Repair",None)],
    "Expert Diagnosis",
    "Sewer Line Repair",
    "Camera inspection, trenchless repair, and full sewer line replacement across the Inland Empire"
)
sl_overview = svc_overview(
    "Diagnose & Fix",
    "Expert Sewer Line Repair & Replacement",
    ["Sewer line problems can cause serious damage if left untreated. We use camera inspection technology to accurately diagnose sewer line issues — root intrusion, cracks, bellied pipes, and more — then provide the most cost-effective repair solution, including trenchless options when available."],
    ["Camera video inspection and diagnosis","Pipe bursting and trenchless repair","Root intrusion removal and clearing","Full sewer line replacement when needed","Spot repairs to extend existing line life","Post-repair inspection and pressure testing"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-line-excavation-ontario-ca.webp",
    "sewer line repair excavation Inland Empire CA",
    "Get a Free Quote",
    "/contact/"
)
sl_covers = covers_section("Sewer Services We Provide", [
    ("📷","Camera Inspection","We send a high-definition camera through your sewer line to pinpoint the exact location and cause of blockages or damage — no guesswork."),
    ("🔄","Trenchless Repair","Where possible, we use pipe bursting or lining to repair sewer lines without major excavation, saving time, money, and landscaping."),
    ("🌳","Root Intrusion","Tree roots invading your sewer line is one of the most common causes of backups. We remove intrusions and restore full flow capacity."),
])

save("sewer-line-repair.json", make_page(
    "Sewer Line Repair | Regal Plumbing & Rooter",
    "Sewer Line Repair | Regal Plumbing & Rooter",
    "Expert sewer line repair and replacement in the Inland Empire. Camera inspection, trenchless options available. Licensed & local. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Services"), "#FFFFFF"),
        (sl_hero, "#111827"),
        (sl_overview, "#FFFFFF"),
        (sl_covers, "#F3F4F6"),
        (why_section_html(), "#1E3A6E"),
        (OTHER_SERVICES, "#FFFFFF"),
        (cta_html("Sewer Problems? Get Expert Help Now", "Licensed sewer line specialists — camera inspection, trenchless repair, full replacement"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 9. WATER HEATER SERVICES ──────────────────────────────────────────────────
wh_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/sink-faucet-installation-ontario-ca.webp",
    "water heater installation Ontario CA",
    [("Home","/"),("Services","/services/"),("Water Heater Services",None)],
    "All Types & Brands",
    "Water Heater Services",
    "Installation, repair, and replacement of tank and tankless water heaters throughout the Inland Empire"
)
wh_overview = svc_overview(
    "Hot Water When You Need It",
    "Water Heater Installation & Repair",
    ["No hot water? We install and repair all types of water heaters — traditional tank units, tankless (on-demand) systems, and hybrid heat pump models. Our technicians are experienced with all major brands and can help you choose the right system for your household's needs and budget."],
    ["Traditional tank water heater install & repair","Tankless water heater installation","Heat pump water heater systems","Anode rod replacement and flushing","Pressure relief valve testing and replacement","Same-day service often available"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/water-heater-installation-inland-empire.webp",
    "water heater installation Ontario CA",
    "Get a Free Quote",
    "/contact/"
)
wh_covers = covers_section("Water Heater Services We Provide", [
    ("🔥","Tank Water Heaters","We install, repair, and replace traditional storage tank water heaters from all major brands. Fast, affordable, and backed by our workmanship warranty."),
    ("⚡","Tankless Systems","Tankless water heaters provide endless hot water on demand and reduce energy costs. We install and service all major tankless brands."),
    ("♻️","Heat Pump Systems","Hybrid heat pump water heaters are the most energy-efficient option available. We install and service these high-efficiency systems for qualified homes."),
])

save("water-heater-services.json", make_page(
    "Water Heater Installation & Repair | Regal Plumbing & Rooter",
    "Water Heater Installation & Repair | Regal Plumbing & Rooter",
    "Water heater installation, repair & replacement in the Inland Empire. Tank and tankless options. Same-day available. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Services"), "#FFFFFF"),
        (wh_hero, "#111827"),
        (wh_overview, "#FFFFFF"),
        (wh_covers, "#F3F4F6"),
        (why_section_html(), "#1E3A6E"),
        (OTHER_SERVICES, "#FFFFFF"),
        (cta_html("No Hot Water? Call Us Now", "Same-day water heater service often available — licensed & insured"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 10. SLAB LEAK DETECTION ───────────────────────────────────────────────────
sk_hero = img_hero_html(
    "http://regal-plumbing.local/wp-content/uploads/2026/03/leak-repair-wall-open-ontario-ca.webp",
    "slab leak detection pipe repair Inland Empire CA",
    [("Home","/"),("Services","/services/"),("Slab Leak Detection",None)],
    "Non-Invasive Technology",
    "Slab Leak Detection",
    "Electronic detection and repair of slab leaks throughout the Inland Empire — precise and minimally invasive"
)
sk_overview = svc_overview(
    "Find It Fast, Fix It Right",
    "Professional Slab Leak Detection & Repair",
    ["Slab leaks are among the most damaging — and hardest to find — plumbing problems a homeowner can face. We use electronic detection equipment to precisely locate leaks beneath your concrete slab without unnecessary excavation, saving you time, money, and the headache of major property disruption.","Signs you may have a slab leak: warm spots on floors, unexplained spikes in your water bill, the sound of running water with nothing in use, or cracks in your flooring or foundation. Call us immediately if you notice any of these."],
    ["Electronic leak detection — no guesswork","Spot repair and re-routing options","Epoxy pipe lining (non-invasive)","Post-repair pressure testing","Insurance documentation assistance","Fast response to minimize water damage"],
    "http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-repair-leak-detection-chino-hills-ca.webp",
    "slab leak detection pipe repair Inland Empire CA",
    "Get a Free Quote",
    "/contact/"
)
sk_covers = covers_section("Slab Leak Services We Provide", [
    ("🔍","Electronic Detection","We use advanced acoustic and electronic equipment to pinpoint the exact location of slab leaks without breaking concrete unnecessarily."),
    ("🔧","Spot Repair","Once located, we perform targeted spot repairs — opening only the minimum amount of concrete required to fix the leak."),
    ("🔄","Pipe Re-Routing","In cases where pipes are severely corroded or repeatedly failing, we re-route new lines through accessible areas to avoid future slab leaks."),
])

save("slab-leak-detection.json", make_page(
    "Slab Leak Detection & Repair | Regal Plumbing & Rooter",
    "Slab Leak Detection & Repair | Regal Plumbing & Rooter",
    "Professional slab leak detection and repair in the Inland Empire. Non-invasive technology, licensed & insured. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Services"), "#FFFFFF"),
        (sk_hero, "#111827"),
        (sk_overview, "#FFFFFF"),
        (sk_covers, "#F3F4F6"),
        (why_section_html(), "#1E3A6E"),
        (OTHER_SERVICES, "#FFFFFF"),
        (cta_html("Suspect a Slab Leak? Call Now", "Fast electronic detection — minimize damage to your home and foundation"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

print("Pages 4-10 done.")
