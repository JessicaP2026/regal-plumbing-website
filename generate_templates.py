import json, os, random, string

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
    nav_links = [
        ("/", "Home"),
        ("/services/", "Services"),
        ("/about/", "About"),
        ("/service-area/", "Service Area"),
        ("/contact/", "Contact"),
    ]
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

FOOTER = """<style>.site-footer{background:#2D2D2D;color:#fff;padding:64px 24px 0}.footer-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.6fr 1fr 1fr 1.3fr;gap:48px;padding-bottom:48px;border-bottom:1px solid rgba(255,255,255,.10)}.footer-logo-name{font-family:'Oswald',sans-serif;font-weight:700;font-size:18px;color:#fff;letter-spacing:1px;text-transform:uppercase;margin-bottom:6px}.footer-tagline{font-size:13px;color:#9CA3AF;margin-bottom:16px;line-height:1.6}.footer-license{display:inline-block;background:rgba(185,28,28,.2);border:1px solid rgba(185,28,28,.4);color:#fca5a5;font-size:11.5px;font-family:'Oswald',sans-serif;letter-spacing:1px;padding:4px 10px;border-radius:3px}.footer-col h4{font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:18px;padding-bottom:10px;border-bottom:2px solid #B91C1C;display:inline-block}.footer-links{list-style:none;display:flex;flex-direction:column;gap:9px;padding:0}.footer-links a{font-size:13.5px;color:#9CA3AF;text-decoration:none;display:flex;align-items:center;gap:6px}.footer-links a::before{content:"›";color:#B91C1C;font-size:16px}.footer-contact-list{list-style:none;display:flex;flex-direction:column;gap:12px;padding:0}.footer-contact-list li{display:flex;gap:10px;font-size:13.5px;color:#9CA3AF;line-height:1.5}.footer-contact-list a{color:#9CA3AF;text-decoration:none}.footer-bottom{max-width:1200px;margin:0 auto;padding:18px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}.footer-bottom-text{font-size:12.5px;color:#6B7280}.footer-bottom-links{display:flex;gap:20px}.footer-bottom-links a{font-size:12.5px;color:#6B7280;text-decoration:none}@media(max-width:900px){.footer-inner{grid-template-columns:1fr 1fr;gap:32px}}@media(max-width:640px){.footer-inner{grid-template-columns:1fr;gap:28px}.footer-bottom{flex-direction:column;text-align:center}}</style>
<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <div class="footer-logo-name">Regal Plumbing &amp; Rooter</div>
      <p class="footer-tagline">Honest, professional plumbing &amp; rooter services for the Inland Empire &amp; San Gabriel Valley.</p>
      <span class="footer-license">CA License #1097482</span>
    </div>
    <div class="footer-col">
      <h4>Services</h4>
      <ul class="footer-links">
        <li><a href="/emergency-plumbing/">Emergency Plumbing</a></li>
        <li><a href="/drain-cleaning/">Drain Cleaning</a></li>
        <li><a href="/sewer-line-repair/">Sewer Line Repair</a></li>
        <li><a href="/water-heater-services/">Water Heater Services</a></li>
        <li><a href="/slab-leak-detection/">Slab Leak Detection</a></li>
        <li><a href="/hydrojetting/">Hydrojetting</a></li>
        <li><a href="/gas-leak-detection/">Gas Leak Detection</a></li>
        <li><a href="/water-filtration/">Water Filtration</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Service Area</h4>
      <ul class="footer-links">
        <li><a href="/service-area/ontario-ca/">Ontario</a></li>
        <li><a href="/service-area/rancho-cucamonga-ca/">Rancho Cucamonga</a></li>
        <li><a href="/service-area/fontana-ca/">Fontana</a></li>
        <li><a href="/service-area/pomona-ca/">Pomona</a></li>
        <li><a href="/service-area/chino-ca/">Chino</a></li>
        <li><a href="/service-area/corona-ca/">Corona</a></li>
        <li><a href="/service-area/upland-ca/">Upland</a></li>
        <li><a href="/service-area/west-covina-ca/">West Covina</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contact Us</h4>
      <ul class="footer-contact-list">
        <li><span>📍</span><span>2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</span></li>
        <li><span>📞</span><a href="tel:9096004561">(909) 600-4561</a></li>
        <li><span>✉️</span><a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></li>
        <li><span>🕐</span><span>24/7 Emergency<br>Mon–Sat: 7am–7pm</span></li>
      </ul>
    </div>
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
<section class="cta-section">
  <div class="cta-inner">
    <h2>{heading}</h2>
    <p class="cta-sub">{subtext}</p>
    <a href="tel:9096004561" class="cta-phone">(909) 600-4561</a><br>
    <a href="tel:9096004561" class="btn-white-red">📞 Call Now</a>
  </div>
</section>"""

def make_container(html_content, bg_color="#FFFFFF"):
    return {
        "id": uid(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "background_background": "classic",
            "background_color": bg_color,
            "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
        },
        "elements": [
            {
                "id": uid(),
                "elType": "widget",
                "widgetType": "html",
                "settings": {"html": html_content},
                "elements": []
            }
        ]
    }

def make_page(title, seo_title, seo_desc, sections_html):
    content = []
    for html, bg in sections_html:
        content.append(make_container(html, bg))
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

