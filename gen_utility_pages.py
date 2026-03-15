import json, os

base_dir = "c:/Users/Nick/Projects/regal-plumbing-website/elementor-templates"
IMG = "http://regal-plumbing.local/wp-content/uploads/2026/03/"

FOOTER_HTML = "<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;\"><li><a href=\"/emergency-plumbing/\" style=\"font-size:13.5px;color:#9CA3AF;\">Emergency Plumbing</a></li><li><a href=\"/drain-cleaning/\" style=\"font-size:13.5px;color:#9CA3AF;\">Drain Cleaning</a></li><li><a href=\"/sewer-line-repair/\" style=\"font-size:13.5px;color:#9CA3AF;\">Sewer Line Repair</a></li><li><a href=\"/water-heater-services/\" style=\"font-size:13.5px;color:#9CA3AF;\">Water Heater Services</a></li><li><a href=\"/slab-leak-detection/\" style=\"font-size:13.5px;color:#9CA3AF;\">Slab Leak Detection</a></li><li><a href=\"/hydrojetting/\" style=\"font-size:13.5px;color:#9CA3AF;\">Hydrojetting</a></li><li><a href=\"/gas-leak-detection/\" style=\"font-size:13.5px;color:#9CA3AF;\">Gas Leak Detection</a></li><li><a href=\"/water-filtration/\" style=\"font-size:13.5px;color:#9CA3AF;\">Water Filtration</a></li></ul>"
FOOTER_AREA = "<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;\"><li><a href=\"/service-area/ontario-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Ontario</a></li><li><a href=\"/service-area/rancho-cucamonga-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Rancho Cucamonga</a></li><li><a href=\"/service-area/fontana-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Fontana</a></li><li><a href=\"/service-area/pomona-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Pomona</a></li><li><a href=\"/service-area/chino-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Chino</a></li><li><a href=\"/service-area/corona-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Corona</a></li><li><a href=\"/service-area/upland-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Upland</a></li><li><a href=\"/service-area/west-covina-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">West Covina</a></li></ul>"

