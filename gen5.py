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

# ── SHARED NAVY HERO ───────────────────────────────────────────────────────────
def navy_hero_with_bc(h1, sub, bc_items):
    bc = ""
    for label, href in bc_items:
        if href:
            bc += f'<a href="{href}" style="color:#93C5FD;text-decoration:none">{label}</a><span style="color:rgba(255,255,255,.3)"> › </span>'
        else:
            bc += f'<span style="color:rgba(255,255,255,.7)">{label}</span>'
    return f"""<style>.page-hero{{background:#1E3A6E;position:relative;overflow:hidden;padding:64px 24px}}.page-hero::before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(45deg,transparent,transparent 2px,rgba(255,255,255,.015) 2px,rgba(255,255,255,.015) 4px)}}.page-hero-inner{{position:relative;z-index:2;max-width:1200px;margin:0 auto}}.breadcrumb{{display:flex;align-items:center;gap:8px;font-size:13px;color:#93C5FD;margin-bottom:14px;flex-wrap:wrap}}.page-hero h1{{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(30px,4vw,48px);color:#fff;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}}.page-hero-sub{{font-size:16px;color:#93C5FD;max-width:580px}}</style>
<div class="page-hero"><div class="page-hero-inner"><div class="breadcrumb">{bc}</div><h1>{h1}</h1><p class="page-hero-sub">{sub}</p></div></div>"""

# ── 22. PRIVACY POLICY ────────────────────────────────────────────────────────
privacy_hero = navy_hero_with_bc(
    "Privacy Policy",
    "How Regal Plumbing &amp; Rooter collects, uses, and protects your information.",
    [("Home","/"),("Privacy Policy",None)]
)

