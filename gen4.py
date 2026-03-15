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
<div class="emergency-bar">24/7 Emergency Service Available \u2014 Call <a href="tel:9096004561">(909) 600-4561</a></div>"""

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

# ── SHARED CITY HELPERS ────────────────────────────────────────────────────────

def city_hero(city, h1_suffix, hero_sub):
    bc = f'<a href="/" style="color:#93C5FD;text-decoration:none">Home</a><span style="color:rgba(255,255,255,.3)"> › </span><a href="/service-area/" style="color:#93C5FD;text-decoration:none">Service Area</a><span style="color:rgba(255,255,255,.3)"> › </span><span style="color:rgba(255,255,255,.7)">{city} CA</span>'
    return f"""<style>.city-hero{{background:#1E3A6E;position:relative;overflow:hidden;padding:64px 24px}}.city-hero::before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent,transparent 2px,rgba(255,255,255,.015) 2px,rgba(255,255,255,.015) 4px)}}.city-hero-inner{{position:relative;z-index:2;max-width:1200px;margin:0 auto}}.breadcrumb{{display:flex;align-items:center;gap:8px;font-size:13px;color:#93C5FD;margin-bottom:14px;flex-wrap:wrap}}.city-hero h1{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}.city-hero-sub{{font-size:16px;color:#93C5FD;max-width:580px}}</style>
<div class="city-hero"><div class="city-hero-inner"><div class="breadcrumb">{bc}</div><h1>{h1_suffix}</h1><p class="city-hero-sub">{hero_sub}</p></div></div>"""

def city_map_section(city, map_src, map_title, intro_p1, intro_p2):
    return f"""<style>.map-sec{{background:#fff;padding:80px 24px}}.map-inner{{max-width:1200px;margin:0 auto}}.map-layout{{display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:start}}.map-embed{{border-radius:8px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.12);height:420px}}.map-embed iframe{{width:100%;height:100%;border:0;display:block}}.map-intro p{{font-size:15.5px;color:#4B5563;line-height:1.8;margin-bottom:16px}}.section-eyebrow{{font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px}}.section-title{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);letter-spacing:.5px;text-transform:uppercase;line-height:1.15;margin-bottom:14px}}.red-divider{{width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0 0}}@media(max-width:900px){{.map-layout{{grid-template-columns:1fr}}}}</style>
<section class="map-sec"><div class="map-inner"><div class="map-layout">
  <div class="map-embed"><iframe src="{map_src}" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="{map_title}"></iframe></div>
  <div class="map-intro">
    <div class="section-eyebrow">Your Local Plumber</div>
    <h2 class="section-title">Serving All of {city}, CA</h2>
    <div class="red-divider"></div>
    <p style="margin-top:20px;">{intro_p1}</p>
    <p>{intro_p2}</p>
  </div>
</div></div></section>"""

def city_trust_bar():
    return """<style>.trust-bar{background:#F3F4F6;padding:28px 24px;border-bottom:1px solid #E5E7EB}.trust-bar-inner{max-width:1200px;margin:0 auto;display:flex;flex-wrap:wrap;justify-content:center}.trust-item{display:flex;align-items:center;gap:12px;padding:12px 28px;border-right:1px solid #D1D5DB;flex:1;min-width:180px;justify-content:center}.trust-item:last-child{border-right:none}.trust-icon{font-size:24px;flex-shrink:0}.trust-label{font-family:'Oswald',sans-serif;font-weight:500;font-size:14px;letter-spacing:.5px;color:#2D2D2D;line-height:1.3}.trust-label span{display:block;font-family:'Open Sans',sans-serif;font-weight:400;font-size:11.5px;color:#6B7280;letter-spacing:0}@media(max-width:900px){.trust-bar-inner{flex-direction:column}.trust-item{border-right:none;border-bottom:1px solid #D1D5DB;padding:14px 16px}.trust-item:last-child{border-bottom:none}}</style>
<div class="trust-bar"><div class="trust-bar-inner">
  <div class="trust-item"><span class="trust-icon">⏰</span><div class="trust-label">24/7 Emergency<span>Always Available</span></div></div>
  <div class="trust-item"><span class="trust-icon">👨‍👩‍👧</span><div class="trust-label">Family Owned &amp; Operated<span>Community Focused</span></div></div>
  <div class="trust-item"><span class="trust-icon">✅</span><div class="trust-label">CA Licensed #1097482<span>Fully Insured</span></div></div>
  <div class="trust-item"><span class="trust-icon">⭐</span><div class="trust-label">4+ Years Experience<span>Proven Track Record</span></div></div>
  <div class="trust-item"><span class="trust-icon">📍</span><div class="trust-label">32+ Cities Served<span>Southern California</span></div></div>
</div></div>"""

def city_services(city, cards):
    cards_html = ""
    for img, alt, name, desc in cards:
        cards_html += f"""<a href="/{alt.replace(' ','').lower().split('ca')[0].strip().replace(' ','-')}/" class="svc-card" style="background:#fff;border:1px solid #E5E7EB;border-radius:8px;overflow:hidden;display:block;text-decoration:none">
  <div style="height:180px;overflow:hidden"><img src="{img}" alt="{alt}" loading="lazy" style="width:100%;height:100%;object-fit:cover" /></div>
  <div style="padding:16px 18px 20px"><div style="font-family:'Oswald',sans-serif;font-weight:600;font-size:17px;color:#2D2D2D;margin-bottom:7px">{name}</div><p style="font-size:13.5px;color:#6B7280;line-height:1.6;margin-bottom:14px">{desc}</p><span style="font-family:'Oswald',sans-serif;font-weight:500;font-size:13px;letter-spacing:1px;text-transform:uppercase;color:#B91C1C">Learn More →</span></div>
</a>"""
    return f"""<style>.city-svcs{{background:#F3F4F6;padding:80px 24px}}.city-svcs-inner{{max-width:1200px;margin:0 auto}}.svc-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px}}@media(max-width:900px){{.svc-grid{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:640px){{.svc-grid{{grid-template-columns:repeat(2,1fr)}}}}</style>
<section class="city-svcs"><div class="city-svcs-inner">
  <div style="text-align:center"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">What We Do</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">Plumbing Services in {city}, CA</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div class="svc-grid">{cards_html}</div>
</div></section>"""

def city_why(city, w1_icon, w1_title, w1_desc, w2_icon, w2_title, w2_desc, w3_icon, w3_title, w3_desc):
    def card(icon, title, desc):
        return f'<div style="text-align:center;padding:36px 28px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);border-radius:8px"><span style="font-size:42px;display:block;margin-bottom:16px">{icon}</span><div style="font-family:Oswald,sans-serif;font-weight:600;font-size:20px;color:#fff;text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px">{title}</div><p style="font-size:14.5px;color:#93C5FD;line-height:1.7">{desc}</p></div>'
    return f"""<style>.city-why{{background:#1E3A6E;padding:80px 24px}}.why-grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}}@media(max-width:640px){{.why-grid3{{grid-template-columns:1fr}}}}</style>
<section class="city-why"><div style="max-width:1200px;margin:0 auto">
  <div style="text-align:center;margin-bottom:48px"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#fca5a5;margin-bottom:10px">Our Promise</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);color:#fff;text-transform:uppercase;letter-spacing:.5px">Why {city} Residents Choose Regal</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div class="why-grid3">{card(w1_icon,w1_title,w1_desc)}{card(w2_icon,w2_title,w2_desc)}{card(w3_icon,w3_title,w3_desc)}</div>
</div></section>"""

def city_seo(city, seo_h2, p1, p2, p3, p4):
    return f"""<style>.seo-sec{{background:#fff;padding:80px 24px}}.seo-body p{{font-size:15.5px;color:#4B5563;line-height:1.85;margin-bottom:18px}}.seo-body strong{{color:#2D2D2D}}</style>
<section class="seo-sec"><div style="max-width:860px;margin:0 auto">
  <div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Local Expertise</div>
  <h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">{seo_h2}</h2>
  <div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px 0"></div>
  <div class="seo-body" style="margin-top:28px"><p>{p1}</p><p>{p2}</p><p>{p3}</p><p>{p4}</p></div>
</div></section>"""

def city_faq(city, faqs):
    items = ""
    for i,(q,a) in enumerate(faqs, 1):
        items += f"""<div style="background:#fff;border-radius:6px;overflow:hidden;border:1px solid #E5E7EB;margin-bottom:8px">
  <details><summary style="display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 24px;cursor:pointer;font-family:'Oswald',sans-serif;font-weight:500;font-size:16px;color:#2D2D2D;letter-spacing:.3px;list-style:none">{q}<span style="font-size:20px;color:#B91C1C;flex-shrink:0">+</span></summary>
  <div style="font-size:14.5px;color:#4B5563;line-height:1.7;padding:0 24px 20px">{a}</div></details>
</div>"""
    return f"""<section style="background:#F3F4F6;padding:80px 24px"><div style="max-width:1200px;margin:0 auto">
  <div style="text-align:center;margin-bottom:48px"><div style="font-family:'Oswald',sans-serif;font-weight:500;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#B91C1C;margin-bottom:10px">Common Questions</div><h2 style="font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,3.5vw,38px);text-transform:uppercase;letter-spacing:.5px">{city} Plumbing FAQs</h2><div style="width:56px;height:4px;background:#B91C1C;border-radius:2px;margin:14px auto 0"></div></div>
  <div style="max-width:800px;margin:0 auto">{items}</div>
</div></section>"""

def make_city_page(filename, title, seo_title, seo_desc, city, map_src, map_title,
                   intro_p1, intro_p2,
                   hero_sub,
                   w1_icon, w1_title, w1_desc,
                   w2_icon, w2_title, w2_desc,
                   w3_icon, w3_title, w3_desc,
                   seo_h2, seo_p1, seo_p2, seo_p3, seo_p4,
                   faqs, svc_cards,
                   cta_heading, cta_sub):
    hero = city_hero(city, f"Plumber in {city}, CA", hero_sub)
    map_sec = city_map_section(city, map_src, map_title, intro_p1, intro_p2)
    trust = city_trust_bar()
    svcs = city_services(city, svc_cards)
    why = city_why(city, w1_icon, w1_title, w1_desc, w2_icon, w2_title, w2_desc, w3_icon, w3_title, w3_desc)
    seo = city_seo(city, seo_h2, seo_p1, seo_p2, seo_p3, seo_p4)
    faq = city_faq(city, faqs)
    cta = cta_html(cta_heading, cta_sub)
    sections = [
        (EMERGENCY_BAR,"#2D2D2D"),
        (header_html("Service Area"),"#FFFFFF"),
        (hero,"#1E3A6E"),
        (map_sec,"#FFFFFF"),
        (trust,"#F3F4F6"),
        (svcs,"#F3F4F6"),
        (why,"#1E3A6E"),
        (seo,"#FFFFFF"),
        (faq,"#F3F4F6"),
        (cta,"#B91C1C"),
        (FOOTER,"#2D2D2D"),
    ]
    page = make_page(title, seo_title, seo_desc, sections)
    save(filename, page)

CITY_SVC_CARDS = [
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-repair-service-truck-inland-empire.webp","Emergency Plumbing","Emergency Plumbing","24/7 rapid response — we reach all neighborhoods fast, any hour of the day or night."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/drain-cleaning-shower-upland-ca.webp","Drain Cleaning","Drain Cleaning","Professional drain clearing using snaking, video inspection, and hydrojetting."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/sewer-line-excavation-ontario-ca.webp","Sewer Line Repair","Sewer Line Repair","Camera inspection and trenchless sewer repair — minimal disruption to your property."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/sink-faucet-installation-ontario-ca.webp","Water Heater Services","Water Heater Services","Tank, tankless, and heat pump water heater installation, repair, and replacement."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/pipe-repair-leak-detection-chino-hills-ca.webp","Slab Leak Detection","Slab Leak Detection","Electronic leak detection beneath concrete slabs — precise location, minimal demo."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/hydro-jetting-roof-rancho-cucamonga-ca.webp","Hydrojetting","Hydrojetting","High-pressure water jetting to scour pipe walls clean of scale, grease, and roots."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/camera-inspection-drain-cleaning-san-bernardino-ca.webp","Gas Leak Detection","Gas Leak Detection","Licensed gas line detection, repair, and pressure testing for your safety."),
    ("http://regal-plumbing.local/wp-content/uploads/2026/03/copper-pipe-installation-chino-ca.webp","Water Filtration","Water Filtration","Whole-home softeners, reverse osmosis, and filtration systems installed."),
]

# ── 18. CHINO, CA ─────────────────────────────────────────────────────────────
make_city_page(
    "chino-ca.json",
    "Plumber in Chino, CA | Regal Plumbing & Rooter",
    "Plumber in Chino CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Reliable plumber in Chino CA — drain cleaning, slab leak detection & water heater repair. 24/7 emergency service available. Call (909) 600-4561.",
    "Chino",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.6889!3d34.0122!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Plumber in Chino CA — Regal Plumbing Service Area",
    "Chino, CA is a city in rapid transition — historic agricultural roots giving way to one of the Inland Empire's fastest-growing residential developments. From the master-planned <strong>The Preserve</strong> community in the south to established neighborhoods like <strong>College Park</strong>, the original <strong>Downtown Chino</strong> corridor, and the <strong>Airport Area</strong>, Chino's plumbing landscape spans everything from brand-new construction to mid-century pipe systems.",
    "Regal Plumbing &amp; Rooter is a frequent presence in Chino homes and businesses. We handle slab leak detection in Preserve homes, drain cleaning in College Park's aging drainage systems, and gas line work near the Chino Airport corridor. Our team also regularly serves Chino's neighboring cities of <strong>Ontario</strong>, <strong>Chino Hills</strong>, and <strong>Corona</strong>.",
    "Trusted, local plumbing services for Chino homeowners and businesses — 24/7 emergency response and same-day appointments across the city.",
    "🏡","New &amp; Old Chino Homes","Whether your Chino home is in a new Preserve development or a decades-old College Park neighborhood, we have the experience to handle every plumbing system correctly.",
    "⚡","Fast Chino Response","From our Ontario base, we reach all of Chino — The Preserve, College Park, Downtown Chino, and the Airport Area — quickly for emergency and same-day service.",
    "✅","Licensed &amp; Insured","CA License #1097482. Every Chino job is performed by fully licensed plumbers with comprehensive liability coverage and straightforward, honest pricing.",
    "Trusted Plumber in Chino CA",
    "When you need a <strong>plumber in Chino CA</strong>, you want a team that understands the city's unique mix of brand-new residential development and established neighborhoods. <strong>The Preserve</strong> community in south Chino is among the region's newest master-planned developments, while <strong>College Park</strong>, <strong>Downtown Chino</strong>, and the neighborhoods around the <strong>Airport Area</strong> represent older housing stock with aging plumbing infrastructure. Regal Plumbing &amp; Rooter regularly serves both ends of Chino's spectrum — and everything in between. Our reach extends to neighboring cities like <strong>Ontario</strong>, <strong>Chino Hills</strong>, and <strong>Corona</strong> as well.",
    "As your trusted <strong>emergency plumber Chino CA</strong> service, we're available around the clock for everything from burst pipes to sewage backups to sudden water heater failures. Chino's rapid growth has put pressure on water supply infrastructure — new homes in The Preserve sometimes experience pressure regulator issues, water hammer, or pipe fittings that fail under high demand. Our team diagnoses these problems efficiently and fixes them right the first time.",
    "<strong>Drain cleaning Chino CA</strong> is a regular service we perform throughout the city. The groundwater that supplies Chino has historically been influenced by the region's agricultural past, contributing to higher-than-average mineral content in the water supply. This results in faster scale buildup inside pipes and drains, making routine maintenance especially important for Chino homeowners.",
    "For <strong>slab leak Chino</strong> detection, our electronic equipment gives us a precise location without demolishing large sections of flooring. Chino's slab-built homes — both older ones near Downtown and newer ones in master-planned sections — are all susceptible to copper pipe failures when soil shifts or water pressure is inconsistent. Our <strong>water heater repair Chino CA</strong> service covers traditional tank units, tankless systems, and heat pump water heaters with same-day or next-day availability in most cases.",
    [
        ("How fast can Regal Plumbing reach Chino in an emergency?","We typically reach Chino locations within 45–60 minutes of your call. Our Ontario base and regular service routes through the Chino area mean we're rarely more than a few minutes away. Emergency calls receive immediate dispatch priority."),
        ("Do you serve The Preserve and all of Chino's neighborhoods?","Yes — we serve all of Chino including The Preserve, College Park, Downtown Chino, the Airport Area, and every residential community throughout the city. No part of Chino is outside our service range."),
        ("Why does my Chino home have such bad water pressure issues?","Chino's newer developments sometimes experience pressure regulator failures, mineral scale buildup inside supply lines, or shared water main pressure fluctuations. We diagnose pressure issues by testing at the meter, main shutoff, and fixture level — then address the root cause."),
        ("Is Chino's water quality particularly bad for plumbing systems?","Chino's water carries above-average mineral content, which accelerates scale buildup inside pipes, water heaters, and appliances. This shortens the lifespan of water heaters and reduces water flow over time. A whole-home water softener and/or reverse osmosis system dramatically reduces these effects."),
        ("Do you offer weekend plumbing appointments in Chino?","Yes — we offer emergency plumbing service in Chino 24/7, including all weekends and holidays. For non-emergency work, we also have weekend scheduling available. Call (909) 600-4561 to check availability."),
    ],
    CITY_SVC_CARDS,
    "Need a Plumber in Chino? We're Ready",
    "24/7 emergency and same-day service throughout Chino, CA"
)

# ── 19. CORONA, CA ────────────────────────────────────────────────────────────
make_city_page(
    "corona-ca.json",
    "Plumber in Corona, CA | Regal Plumbing & Rooter",
    "Plumber in Corona CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Trusted plumber in Corona CA — drain cleaning, slab leak detection & water heater repair. 24/7 emergency service available. Call (909) 600-4561.",
    "Corona",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.5664!3d33.8753!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Plumber in Corona CA — Regal Plumbing Service Area",
    "Corona, CA sits at the gateway between the Inland Empire and Orange County, spanning a wide range of communities from <strong>South Corona</strong>'s master-planned neighborhoods and <strong>Eagle Glen</strong>'s hillside homes to older residential areas near historic downtown. Corona's location in the Santa Ana River watershed area means its water supply carries high mineral content, making scale buildup a persistent challenge throughout the city's plumbing systems.",
    "Regal Plumbing &amp; Rooter serves all of Corona with the same fast, professional service we provide across the Inland Empire. We're well-acquainted with the slab construction common in Corona's 1980s and 1990s developments, the irrigation line pressures in hillside communities like Eagle Glen, and the older pipe systems near downtown Corona. Our team also regularly serves neighboring cities <strong>Chino</strong>, <strong>Ontario</strong>, and <strong>Riverside</strong>.",
    "Professional plumbing services for Corona homeowners and businesses — 24/7 emergency response with fast dispatch across all Corona neighborhoods.",
    "🌊","Hard Water Specialists","We understand the mineral-heavy water challenges that affect Corona pipes, water heaters, and fixtures — and we address the root cause, not just the visible symptoms.",
    "⚡","Fast Corona Response","We reach South Corona, Eagle Glen, and all Corona neighborhoods quickly. Emergency calls receive immediate dispatch — no waiting for the next business day.",
    "✅","Licensed &amp; Insured","CA License #1097482. Every Corona job is performed by licensed plumbers with full liability insurance and transparent, upfront pricing on every service call.",
    "Trusted Plumber in Corona CA",
    "Homeowners searching for a <strong>plumber in Corona CA</strong> need someone familiar with the city's diverse neighborhoods and the water quality challenges that come with the Santa Ana River watershed area. From <strong>South Corona</strong>'s large master-planned communities to the hillside homes of <strong>Eagle Glen</strong> and the older established areas near <strong>downtown Corona</strong>, plumbing systems vary widely in age, material, and condition. Regal Plumbing &amp; Rooter serves all of Corona — and regularly handles calls from neighboring cities like <strong>Chino</strong>, <strong>Ontario</strong>, and <strong>Riverside</strong>.",
    "As the go-to <strong>emergency plumber Corona CA</strong> for the region, we respond immediately when you call. Burst pipes in Eagle Glen's elevated terrain, sewage backups in South Corona's newer subdivisions, and main line failures near downtown — we handle them all with professional urgency. Our vehicles are stocked with the parts and equipment needed to resolve most plumbing emergencies on the first visit.",
    "<strong>Drain cleaning Corona CA</strong> is particularly important given the city's hard water profile. Corona's water supply carries elevated levels of calcium and magnesium that leave scale deposits inside pipe walls, shower drains, and kitchen lines. Over time, this buildup restricts flow and eventually causes complete blockages. Our hydrojetting service is especially effective in Corona because it removes mineral deposits that snaking cannot.",
    "For <strong>slab leak Corona</strong> detection, we use electronic equipment to precisely locate leaks beneath concrete without unnecessary demolition — critical in Corona's many slab-built 1980s and 1990s homes where copper supply lines have been under long-term stress. Our <strong>water heater repair Corona CA</strong> team handles everything from faulty anode rods to full system replacement, and we always provide clear, honest assessments before any work begins.",
    [
        ("How fast can Regal Plumbing get to Corona in an emergency?","We typically reach Corona locations within 60–75 minutes of your call. Our technicians travel through the Inland Empire daily, so we're frequently near the Corona area. Emergency calls are dispatched immediately with priority routing."),
        ("Do you serve all of Corona, including Eagle Glen and South Corona?","Yes — we serve all of Corona, including Eagle Glen, South Corona, the historic downtown area, and all residential communities throughout the city. No neighborhood in Corona is outside our service range."),
        ("Why is Corona's water so hard on plumbing fixtures and water heaters?","Corona's water supply draws from the Santa Ana River watershed, which contains naturally occurring calcium and magnesium at elevated levels. These minerals deposit as scale inside water heaters, shower heads, faucets, and pipe walls — reducing efficiency and restricting flow. A whole-home water softener is the most effective long-term solution."),
        ("What are the signs of a slab leak in my Corona home?","Common slab leak signs include unexplained spikes in your water bill, warm or wet spots on your floor, a sound of running water when all fixtures are off, reduced water pressure, and cracks appearing in walls or flooring. Call us right away — slab leaks get much more expensive the longer they go undetected."),
        ("Does Regal Plumbing offer weekend service in Corona?","Yes — our emergency plumbing line is available 24/7 in Corona, including weekends and holidays. For non-emergency scheduled service, weekend appointments are also available. Call (909) 600-4561 to get started."),
    ],
    CITY_SVC_CARDS,
    "Need a Plumber in Corona? Call Now",
    "24/7 emergency and same-day service throughout Corona, CA"
)

# ── 20. UPLAND, CA ────────────────────────────────────────────────────────────
make_city_page(
    "upland-ca.json",
    "Plumber in Upland, CA | Regal Plumbing & Rooter",
    "Plumber in Upland CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Licensed plumber in Upland CA — drain cleaning, slab leak detection & water heater repair. 24/7 emergency service. Call (909) 600-4561.",
    "Upland",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.6484!3d34.0975!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Plumber in Upland CA — Regal Plumbing Service Area",
    "Upland, CA is a charming foothill city known for its tree-lined streets and historic character — and for the plumbing challenges that come with mature urban landscapes. Neighborhoods like <strong>North Upland</strong> and <strong>San Antonio Heights</strong> sit against the base of the San Gabriel Mountains, while the <strong>Upland Village</strong> corridor and the <strong>Cable</strong> neighborhood closer to the 10 freeway represent older mid-century housing stock with aging infrastructure throughout.",
    "Regal Plumbing &amp; Rooter serves all of Upland from our Ontario base, just minutes away. Tree root intrusions into sewer lines are one of our most common Upland service calls — the city's beautiful mature tree canopy comes with a cost to underground pipe systems. We also frequently handle drain cleaning, slab leak detection, and water heater work throughout Upland. Our team regularly covers neighboring cities <strong>Rancho Cucamonga</strong>, <strong>Ontario</strong>, and <strong>Claremont</strong>.",
    "Licensed, local plumbing for Upland homes and businesses — emergency response 24/7 and same-day service across all Upland neighborhoods.",
    "🌳","Root Intrusion Experts","Upland's beautiful tree canopy creates real sewer line challenges. We specialize in diagnosing and clearing root intrusions throughout North Upland, San Antonio Heights, Cable, and Upland Village.",
    "⚡","Fast Upland Response","Based in neighboring Ontario, we reach all Upland neighborhoods quickly. Most emergency calls in Upland receive a response in under an hour — any day, any time.",
    "✅","Licensed &amp; Insured","CA License #1097482. Every Upland job is completed by licensed professionals with full liability coverage and honest, upfront pricing — no hidden charges.",
    "Trusted Plumber in Upland CA",
    "When Upland residents search for a <strong>plumber in Upland CA</strong>, they're often dealing with the consequences of the city's beautiful, mature landscape. The tree-lined streets of <strong>San Antonio Heights</strong> and <strong>North Upland</strong> are some of the most desirable in the Inland Empire — but the roots of those mature trees have spent decades working their way into aging clay sewer lines. The established <strong>Upland Village</strong> corridor and the <strong>Cable</strong> neighborhood closer to the 10 freeway have older housing with plumbing systems that require experienced hands. Regal Plumbing &amp; Rooter serves all of Upland, and our neighboring city routes through <strong>Rancho Cucamonga</strong>, <strong>Ontario</strong>, and <strong>Claremont</strong> mean we're always close by.",
    "As a trusted <strong>emergency plumber Upland CA</strong> residents depend on, we understand that plumbing disasters don't wait for convenient times. A sewer backup in the middle of the night in North Upland, a burst pipe in San Antonio Heights on a Sunday morning — these situations need immediate, professional response. We dispatch quickly and arrive equipped to handle the problem without unnecessary delays or repeat visits.",
    "<strong>Drain cleaning Upland CA</strong> is one of our highest-volume services in this area, largely because of the combination of tree root infiltration and Upland's hard water mineral content. Many Upland homeowners experience recurring slow drains and think it's a simple clog — when in reality, a growing root mass inside their sewer main is the real problem. Our camera inspection service identifies the issue definitively, and our hydrojetting equipment clears it completely.",
    "For <strong>slab leak Upland</strong> detection, our team uses electronic listening devices and pressure testing to find leaks beneath concrete without tearing up your floors unnecessarily. Upland's mid-century homes — particularly those in Cable and the lower Upland Village areas — have copper supply lines that have been corroding for decades. Our <strong>water heater repair Upland CA</strong> service is well-regarded throughout the city — we stock common water heater parts and units on our service vehicles, so most jobs are completed in a single visit.",
    [
        ("How fast can Regal Plumbing reach Upland in an emergency?","From our Ontario base, we reach most Upland neighborhoods within 45–60 minutes of your call. Our technicians work throughout the Upland, Rancho Cucamonga, and Ontario area regularly, so response times are typically fast — even on nights and weekends."),
        ("Do you serve all of Upland, including North Upland and San Antonio Heights?","Yes — we serve all of Upland from the foothill areas of North Upland and San Antonio Heights down through Upland Village and the Cable neighborhood near the 10 freeway. Every part of Upland is in our service area."),
        ("Why do tree roots keep invading my Upland sewer line?","Tree roots grow toward moisture sources, and even tiny cracks in older clay or cast iron sewer pipes release enough moisture to attract them. Once inside, roots grow rapidly and can cause complete blockages or pipe collapse. Upland's mature tree canopy makes this one of the city's most common plumbing problems. Camera inspection and trenchless repair provide the most permanent solution."),
        ("Can you fix a slab leak in Upland without tearing up my floors?","In most cases, yes. Our electronic detection equipment pinpoints the leak location so we only need to access the specific area. In some cases, epoxy pipe lining or rerouting the line through walls is the best approach — we assess each situation individually and recommend the least invasive effective solution."),
        ("Is a water softener worth it for an Upland home?","For most Upland homeowners, yes — Upland's water is high in calcium and magnesium, which creates scale inside pipes, water heaters, and appliances. A whole-home water softener extends the life of your water heater by years and prevents scale buildup in shower heads and faucets. Most systems pay for themselves in reduced repair costs within a few years."),
    ],
    CITY_SVC_CARDS,
    "Need a Plumber in Upland? We're Ready",
    "24/7 emergency and same-day service throughout Upland, CA"
)

# ── 21. WEST COVINA, CA ───────────────────────────────────────────────────────
make_city_page(
    "west-covina-ca.json",
    "Plumber in West Covina, CA | Regal Plumbing & Rooter",
    "Plumber in West Covina CA — 24/7 Emergency Service | Regal Plumbing & Rooter",
    "Professional plumber in West Covina CA — drain cleaning, slab leak detection & water heater repair. 24/7 emergency service. Call (909) 600-4561.",
    "West Covina",
    "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d-117.9390!3d34.0686!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1",
    "Plumber in West Covina CA — Regal Plumbing Service Area",
    "West Covina is a well-established San Gabriel Valley city with a large portion of its housing stock built between the 1950s and 1970s — an era known for galvanized steel supply pipes and cast iron drain systems that are now reaching the end of their service life. Neighborhoods like <strong>Shadow Oak</strong>, <strong>Merced Heights</strong>, <strong>Sunset</strong>, and <strong>Monte Vista</strong> are full of post-war homes where plumbing problems are becoming increasingly common as original systems age.",
    "Regal Plumbing &amp; Rooter serves all of West Covina with the same professional standards we bring to every city in our coverage area. We handle galvanized pipe replacements, slab leak detection, drain cleaning in older clay sewer systems, and water heater upgrades in West Covina homes regularly. Our service area also encompasses West Covina's neighboring cities of <strong>Covina</strong>, <strong>Diamond Bar</strong>, and <strong>Pomona</strong>.",
    "Professional plumbing services for West Covina homeowners and businesses — 24/7 emergency response and same-day service across the city.",
    "🏚️","Old-Home Specialists","West Covina's post-war housing stock — in Shadow Oak, Merced Heights, Sunset, and Monte Vista — requires knowledge of galvanized pipes, cast iron drains, and aging slab systems. We have it.",
    "⚡","Fast West Covina Response","We reach West Covina from our Ontario base via the 10 freeway quickly. Most emergency calls in West Covina receive a response within an hour — including nights and weekends.",
    "✅","Licensed &amp; Insured","CA License #1097482. Every West Covina job is backed by licensed technicians, full liability insurance, and honest pricing — we quote before we work, every time.",
    "Trusted Plumber in West Covina CA",
    "When residents search for a <strong>plumber in West Covina CA</strong>, they're often dealing with the plumbing failures that come naturally with a city built primarily in the post-war era. The majority of West Covina's residential neighborhoods — including <strong>Shadow Oak</strong>, <strong>Merced Heights</strong>, <strong>Sunset</strong>, and <strong>Monte Vista</strong> — contain homes built between 1950 and 1975, when galvanized steel supply pipes and clay or cast iron drain systems were standard. These materials are now well past their designed service life. Regal Plumbing &amp; Rooter understands West Covina's plumbing landscape and serves the city and its neighbors <strong>Covina</strong>, <strong>Diamond Bar</strong>, and <strong>Pomona</strong>.",
    "As the trusted <strong>emergency plumber West Covina CA</strong> residents call at any hour, we're prepared for the types of emergencies that plague aging housing stock. Galvanized pipe failures cause sudden pressure drops and discolored water. Clay sewer main collapses cause sewage backups. Corroding copper slab lines cause unexplained water bill spikes and wet floors. Our team arrives equipped for all of these scenarios and resolves them efficiently.",
    "<strong>Drain cleaning West Covina CA</strong> is one of our most frequent service calls in this area. West Covina's 60–70 year old drain systems have decades of grease, scale, and tree root infiltration accumulated inside them. Basic snaking provides temporary relief, but for homes with recurring blockages, hydrojetting is the superior solution — it scours the pipe wall completely clean rather than just punching a temporary hole through the obstruction.",
    "For <strong>slab leak West Covina</strong> detection, our team uses electronic listening equipment and pressure testing to locate the precise failure point beneath your concrete slab — minimizing the area of flooring that must be disturbed. Our <strong>water heater repair West Covina CA</strong> service is equally important in this city — many original water heaters installed in West Covina homes decades ago are long overdue for replacement, and our team can complete most standard tank replacements in a single visit.",
    [
        ("How fast can Regal Plumbing get to West Covina in an emergency?","We typically reach West Covina within 60–75 minutes of your call via the 10 freeway from our Ontario base. Our technicians also work throughout the San Gabriel Valley regularly, so we're often closer than the drive time suggests. Emergency calls are dispatched immediately, day or night."),
        ("Do you serve all of West Covina, including Shadow Oak and Merced Heights?","Yes — we serve all of West Covina, including Shadow Oak, Merced Heights, Sunset, Monte Vista, and all residential neighborhoods throughout the city. We also serve neighboring communities like Covina, Diamond Bar, and Pomona."),
        ("My West Covina home was built in the 1960s — should I replace all the pipes?","Not necessarily all at once — it depends on what material was used and current condition. Many West Covina homes from that era have galvanized steel supply pipes, which may be showing signs of corrosion, reduced flow, or rust-colored water. We assess the actual condition of your pipes before making recommendations, and we're honest about what's truly necessary versus what can wait."),
        ("What causes slab leaks in West Covina's older homes?","In West Covina's post-war slab homes, copper supply lines were embedded directly in concrete. Over 60–70 years, the water's mineral content corrodes copper from the inside, while soil movement and thermal expansion stress the pipe from the outside. Eventually this creates pinhole leaks or larger failures — the longer they go undetected, the more damage they cause."),
        ("Can you replace a water heater in West Covina the same day?","In most cases, yes. Our service vehicles carry standard tank water heater sizes, so same-day replacements are common for West Covina homeowners with a failed or failing tank unit. Tankless system installations typically require a scheduled follow-up appointment. Call (909) 600-4561 to get started."),
    ],
    CITY_SVC_CARDS,
    "Need a Plumber in West Covina? Call Now",
    "24/7 emergency and same-day service throughout West Covina, CA"
)

print("Pages 18-21 done.")