def std_footer(p):
    return {
        "id": f"{p}zz01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#2D2D2D",
            "padding": {"unit":"px","top":"64","right":"24","bottom":"24","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}zz02", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "flex_wrap": "wrap",
                    "gap": {"unit":"px","size":48}, "_element_width": "initial"
                },
                "elements": [
                    {
                        "id": f"{p}zz03", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"25%"},
                        "elements": [
                            {"id":f"{p}zz04","elType":"widget","widgetType":"heading","settings":{"title":"Regal Plumbing &amp; Rooter","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":18},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                            {"id":f"{p}zz05","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:13px;color:#9CA3AF;line-height:1.6;\">Honest, professional plumbing &amp; rooter services for the Inland Empire &amp; San Gabriel Valley.</p>"}},
                            {"id":f"{p}zz06","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"display:inline-block;background:rgba(185,28,28,0.2);border:1px solid rgba(185,28,28,0.4);color:#fca5a5;font-size:11.5px;font-family:Oswald,sans-serif;letter-spacing:1px;padding:4px 10px;border-radius:3px;\">CA License #1097482</p>"}}
                        ]
                    },
                    {
                        "id": f"{p}zz07", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"15%"},
                        "elements": [
                            {"id":f"{p}zz08","elType":"widget","widgetType":"heading","settings":{"title":"Services","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"typography_letter_spacing":{"unit":"px","size":1.5},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                            {"id":f"{p}zz09","elType":"widget","widgetType":"text-editor","settings":{"editor":FOOTER_HTML}}
                        ]
                    },
                    {
                        "id": f"{p}zz10", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"15%"},
                        "elements": [
                            {"id":f"{p}zz11","elType":"widget","widgetType":"heading","settings":{"title":"Service Area","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"typography_letter_spacing":{"unit":"px","size":1.5},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                            {"id":f"{p}zz12","elType":"widget","widgetType":"text-editor","settings":{"editor":FOOTER_AREA}}
                        ]
                    },
                    {
                        "id": f"{p}zz13", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"20%"},
                        "elements": [
                            {"id":f"{p}zz14","elType":"widget","widgetType":"heading","settings":{"title":"Contact Us","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"typography_letter_spacing":{"unit":"px","size":1.5},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                            {"id":f"{p}zz15","elType":"widget","widgetType":"text-editor","settings":{"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:12px;\"><li style=\"font-size:13.5px;color:#9CA3AF;\">2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</li><li><a href=\"tel:9096004561\" style=\"font-size:13.5px;color:#9CA3AF;\">(909) 600-4561</a></li><li><a href=\"mailto:info@regalplumbingservices.com\" style=\"font-size:13.5px;color:#9CA3AF;\">info@regalplumbingservices.com</a></li><li style=\"font-size:13.5px;color:#9CA3AF;\">24/7 Emergency | Mon\u2013Sat: 7am\u20137pm</li></ul>"}}
                        ]
                    }
                ]
            },
            {"id":f"{p}zz16","elType":"widget","widgetType":"divider","settings":{"color":"rgba(255,255,255,0.10)","weight":{"unit":"px","size":1},"width":{"unit":"%","size":100}}},
            {
                "id": f"{p}zz17", "elType": "container",
                "settings": {"content_width":"full","flex_direction":"row","flex_justify_content":"space-between","flex_align_items":"center","padding":{"unit":"px","top":"18","right":"0","bottom":"18","left":"0","isLinked":False}},
                "elements": [
                    {"id":f"{p}zz18","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:12.5px;color:#6B7280;\">&copy; 2025 Regal Plumbing &amp; Rooter. All Rights Reserved. CA License #1097482</p>"}},
                    {"id":f"{p}zz19","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:12.5px;color:#6B7280;\"><a href=\"/privacy-policy/\" style=\"color:#6B7280;\">Privacy Policy</a> &nbsp; <a href=\"/terms-of-service/\" style=\"color:#6B7280;\">Terms of Service</a></p>"}}
                ]
            }
        ]
    }

def emerg_bar(p):
    return {
        "id": f"{p}aa01", "elType": "container",
        "settings": {"background_background":"classic","background_color":"#2D2D2D","padding":{"unit":"px","top":"9","right":"16","bottom":"9","left":"16","isLinked":False}},
        "elements": [{"id":f"{p}aa02","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"text-align:center;color:#ffffff;font-size:13.5px;font-weight:600;\">24/7 Emergency Service Available \u2014 Call <a href=\"tel:9096004561\" style=\"color:#fca5a5;\">(909) 600-4561</a></p>"}}]
    }

def header_container(p):
    return {
        "id": f"{p}ab01", "elType": "container",
        "settings": {"background_background":"classic","background_color":"#FFFFFF","box_shadow_box_shadow_type":"yes","box_shadow_box_shadow":{"horizontal":0,"vertical":2,"blur":12,"spread":0,"color":"rgba(0,0,0,0.10)"},"padding":{"unit":"px","top":"0","right":"24","bottom":"0","left":"24","isLinked":False}},
        "elements": [{
            "id": f"{p}ab02", "elType": "container",
            "settings": {"content_width":"full","flex_direction":"row","flex_align_items":"center","flex_justify_content":"space-between","padding":{"unit":"px","top":"8","right":"0","bottom":"8","left":"0","isLinked":False}},
            "elements": [
                {"id":f"{p}ab03","elType":"widget","widgetType":"image","settings":{"image":{"url":IMG+"regal-plumbing-logo.png","alt":"Regal Plumbing & Rooter"},"image_size":"full","width":{"unit":"px","size":180},"link_to":"custom","link":{"url":"/"}}},
                {"id":f"{p}ab04","elType":"widget","widgetType":"nav-menu","settings":{"menu":"primary-menu","layout":"horizontal","typography_typography":"custom","typography_font_family":"Oswald","typography_font_weight":"500","typography_font_size":{"unit":"px","size":14},"typography_letter_spacing":{"unit":"px","size":1.2},"typography_text_transform":"uppercase","color":"#2D2D2D","color_hover":"#B91C1C"}},
                {
                    "id": f"{p}ab05", "elType": "container",
                    "settings": {"flex_direction":"row","flex_align_items":"center","gap":{"unit":"px","size":14}},
                    "elements": [
                        {"id":f"{p}ab06","elType":"widget","widgetType":"heading","settings":{"title":"<a href=\"tel:9096004561\">(909) 600-4561</a>","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":16},"title_color":"#1E3A6E"}},
                        {"id":f"{p}ab07","elType":"widget","widgetType":"button","settings":{"text":"Call Now","link":{"url":"tel:9096004561"},"background_color":"#B91C1C","button_text_color":"#FFFFFF","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":4,"right":4,"bottom":4,"left":4,"isLinked":True}}}
                    ]
                }
            ]
        }]
    }