privacy_content = """<style>.policy-section{background:#fff;padding:80px 24px}.policy-inner{max-width:860px;margin:0 auto;font-family:'Open Sans',sans-serif;font-size:15.5px;color:#4B5563;line-height:1.85}.policy-inner h2{font-family:'Oswald',sans-serif;font-weight:600;font-size:22px;color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px;margin:36px 0 12px;padding-bottom:8px;border-bottom:2px solid #B91C1C}.policy-inner p{margin-bottom:16px}.policy-inner ul{margin:0 0 16px 20px}.policy-inner ul li{margin-bottom:8px}.policy-inner strong{color:#2D2D2D}.policy-updated{font-size:13px;color:#6B7280;margin-bottom:24px}.policy-nap{background:#F3F4F6;border-left:4px solid #B91C1C;padding:16px 20px;border-radius:0 6px 6px 0;margin-bottom:28px;font-size:14px;color:#2D2D2D}.policy-nap p{margin-bottom:0}.policy-nap a{color:#B91C1C;text-decoration:none}</style>
<section class="policy-section"><div class="policy-inner">
  <p class="policy-updated">Last Updated: March 1, 2025</p>
  <div class="policy-nap"><strong>Regal Plumbing &amp; Rooter</strong><p>2141 E Philadelphia St, Suite R, Ontario, CA 91761 &nbsp;|&nbsp; <a href="tel:9096004561">(909) 600-4561</a> &nbsp;|&nbsp; <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></p></div>
  <h2>1. Introduction</h2>
  <p>Regal Plumbing &amp; Rooter ("we," "us," or "our") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or contact us for plumbing services. Please read this policy carefully. If you disagree with its terms, please discontinue use of our site.</p>
  <h2>2. Information We Collect</h2>
  <p>We may collect information about you in a variety of ways. The information we may collect includes:</p>
  <ul>
    <li><strong>Personal Data:</strong> Name, email address, phone number, city, and service information you voluntarily provide when submitting a contact form or calling us.</li>
    <li><strong>Derivative Data:</strong> Information our servers automatically collect when you visit our website, such as your IP address, browser type, operating system, access times, and pages you have viewed.</li>
    <li><strong>Mobile Device Data:</strong> If you access our site from a mobile device, we may collect information about your mobile device, including the hardware model, operating system, and mobile network information.</li>
  </ul>
  <h2>3. Contact Forms</h2>
  <p>When you submit a contact form on our website, we collect your full name, phone number, email address, city, service needed, and any message you provide. This information is used solely to respond to your service inquiry, schedule appointments, and provide plumbing services to you. We do not sell or rent this information to third parties.</p>
  <p>Form submissions are sent directly to <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a> and may be processed by our email service provider for delivery purposes.</p>
  <h2>4. Cookies and Tracking Technologies</h2>
  <p>We may use cookies, web beacons, tracking pixels, and other tracking technologies on our website to help customize the site and improve your experience. When you access our website, your personal information is not collected through the use of tracking technology.</p>
  <p>Most browsers are set to accept cookies by default. You can remove or reject cookies in your browser's settings. Please be aware that such action could affect the availability and functionality of the website.</p>
  <h2>5. Google Analytics</h2>
  <p>We use Google Analytics to analyze traffic and usage patterns on our website. Google Analytics collects information such as how often users visit the site, what pages they visit, and what other sites they used prior to coming to our site. We use this information to improve our website and marketing efforts.</p>
  <p>Google Analytics collects only the IP address assigned to you on the date you visit this site, rather than your name or other identifying information. We do not combine the information collected through the use of Google Analytics with personally identifiable information.</p>
  <h2>6. Third-Party Services</h2>
  <p>We may share your information with third parties that perform services on our behalf, including:</p>
  <ul>
    <li><strong>Email delivery services</strong> used to transmit contact form submissions.</li>
    <li><strong>Google Maps</strong> embedded on our website for location display purposes.</li>
    <li><strong>Web hosting and analytics providers</strong> that help us operate and improve our website.</li>
  </ul>
  <p>These third parties have access to your personal information only to perform their specific functions and are obligated not to disclose or use it for any other purpose.</p>
  <h2>7. How We Use Your Information</h2>
  <p>Having accurate information about you permits us to provide you with a smooth, efficient, and customized experience. Specifically, we may use information collected about you to:</p>
  <ul>
    <li>Respond to your service inquiries and schedule plumbing appointments.</li>
    <li>Email or call you regarding your inquiry or existing service request.</li>
    <li>Monitor and analyze usage and trends to improve your experience with our website.</li>
    <li>Comply with legal obligations and resolve any disputes we may have.</li>
    <li>Send you administrative information such as changes to our terms and policies.</li>
  </ul>
  <h2>8. Disclosure of Your Information</h2>
  <p>We do not sell, trade, or otherwise transfer your personally identifiable information to outside parties. We may share your information in the following situations:</p>
  <ul>
    <li><strong>By Law or to Protect Rights:</strong> If we believe the release of information about you is necessary to respond to legal process, to investigate or remedy potential violations of our policies, or to protect the rights, property, and safety of others.</li>
    <li><strong>Business Transfers:</strong> We may share or transfer your information in connection with, or during negotiations of, any merger, sale of company assets, financing, or acquisition of all or a portion of our business.</li>
  </ul>
  <h2>9. Security of Your Information</h2>
  <p>We use administrative, technical, and physical security measures to help protect your personal information. While we have taken reasonable steps to secure the personal information you provide to us, please be aware that despite our efforts, no security measures are perfect or impenetrable, and no method of data transmission can be guaranteed against any interception or other type of misuse.</p>
  <h2>10. Your Rights</h2>
  <p>Depending on your location, you may have certain rights regarding your personal information, including:</p>
  <ul>
    <li><strong>Right to Access:</strong> You may request a copy of the personal information we hold about you.</li>
    <li><strong>Right to Correct:</strong> You may request that we correct inaccurate or incomplete personal information.</li>
    <li><strong>Right to Delete:</strong> You may request that we delete your personal information, subject to certain exceptions.</li>
    <li><strong>Right to Opt-Out:</strong> California residents have the right to opt out of the sale of personal information (we do not sell your information).</li>
  </ul>
  <p>To exercise any of these rights, please contact us at <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a> or call <a href="tel:9096004561">(909) 600-4561</a>.</p>
  <h2>11. California Privacy Rights (CCPA)</h2>
  <p>California residents may have additional rights under the California Consumer Privacy Act (CCPA). If you are a California resident, you have the right to know what personal information we collect, the right to delete personal information, the right to opt-out of the sale of personal information, and the right to non-discrimination for exercising your CCPA rights. To make a CCPA-related request, contact us at the information provided below.</p>
  <h2>12. Children's Privacy</h2>
  <p>Our website is not directed to children under the age of 13, and we do not knowingly collect personal information from children under 13. If we learn we have collected or received personal information from a child under 13 without verification of parental consent, we will delete that information.</p>
  <h2>13. Changes to This Privacy Policy</h2>
  <p>We may update this Privacy Policy from time to time. The updated version will be indicated by an updated "Last Updated" date at the top of this page. We encourage you to review this Privacy Policy periodically to stay informed about how we are protecting your information.</p>
  <h2>14. Contact Us</h2>
  <p>If you have questions or concerns about this Privacy Policy or our privacy practices, please contact us:</p>
  <div class="policy-nap"><strong>Regal Plumbing &amp; Rooter</strong><p>2141 E Philadelphia St, Suite R, Ontario, CA 91761<br>Phone: <a href="tel:9096004561">(909) 600-4561</a><br>Email: <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></p></div>
</div></section>"""