# ── 1. INDEX ──────────────────────────────────────────────────────────────────
hero_index = """<style>
.hero{position:relative;background:#1E3A6E;min-height:560px;display:flex;align-items:center;overflow:hidden}
.hero-bg{position:absolute;inset:0;background:linear-gradient(105deg,rgba(0,0,0,.75) 0%,rgba(30,58,110,.55) 60%,rgba(185,28,28,.2) 100%)}
.hero-inner{position:relative;z-index:2;max-width:1200px;margin:0 auto;padding:80px 24px;width:100%}
.hero-badge{display:inline-block;background:#B91C1C;color:#fff;font-family:'Oswald',sans-serif;font-weight:600;font-size:12px;letter-spacing:2px;text-transform:uppercase;padding:5px 16px;border-radius:3px;margin-bottom:20px}
.hero h1{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(34px,5vw,62px);color:#fff;text-transform:uppercase;letter-spacing:1px;line-height:1.05;margin-bottom:16px}
.hero h1 span{color:#fca5a5}
.hero-sub{font-size:17px;color:#D1D5DB;max-width:540px;line-height:1.7;margin-bottom:32px}
.hero-btns{display:flex;gap:16px;flex-wrap:wrap}
.btn-red-lg{display:inline-flex;align-items:center;gap:8px;padding:15px 30px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;border:2px solid #B91C1C;text-decoration:none}
.btn-outline-white{display:inline-flex;align-items:center;gap:8px;padding:15px 30px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;background:transparent;color:#fff;border:2px solid rgba(255,255,255,.7);text-decoration:none}
.hero-trust{display:flex;gap:24px;margin-top:40px;flex-wrap:wrap}
.hero-trust-item{display:flex;align-items:center;gap:8px;font-size:13px;color:rgba(255,255,255,.75)}
.hero-trust-item span{color:#fca5a5;font-weight:700}
</style>
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-inner">
    <div class="hero-badge">CA License #1097482 — Serving 32+ Cities</div>
    <h1>Your <span>Trusted Plumber</span><br>in the Inland Empire</h1>
    <p class="hero-sub">Family-owned, licensed &amp; insured plumbing &amp; rooter services. Emergency response available 24/7 across Ontario, Rancho Cucamonga, Fontana &amp; beyond.</p>
    <div class="hero-btns">
      <a href="tel:9096004561" class="btn-red-lg">📞 Call (909) 600-4561</a>
      <a href="/contact/" class="btn-outline-white">Get a Free Quote</a>
    </div>
    <div class="hero-trust">
      <div class="hero-trust-item"><span>✓</span> 24/7 Emergency Service</div>
      <div class="hero-trust-item"><span>✓</span> Upfront Pricing</div>
      <div class="hero-trust-item"><span>✓</span> Licensed &amp; Insured</div>
      <div class="hero-trust-item"><span>✓</span> Family Owned</div>
    </div>
  </div>
</section>"""

trust_bar_index = """<style>
.trust-bar{background:#F3F4F6;border-top:3px solid #B91C1C;border-bottom:1px solid #E5E7EB}
.trust-bar-inner{max-width:1200px;margin:0 auto;display:flex;align-items:stretch}
.trust-item{flex:1;display:flex;align-items:center;gap:12px;padding:18px 24px;border-right:1px solid #E5E7EB}
.trust-item:last-child{border-right:none}
.trust-icon{font-size:22px}
.trust-label{font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px;line-height:1.2}
.trust-label span{display:block;font-family:'Open Sans',sans-serif;font-weight:400;font-size:12px;color:#6B7280;text-transform:none;letter-spacing:0}
@media(max-width:900px){.trust-bar-inner{flex-wrap:wrap}.trust-item{border-right:none;border-bottom:1px solid #E5E7EB;min-width:50%}}
</style>
<div class="trust-bar">
  <div class="trust-bar-inner">
    <div class="trust-item"><span class="trust-icon">⏰</span><div class="trust-label">24/7 Emergency<span>Always Available</span></div></div>
    <div class="trust-item"><span class="trust-icon">👨‍👩‍👧</span><div class="trust-label">Family Owned<span>Community Focused</span></div></div>
    <div class="trust-item"><span class="trust-icon">✅</span><div class="trust-label">CA Licensed #1097482<span>Fully Insured</span></div></div>
    <div class="trust-item"><span class="trust-icon">⭐</span><div class="trust-label">4+ Years Experience<span>Proven Track Record</span></div></div>
    <div class="trust-item"><span class="trust-icon">📍</span><div class="trust-label">32+ Cities Served<span>Inland Empire &amp; SGV</span></div></div>
  </div>
</div>"""