def cta_container(p, heading, sub):
    return {
        "id": f"{p}yy01", "elType": "container",
        "settings": {"background_background":"classic","background_color":"#B91C1C","padding":{"unit":"px","top":"64","right":"24","bottom":"64","left":"24","isLinked":False},"text_align":"center"},
        "elements": [
            {"id":f"{p}yy02","elType":"widget","widgetType":"heading","settings":{"title":heading,"header_size":"h2","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":42},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
            {"id":f"{p}yy03","elType":"widget","widgetType":"text-editor","settings":{"editor":f"<p style=\"text-align:center;font-size:16px;color:rgba(255,255,255,0.85);\">{sub}</p>"}},
            {"id":f"{p}yy04","elType":"widget","widgetType":"heading","settings":{"title":"<a href=\"tel:9096004561\" style=\"color:#FFFFFF;\">(909) 600-4561</a>","header_size":"h2","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":50},"title_color":"#FFFFFF"}},
            {"id":f"{p}yy05","elType":"widget","widgetType":"button","settings":{"text":"Call Now","link":{"url":"tel:9096004561"},"background_color":"#FFFFFF","button_text_color":"#B91C1C","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":15},"border_border":"solid","border_width":{"unit":"px","top":2,"right":2,"bottom":2,"left":2,"isLinked":True},"border_color":"#FFFFFF","border_radius":{"unit":"px","top":4,"right":4,"bottom":4,"left":4,"isLinked":True},"align":"center","size":"lg"}}
        ]
    }

# ---- Privacy Policy ----
privacy_sections = [
    ("1. Introduction", "Regal Plumbing &amp; Rooter (\"we,\" \"us,\" or \"our\") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or contact us for plumbing services."),
    ("2. Information We Collect", "<strong>Personal Data:</strong> Name, email address, phone number, city, and service information you voluntarily provide when submitting a contact form or calling us.<br><strong>Derivative Data:</strong> Information our servers automatically collect when you visit our website, such as your IP address, browser type, and access times.<br><strong>Mobile Device Data:</strong> Device hardware model, operating system, and mobile network information if you access via a mobile device."),
    ("3. Contact Forms", "When you submit a contact form, we collect your name, phone number, email, city, service needed, and message. This information is used solely to respond to your inquiry and schedule service. We do not sell or rent this information to third parties. Form submissions are sent to info@regalplumbingservices.com."),
    ("4. Cookies and Tracking", "We may use cookies and tracking technologies to improve your experience. Most browsers accept cookies by default. You can disable cookies in your browser settings, which may affect website functionality."),
    ("5. Google Analytics", "We use Google Analytics to analyze traffic patterns on our website. Google Analytics collects information about how often users visit the site and what pages they view. You can opt out by installing the Google Analytics Opt-out Browser Add-on."),
    ("6. Third-Party Services", "We may share your information with email delivery services, Google Maps, and web hosting and analytics providers. These third parties have access only to perform their specific functions."),
    ("7. How We Use Your Information", "We use your information to: respond to service inquiries and schedule appointments; email or call you regarding your service request; monitor usage trends to improve our website; and comply with legal obligations."),
    ("8. Disclosure of Your Information", "We do not sell, trade, or transfer your personally identifiable information to outside parties, except as required by law or in connection with a business transfer."),
    ("9. Security", "We use administrative, technical, and physical security measures to help protect your personal information. No security measures are perfect, but we take reasonable steps to safeguard your data."),
    ("10. Your Rights", "You may request a copy of, correction of, or deletion of your personal information. California residents have additional rights under CCPA. Contact us at info@regalplumbingservices.com or (909) 600-4561 to exercise these rights."),
    ("11. California Privacy Rights (CCPA)", "California residents have the right to know what personal information we collect, the right to delete personal information, the right to opt-out of the sale of personal information (we do not sell your information), and the right to non-discrimination."),
    ("12. Children's Privacy", "Our website is not directed to children under 13. We do not knowingly collect personal information from children under 13."),
    ("13. Changes to This Policy", "We may update this Privacy Policy from time to time. The updated version will be indicated by an updated \"Last Updated\" date at the top of this page."),
    ("14. Contact Us", "Regal Plumbing &amp; Rooter | 2141 E Philadelphia St, Suite R, Ontario, CA 91761 | (909) 600-4561 | info@regalplumbingservices.com")
]