save("privacy-policy.json", make_page(
    "Privacy Policy | Regal Plumbing & Rooter",
    "Privacy Policy | Regal Plumbing & Rooter",
    "Privacy Policy for Regal Plumbing & Rooter — how we collect, use, and protect your information.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html(),"#FFFFFF"),(privacy_hero,"#1E3A6E"),(privacy_content,"#FFFFFF"),(cta_html("Questions? We're Here to Help","Call us anytime — 24/7 emergency plumbing service across Southern California"),"#B91C1C"),(FOOTER,"#2D2D2D")]
))

# ── 23. TERMS OF SERVICE ──────────────────────────────────────────────────────
tos_hero = navy_hero_with_bc(
    "Terms of Service",
    "Please read these terms carefully before using our services or website.",
    [("Home","/"),("Terms of Service",None)]
)

tos_content = """<style>.policy-section{background:#fff;padding:80px 24px}.policy-inner{max-width:860px;margin:0 auto;font-family:'Open Sans',sans-serif;font-size:15.5px;color:#4B5563;line-height:1.85}.policy-inner h2{font-family:'Oswald',sans-serif;font-weight:600;font-size:22px;color:#2D2D2D;text-transform:uppercase;letter-spacing:.5px;margin:36px 0 12px;padding-bottom:8px;border-bottom:2px solid #B91C1C}.policy-inner p{margin-bottom:16px}.policy-inner ul{margin:0 0 16px 20px}.policy-inner ul li{margin-bottom:8px}.policy-inner strong{color:#2D2D2D}.policy-updated{font-size:13px;color:#6B7280;margin-bottom:24px}.policy-nap{background:#F3F4F6;border-left:4px solid #B91C1C;padding:16px 20px;border-radius:0 6px 6px 0;margin-bottom:28px;font-size:14px;color:#2D2D2D}.policy-nap p{margin-bottom:0}.policy-nap a{color:#B91C1C;text-decoration:none}</style>
<section class="policy-section"><div class="policy-inner">
  <p class="policy-updated">Last Updated: March 1, 2025</p>
  <div class="policy-nap"><strong>Regal Plumbing &amp; Rooter</strong><p>2141 E Philadelphia St, Suite R, Ontario, CA 91761 &nbsp;|&nbsp; <a href="tel:9096004561">(909) 600-4561</a> &nbsp;|&nbsp; <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a></p></div>
  <h2>1. Acceptance of Terms</h2>
  <p>By accessing our website or engaging Regal Plumbing &amp; Rooter ("Company," "we," "us," or "our") for plumbing services, you agree to be bound by these Terms of Service ("Terms"). If you do not agree to these Terms, please do not use our website or services. These Terms apply to all visitors, users, and others who access or use our services.</p>
  <h2>2. Services Provided</h2>
  <p>Regal Plumbing &amp; Rooter provides residential and commercial plumbing services including but not limited to: emergency plumbing, drain cleaning, sewer line repair, water heater installation and repair, slab leak detection, hydrojetting, gas leak detection, and water filtration system installation.</p>
  <p>All services are provided by licensed plumbers. Our California Contractor License number is #1097482. We are fully licensed, bonded, and insured to perform plumbing work in the state of California.</p>
  <h2>3. Service Agreement</h2>
  <p>A service agreement is established when:</p>
  <ul>
    <li>You contact us and we agree to perform work at your property, or</li>
    <li>You accept a written or verbal estimate from one of our technicians, or</li>
    <li>Work begins at your property with your consent.</li>
  </ul>
  <p>We reserve the right to refuse service to anyone at our discretion. We may decline to perform work that we determine is unsafe, outside our scope of expertise, or in violation of applicable building codes or regulations.</p>
  <h2>4. Estimates and Pricing</h2>
  <p>We provide upfront, transparent pricing before any work begins. Written or verbal estimates are based on the information available at the time of assessment. Final pricing may vary if:</p>
  <ul>
    <li>Hidden damage or additional issues are discovered during the work.</li>
    <li>Additional materials or labor are required beyond the initial scope.</li>
    <li>Permit fees or inspections are required by local jurisdiction.</li>
  </ul>
  <p>We will notify you of any changes to the estimate before proceeding with additional work. You have the right to approve or decline additional work before it is performed.</p>
  <h2>5. Payment Terms</h2>
  <p>Payment is due upon completion of services unless otherwise agreed in writing. We accept cash, check, and major credit cards. For large projects, we may require a deposit before work begins, which will be disclosed in your written estimate.</p>
  <p>Accounts not paid within 30 days of service completion may be subject to a late fee of 1.5% per month on the outstanding balance. We reserve the right to pursue collection of unpaid balances through legal means, including small claims court.</p>
  <p>Returned checks are subject to a $35 returned check fee in addition to any bank charges incurred.</p>
  <h2>6. Warranties</h2>
  <p>We stand behind our work. Regal Plumbing &amp; Rooter provides the following warranty coverage:</p>
  <ul>
    <li><strong>Labor Warranty:</strong> All labor performed by our technicians is warranted against defects for 30 days from the date of service, unless otherwise specified in writing.</li>
    <li><strong>Parts Warranty:</strong> Parts and materials are covered by the manufacturer's warranty. We will facilitate warranty claims on parts we supply and install.</li>
    <li><strong>Drain Cleaning:</strong> Drain cleaning services carry a 30-day warranty against the same blockage returning, provided no foreign objects are introduced to the drain system.</li>
  </ul>
  <p>Warranties are void if: (a) the plumbing system is modified by another party after our work is completed; (b) damage results from misuse, neglect, or acts of nature; (c) the issue is caused by municipal water supply problems outside our control.</p>
  <h2>7. Liability Limitations</h2>
  <p>Regal Plumbing &amp; Rooter's liability to you for any damages arising from our services shall not exceed the total amount paid for the specific service giving rise to the claim. We are not liable for:</p>
  <ul>
    <li>Pre-existing conditions in your plumbing system not disclosed at the time of service.</li>
    <li>Consequential, incidental, or indirect damages including loss of use, lost profits, or data loss.</li>
    <li>Damage caused by access issues we could not reasonably foresee.</li>
    <li>Damage resulting from municipal infrastructure failures or utility outages.</li>
  </ul>
  <p>We carry general liability insurance and workers' compensation insurance as required by California law. Our liability insurance information is available upon request.</p>
  <h2>8. Property Access and Conditions</h2>
  <p>You agree to provide our technicians with safe, reasonable access to all areas of the property where work is to be performed. This includes clearing the work area of personal belongings, pets, and obstructions. We are not responsible for damage to personal property that was not moved from the work area prior to our arrival.</p>
  <p>You represent that you have the legal authority to authorize work at the property, whether as the property owner or as an authorized agent of the owner.</p>
  <h2>9. Cancellation Policy</h2>
  <p>You may cancel or reschedule a service appointment without penalty by providing at least 2 hours' notice before the scheduled appointment time. Cancellations with less than 2 hours' notice may be subject to a service call fee to cover the cost of dispatching a technician.</p>
  <p>Emergency service calls that are cancelled after a technician has been dispatched may be subject to a trip charge. The applicable trip charge will be disclosed when you schedule emergency service.</p>
  <h2>10. Permits and Code Compliance</h2>
  <p>Work requiring building permits will be identified during the estimate process. Permit fees are the responsibility of the property owner and are not included in labor estimates unless specifically stated. We will obtain required permits on your behalf and include permit costs in the final invoice.</p>
  <p>All work is performed in compliance with the California Plumbing Code and applicable local ordinances. We do not perform work that would violate applicable building codes or regulations.</p>
  <h2>11. Dispute Resolution</h2>
  <p>In the event of a dispute arising from our services, we ask that you first contact us directly to resolve the matter. Most issues can be resolved quickly when brought to our attention. You may contact us at <a href="tel:9096004561">(909) 600-4561</a> or <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a>.</p>
  <p>If a dispute cannot be resolved informally, it shall be submitted to binding arbitration in San Bernardino County, California, under the rules of the American Arbitration Association. The prevailing party shall be entitled to recover reasonable attorney's fees and costs.</p>
  <h2>12. Governing Law</h2>
  <p>These Terms shall be governed by and construed in accordance with the laws of the State of California, without regard to its conflict of law provisions. Any legal proceedings arising from these Terms shall be brought in the courts of San Bernardino County, California.</p>
  <h2>13. Website Use</h2>
  <p>Our website is provided for informational purposes. You may not use our website for any unlawful purpose or in any way that could damage, disable, or impair the website. We reserve the right to update, modify, or discontinue the website at any time without notice.</p>
  <p>The content on our website, including text, images, and logos, is owned by Regal Plumbing &amp; Rooter and protected by copyright law. You may not reproduce or republish any content without our written permission.</p>
  <h2>14. Changes to These Terms</h2>
  <p>We reserve the right to update these Terms at any time. Changes will be posted on this page with an updated "Last Updated" date. Your continued use of our website or services after any changes constitutes your acceptance of the new Terms.</p>
  <h2>15. Contact Information</h2>
  <p>For questions about these Terms of Service, please contact us:</p>
  <div class="policy-nap"><strong>Regal Plumbing &amp; Rooter</strong><p>2141 E Philadelphia St, Suite R, Ontario, CA 91761<br>Phone: <a href="tel:9096004561">(909) 600-4561</a><br>Email: <a href="mailto:info@regalplumbingservices.com">info@regalplumbingservices.com</a><br>CA Contractor License #1097482</p></div>
</div></section>"""