services_index = """<style>
.services-section{background:#F3F4F6;padding:80px 24px}
.section-inner{max-width:1200px;margin:0 auto}
.section-eyebrow{font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px}
.section-title{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);letter-spacing:.5px;text-transform:uppercase;line-height:1.15;margin-bottom:14px}
.red-divider{width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0}
.services-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px}
.service-card{background:#fff;border-radius:8px;overflow:hidden;border:1px solid #E5E7EB;text-decoration:none;display:block;transition:box-shadow .25s,transform .25s}
.service-card:hover{box-shadow:0 8px 32px rgba(0,0,0,.10);transform:translateY(-4px)}
.service-photo{height:160px;overflow:hidden}
.service-photo img{width:100%;height:100%;object-fit:cover}
.service-body{padding:20px}
.service-name{font-family:'Oswald',sans-serif;font-weight:600;font-size:16px;text-transform:uppercase;letter-spacing:.5px;color:#2D2D2D;margin-bottom:8px}
.service-desc{font-size:13.5px;color:#6B7280;line-height:1.6;margin-bottom:14px}
.service-link{font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#B91C1C}
@media(max-width:900px){.services-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.services-grid{grid-template-columns:1fr}}
</style>
<section class="services-section">
  <div class="section-inner">
    <div style="text-align:center;margin-bottom:0">
      <div class="section-eyebrow">What We Do</div>
      <h2 class="section-title">Full-Service Plumbing Solutions</h2>
      <div class="red-divider"></div>
      <p style="font-size:16px;color:#6B7280;max-width:520px;margin:16px auto 0;line-height:1.65;">From emergency repairs to planned installations — our licensed technicians handle it all across the Inland Empire.</p>
    </div>
    <div class="services-grid">
      <a href="/emergency-plumbing/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-repair-leak-detection-chino-hills-ca.webp" alt="24/7 emergency plumber Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Emergency Plumbing</div>
          <p class="service-desc">24/7 rapid response for burst pipes, sewage backups, and major leaks throughout the Inland Empire.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/drain-cleaning/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/drain-cleaning-shower-upland-ca.webp" alt="drain cleaning service Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Drain Cleaning</div>
          <p class="service-desc">Professional clearing of kitchen, bathroom, and main sewer line blockages with same-day service available.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/sewer-line-repair/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-line-repair-excavation-fontana-ca.webp" alt="sewer line repair excavation Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Sewer Line Repair</div>
          <p class="service-desc">Camera inspection, trenchless repair, and full sewer line replacement with minimal disruption.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/water-heater-services/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/sink-faucet-installation-ontario-ca.webp" alt="water heater installation Ontario CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Water Heater Services</div>
          <p class="service-desc">Installation, repair &amp; replacement of tank and tankless water heaters — all brands and models.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/slab-leak-detection/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/leak-repair-wall-open-ontario-ca.webp" alt="slab leak detection pipe repair Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Slab Leak Detection</div>
          <p class="service-desc">Electronic leak detection beneath your concrete slab — precise, minimally invasive, and affordable.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/hydrojetting/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/hydro-jetting-roof-rancho-cucamonga-ca.webp" alt="hydrojetting drain cleaning service Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Hydrojetting</div>
          <p class="service-desc">High-pressure water jetting clears roots, grease, and scale buildup from drain and sewer lines.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/gas-leak-detection/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/camera-inspection-drain-cleaning-san-bernardino-ca.webp" alt="gas leak detection Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Gas Leak Detection</div>
          <p class="service-desc">Safe, licensed gas leak detection and repair — call immediately for emergencies, available 24/7.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
      <a href="/water-filtration/" class="service-card">
        <div class="service-photo"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-replacement-copper-ontario-ca.webp" alt="water filtration copper pipe installation Inland Empire CA" loading="lazy" /></div>
        <div class="service-body">
          <div class="service-name">Water Filtration</div>
          <p class="service-desc">Whole-home softeners and reverse osmosis systems for clean, soft water throughout your home.</p>
          <span class="service-link">Learn More →</span>
        </div>
      </a>
    </div>
  </div>
</section>"""

why_index = """<style>
.why-section{background:#1E3A6E;padding:80px 24px}
.why-inner{max-width:1200px;margin:0 auto}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:48px}
.why-card{text-align:center;padding:32px 24px}
.why-icon{font-size:40px;display:block;margin-bottom:16px}
.why-title{font-family:'Oswald',sans-serif;font-weight:600;font-size:19px;color:#fff;text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px}
.why-desc{font-size:14px;color:#93C5FD;line-height:1.7}
@media(max-width:640px){.why-grid{grid-template-columns:1fr}}
</style>
<section class="why-section">
  <div class="why-inner">
    <div style="text-align:center">
      <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#fca5a5;margin-bottom:10px">Our Promise</div>
      <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);color:#fff;text-transform:uppercase;letter-spacing:.5px">Why Choose Regal Plumbing?</h2>
      <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
    </div>
    <div class="why-grid">
      <div class="why-card"><span class="why-icon">💰</span><div class="why-title">Honest Pricing</div><p class="why-desc">Upfront, transparent quotes before any work begins. No hidden fees, no surprise invoices — ever.</p></div>
      <div class="why-card"><span class="why-icon">⚡</span><div class="why-title">Fast Response</div><p class="why-desc">24/7 availability for emergencies. We mobilize quickly and work efficiently to minimize damage and downtime.</p></div>
      <div class="why-card"><span class="why-icon">🔧</span><div class="why-title">Quality Workmanship</div><p class="why-desc">Every job backed by our commitment to premium craftsmanship. Licensed, insured, and built to last.</p></div>
    </div>
  </div>
</section>"""