section_els = []
for i, (title, body) in enumerate(privacy_sections):
    section_els.append({
        "id": f"ppcc{i+10:02d}", "elType": "widget", "widgetType": "heading",
        "settings": {"title": title, "header_size": "h2", "typography_font_family": "Oswald", "typography_font_weight": "600", "typography_font_size": {"unit":"px","size":22}, "title_color": "#1E3A6E", "_margin": {"unit":"px","top":"24","right":"0","bottom":"8","left":"0","isLinked":False}}
    })
    section_els.append({
        "id": f"ppcc{i+30:02d}", "elType": "widget", "widgetType": "text-editor",
        "settings": {"editor": f"<p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:16px;\">{body}</p>"}
    })

privacy_policy = {
    "version": "0.4", "title": "Privacy Policy", "type": "page",
    "page_settings": {
        "seo_title": "Privacy Policy — Regal Plumbing & Rooter",
        "seo_description": "Privacy Policy for Regal Plumbing & Rooter. Learn how we collect, use, and protect your information."
    },
    "content": [
        emerg_bar("pp"),
        header_container("pp"),
        {
            "id": "ppac01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#1E3A6E","padding":{"unit":"px","top":"56","right":"24","bottom":"56","left":"24","isLinked":False}},
            "elements": [
                {"id":"ppac02","elType":"widget","widgetType":"heading","settings":{"title":"Privacy Policy","header_size":"h1","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":48},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                {"id":"ppac03","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:15px;color:#D1D5DB;\">Last Updated: March 1, 2025</p>"}}
            ]
        },
        {
            "id": "ppcc01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#FFFFFF","padding":{"unit":"px","top":"72","right":"24","bottom":"72","left":"24","isLinked":False}},
            "elements": [
                {
                    "id": "ppcc02", "elType": "container",
                    "settings": {"flex_direction":"column","content_width":"boxed","padding":{"unit":"px","top":"0","right":"0","bottom":"0","left":"0","isLinked":False}},
                    "elements": [
                        {"id":"ppcc03","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:24px;\"><strong>Regal Plumbing &amp; Rooter</strong><br>2141 E Philadelphia St, Suite R, Ontario, CA 91761 &nbsp;|&nbsp; <a href=\"tel:9096004561\">(909) 600-4561</a> &nbsp;|&nbsp; <a href=\"mailto:info@regalplumbingservices.com\">info@regalplumbingservices.com</a></p>"}}
                    ] + section_els
                }
            ]
        },
        cta_container("pp", "Questions? We're Here to Help", "Call us anytime — 24/7 emergency plumbing service across Southern California"),
        std_footer("pp")
    ]
}