save("terms-of-service.json", make_page(
    "Terms of Service | Regal Plumbing & Rooter",
    "Terms of Service | Regal Plumbing & Rooter",
    "Terms of Service for Regal Plumbing & Rooter — licensing, warranties, pricing, and service policies.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html(),"#FFFFFF"),(tos_hero,"#1E3A6E"),(tos_content,"#FFFFFF"),(cta_html("Ready to Schedule Service?","Call us 24/7 for emergency plumbing or schedule a convenient appointment"),"#B91C1C"),(FOOTER,"#2D2D2D")]
))

# ── 24. THANK YOU ─────────────────────────────────────────────────────────────
thank_you_body = """<style>.ty-section{background:#fff;padding:100px 24px;text-align:center}.ty-inner{max-width:600px;margin:0 auto}.ty-icon{font-size:72px;margin-bottom:24px;display:block}.ty-h1{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(32px,5vw,52px);color:#2D2D2D;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px}.ty-sub{font-size:17px;color:#4B5563;line-height:1.7;margin-bottom:32px}.ty-phone{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(28px,4vw,40px);color:#1E3A6E;letter-spacing:2px;display:block;margin-bottom:28px;text-decoration:none}.ty-actions{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}.ty-btn-primary{display:inline-flex;align-items:center;padding:14px 28px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;text-decoration:none}.ty-btn-secondary{display:inline-flex;align-items:center;padding:14px 28px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase;background:#1E3A6E;color:#fff;text-decoration:none}.ty-divider{width:80px;height:4px;background:#B91C1C;border-radius:2px;margin:20px auto 32px}</style>
<section class="ty-section"><div class="ty-inner">
  <span class="ty-icon">✅</span>
  <h1 class="ty-h1">Thank You!</h1>
  <div class="ty-divider"></div>
  <p class="ty-sub">Your message has been received. A member of the Regal Plumbing &amp; Rooter team will contact you shortly to discuss your plumbing needs and schedule your service appointment.</p>
  <p style="font-size:15px;color:#6B7280;margin-bottom:20px">For urgent or emergency plumbing issues, please call us directly:</p>
  <a href="tel:9096004561" class="ty-phone">(909) 600-4561</a>
  <div class="ty-actions">
    <a href="/" class="ty-btn-primary">Back to Home</a>
    <a href="/services/" class="ty-btn-secondary">View Our Services</a>
  </div>
</div></section>"""