area_index = """<style>
.area-section{background:#fff;padding:80px 24px}
.area-inner{max-width:1200px;margin:0 auto}
.area-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px 16px;margin:32px 0}
.area-city{display:flex;align-items:center;gap:8px;font-size:14.5px;color:#2D2D2D;padding:6px 0;border-bottom:1px solid #E5E7EB}
.area-city::before{content:'';width:7px;height:7px;background:#B91C1C;border-radius:50%;flex-shrink:0}
@media(max-width:900px){.area-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.area-grid{grid-template-columns:1fr}}
</style>
<section class="area-section">
  <div class="area-inner">
    <div style="text-align:center;margin-bottom:32px">
      <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Where We Work</div>
      <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Service Area — 32+ Cities</h2>
      <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
      <p style="font-size:16px;color:#6B7280;max-width:500px;margin:16px auto 0;line-height:1.65;">We proudly serve communities throughout the Inland Empire and San Gabriel Valley.</p>
    </div>
    <div class="area-grid">
      <div class="area-city">Ontario</div><div class="area-city">Rancho Cucamonga</div>
      <div class="area-city">Fontana</div><div class="area-city">Pomona</div>
      <div class="area-city">Chino</div><div class="area-city">Chino Hills</div>
      <div class="area-city">Corona</div><div class="area-city">Upland</div>
      <div class="area-city">West Covina</div><div class="area-city">Diamond Bar</div>
      <div class="area-city">Montclair</div><div class="area-city">Claremont</div>
      <div class="area-city">La Verne</div><div class="area-city">San Dimas</div>
      <div class="area-city">Glendora</div><div class="area-city">Covina</div>
      <div class="area-city">Azusa</div><div class="area-city">Eastvale</div>
      <div class="area-city">Rialto</div><div class="area-city">Colton</div>
    </div>
    <div style="text-align:center"><a href="/service-area/" style="display:inline-flex;align-items:center;padding:12px 28px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;text-decoration:none">View Full Service Area →</a></div>
  </div>
</section>"""