# ---- Terms of Service ----
tos_sections = [
    ("1. Acceptance of Terms", "By accessing our website or engaging Regal Plumbing &amp; Rooter for plumbing services, you agree to be bound by these Terms of Service. If you do not agree to these Terms, please do not use our website or services."),
    ("2. Services Provided", "Regal Plumbing &amp; Rooter provides residential and commercial plumbing services including emergency plumbing, drain cleaning, sewer line repair, water heater installation and repair, slab leak detection, hydrojetting, gas leak detection, and water filtration system installation. CA Contractor License #1097482."),
    ("3. Service Agreement", "A service agreement is established when you contact us and we agree to perform work, you accept an estimate from our technicians, or work begins with your consent. We reserve the right to refuse service at our discretion."),
    ("4. Estimates and Pricing", "We provide upfront, transparent pricing before any work begins. Final pricing may vary if hidden damage is discovered, additional materials are required, or permits are needed. We will notify you of any changes before proceeding."),
    ("5. Payment Terms", "Payment is due upon completion of services unless otherwise agreed in writing. We accept cash, check, and major credit cards. Accounts not paid within 30 days may be subject to a 1.5% per month late fee. Returned checks are subject to a $35 fee."),
    ("6. Warranties", "<strong>Labor Warranty:</strong> All labor is warranted against defects for 30 days from service date.<br><strong>Parts Warranty:</strong> Parts and materials are covered by manufacturer warranty.<br><strong>Drain Cleaning:</strong> 30-day warranty against the same blockage returning, provided no foreign objects are introduced. Warranties are void if the system is modified by another party after our work."),
    ("7. Liability Limitations", "Our liability shall not exceed the total amount paid for the specific service. We are not liable for pre-existing conditions, consequential or incidental damages, or damage caused by access issues. We carry general liability and workers' compensation insurance as required by California law."),
    ("8. Property Access", "You agree to provide safe, reasonable access to all work areas. Please clear the work area of personal belongings, pets, and obstructions before our arrival. You represent that you have the legal authority to authorize work at the property."),
    ("9. Cancellation Policy", "You may cancel or reschedule without penalty by providing at least 2 hours' notice. Cancellations with less than 2 hours' notice may be subject to a service call fee. Emergency calls cancelled after dispatch may be subject to a trip charge."),
    ("10. Permits and Code Compliance", "Work requiring permits will be identified during the estimate process. Permit fees are the property owner's responsibility unless specifically included in the estimate. All work is performed in compliance with the California Plumbing Code."),
    ("11. Dispute Resolution", "In the event of a dispute, please contact us directly first at (909) 600-4561 or info@regalplumbingservices.com. Unresolved disputes shall be submitted to binding arbitration in San Bernardino County, California."),
    ("12. Governing Law", "These Terms shall be governed by the laws of the State of California. Any legal proceedings shall be brought in the courts of San Bernardino County, California."),
    ("13. Website Use", "Our website is provided for informational purposes. You may not use our website for any unlawful purpose. Content on our website is owned by Regal Plumbing &amp; Rooter and protected by copyright law."),
    ("14. Changes to These Terms", "We reserve the right to update these Terms at any time. Changes will be posted with an updated \"Last Updated\" date. Continued use of our services constitutes acceptance of the new Terms."),
    ("15. Contact Information", "Regal Plumbing &amp; Rooter | 2141 E Philadelphia St, Suite R, Ontario, CA 91761 | (909) 600-4561 | info@regalplumbingservices.com | CA Contractor License #1097482")
]

tos_els = []
for i, (title, body) in enumerate(tos_sections):
    tos_els.append({
        "id": f"tscc{i+10:02d}", "elType": "widget", "widgetType": "heading",
        "settings": {"title": title, "header_size": "h2", "typography_font_family": "Oswald", "typography_font_weight": "600", "typography_font_size": {"unit":"px","size":22}, "title_color": "#1E3A6E", "_margin": {"unit":"px","top":"24","right":"0","bottom":"8","left":"0","isLinked":False}}
    })
    tos_els.append({
        "id": f"tscc{i+40:02d}", "elType": "widget", "widgetType": "text-editor",
        "settings": {"editor": f"<p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:16px;\">{body}</p>"}
    })