save("thank-you.json", make_page(
    "Thank You | Regal Plumbing & Rooter",
    "Thank You | Regal Plumbing & Rooter",
    "Thank you for contacting Regal Plumbing & Rooter. We'll be in touch shortly to schedule your plumbing service.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html(),"#FFFFFF"),(thank_you_body,"#FFFFFF"),(FOOTER,"#2D2D2D")]
))

# ── 25. 404 NOT FOUND ─────────────────────────────────────────────────────────
not_found_body = """<style>.nf-section{background:#fff;padding:100px 24px;text-align:center}.nf-inner{max-width:640px;margin:0 auto}.nf-code{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(80px,15vw,140px);color:#F3F4F6;line-height:1;margin-bottom:-10px;display:block;letter-spacing:4px}.nf-h1{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(26px,4vw,42px);color:#2D2D2D;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px}.nf-sub{font-size:16px;color:#6B7280;line-height:1.7;margin-bottom:28px;max-width:480px;margin-left:auto;margin-right:auto}.nf-divider{width:60px;height:4px;background:#B91C1C;border-radius:2px;margin:16px auto 28px}.nf-links{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:40px}.nf-btn-red{display:inline-flex;align-items:center;padding:12px 24px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#B91C1C;color:#fff;text-decoration:none}.nf-btn-navy{display:inline-flex;align-items:center;padding:12px 24px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#1E3A6E;color:#fff;text-decoration:none}.nf-btn-grey{display:inline-flex;align-items:center;padding:12px 24px;border-radius:4px;font-family:'Oswald',sans-serif;font-weight:600;font-size:14px;letter-spacing:1px;text-transform:uppercase;background:#F3F4F6;color:#2D2D2D;border:1px solid #E5E7EB;text-decoration:none}.nf-phone-label{font-size:14px;color:#6B7280;margin-bottom:8px}.nf-phone{font-family:'Oswald',sans-serif;font-weight:700;font-size:clamp(28px,4vw,38px);color:#1E3A6E;letter-spacing:2px;display:block;text-decoration:none}</style>
<section class="nf-section"><div class="nf-inner">
  <span class="nf-code">404</span>
  <h1 class="nf-h1">Page Not Found</h1>
  <div class="nf-divider"></div>
  <p class="nf-sub">The page you're looking for doesn't exist or may have been moved. Use the links below to find what you need, or call us directly — we're always available.</p>
  <div class="nf-links">
    <a href="/" class="nf-btn-red">Home</a>
    <a href="/services/" class="nf-btn-navy">Our Services</a>
    <a href="/service-area/" class="nf-btn-grey">Service Area</a>
    <a href="/contact/" class="nf-btn-grey">Contact Us</a>
  </div>
  <p class="nf-phone-label">Need emergency plumbing help right now?</p>
  <a href="tel:9096004561" class="nf-phone">(909) 600-4561</a>
</div></section>"""

save("404.json", make_page(
    "404 Not Found | Regal Plumbing & Rooter",
    "404 Not Found | Regal Plumbing & Rooter",
    "Page not found — return to Regal Plumbing & Rooter's homepage or call (909) 600-4561 for emergency plumbing service.",
    [(EMERGENCY_BAR,"#2D2D2D"),(header_html(),"#FFFFFF"),(not_found_body,"#FFFFFF"),(FOOTER,"#2D2D2D")]
))

print("Pages 22-25 done.")