save("index.json", make_page(
    "Regal Plumbing & Rooter — 24/7 Plumber | Inland Empire",
    "Regal Plumbing & Rooter — 24/7 Plumber | Inland Empire",
    "Family-owned licensed plumbers serving Ontario, Rancho Cucamonga, Fontana & 30+ cities. Emergency plumbing, drain cleaning, slab leak repair & more. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Home"), "#FFFFFF"),
        (hero_index, "#1E3A6E"),
        (trust_bar_index, "#F3F4F6"),
        (services_index, "#F3F4F6"),
        (why_index, "#1E3A6E"),
        (area_index, "#FFFFFF"),
        (cta_html("Ready for Expert Plumbing Service?", "Call now for a free quote or immediate emergency response"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 2. ABOUT ──────────────────────────────────────────────────────────────────
about_hero = """<style>
.page-hero{background:#111827;position:relative;overflow:hidden;padding:64px 24px}
.page-hero-bg{position:absolute;inset:0;background:linear-gradient(135deg,rgba(30,58,110,.7) 0%,rgba(0,0,0,.8) 70%)}
.page-hero-inner{position:relative;z-index:2;max-width:1200px;margin:0 auto}
.breadcrumb{display:flex;align-items:center;gap:8px;font-size:13px;color:#9CA3AF;margin-bottom:14px}
.breadcrumb a{color:#9CA3AF;text-decoration:none}
.breadcrumb-sep{color:#4B5563}
.breadcrumb-current{color:#fca5a5}
.page-hero h1{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}
.page-hero-sub{font-size:16px;color:#D1D5DB;max-width:540px}
</style>
<div class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="/">Home</a><span class="breadcrumb-sep">›</span><span class="breadcrumb-current">About Us</span></div>
    <h1>About Regal Plumbing &amp; Rooter</h1>
    <p class="page-hero-sub">A family-owned plumbing company built on honesty, craftsmanship, and community service across Southern California.</p>
  </div>
</div>"""

about_intro = """<style>
.about-section{background:#fff;padding:80px 24px}
.about-inner{max-width:1200px;margin:0 auto}
.about-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:72px;align-items:center}
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;width:100%;margin-top:16px}
.stat-box{background:#F3F4F6;border:1px solid #E5E7EB;border-top:3px solid #B91C1C;border-radius:6px;padding:18px 12px;text-align:center}
.stat-number{font-family:'Oswald',sans-serif;font-weight:700;font-size:28px;color:#B91C1C;line-height:1;margin-bottom:4px}
.stat-label{font-size:11.5px;color:#6B7280;letter-spacing:.3px;line-height:1.4}
.section-eyebrow{font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px}
.section-title{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);letter-spacing:.5px;text-transform:uppercase;line-height:1.15}
.red-divider{width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0 24px}
.about-body{font-size:15.5px;color:#4B5563;line-height:1.8;margin-bottom:18px}
@media(max-width:900px){.about-grid{grid-template-columns:1fr;gap:40px}}
</style>
<section class="about-section">
  <div class="about-inner">
    <div class="about-grid">
      <div>
        <img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumbing-rooter-office-ontario-ca.webp" alt="Regal Plumbing &amp; Rooter Ontario CA Office" style="width:100%;border-radius:10px;box-shadow:0 8px 30px rgba(0,0,0,.15);" loading="lazy" />
        <div class="stat-row">
          <div class="stat-box"><div class="stat-number">32+</div><div class="stat-label">Cities Served</div></div>
          <div class="stat-box"><div class="stat-number">4+</div><div class="stat-label">Years in Business</div></div>
          <div class="stat-box"><div class="stat-number">24/7</div><div class="stat-label">Emergency Service</div></div>
        </div>
      </div>
      <div>
        <div class="section-eyebrow">Our Story</div>
        <h2 class="section-title">Who We Are</h2>
        <div class="red-divider"></div>
        <p class="about-body">Regal Plumbing &amp; Rooter was founded with one clear goal: to bring honesty, professionalism, and premium craftsmanship to every customer we serve. We saw a gap in the market — too many homeowners were being overcharged, under-informed, and left frustrated by plumbers who didn't treat them with respect. We set out to change that.</p>
        <p class="about-body">As a family-owned business based in Ontario, CA, we take pride in building real relationships with our customers. When you call Regal, you're not calling a call center — you're calling a local team that genuinely cares about your home and your family's wellbeing. We treat every job as if it were our own home.</p>
        <p class="about-body">Licensed, insured, and serving over 32 cities across the Inland Empire and San Gabriel Valley, Regal Plumbing &amp; Rooter has become a trusted name in Southern California plumbing.</p>
        <a href="tel:9096004561" style="display:inline-flex;align-items:center;padding:12px 24px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;text-decoration:none;margin-right:14px;">📞 Call Us Today</a>
        <a href="/services/" style="font-family:'Oswald',sans-serif;font-weight:500;font-size:14px;letter-spacing:1px;text-transform:uppercase;color:#B91C1C;text-decoration:none">View Our Services →</a>
      </div>
    </div>
  </div>
</section>"""

values_section = """<style>
.values-section{background:#F3F4F6;padding:80px 24px}
.values-inner{max-width:1200px;margin:0 auto}
.values-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.value-card{background:#fff;border-radius:10px;border:1px solid #E5E7EB;padding:36px 28px;text-align:center}
.value-icon{font-size:48px;display:block;margin-bottom:16px}
.value-title{font-family:'Oswald',sans-serif;font-weight:600;font-size:19px;color:#2D2D2D;margin-bottom:10px}
.value-desc{font-size:14px;color:#6B7280;line-height:1.7}
@media(max-width:900px){.values-grid{grid-template-columns:1fr}}
</style>
<section class="values-section">
  <div class="values-inner">
    <div style="text-align:center;margin-bottom:52px">
      <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">What Drives Us</div>
      <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Our Core Values</h2>
      <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
    </div>
    <div class="values-grid">
      <div class="value-card"><span class="value-icon">🤝</span><div class="value-title">Honesty &amp; Transparency</div><p class="value-desc">We believe every customer deserves clear, upfront pricing and honest advice — even when that means recommending a less expensive solution. We never upsell work that isn't needed.</p></div>
      <div class="value-card"><span class="value-icon">🔧</span><div class="value-title">Quality Craftsmanship</div><p class="value-desc">We take pride in doing the job right the first time. Our work is done to last, using quality materials and proven techniques. We stand behind everything we install or repair.</p></div>
      <div class="value-card"><span class="value-icon">❤️</span><div class="value-title">Community Commitment</div><p class="value-desc">We're not just serving homes — we're building relationships in the communities where we live and work. Supporting our neighbors is at the heart of everything Regal does.</p></div>
    </div>
  </div>
</section>"""

credentials_section = """<style>
.creds-section{background:#fff;padding:80px 24px}
.creds-inner{max-width:1200px;margin:0 auto}
.creds-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.cred-card{display:flex;align-items:flex-start;gap:20px;background:#F3F4F6;border:1px solid #E5E7EB;border-left:5px solid #B91C1C;border-radius:8px;padding:24px 22px}
.cred-icon{font-size:32px;flex-shrink:0}
.cred-title{font-family:'Oswald',sans-serif;font-weight:600;font-size:16px;color:#2D2D2D;margin-bottom:4px}
.cred-desc{font-size:13.5px;color:#6B7280;line-height:1.6}
@media(max-width:900px){.creds-grid{grid-template-columns:1fr}}
</style>
<section class="creds-section">
  <div class="creds-inner">
    <div style="text-align:center;margin-bottom:52px">
      <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Verified &amp; Trusted</div>
      <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Our Credentials</h2>
      <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
    </div>
    <div class="creds-grid">
      <div class="cred-card"><span class="cred-icon">📋</span><div><div class="cred-title">California Contractor's License #1097482</div><p class="cred-desc">Fully licensed by the California Contractors State License Board (CSLB). Our license is verifiable at cslb.ca.gov.</p></div></div>
      <div class="cred-card"><span class="cred-icon">🛡️</span><div><div class="cred-title">Fully Insured &amp; Bonded</div><p class="cred-desc">Regal Plumbing &amp; Rooter carries comprehensive general liability insurance and workers' compensation coverage on every job.</p></div></div>
      <div class="cred-card"><span class="cred-icon">👨‍👩‍👧</span><div><div class="cred-title">Family Owned &amp; Operated</div><p class="cred-desc">We are a locally owned, family-operated business — not a franchise. Every decision is made with our customers and community in mind.</p></div></div>
      <div class="cred-card"><span class="cred-icon">⏰</span><div><div class="cred-title">24/7 Emergency Availability</div><p class="cred-desc">Plumbing emergencies don't follow business hours. Our team is on-call around the clock, every day of the year.</p></div></div>
      <div class="cred-card"><span class="cred-icon">📍</span><div><div class="cred-title">Locally Based in Ontario, CA</div><p class="cred-desc">Our shop is at 2141 E Philadelphia St, Suite R, Ontario, CA 91761 — right in the heart of the Inland Empire.</p></div></div>
      <div class="cred-card"><span class="cred-icon">⭐</span><div><div class="cred-title">4+ Years of Proven Service</div><p class="cred-desc">Since our founding, we've built a track record of five-star reviews and satisfied customers across Southern California.</p></div></div>
    </div>
  </div>
</section>"""

team_section = """<style>
.team-section{background:#fff;padding:80px 24px}
.team-inner{max-width:1200px;margin:0 auto}
.team-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:32px}
.team-member{text-align:center}
.team-member img{width:100%;aspect-ratio:3/4;object-fit:cover;object-position:top;border-radius:8px;margin-bottom:14px}
.team-name{font-family:'Oswald',sans-serif;font-weight:600;font-size:17px;color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px}
.team-role{font-size:13px;color:#6B7280;margin-top:3px}
</style>
<section class="team-section">
  <div class="team-inner">
    <div style="text-align:center;margin-bottom:52px">
      <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">The People Behind the Work</div>
      <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Meet Our Team</h2>
      <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div>
      <p style="font-size:16px;color:#6B7280;max-width:500px;margin:16px auto 0;line-height:1.65;">Skilled, licensed, and genuinely committed to doing right by every customer.</p>
    </div>
    <div class="team-grid">
      <div class="team-member"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumber-brayden-ontario-ca.webp" alt="Brayden — Plumbing Technician" loading="lazy" /><div class="team-name">Brayden</div><div class="team-role">Plumbing Technician</div></div>
      <div class="team-member"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumber-tony-ontario-ca.webp" alt="Tony — Plumbing Technician" loading="lazy" /><div class="team-name">Tony</div><div class="team-role">Plumbing Technician</div></div>
      <div class="team-member"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumber-ashton-ontario-ca.webp" alt="Ashton — Plumbing Technician" loading="lazy" /><div class="team-name">Ashton</div><div class="team-role">Plumbing Technician</div></div>
      <div class="team-member"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumber-nick-ontario-ca.webp" alt="Nick — Plumbing Technician" loading="lazy" /><div class="team-name">Nick</div><div class="team-role">Plumbing Technician</div></div>
      <div class="team-member"><img src="http://regal-plumbing.local/wp-content/uploads/2026/03/regal-plumbing-office-natalie-ontario-ca.webp" alt="Natalie — Office Manager" loading="lazy" /><div class="team-name">Natalie</div><div class="team-role">Office Manager</div></div>
    </div>
  </div>
</section>"""

promise_section = """<style>
.promise-section{background:#2D2D2D;padding:80px 24px}
.promise-inner{max-width:1200px;margin:0 auto}
.promise-grid{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.promise-list{list-style:none;display:flex;flex-direction:column;gap:20px;margin-top:28px;padding:0}
.promise-item{display:flex;align-items:flex-start;gap:16px}
.promise-icon{font-size:28px;flex-shrink:0;margin-top:2px}
.promise-item-title{font-family:'Oswald',sans-serif;font-weight:600;font-size:17px;color:#fff;margin-bottom:4px}
.promise-item-desc{font-size:14px;color:#9CA3AF;line-height:1.65}
.promise-visual{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:40px 32px}
.promise-visual-title{font-family:'Oswald',sans-serif;font-weight:700;font-size:22px;color:#fff;margin-bottom:20px;letter-spacing:.5px}
.promise-quote{font-size:17px;color:#D1D5DB;line-height:1.8;font-style:italic;padding-left:20px;border-left:4px solid #B91C1C}
.promise-sig{margin-top:24px;font-family:'Oswald',sans-serif;font-weight:500;font-size:15px;color:#fca5a5;letter-spacing:.5px}
@media(max-width:900px){.promise-grid{grid-template-columns:1fr;gap:40px}}
</style>
<section class="promise-section">
  <div class="promise-inner">
    <div class="promise-grid">
      <div>
        <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#fca5a5;margin-bottom:10px">Our Commitment to You</div>
        <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);color:#fff;text-transform:uppercase;letter-spacing:.5px">The Regal Promise</h2>
        <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0 28px"></div>
        <ul class="promise-list">
          <li class="promise-item"><span class="promise-icon">💰</span><div><div class="promise-item-title">Upfront Pricing — Always</div><p class="promise-item-desc">You'll know the full cost before we begin any work. No hidden fees, no surprise invoices.</p></div></li>
          <li class="promise-item"><span class="promise-icon">🎯</span><div><div class="promise-item-title">First-Time Fixes</div><p class="promise-item-desc">We properly diagnose problems before starting work, so we fix it right the first time.</p></div></li>
          <li class="promise-item"><span class="promise-icon">🧹</span><div><div class="promise-item-title">Respect for Your Home</div><p class="promise-item-desc">Our technicians wear shoe covers, protect your floors, and leave the work area cleaner than we found it.</p></div></li>
          <li class="promise-item"><span class="promise-icon">📞</span><div><div class="promise-item-title">Real People, Real Answers</div><p class="promise-item-desc">When you call us, a real person answers. We communicate clearly at every step.</p></div></li>
        </ul>
      </div>
      <div class="promise-visual">
        <div class="promise-visual-title">A Note From Our Family</div>
        <p class="promise-quote">"When we started Regal Plumbing &amp; Rooter, we made a promise to every customer: we would treat your home the way we treat our own. That means honest advice, quality work, and being there when you need us most. That promise hasn't changed — and it never will."</p>
        <div class="promise-sig">— The Regal Plumbing &amp; Rooter Team</div>
      </div>
    </div>
  </div>
</section>"""

save("about.json", make_page(
    "About Us | Regal Plumbing & Rooter",
    "About Us | Regal Plumbing & Rooter",
    "Family-owned CA licensed plumbing company serving the Inland Empire. Honest pricing, fast response, quality workmanship. CA License #1097482. Call (909) 600-4561.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("About"), "#FFFFFF"),
        (about_hero, "#111827"),
        (about_intro, "#FFFFFF"),
        (values_section, "#F3F4F6"),
        (credentials_section, "#FFFFFF"),
        (team_section, "#FFFFFF"),
        (promise_section, "#2D2D2D"),
        (cta_html("Ready to Work With Us?", "Call now for a free quote — or reach out anytime for emergency service"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

# ── 3. CONTACT ────────────────────────────────────────────────────────────────
contact_hero = """<style>
.page-hero{background:#2D2D2D;position:relative;overflow:hidden;padding:64px 24px}
.page-hero::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent,transparent 2px,rgba(255,255,255,.015) 2px,rgba(255,255,255,.015) 4px)}
.page-hero-inner{position:relative;z-index:2;max-width:1200px;margin:0 auto}
.breadcrumb{display:flex;align-items:center;gap:8px;font-size:13px;color:#9CA3AF;margin-bottom:14px}
.breadcrumb a{color:#9CA3AF;text-decoration:none}
.breadcrumb-sep{color:#4B5563}
.breadcrumb-current{color:#fca5a5}
.page-hero h1{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}
.page-hero-sub{font-size:16px;color:#D1D5DB;max-width:540px}
</style>
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="breadcrumb"><a href="/">Home</a><span class="breadcrumb-sep">›</span><span class="breadcrumb-current">Contact Us</span></div>
    <h1>Contact Regal Plumbing &amp; Rooter</h1>
    <p class="page-hero-sub">Call now for immediate service or fill out the form below — we'll get back to you fast.</p>
  </div>
</div>"""

contact_body = """<style>
.contact-section{background:#fff;padding:80px 24px}
.contact-inner{max-width:1200px;margin:0 auto}
.contact-layout{display:grid;grid-template-columns:1.1fr 1fr;gap:64px;align-items:start}
.form-heading{font-family:'Oswald',sans-serif;font-weight:700;font-size:28px;color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px}
.form-subheading{font-size:15px;color:#6B7280;margin-bottom:32px;line-height:1.6}
.contact-form{display:flex;flex-direction:column;gap:18px}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.form-group{display:flex;flex-direction:column;gap:6px}
.form-group label{font-family:'Oswald',sans-serif;font-weight:500;font-size:13px;letter-spacing:.8px;text-transform:uppercase;color:#2D2D2D}
.form-group input,.form-group select,.form-group textarea{width:100%;padding:12px 14px;border:1.5px solid #D1D5DB;border-radius:4px;font-family:'Open Sans',sans-serif;font-size:14px;color:#2D2D2D;background:#fff;outline:none;appearance:none}
.form-group textarea{resize:vertical;min-height:120px}
.btn-submit{width:100%;padding:15px 24px;font-size:16px;background:#B91C1C;color:#fff;border:2px solid #B91C1C;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;letter-spacing:1px;text-transform:uppercase;cursor:pointer}
.form-note{font-size:12px;color:#9CA3AF;text-align:center;margin-top:10px}
.info-phone-box{background:#1E3A6E;border-radius:8px;padding:32px 28px;text-align:center;margin-bottom:28px}
.info-phone-label{font-family:'Oswald',sans-serif;font-size:13px;font-weight:500;letter-spacing:2px;text-transform:uppercase;color:#93C5FD;margin-bottom:8px}
.info-phone-num{font-family:'Oswald',sans-serif;font-weight:700;font-size:36px;color:#fff;letter-spacing:1px;display:block;margin-bottom:16px;text-decoration:none}
.info-call-btn{display:block;width:100%;padding:13px;background:#B91C1C;color:#fff;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;text-decoration:none;text-align:center}
.info-blocks{display:flex;flex-direction:column;gap:16px}
.info-block{display:flex;gap:14px;align-items:flex-start;padding:18px;background:#F3F4F6;border-radius:6px;border-left:4px solid #B91C1C}
.info-block-icon{font-size:20px;flex-shrink:0;margin-top:1px}
.info-block-title{font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;text-transform:uppercase;letter-spacing:.5px;color:#2D2D2D;margin-bottom:4px}
.info-block-text{font-size:13.5px;color:#4B5563;line-height:1.6}
.info-block-text a{color:#B91C1C}
@media(max-width:900px){.contact-layout{grid-template-columns:1fr}}
@media(max-width:640px){.form-row{grid-template-columns:1fr}}
</style>
<section class="contact-section">
  <div class="contact-inner">
    <div class="contact-layout">
      <div class="form-side">
        <h2 class="form-heading">Send Us a Message</h2>
        <p class="form-subheading">Fill out the form and we'll respond promptly. For emergencies, call us directly at <a href="tel:9096004561" style="color:#B91C1C;font-weight:600;">(909) 600-4561</a>.</p>
        <form class="contact-form" action="/thank-you/" method="POST">
          <div class="form-row">
            <div class="form-group"><label for="full-name">Full Name *</label><input type="text" id="full-name" name="full-name" placeholder="John Smith" /></div>
            <div class="form-group"><label for="phone">Phone Number *</label><input type="tel" id="phone" name="phone" placeholder="(909) 000-0000" /></div>
          </div>
          <div class="form-group"><label for="email">Email Address</label><input type="email" id="email" name="email" placeholder="john@example.com" /></div>
          <div class="form-row">
            <div class="form-group"><label for="city">City *</label>
              <select id="city" name="city"><option value="">Select your city...</option><option>Ontario</option><option>Rancho Cucamonga</option><option>Fontana</option><option>Pomona</option><option>Chino</option><option>Chino Hills</option><option>Corona</option><option>Upland</option><option>West Covina</option><option>Diamond Bar</option><option>Claremont</option><option>Montclair</option><option>La Verne</option><option>San Dimas</option><option>Glendora</option><option>Covina</option><option>Azusa</option><option>Eastvale</option><option>Rialto</option><option>Colton</option><option>Other</option></select>
            </div>
            <div class="form-group"><label for="service">Service Needed *</label>
              <select id="service" name="service"><option value="">Select a service...</option><option value="emergency-plumbing">Emergency Plumbing</option><option value="drain-cleaning">Drain Cleaning</option><option value="sewer-line-repair">Sewer Line Repair</option><option value="water-heater">Water Heater Install &amp; Repair</option><option value="slab-leak">Slab Leak Detection &amp; Repair</option><option value="hydrojetting">Hydrojetting</option><option value="gas-leak-detection">Gas Leak Detection</option><option value="water-filtration">Water Filtration &amp; Softeners</option><option value="other">Other / Not Sure</option></select>
            </div>
          </div>
          <div class="form-group"><label for="message">Describe Your Issue</label><textarea id="message" name="message" placeholder="Tell us a bit about what's going on..."></textarea></div>
          <button type="submit" class="btn-submit">Send Message →</button>
          <p class="form-note">🔒 Your information is private. We respond within 1 business hour during operating hours.</p>
        </form>
      </div>
      <div class="info-side">
        <div class="info-phone-box">
          <div class="info-phone-label">For Fastest Service — Call Us</div>
          <a href="tel:9096004561" class="info-phone-num">(909) 600-4561</a>
          <a href="tel:9096004561" class="info-call-btn">📞 Call Now — We Answer 24/7</a>
        </div>
        <div class="info-blocks">
          <div class="info-block"><div class="info-block-icon">📍</div><div><div class="info-block-title">Our Location</div><div class="info-block-text">2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</div></div></div>
          <div class="info-block"><div class="info-block-icon">✉️</div><div><div class="info-block-title">Email Us</div><div class="info-block-text"><a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></div></div></div>
          <div class="info-block"><div class="info-block-icon">🕐</div><div><div class="info-block-title">Hours of Operation</div><div class="info-block-text"><strong>Emergency Line:</strong> 24/7, 365 days<br><strong>Office Hours:</strong> Mon–Sat, 7am–7pm<br><strong>Sunday:</strong> Emergency service only</div></div></div>
          <div class="info-block"><div class="info-block-icon">📍</div><div><div class="info-block-title">Service Area</div><div class="info-block-text">Serving 32+ cities across the Inland Empire &amp; San Gabriel Valley. <a href="/service-area/">View full list →</a></div></div></div>
          <div class="info-block"><div class="info-block-icon">✅</div><div><div class="info-block-title">License &amp; Insurance</div><div class="info-block-text">CA Contractor License #1097482<br>Fully licensed, bonded &amp; insured</div></div></div>
        </div>
      </div>
    </div>
  </div>
</section>"""

save("contact.json", make_page(
    "Contact Us | Regal Plumbing & Rooter",
    "Contact Us | Regal Plumbing & Rooter",
    "Contact Regal Plumbing & Rooter for 24/7 emergency plumbing service in the Inland Empire. Call (909) 600-4561 or fill out our contact form.",
    [
        (EMERGENCY_BAR, "#2D2D2D"),
        (header_html("Contact"), "#FFFFFF"),
        (contact_hero, "#2D2D2D"),
        (contact_body, "#FFFFFF"),
        (cta_html("Plumbing Emergency? Don't Wait — Call Now", "We're available 24/7 for emergency plumbing across Southern California"), "#B91C1C"),
        (FOOTER, "#2D2D2D"),
    ]
))

print("Pages 1-3 done (index, about, contact)")