terms_of_service = {
    "version": "0.4", "title": "Terms of Service", "type": "page",
    "page_settings": {
        "seo_title": "Terms of Service — Regal Plumbing & Rooter",
        "seo_description": "Terms of Service for Regal Plumbing & Rooter. Read our service agreement, warranty, and payment terms."
    },
    "content": [
        emerg_bar("ts"),
        header_container("ts"),
        {
            "id": "tsac01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#1E3A6E","padding":{"unit":"px","top":"56","right":"24","bottom":"56","left":"24","isLinked":False}},
            "elements": [
                {"id":"tsac02","elType":"widget","widgetType":"heading","settings":{"title":"Terms of Service","header_size":"h1","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":48},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                {"id":"tsac03","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:15px;color:#D1D5DB;\">Last Updated: March 1, 2025</p>"}}
            ]
        },
        {
            "id": "tscc01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#FFFFFF","padding":{"unit":"px","top":"72","right":"24","bottom":"72","left":"24","isLinked":False}},
            "elements": [
                {
                    "id": "tscc02", "elType": "container",
                    "settings": {"flex_direction":"column","content_width":"boxed"},
                    "elements": [
                        {"id":"tscc03","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:24px;\"><strong>Regal Plumbing &amp; Rooter</strong><br>2141 E Philadelphia St, Suite R, Ontario, CA 91761 &nbsp;|&nbsp; <a href=\"tel:9096004561\">(909) 600-4561</a> &nbsp;|&nbsp; <a href=\"mailto:info@regalplumbingservices.com\">info@regalplumbingservices.com</a></p>"}}
                    ] + tos_els
                }
            ]
        },
        cta_container("ts", "Ready to Schedule Service?", "Call us 24/7 for emergency plumbing or schedule a convenient appointment"),
        std_footer("ts")
    ]
}

# ---- Thank You ----
thank_you = {
    "version": "0.4", "title": "Thank You", "type": "page",
    "page_settings": {
        "seo_title": "Thank You — Regal Plumbing & Rooter",
        "seo_description": "Thank you for contacting Regal Plumbing & Rooter. We'll be in touch within 1 business hour."
    },
    "content": [
        emerg_bar("ty"),
        header_container("ty"),
        {
            "id": "tyac01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#1E3A6E","padding":{"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False},"text_align":"center"},
            "elements": [
                {"id":"tyac02","elType":"widget","widgetType":"heading","settings":{"title":"Thank You!","header_size":"h1","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":56},"typography_text_transform":"uppercase","title_color":"#FFFFFF"}},
                {"id":"tyac03","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"text-align:center;font-size:20px;color:#D1D5DB;margin-top:16px;\">Your message has been received. We'll be in touch soon.</p>"}}
            ]
        },
        {
            "id": "tycc01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#FFFFFF","padding":{"unit":"px","top":"72","right":"24","bottom":"72","left":"24","isLinked":False}},
            "elements": [
                {
                    "id": "tycc02", "elType": "container",
                    "settings": {"content_width":"boxed","flex_direction":"column","flex_align_items":"center"},
                    "elements": [
                        {"id":"tycc03","elType":"widget","widgetType":"heading","settings":{"title":"What Happens Next?","header_size":"h2","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":36},"typography_text_transform":"uppercase","title_color":"#2D2D2D"}},
                        {"id":"tycc04","elType":"widget","widgetType":"divider","settings":{"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}},
                        {"id":"tycc05","elType":"widget","widgetType":"icon-box","settings":{"title_text":"Step 1 — We Review Your Inquiry","description_text":"A Regal Plumbing team member will review your inquiry and call or email you within 1 business hour during regular operating hours (Mon–Sat 7am–7pm).","icon":{"value":"fas fa-clock","library":"fa-solid"},"title_typography_typography":"custom","title_typography_font_family":"Oswald","title_typography_font_weight":"600","title_typography_font_size":{"unit":"px","size":18},"title_color":"#2D2D2D","_margin":{"unit":"px","top":"24","right":"0","bottom":"0","left":"0","isLinked":False}}},
                        {"id":"tycc06","elType":"widget","widgetType":"icon-box","settings":{"title_text":"Step 2 — Free Estimate","description_text":"We'll discuss the details of your plumbing issue, answer your questions, and provide a transparent, upfront estimate at no cost to you.","icon":{"value":"fas fa-dollar-sign","library":"fa-solid"},"title_typography_typography":"custom","title_typography_font_family":"Oswald","title_typography_font_weight":"600","title_typography_font_size":{"unit":"px","size":18},"title_color":"#2D2D2D","_margin":{"unit":"px","top":"24","right":"0","bottom":"0","left":"0","isLinked":False}}},
                        {"id":"tycc07","elType":"widget","widgetType":"icon-box","settings":{"title_text":"Step 3 — Schedule Service","description_text":"We'll schedule a convenient appointment — with same-day and emergency service available for urgent plumbing situations.","icon":{"value":"fas fa-calendar","library":"fa-solid"},"title_typography_typography":"custom","title_typography_font_family":"Oswald","title_typography_font_weight":"600","title_typography_font_size":{"unit":"px","size":18},"title_color":"#2D2D2D","_margin":{"unit":"px","top":"24","right":"0","bottom":"0","left":"0","isLinked":False}}},
                        {"id":"tycc08","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"text-align:center;font-size:15px;color:#4B5563;margin-top:32px;\">Have a plumbing emergency? Don't wait — <a href=\"tel:9096004561\" style=\"color:#B91C1C;font-weight:600;\">call (909) 600-4561</a> now for immediate dispatch. &nbsp;|&nbsp; <a href=\"/\" style=\"color:#B91C1C;\">Return to homepage &rarr;</a></p>"}}
                    ]
                }
            ]
        },
        cta_container("ty", "Need Immediate Help? Call Us Now", "24/7 emergency plumbing service across the Inland Empire — we answer every call"),
        std_footer("ty")
    ]
}

# ---- 404 ----
page_404 = {
    "version": "0.4", "title": "404 Not Found", "type": "page",
    "page_settings": {
        "seo_title": "Page Not Found — Regal Plumbing & Rooter",
        "seo_description": "The page you're looking for doesn't exist. Find our plumbing services or contact us at (909) 600-4561."
    },
    "content": [
        emerg_bar("nf"),
        header_container("nf"),
        {
            "id": "nfac01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#1E3A6E","padding":{"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False},"text_align":"center"},
            "elements": [
                {"id":"nfac02","elType":"widget","widgetType":"heading","settings":{"title":"404","header_size":"h1","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":96},"title_color":"#FFFFFF"}},
                {"id":"nfac03","elType":"widget","widgetType":"heading","settings":{"title":"Page Not Found","header_size":"h2","align":"center","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":36},"typography_text_transform":"uppercase","title_color":"#D1D5DB"}},
                {"id":"nfac04","elType":"widget","widgetType":"text-editor","settings":{"editor":"<p style=\"text-align:center;font-size:17px;color:#9CA3AF;margin-top:16px;\">The page you're looking for doesn't exist or has been moved. Let us help you find what you need.</p>"}}
            ]
        },
        {
            "id": "nfcc01", "elType": "container",
            "settings": {"background_background":"classic","background_color":"#FFFFFF","padding":{"unit":"px","top":"72","right":"24","bottom":"72","left":"24","isLinked":False}},
            "elements": [
                {
                    "id": "nfcc02", "elType": "container",
                    "settings": {"content_width":"boxed","flex_direction":"column","flex_align_items":"center"},
                    "elements": [
                        {"id":"nfcc03","elType":"widget","widgetType":"heading","settings":{"title":"Have a Plumbing Emergency?","header_size":"h2","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":36},"typography_text_transform":"uppercase","title_color":"#2D2D2D"}},
                        {"id":"nfcc04","elType":"widget","widgetType":"heading","settings":{"title":"<a href=\"tel:9096004561\" style=\"color:#B91C1C;\">(909) 600-4561</a>","header_size":"h2","align":"center","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":48},"title_color":"#B91C1C"}},
                        {"id":"nfcc05","elType":"widget","widgetType":"button","settings":{"text":"Call Now — We Answer 24/7","link":{"url":"tel:9096004561"},"background_color":"#B91C1C","button_text_color":"#FFFFFF","typography_font_family":"Oswald","typography_font_weight":"700","typography_font_size":{"unit":"px","size":15},"border_radius":{"unit":"px","top":4,"right":4,"bottom":4,"left":4,"isLinked":True},"align":"center","size":"lg"}},
                        {"id":"nfcc06","elType":"widget","widgetType":"divider","settings":{"color":"#D1D5DB","weight":{"unit":"px","size":1},"width":{"unit":"%","size":100},"_margin":{"unit":"px","top":"40","right":"0","bottom":"40","left":"0","isLinked":False}}},
                        {"id":"nfcc07","elType":"widget","widgetType":"heading","settings":{"title":"Popular Pages","header_size":"h3","align":"center","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":24},"typography_text_transform":"uppercase","title_color":"#2D2D2D"}},
                        {
                            "id": "nfcc08", "elType": "container",
                            "settings": {"content_width":"full","flex_direction":"row","flex_wrap":"wrap","gap":{"unit":"px","size":20},"_element_width":"initial"},
                            "elements": [
                                {"id":"nfcc09","elType":"widget","widgetType":"button","settings":{"text":"Emergency Plumbing","link":{"url":"/emergency-plumbing/"},"background_color":"#F3F4F6","button_text_color":"#2D2D2D","border_border":"solid","border_width":{"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},"border_color":"#E5E7EB","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},"size":"lg"}},
                                {"id":"nfcc10","elType":"widget","widgetType":"button","settings":{"text":"Drain Cleaning","link":{"url":"/drain-cleaning/"},"background_color":"#F3F4F6","button_text_color":"#2D2D2D","border_border":"solid","border_width":{"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},"border_color":"#E5E7EB","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},"size":"lg"}},
                                {"id":"nfcc11","elType":"widget","widgetType":"button","settings":{"text":"Sewer Line Repair","link":{"url":"/sewer-line-repair/"},"background_color":"#F3F4F6","button_text_color":"#2D2D2D","border_border":"solid","border_width":{"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},"border_color":"#E5E7EB","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},"size":"lg"}},
                                {"id":"nfcc12","elType":"widget","widgetType":"button","settings":{"text":"Water Heater Services","link":{"url":"/water-heater-services/"},"background_color":"#F3F4F6","button_text_color":"#2D2D2D","border_border":"solid","border_width":{"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},"border_color":"#E5E7EB","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},"size":"lg"}},
                                {"id":"nfcc13","elType":"widget","widgetType":"button","settings":{"text":"Service Area","link":{"url":"/service-area/"},"background_color":"#F3F4F6","button_text_color":"#2D2D2D","border_border":"solid","border_width":{"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},"border_color":"#E5E7EB","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},"size":"lg"}},
                                {"id":"nfcc14","elType":"widget","widgetType":"button","settings":{"text":"Contact Us","link":{"url":"/contact/"},"background_color":"#F3F4F6","button_text_color":"#2D2D2D","border_border":"solid","border_width":{"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},"border_color":"#E5E7EB","typography_font_family":"Oswald","typography_font_weight":"600","typography_font_size":{"unit":"px","size":14},"border_radius":{"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},"size":"lg"}}
                            ]
                        }
                    ]
                }
            ]
        },
        cta_container("nf", "Plumbing Emergency? Don't Wait", "We're available 24/7 for emergency plumbing across Southern California"),
        std_footer("nf")
    ]
}

pages = [
    ("privacy-policy.json", privacy_policy),
    ("terms-of-service.json", terms_of_service),
    ("thank-you.json", thank_you),
    ("404.json", page_404)
]

for filename, doc in pages:
    out_path = os.path.join(base_dir, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"Written: {filename}")

print("All 4 utility pages done.")
