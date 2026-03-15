import json, os

base_dir = "c:/Users/Nick/Projects/regal-plumbing-website/elementor-templates"
IMG = "http://regal-plumbing.local/wp-content/uploads/2026/03/"

def emerg_bar(p):
    return {
        "id": f"{p}aa01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#2D2D2D",
            "padding": {"unit":"px","top":"9","right":"16","bottom":"9","left":"16","isLinked":False}
        },
        "elements": [{
            "id": f"{p}aa02", "elType": "widget", "widgetType": "text-editor",
            "settings": {"editor": "<p style=\"text-align:center;color:#ffffff;font-size:13.5px;font-weight:600;\">24/7 Emergency Service Available \u2014 Call <a href=\"tel:9096004561\" style=\"color:#fca5a5;\">(909) 600-4561</a></p>"}
        }]
    }

def header_container(p):
    return {
        "id": f"{p}ab01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#FFFFFF",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal":0,"vertical":2,"blur":12,"spread":0,"color":"rgba(0,0,0,0.10)"},
            "padding": {"unit":"px","top":"0","right":"24","bottom":"0","left":"24","isLinked":False}
        },
        "elements": [{
            "id": f"{p}ab02", "elType": "container",
            "settings": {
                "content_width": "full", "flex_direction": "row",
                "flex_align_items": "center", "flex_justify_content": "space-between",
                "padding": {"unit":"px","top":"8","right":"0","bottom":"8","left":"0","isLinked":False}
            },
            "elements": [
                {
                    "id": f"{p}ab03", "elType": "widget", "widgetType": "image",
                    "settings": {
                        "image": {"url": IMG+"regal-plumbing-logo.png","alt":"Regal Plumbing & Rooter"},
                        "image_size": "full", "width": {"unit":"px","size":180},
                        "link_to": "custom", "link": {"url":"/"}
                    }
                },
                {
                    "id": f"{p}ab04", "elType": "widget", "widgetType": "nav-menu",
                    "settings": {
                        "menu": "primary-menu", "layout": "horizontal",
                        "typography_typography": "custom", "typography_font_family": "Oswald",
                        "typography_font_weight": "500",
                        "typography_font_size": {"unit":"px","size":14},
                        "typography_letter_spacing": {"unit":"px","size":1.2},
                        "typography_text_transform": "uppercase",
                        "color": "#2D2D2D", "color_hover": "#B91C1C"
                    }
                },
                {
                    "id": f"{p}ab05", "elType": "container",
                    "settings": {"flex_direction":"row","flex_align_items":"center","gap":{"unit":"px","size":14}},
                    "elements": [
                        {
                            "id": f"{p}ab06", "elType": "widget", "widgetType": "heading",
                            "settings": {
                                "title": "<a href=\"tel:9096004561\">(909) 600-4561</a>",
                                "typography_font_family": "Oswald", "typography_font_weight": "600",
                                "typography_font_size": {"unit":"px","size":16}, "title_color": "#1E3A6E"
                            }
                        },
                        {
                            "id": f"{p}ab07", "elType": "widget", "widgetType": "button",
                            "settings": {
                                "text": "Call Now", "link": {"url":"tel:9096004561"},
                                "background_color": "#B91C1C", "button_text_color": "#FFFFFF",
                                "typography_font_family": "Oswald", "typography_font_weight": "600",
                                "typography_font_size": {"unit":"px","size":14},
                                "border_radius": {"unit":"px","top":4,"right":4,"bottom":4,"left":4,"isLinked":True}
                            }
                        }
                    ]
                }
            ]
        }]
    }

def hero_container(p, h1, sub):
    return {
        "id": f"{p}ac01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#1E3A6E",
            "padding": {"unit":"px","top":"72","right":"24","bottom":"72","left":"24","isLinked":False},
            "min_height": {"unit":"px","size":280}
        },
        "elements": [
            {
                "id": f"{p}ac02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": h1, "header_size": "h1",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":52},
                    "typography_text_transform": "uppercase",
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}ac03", "elType": "widget", "widgetType": "text-editor",
                "settings": {"editor": f"<p style=\"font-size:17px;color:#D1D5DB;max-width:640px;line-height:1.6;\">{sub}</p>"}
            }
        ]
    }

def map_intro_container(p, city, map_src, map_title, intro_p1, intro_p2):
    return {
        "id": f"{p}ad01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#FFFFFF",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ad02", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row",
                    "flex_align_items": "flex-start", "gap": {"unit":"px","size":56},
                    "_element_width": "initial"
                },
                "elements": [
                    {
                        "id": f"{p}ad03", "elType": "widget", "widgetType": "google_maps",
                        "settings": {
                            "address": city + ", CA",
                            "zoom": {"size":12},
                            "height": {"unit":"px","size":420},
                            "_element_width": "50%"
                        }
                    },
                    {
                        "id": f"{p}ad04", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"50%"},
                        "elements": [
                            {
                                "id": f"{p}ad05", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": "Your Local Plumber", "header_size": "p",
                                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                                    "typography_font_size": {"unit":"px","size":12},
                                    "typography_letter_spacing": {"unit":"px","size":3},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#B91C1C"
                                }
                            },
                            {
                                "id": f"{p}ad06", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": f"Serving All of {city}, CA",
                                    "header_size": "h2",
                                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                                    "typography_font_size": {"unit":"px","size":36},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#2D2D2D"
                                }
                            },
                            {
                                "id": f"{p}ad07", "elType": "widget", "widgetType": "divider",
                                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":20}}
                            },
                            {
                                "id": f"{p}ad08", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor": f"<p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-top:20px;\">{intro_p1}</p><p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-top:16px;\">{intro_p2}</p>"}
                            }
                        ]
                    }
                ]
            }
        ]
    }

def trust_bar(p):
    items = [
        {"icon":"⏰","label":"24/7 Emergency","sub":"Always Available"},
        {"icon":"👨‍👩‍👧","label":"Family Owned &amp; Operated","sub":"Community Focused"},
        {"icon":"✅","label":"CA Licensed #1097482","sub":"Fully Insured"},
        {"icon":"⭐","label":"4+ Years Experience","sub":"Proven Track Record"},
        {"icon":"📍","label":"32+ Cities Served","sub":"Southern California"}
    ]
    icon_els = []
    for i, item in enumerate(items):
        icon_els.append({
            "id": f"{p}ae{i+10:02d}", "elType": "widget", "widgetType": "icon-box",
            "settings": {
                "title_text": item["label"],
                "description_text": item["sub"],
                "icon": {"value":"fas fa-check","library":"fa-solid"},
                "title_typography_typography": "custom",
                "title_typography_font_family": "Oswald",
                "title_typography_font_weight": "600",
                "title_typography_font_size": {"unit":"px","size":14},
                "title_color": "#2D2D2D",
                "description_color": "#6B7280",
                "description_typography_typography": "custom",
                "description_typography_font_size": {"unit":"px","size":12},
                "position": "left", "view": "default"
            }
        })
    return {
        "id": f"{p}ae01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#F3F4F6",
            "border_border": "solid",
            "border_width": {"unit":"px","top":1,"right":0,"bottom":1,"left":0,"isLinked":False},
            "border_color": "#D1D5DB",
            "padding": {"unit":"px","top":"20","right":"24","bottom":"20","left":"24","isLinked":False}
        },
        "elements": [{
            "id": f"{p}ae05", "elType": "container",
            "settings": {
                "content_width": "full", "flex_direction": "row",
                "flex_justify_content": "space-between", "flex_align_items": "center",
                "gap": {"unit":"px","size":16}
            },
            "elements": icon_els
        }]
    }

def services_section(p, city, service_descs):
    # service_descs: list of 8 descriptions, one per service
    services = [
        {"name":"Emergency Plumbing","slug":"emergency-plumbing","img":"sewer-repair-service-truck-inland-empire.webp"},
        {"name":"Drain Cleaning","slug":"drain-cleaning","img":"drain-cleaning-shower-upland-ca.webp"},
        {"name":"Sewer Line Repair","slug":"sewer-line-repair","img":"sewer-line-excavation-ontario-ca.webp"},
        {"name":"Water Heater Services","slug":"water-heater-services","img":"sink-faucet-installation-ontario-ca.webp"},
        {"name":"Slab Leak Detection","slug":"slab-leak-detection","img":"pipe-repair-leak-detection-chino-hills-ca.webp"},
        {"name":"Hydrojetting","slug":"hydrojetting","img":"hydro-jetting-roof-rancho-cucamonga-ca.webp"},
        {"name":"Gas Leak Detection","slug":"gas-leak-detection","img":"camera-inspection-drain-cleaning-san-bernardino-ca.webp"},
        {"name":"Water Filtration","slug":"water-filtration","img":"copper-pipe-installation-chino-ca.webp"},
    ]
    card_els = []
    for i, (svc, desc) in enumerate(zip(services, service_descs)):
        card_els.append({
            "id": f"{p}af{i+10:02d}", "elType": "container",
            "settings": {
                "background_background": "classic", "background_color": "#FFFFFF",
                "border_radius": {"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},
                "box_shadow_box_shadow_type": "yes",
                "box_shadow_box_shadow": {"horizontal":0,"vertical":2,"blur":12,"spread":0,"color":"rgba(0,0,0,0.06)"},
                "flex_direction": "column",
                "overflow": "hidden"
            },
            "elements": [
                {
                    "id": f"{p}af{i+20:02d}", "elType": "widget", "widgetType": "image",
                    "settings": {
                        "image": {"url": IMG+svc["img"], "alt": f"{svc['name']} {city} CA"},
                        "image_size": "full",
                        "width": {"unit":"%","size":100},
                        "height": {"unit":"px","size":180},
                        "object_fit": "cover"
                    }
                },
                {
                    "id": f"{p}af{i+30:02d}", "elType": "container",
                    "settings": {"flex_direction":"column","padding":{"unit":"px","top":"20","right":"20","bottom":"20","left":"20","isLinked":False}},
                    "elements": [
                        {
                            "id": f"{p}af{i+40:02d}", "elType": "widget", "widgetType": "heading",
                            "settings": {
                                "title": svc["name"], "header_size": "h3",
                                "typography_font_family": "Oswald", "typography_font_weight": "600",
                                "typography_font_size": {"unit":"px","size":16},
                                "typography_text_transform": "uppercase",
                                "title_color": "#2D2D2D"
                            }
                        },
                        {
                            "id": f"{p}af{i+50:02d}", "elType": "widget", "widgetType": "text-editor",
                            "settings": {"editor": f"<p style=\"font-size:13px;color:#6B7280;line-height:1.6;\">{desc}</p>"}
                        },
                        {
                            "id": f"{p}af{i+60:02d}", "elType": "widget", "widgetType": "button",
                            "settings": {
                                "text": "Learn More", "link": {"url": f"/{svc['slug']}/"},
                                "background_color": "transparent", "button_text_color": "#B91C1C",
                                "typography_font_family": "Oswald", "typography_font_weight": "500",
                                "typography_font_size": {"unit":"px","size":12},
                                "size": "xs"
                            }
                        }
                    ]
                }
            ]
        })

    return {
        "id": f"{p}af01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#FFFFFF",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}af02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "What We Do", "header_size": "p", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                    "typography_font_size": {"unit":"px","size":12},
                    "typography_letter_spacing": {"unit":"px","size":3},
                    "typography_text_transform": "uppercase",
                    "title_color": "#B91C1C"
                }
            },
            {
                "id": f"{p}af03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": f"Plumbing Services in {city}, CA", "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":38},
                    "typography_text_transform": "uppercase",
                    "title_color": "#2D2D2D"
                }
            },
            {
                "id": f"{p}af04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}
            },
            {
                "id": f"{p}af05", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "flex_wrap": "wrap",
                    "gap": {"unit":"px","size":24}, "_element_width": "initial"
                },
                "elements": card_els
            }
        ]
    }

def why_section(p, city, why_heading, why_cards):
    card_els = []
    for i, c in enumerate(why_cards):
        card_els.append({
            "id": f"{p}ag{i+10:02d}", "elType": "widget", "widgetType": "icon-box",
            "settings": {
                "title_text": c["title"], "description_text": c["desc"],
                "icon": {"value":"fas fa-check","library":"fa-solid"},
                "_padding": {"unit":"px","top":"32","right":"24","bottom":"32","left":"24","isLinked":False},
                "title_typography_typography": "custom",
                "title_typography_font_family": "Oswald", "title_typography_font_weight": "600",
                "title_typography_font_size": {"unit":"px","size":18},
                "title_typography_text_transform": "uppercase",
                "title_color": "#FFFFFF",
                "description_color": "#93C5FD",
                "description_typography_typography": "custom",
                "description_typography_font_size": {"unit":"px","size":14},
                "position": "top", "title_size": "h3", "view": "default"
            }
        })
    return {
        "id": f"{p}ag01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#1E3A6E",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ag02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "Our Promise", "header_size": "p", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                    "typography_font_size": {"unit":"px","size":12},
                    "typography_letter_spacing": {"unit":"px","size":3},
                    "typography_text_transform": "uppercase",
                    "title_color": "#fca5a5"
                }
            },
            {
                "id": f"{p}ag03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": why_heading, "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":38},
                    "typography_text_transform": "uppercase",
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}ag04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}
            },
            {
                "id": f"{p}ag05", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "gap": {"unit":"px","size":32},
                    "_element_width": "initial"
                },
                "elements": card_els
            }
        ]
    }

def seo_section(p, city, seo_heading, seo_paragraphs):
    paras = "".join(f"<p style=\"font-size:15px;color:#4B5563;line-height:1.8;margin-bottom:18px;\">{para}</p>" for para in seo_paragraphs)
    return {
        "id": f"{p}ah01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#FFFFFF",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ah02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "Local Expertise", "header_size": "p",
                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                    "typography_font_size": {"unit":"px","size":12},
                    "typography_letter_spacing": {"unit":"px","size":3},
                    "typography_text_transform": "uppercase",
                    "title_color": "#B91C1C"
                }
            },
            {
                "id": f"{p}ah03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": seo_heading, "header_size": "h2",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":36},
                    "typography_text_transform": "uppercase",
                    "title_color": "#2D2D2D"
                }
            },
            {
                "id": f"{p}ah04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":15}}
            },
            {
                "id": f"{p}ah05", "elType": "widget", "widgetType": "text-editor",
                "settings": {"editor": paras}
            }
        ]
    }

def faq_section(p, city, faq_items):
    # faq_items: list of {"q": ..., "a": ...}
    accordion_items = [{"faq_question": item["q"], "faq_answer": item["a"]} for item in faq_items]
    return {
        "id": f"{p}ai01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#F3F4F6",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ai02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "Common Questions", "header_size": "p", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                    "typography_font_size": {"unit":"px","size":12},
                    "typography_letter_spacing": {"unit":"px","size":3},
                    "typography_text_transform": "uppercase",
                    "title_color": "#B91C1C"
                }
            },
            {
                "id": f"{p}ai03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": f"{city} Plumbing FAQs", "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":36},
                    "typography_text_transform": "uppercase",
                    "title_color": "#2D2D2D"
                }
            },
            {
                "id": f"{p}ai04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}
            },
            {
                "id": f"{p}ai05", "elType": "widget", "widgetType": "accordion",
                "settings": {
                    "tabs": accordion_items,
                    "title_html_tag": "h3",
                    "border_width": {"unit":"px","size":1},
                    "border_color": "#D1D5DB",
                    "title_color": "#2D2D2D",
                    "title_active_color": "#B91C1C",
                    "title_typography_typography": "custom",
                    "title_typography_font_family": "Oswald",
                    "title_typography_font_weight": "600",
                    "title_typography_font_size": {"unit":"px","size":15}
                }
            }
        ]
    }

def cta_container(p, heading, subtext):
    return {
        "id": f"{p}aj01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#B91C1C",
            "padding": {"unit":"px","top":"64","right":"24","bottom":"64","left":"24","isLinked":False},
            "text_align": "center"
        },
        "elements": [
            {
                "id": f"{p}aj02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": heading, "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":42},
                    "typography_text_transform": "uppercase",
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}aj03", "elType": "widget", "widgetType": "text-editor",
                "settings": {"editor": f"<p style=\"text-align:center;font-size:16px;color:rgba(255,255,255,0.85);\">{subtext}</p>"}
            },
            {
                "id": f"{p}aj04", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "<a href=\"tel:9096004561\" style=\"color:#FFFFFF;\">(909) 600-4561</a>",
                    "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":50},
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}aj05", "elType": "widget", "widgetType": "button",
                "settings": {
                    "text": "Call Now", "link": {"url":"tel:9096004561"},
                    "background_color": "#FFFFFF", "button_text_color": "#B91C1C",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":15},
                    "border_border": "solid",
                    "border_width": {"unit":"px","top":2,"right":2,"bottom":2,"left":2,"isLinked":True},
                    "border_color": "#FFFFFF",
                    "border_radius": {"unit":"px","top":4,"right":4,"bottom":4,"left":4,"isLinked":True},
                    "align": "center", "size": "lg"
                }
            }
        ]
    }

def footer_container(p):
    return {
        "id": f"{p}ak01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#2D2D2D",
            "padding": {"unit":"px","top":"64","right":"24","bottom":"24","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ak02", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "flex_wrap": "wrap",
                    "gap": {"unit":"px","size":48}, "_element_width": "initial"
                },
                "elements": [
                    {
                        "id": f"{p}ak03", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"25%"},
                        "elements": [
                            {
                                "id": f"{p}ak04", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": "Regal Plumbing &amp; Rooter",
                                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                                    "typography_font_size": {"unit":"px","size":18},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#FFFFFF"
                                }
                            },
                            {
                                "id": f"{p}ak05", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<p style=\"font-size:13px;color:#9CA3AF;line-height:1.6;\">Honest, professional plumbing &amp; rooter services for the Inland Empire &amp; San Gabriel Valley.</p>"}
                            },
                            {
                                "id": f"{p}ak06", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<p style=\"display:inline-block;background:rgba(185,28,28,0.2);border:1px solid rgba(185,28,28,0.4);color:#fca5a5;font-size:11.5px;font-family:Oswald,sans-serif;letter-spacing:1px;padding:4px 10px;border-radius:3px;\">CA License #1097482</p>"}
                            }
                        ]
                    },
                    {
                        "id": f"{p}ak07", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"15%"},
                        "elements": [
                            {
                                "id": f"{p}ak08", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": "Services",
                                    "typography_font_family": "Oswald", "typography_font_weight": "600",
                                    "typography_font_size": {"unit":"px","size":14},
                                    "typography_letter_spacing": {"unit":"px","size":1.5},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#FFFFFF"
                                }
                            },
                            {
                                "id": f"{p}ak09", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;\"><li><a href=\"/emergency-plumbing/\" style=\"font-size:13.5px;color:#9CA3AF;\">Emergency Plumbing</a></li><li><a href=\"/drain-cleaning/\" style=\"font-size:13.5px;color:#9CA3AF;\">Drain Cleaning</a></li><li><a href=\"/sewer-line-repair/\" style=\"font-size:13.5px;color:#9CA3AF;\">Sewer Line Repair</a></li><li><a href=\"/water-heater-services/\" style=\"font-size:13.5px;color:#9CA3AF;\">Water Heater Services</a></li><li><a href=\"/slab-leak-detection/\" style=\"font-size:13.5px;color:#9CA3AF;\">Slab Leak Detection</a></li><li><a href=\"/hydrojetting/\" style=\"font-size:13.5px;color:#9CA3AF;\">Hydrojetting</a></li><li><a href=\"/gas-leak-detection/\" style=\"font-size:13.5px;color:#9CA3AF;\">Gas Leak Detection</a></li><li><a href=\"/water-filtration/\" style=\"font-size:13.5px;color:#9CA3AF;\">Water Filtration</a></li></ul>"}
                            }
                        ]
                    },
                    {
                        "id": f"{p}ak10", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"15%"},
                        "elements": [
                            {
                                "id": f"{p}ak11", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": "Service Area",
                                    "typography_font_family": "Oswald", "typography_font_weight": "600",
                                    "typography_font_size": {"unit":"px","size":14},
                                    "typography_letter_spacing": {"unit":"px","size":1.5},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#FFFFFF"
                                }
                            },
                            {
                                "id": f"{p}ak12", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;\"><li><a href=\"/service-area/ontario-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Ontario</a></li><li><a href=\"/service-area/rancho-cucamonga-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Rancho Cucamonga</a></li><li><a href=\"/service-area/fontana-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Fontana</a></li><li><a href=\"/service-area/pomona-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Pomona</a></li><li><a href=\"/service-area/chino-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Chino</a></li><li><a href=\"/service-area/corona-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Corona</a></li><li><a href=\"/service-area/upland-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Upland</a></li><li><a href=\"/service-area/west-covina-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">West Covina</a></li></ul>"}
                            }
                        ]
                    },
                    {
                        "id": f"{p}ak13", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"20%"},
                        "elements": [
                            {
                                "id": f"{p}ak14", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": "Contact Us",
                                    "typography_font_family": "Oswald", "typography_font_weight": "600",
                                    "typography_font_size": {"unit":"px","size":14},
                                    "typography_letter_spacing": {"unit":"px","size":1.5},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#FFFFFF"
                                }
                            },
                            {
                                "id": f"{p}ak15", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:12px;\"><li style=\"font-size:13.5px;color:#9CA3AF;\">2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</li><li><a href=\"tel:9096004561\" style=\"font-size:13.5px;color:#9CA3AF;\">(909) 600-4561</a></li><li><a href=\"mailto:info@regalplumbingservices.com\" style=\"font-size:13.5px;color:#9CA3AF;\">info@regalplumbingservices.com</a></li><li style=\"font-size:13.5px;color:#9CA3AF;\">24/7 Emergency | Mon\u2013Sat: 7am\u20137pm</li></ul>"}
                            }
                        ]
                    }
                ]
            },
            {
                "id": f"{p}ak16", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"rgba(255,255,255,0.10)","weight":{"unit":"px","size":1},"width":{"unit":"%","size":100}}
            },
            {
                "id": f"{p}ak17", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row",
                    "flex_justify_content": "space-between", "flex_align_items": "center",
                    "padding": {"unit":"px","top":"18","right":"0","bottom":"18","left":"0","isLinked":False}
                },
                "elements": [
                    {
                        "id": f"{p}ak18", "elType": "widget", "widgetType": "text-editor",
                        "settings": {"editor":"<p style=\"font-size:12.5px;color:#6B7280;\">&copy; 2025 Regal Plumbing &amp; Rooter. All Rights Reserved. CA License #1097482</p>"}
                    },
                    {
                        "id": f"{p}ak19", "elType": "widget", "widgetType": "text-editor",
                        "settings": {"editor":"<p style=\"font-size:12.5px;color:#6B7280;\"><a href=\"/privacy-policy/\" style=\"color:#6B7280;\">Privacy Policy</a> &nbsp; <a href=\"/terms-of-service/\" style=\"color:#6B7280;\">Terms of Service</a></p>"}
                    }
                ]
            }
        ]
    }

# ====== City data ======

city_pages = [
    {
        "file": "ontario-ca.json", "prefix": "on",
        "title": "Plumber in Ontario CA",
        "seo_title": "Plumber in Ontario, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Licensed, local plumbing services in Ontario, CA. 24/7 emergency response, same-day service. Slab leaks, drain cleaning, water heaters. Call (909) 600-4561.",
        "city": "Ontario",
        "h1": "Plumber in Ontario, CA",
        "sub": "Licensed, local plumbing services for Ontario homeowners and businesses — available 24/7 for emergencies and same-day scheduled work.",
        "map_p1": "Ontario, CA is one of the Inland Empire's fastest-growing cities, home to neighborhoods like Ontario Ranch, Gramercy, Creekside, and the bustling corridor near Ontario International Airport. As the region expands, plumbing demands have grown alongside it — from brand-new subdivisions facing high water pressure issues to older homes near downtown contending with aging cast iron pipes and galvanized supply lines.",
        "map_p2": "Regal Plumbing &amp; Rooter is based right here in Ontario at 2141 E Philadelphia St, Suite R — which means we respond faster than anyone else when emergencies strike. Whether you're dealing with a slab leak in Ontario Ranch, a clogged main sewer near Gramercy, or a failed water heater near the airport corridor, our licensed technicians are on the road within the hour.",
        "service_descs": [
            "When a burst pipe or sewage backup strikes your Ontario home, we dispatch immediately — day or night — to stop damage fast.",
            "Ontario's hard water accelerates buildup in drains. We clear kitchen, bathroom, and main sewer lines with professional snaking and hydrojetting.",
            "Older Ontario neighborhoods near Euclid Ave have aging clay sewer pipes prone to cracking. We offer camera inspection and trenchless repair.",
            "From tankless installations in new Ontario Ranch homes to traditional tank replacements near Mountain Ave, we handle all water heater work in Ontario.",
            "Ontario's clay-heavy soil causes pipes beneath concrete slabs to shift and crack. Our electronic detection pinpoints the exact leak with minimal disruption.",
            "Hard water scale and grease coat Ontario's pipe walls over time. Our high-pressure hydrojetting scours lines clean and restores full flow capacity.",
            "Ontario's mix of older homes and new construction creates diverse gas line risks. Our licensed team uses advanced sensors to locate and repair leaks safely.",
            "Ontario tap water carries high mineral content. We install whole-home softeners and reverse osmosis systems to protect your appliances and improve taste."
        ],
        "why_heading": "Why Ontario Residents Choose Regal",
        "why_cards": [
            {"title":"Based in Ontario","desc":"Our shop is in Ontario at 2141 E Philadelphia St. When you call, we're already nearby — reaching most Ontario locations in under an hour."},
            {"title":"Ontario Experts","desc":"We know Ontario's soil conditions, water quality challenges, and infrastructure age across neighborhoods like Ontario Ranch, Gramercy, and Creekside."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Ontario job is covered by full liability insurance, and every quote is upfront with no hidden fees."}
        ],
        "seo_heading": "Trusted Plumber in Ontario CA",
        "seo_paragraphs": [
            "When you need a reliable <strong>plumber in Ontario CA</strong>, Regal Plumbing &amp; Rooter is your local choice. Based in Ontario, we understand the specific plumbing challenges homeowners and businesses face throughout this growing city. From the sprawling <strong>Ontario Ranch</strong> master-planned community to the established <strong>Gramercy</strong> and <strong>Creekside</strong> neighborhoods near the heart of town, we've seen and solved every type of plumbing problem Ontario has to offer.",
            "As your trusted <strong>emergency plumber Ontario CA</strong>, our team is on call around the clock. Whether it's a slab leak beneath a concrete foundation in an older Ontario home, a broken water main along Euclid Avenue, or a sewage backup in a commercial property — we dispatch fast and arrive with the tools to fix it right.",
            "<strong>Drain cleaning Ontario CA</strong> is one of our most frequent services. Ontario's water supply carries heavy mineral content from the local groundwater system, which accelerates scale buildup inside pipes. We use professional snaking and high-pressure hydrojetting to restore full function.",
            "<strong>Slab leak Ontario</strong> detection is particularly important here because the clay-heavy soil under many Ontario properties shifts seasonally, putting stress on copper supply pipes embedded in concrete. Our <strong>water heater repair Ontario CA</strong> services are equally dependable — backed by upfront pricing and licensed technicians."
        ],
        "faq_items": [
            {"q":"How fast can Regal Plumbing get to my Ontario, CA home?","a":"Because we're based in Ontario at 2141 E Philadelphia St, our technicians can typically reach most parts of Ontario within 45–60 minutes of your call. For plumbing emergencies, we prioritize the fastest possible dispatch — including nights and weekends."},
            {"q":"Do you serve all neighborhoods in Ontario, CA?","a":"Yes — we serve all of Ontario, including Ontario Ranch, Gramercy, Creekside, the Airport District, downtown Ontario, and every area in between. No part of the city is outside our service range."},
            {"q":"What are the most common plumbing problems in Ontario, CA?","a":"The most frequent calls we get from Ontario residents involve slab leaks — especially in older neighborhoods where copper pipes sit in calcium-heavy soil — drain blockages from hard water buildup, and water heater failures."},
            {"q":"Does Regal Plumbing work on new construction homes in Ontario Ranch?","a":"Yes — we work on both new construction and established homes throughout Ontario. For Ontario Ranch properties, we're familiar with current building standards and frequently handle water heater upgrades, whole-home filtration installations, and pressure regulator replacements."},
            {"q":"Is emergency plumbing service available on weekends in Ontario?","a":"Absolutely. Our emergency plumbing line is staffed 24 hours a day, 7 days a week — including weekends and holidays. Call (909) 600-4561 any time and a real person will answer."}
        ],
        "cta_heading": "Need a Plumber in Ontario? We're Ready Now",
        "cta_sub": "24/7 emergency and same-day service throughout Ontario, CA"
    },
    {
        "file": "rancho-cucamonga-ca.json", "prefix": "rc",
        "title": "Plumber in Rancho Cucamonga CA",
        "seo_title": "Plumber in Rancho Cucamonga, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Fast, licensed plumbing in Rancho Cucamonga. 24/7 emergency response. Slab leaks, drain cleaning, water heaters, hydrojetting. Call (909) 600-4561.",
        "city": "Rancho Cucamonga",
        "h1": "Plumber in Rancho Cucamonga, CA",
        "sub": "Fast, licensed plumbing service for Rancho Cucamonga homes and businesses — 24/7 emergency response and same-day appointments available.",
        "map_p1": "Rancho Cucamonga is one of the Inland Empire's most desirable communities, spanning from the foothills of the San Gabriel Mountains down through neighborhoods like Etiwanda, Victoria, Alta Loma, and Haven View Estates. With a mix of older ranch-style homes and modern developments, Rancho Cucamonga presents a wide range of plumbing challenges — from hard water mineral buildup in newer homes to tree root intrusions in the mature oak-lined streets of Etiwanda.",
        "map_p2": "Regal Plumbing &amp; Rooter serves all of Rancho Cucamonga from our base in neighboring Ontario. We're familiar with the city's specific groundwater quality, the pressurized irrigation systems that many Rancho Cucamonga properties share with municipal lines, and the slab construction common throughout the <strong>Victoria</strong> and <strong>Alta Loma</strong> areas.",
        "service_descs": [
            "Rancho Cucamonga emergencies get fast response — from Etiwanda to Victoria Park, we're on the road within minutes of your call, 24/7.",
            "Hard water from Rancho Cucamonga's groundwater system creates stubborn scale in drains. We restore full flow with professional snaking and jetting.",
            "Tree roots in Rancho Cucamonga's mature Etiwanda neighborhood can crush aging clay sewer lines. We offer camera inspection and trenchless repair options.",
            "From tankless upgrades in Haven View Estates to standard tank replacements throughout Rancho Cucamonga, we handle all water heater work efficiently.",
            "Rancho Cucamonga's slab-built homes in Victoria and Alta Loma are susceptible to copper pipe failures beneath concrete. Our electronic detection finds leaks precisely.",
            "Mineral deposits and grease coat Rancho Cucamonga pipe walls over years of use. Our high-pressure jetting scours lines completely clean from the inside out.",
            "Whether in a newer Rancho Cucamonga development or an older foothills home, our licensed technicians use precision equipment to locate and repair gas line issues safely.",
            "Rancho Cucamonga's hard water is notorious for damaging appliances and leaving mineral deposits. We install whole-home softeners and filtration systems that last."
        ],
        "why_heading": "Why Rancho Cucamonga Residents Choose Regal",
        "why_cards": [
            {"title":"Fast RC Response","desc":"From our Ontario base, we reach Rancho Cucamonga quickly — covering Etiwanda, Victoria, Alta Loma, and Haven View with no wasted time."},
            {"title":"Hard Water Specialists","desc":"We know Rancho Cucamonga's high-mineral water creates unique pipe and appliance problems. Our solutions address the root cause, not just the symptom."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Rancho Cucamonga job is performed by licensed technicians with full liability coverage and upfront, transparent pricing."}
        ],
        "seo_heading": "Trusted Plumber in Rancho Cucamonga CA",
        "seo_paragraphs": [
            "Finding a dependable <strong>plumber in Rancho Cucamonga CA</strong> means finding someone who understands this city's unique landscape — from the gated communities along the foothills to the established neighborhoods of <strong>Etiwanda</strong>, <strong>Victoria</strong>, <strong>Alta Loma</strong>, and <strong>Haven View Estates</strong>.",
            "As the trusted <strong>emergency plumber Rancho Cucamonga CA</strong> residents rely on, we're available day and night. Rancho Cucamonga homes — particularly those in the older Etiwanda district — experience tree root intrusions into sewer lines and seasonal slab movement that can crack supply lines.",
            "<strong>Drain cleaning Rancho Cucamonga CA</strong> is a frequent need here because of the city's well-documented hard water. Our hydrojetting service is particularly effective for Rancho Cucamonga properties, blasting away years of mineral scale to restore full pipe capacity.",
            "For <strong>slab leak Rancho Cucamonga</strong> detection, our team uses electronic listening equipment and thermal imaging to pinpoint leak locations without unnecessary demolition. We also provide complete <strong>water heater repair Rancho Cucamonga CA</strong> services — from fixing faulty heating elements to full tankless system installations."
        ],
        "faq_items": [
            {"q":"How fast can you get to Rancho Cucamonga in an emergency?","a":"We typically reach Rancho Cucamonga locations within 45–60 minutes of your call. Our Ontario base puts us close to all Rancho Cucamonga neighborhoods, including Etiwanda, Victoria, Alta Loma, and Haven View."},
            {"q":"Do you serve all of Rancho Cucamonga, including the foothills areas?","a":"Yes — we serve all of Rancho Cucamonga, including the foothill communities near Cucamonga Peak, the Etiwanda area, Victoria neighborhood, and all residential communities throughout the city."},
            {"q":"Why is hard water such a big problem in Rancho Cucamonga?","a":"Rancho Cucamonga's water supply contains elevated levels of calcium and magnesium from local groundwater sources. Over time, this mineral content builds up inside pipes, water heaters, and appliances — reducing efficiency and shortening lifespan."},
            {"q":"What signs indicate a slab leak in my Rancho Cucamonga home?","a":"Common slab leak indicators include warm or wet spots on your floor, the sound of running water when nothing is in use, unexplained spikes in your water bill, cracks in flooring or walls, and reduced water pressure."},
            {"q":"Does Regal Plumbing offer weekend service in Rancho Cucamonga?","a":"Yes — we offer emergency plumbing service in Rancho Cucamonga 24 hours a day, 7 days a week, including weekends and holidays. Call (909) 600-4561 to book."}
        ],
        "cta_heading": "Need a Plumber in Rancho Cucamonga? We're Ready",
        "cta_sub": "24/7 emergency and same-day service throughout Rancho Cucamonga, CA"
    },
    {
        "file": "fontana-ca.json", "prefix": "fo",
        "title": "Plumber in Fontana CA",
        "seo_title": "Plumber in Fontana, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Reliable, licensed plumbing in Fontana, CA. Emergency response 24/7. Slab leaks, drain cleaning, sewer repair, water heaters. Call (909) 600-4561.",
        "city": "Fontana",
        "h1": "Plumber in Fontana, CA",
        "sub": "Reliable, licensed plumbing for Fontana homes and businesses — emergency response 24/7 and same-day service when you need it most.",
        "map_p1": "Fontana is one of the Inland Empire's largest and most diverse cities, spanning from the industrial corridor near I-10 up through residential communities like <strong>Sierra Lakes</strong>, <strong>South Fontana</strong>, <strong>North Fontana</strong>, and the <strong>Catawba</strong> neighborhood. With a significant portion of the city's housing stock dating back to the 1970s and 1980s, Fontana is home to aging sewer infrastructure and galvanized supply lines that require expert attention.",
        "map_p2": "Regal Plumbing &amp; Rooter serves all of Fontana from our Ontario headquarters. We regularly handle slab leak repairs in South Fontana homes, drain cleaning in the high-density neighborhoods near Baseline Avenue, and sewer line repairs throughout the city.",
        "service_descs": [
            "From Sierra Lakes to South Fontana, our emergency plumbers reach every corner of Fontana fast — 24 hours a day, every day of the year.",
            "Fontana's aging pipes and hard water create stubborn drain blockages. We clear all drain types in Fontana quickly using professional-grade snaking and jetting equipment.",
            "Older Fontana neighborhoods have clay sewer pipes that crack and collapse over time. We perform camera inspection and trenchless repair with minimal yard disruption.",
            "Fontana's hard water shortens water heater lifespan through scale buildup. We repair and replace all water heater types in Fontana, including energy-efficient tankless units.",
            "South Fontana's older slab-built homes are particularly prone to copper pipe corrosion beneath concrete. Our electronic detection finds leaks without destructive excavation.",
            "Years of mineral buildup and grease accumulation in Fontana sewer lines call for hydrojetting. We blast pipes clean for lasting results that basic snaking cannot achieve.",
            "Gas line problems in Fontana homes require immediate, licensed response. Our technicians locate and repair gas leaks throughout Fontana with precision testing equipment.",
            "Fontana residents deal with some of the region's hardest water. We install whole-home softeners and filtration systems to protect appliances, pipes, and drinking water quality."
        ],
        "why_heading": "Why Fontana Residents Choose Regal",
        "why_cards": [
            {"title":"Quick Fontana Dispatch","desc":"From our Ontario base, we reach Fontana neighborhoods — Sierra Lakes, South Fontana, North Fontana, and Catawba — in under an hour for any plumbing emergency."},
            {"title":"Aging Pipe Experts","desc":"Fontana's older housing stock requires specialized knowledge. We diagnose and repair aging sewer lines, galvanized pipes, and deteriorating slab systems correctly the first time."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Fontana job is done by licensed plumbers with full insurance coverage and transparent, upfront pricing — no surprises on your invoice."}
        ],
        "seo_heading": "Trusted Plumber in Fontana CA",
        "seo_paragraphs": [
            "When Fontana residents search for a <strong>plumber in Fontana CA</strong>, they need someone who understands the city's unique infrastructure challenges. From the industrial roots that shaped South Fontana's older neighborhoods to the newer master-planned communities in <strong>Sierra Lakes</strong> and <strong>North Fontana</strong>, the plumbing needs vary dramatically across the city.",
            "As a trusted <strong>emergency plumber Fontana CA</strong> residents rely on, we don't believe in long hold times or estimated arrival windows. When you call us with a plumbing emergency in Fontana, we dispatch immediately. Burst pipes, sewage backups, and gas leaks get our fastest response — day or night.",
            "<strong>Drain cleaning Fontana CA</strong> is a frequent service call we handle throughout the city. Fontana's water is high in dissolved minerals that coat the inside of pipes over time. Our team uses professional drain snaking for straightforward blockages and high-pressure hydrojetting for persistent clogs.",
            "For <strong>slab leak Fontana</strong> diagnosis, we use electronic leak detection equipment that pinpoints the exact location of underground pipe failures without tearing up your entire floor. Our <strong>water heater repair Fontana CA</strong> team handles everything from simple thermostat replacements to full tankless system conversions."
        ],
        "faq_items": [
            {"q":"How fast can you get to Fontana for an emergency?","a":"We typically reach Fontana within 45–60 minutes of your call. Our technicians are regularly working in the area — servicing Fontana, Rancho Cucamonga, Rialto, and Ontario — so we're never far away when you need us."},
            {"q":"Do you serve all of Fontana, including South Fontana and Sierra Lakes?","a":"Yes — we serve all of Fontana, from South Fontana and the industrial corridor near I-10 up through Sierra Lakes, North Fontana, and the Catawba community near the foothills."},
            {"q":"Why do so many Fontana homes have slab leak problems?","a":"Many Fontana homes built in the 1970s and 1980s used copper supply pipes embedded directly in concrete slabs. Over the decades, Fontana's mineral-rich water has corroded these pipes from the inside, and soil movement has stressed them from the outside."},
            {"q":"What's the difference between snaking and hydrojetting for Fontana drains?","a":"Drain snaking breaks up clogs with a rotating cable — effective for soft blockages like hair and grease. Hydrojetting uses high-pressure water to scour the entire pipe wall, removing mineral scale and debris. For Fontana's hard water conditions, hydrojetting often provides a much longer-lasting result."},
            {"q":"Can you fix a sewer line in Fontana without digging up my yard?","a":"In many cases, yes. We offer trenchless sewer line repair options for Fontana properties — pipe lining and pipe bursting methods that repair or replace damaged sewer lines with minimal excavation."}
        ],
        "cta_heading": "Need a Plumber in Fontana? We're Ready Now",
        "cta_sub": "24/7 emergency and same-day service throughout Fontana, CA"
    },
    {
        "file": "pomona-ca.json", "prefix": "po",
        "title": "Plumber in Pomona CA",
        "seo_title": "Plumber in Pomona, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Expert plumbing in Pomona, CA. Emergency service 24/7. Serving Downtown Pomona, Lincoln Park, Arroyo Park, Ganesha Hills. Call (909) 600-4561.",
        "city": "Pomona",
        "h1": "Plumber in Pomona, CA",
        "sub": "Expert plumbing for Pomona homes and businesses — emergency response 24/7 and same-day service available.",
        "map_p1": "Pomona is one of the oldest and most historically rich cities in the San Gabriel Valley, with neighborhoods like <strong>Downtown Pomona</strong>, <strong>Lincoln Park</strong>, <strong>Arroyo Park</strong>, and <strong>Ganesha Hills</strong>. Much of Pomona's residential housing stock was built decades ago, which means aging plumbing infrastructure is a common challenge — from corroded galvanized supply lines to deteriorating clay sewer pipes beneath established streets.",
        "map_p2": "Regal Plumbing &amp; Rooter serves all of Pomona from our Ontario base, just minutes away. We regularly handle drain cleaning, slab leak detection, and sewer line repairs throughout Pomona's diverse neighborhoods. Our familiarity with the city's older plumbing systems means accurate diagnosis and lasting repairs on every visit.",
        "service_descs": [
            "Pomona emergencies require immediate response. From Downtown Pomona to Lincoln Park, we dispatch 24/7 and arrive fast to stop burst pipes and sewage backups.",
            "Pomona's aging pipes and hard water create persistent drain blockages. We clear all drain types professionally — kitchen, bathroom, and main sewer lines.",
            "Pomona's older clay sewer lines are vulnerable to cracking and root intrusion. We use camera inspection to diagnose accurately and offer trenchless repair when possible.",
            "From traditional tank replacements in established Pomona neighborhoods to tankless upgrades, our licensed technicians handle all water heater work with same-day availability.",
            "Pomona's aging slab homes have copper pipes that corrode over decades. Our electronic detection equipment locates slab leaks precisely without unnecessary floor demolition.",
            "Mineral and grease buildup in Pomona's older pipes requires powerful hydrojetting to clear completely. We restore full pipe capacity for lasting results.",
            "Gas line issues in Pomona's older homes require careful, licensed response. We locate and repair gas leaks safely with advanced detection equipment and proper permits.",
            "Pomona's hard water affects pipes, fixtures, and appliances. We install whole-home water softeners and reverse osmosis systems to improve water quality throughout your home."
        ],
        "why_heading": "Why Pomona Residents Choose Regal",
        "why_cards": [
            {"title":"Old-Home Experts","desc":"We specialize in the aging infrastructure common in Pomona's established neighborhoods — galvanized pipes, clay sewer lines, and older slab systems."},
            {"title":"Fast Pomona Response","desc":"From our Ontario base, we reach all Pomona neighborhoods quickly — Downtown, Lincoln Park, Arroyo Park, and Ganesha Hills — with no long wait times."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Pomona job is performed by licensed plumbers with full liability coverage and transparent, upfront pricing."}
        ],
        "seo_heading": "Trusted Plumber in Pomona CA",
        "seo_paragraphs": [
            "When you need a reliable <strong>plumber in Pomona CA</strong>, Regal Plumbing &amp; Rooter brings the expertise your home deserves. Pomona's older housing stock — particularly in <strong>Downtown Pomona</strong>, <strong>Lincoln Park</strong>, and <strong>Arroyo Park</strong> — presents unique plumbing challenges that require experience with aging infrastructure.",
            "As your <strong>emergency plumber Pomona CA</strong>, we respond around the clock. Whether it's a burst pipe in a historic downtown building or a sewer backup in a Ganesha Hills home, our team dispatches immediately with fully stocked service vehicles.",
            "<strong>Drain cleaning Pomona CA</strong> is one of our most common services in the city. Decades of hard water mineral buildup combine with grease and debris in Pomona's older drain lines to cause persistent blockages. We use both snaking and hydrojetting to provide lasting solutions.",
            "For <strong>slab leak Pomona</strong> detection and <strong>water heater repair Pomona CA</strong>, our team brings the same precision and upfront pricing that Pomona residents have come to expect from Regal Plumbing. We know this city, and we know how to fix its plumbing right."
        ],
        "faq_items": [
            {"q":"How quickly can you respond to a plumbing emergency in Pomona?","a":"We typically reach Pomona locations within 45–60 minutes of your call, day or night. Our Ontario base is just minutes from Pomona, so response times are consistently fast."},
            {"q":"Do you serve all Pomona neighborhoods?","a":"Yes — we serve all of Pomona, including Downtown Pomona, Lincoln Park, Arroyo Park, Ganesha Hills, and every residential and commercial area throughout the city."},
            {"q":"Why do older Pomona homes have so many plumbing issues?","a":"Many Pomona homes were built in the 1950s through 1970s using galvanized steel pipes and clay sewer lines that have since corroded or collapsed. Hard water accelerates corrosion, and tree roots take advantage of even small pipe cracks."},
            {"q":"Can you do trenchless sewer repair in Pomona?","a":"In many cases, yes. Trenchless pipe lining and pipe bursting methods allow us to repair or replace damaged Pomona sewer lines with minimal excavation — saving your landscaping and reducing repair time."},
            {"q":"Is weekend plumbing service available in Pomona?","a":"Absolutely — we offer 24/7 emergency service in Pomona, including weekends and holidays. Call (909) 600-4561 any time."}
        ],
        "cta_heading": "Need a Plumber in Pomona? We're Ready Now",
        "cta_sub": "24/7 emergency and same-day service throughout Pomona, CA"
    },
    {
        "file": "chino-ca.json", "prefix": "ch",
        "title": "Plumber in Chino CA",
        "seo_title": "Plumber in Chino, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Licensed plumbing in Chino, CA. Serving The Preserve, College Park, Downtown Chino, Airport Area. 24/7 emergency response. Call (909) 600-4561.",
        "city": "Chino",
        "h1": "Plumber in Chino, CA",
        "sub": "Fast, licensed plumbing for Chino homes and businesses — 24/7 emergency response and same-day service available.",
        "map_p1": "Chino blends newer master-planned communities with its historic downtown roots. Neighborhoods like <strong>The Preserve</strong>, <strong>College Park</strong>, <strong>Downtown Chino</strong>, and the <strong>Airport Area</strong> reflect the city's rapid growth alongside its established character. Newer subdivisions in The Preserve face hard water and pressure regulation challenges, while older homes near downtown Chino contend with aging galvanized pipes and deteriorating sewer lines.",
        "map_p2": "Regal Plumbing &amp; Rooter serves all of Chino from our Ontario base, just minutes away. We're experienced with both new construction plumbing demands and the older infrastructure challenges common in established Chino neighborhoods. Our team is on call 24/7 for plumbing emergencies throughout the city.",
        "service_descs": [
            "Chino plumbing emergencies get immediate response — from The Preserve to Downtown Chino, we dispatch 24/7 to stop burst pipes and backups fast.",
            "Chino's mix of new and older pipes both suffer from hard water buildup. We clear all drain types professionally with snaking and hydrojetting equipment.",
            "From clay pipes near downtown Chino to newer PVC in The Preserve, we use camera inspection to diagnose sewer issues accurately and repair them right.",
            "Whether it's a new tankless install in College Park or a traditional tank replacement near Downtown Chino, we handle all water heater work throughout the city.",
            "Chino's slab homes — both older and new construction — can develop pipe failures beneath concrete. Our electronic detection finds leaks precisely without unnecessary digging.",
            "Years of hard water scale and grease accumulation in Chino pipes call for powerful hydrojetting. We restore full pipe capacity for lasting results throughout the city.",
            "Gas line issues in Chino homes require licensed, careful response. We locate and repair gas leaks throughout Chino with advanced detection equipment.",
            "Chino's hard water affects pipes and appliances throughout the city. We install whole-home softeners and RO systems for clean, soft water."
        ],
        "why_heading": "Why Chino Residents Choose Regal",
        "why_cards": [
            {"title":"New & Old Chino Homes","desc":"We serve both new master-planned communities like The Preserve and College Park and established older neighborhoods near downtown Chino with equal expertise."},
            {"title":"Fast Chino Response","desc":"Our Ontario base is minutes from Chino. We reach every Chino neighborhood quickly — The Preserve, College Park, Downtown, and the Airport Area."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Chino job is performed by licensed plumbers with full liability coverage and transparent pricing — no hidden fees."}
        ],
        "seo_heading": "Trusted Plumber in Chino CA",
        "seo_paragraphs": [
            "For a reliable <strong>plumber in Chino CA</strong>, Regal Plumbing &amp; Rooter brings the expertise to handle Chino's unique mix of old and new plumbing infrastructure. From the newer homes in <strong>The Preserve</strong> and <strong>College Park</strong> to the older properties near <strong>Downtown Chino</strong>, we've worked throughout this city.",
            "As your <strong>emergency plumber Chino CA</strong>, we respond 24 hours a day. Chino plumbing emergencies — burst pipes, sewage backups, gas leaks — receive our fastest dispatch, any time of day or night.",
            "<strong>Drain cleaning Chino CA</strong> is a common service need throughout the city. Hard water mineral buildup affects both new and older Chino pipe systems. We use professional snaking for everyday clogs and hydrojetting for deep-cleaning of pipe walls.",
            "Our <strong>slab leak Chino</strong> detection uses electronic equipment to pinpoint leaks precisely. We also handle all <strong>water heater repair Chino CA</strong> needs — from emergency repairs to full tankless installations — with upfront pricing on every job."
        ],
        "faq_items": [
            {"q":"How fast can you respond to plumbing emergencies in Chino?","a":"We typically reach Chino within 45–60 minutes of your call. Our Ontario base is just minutes from Chino, so our response times are consistently fast throughout the city."},
            {"q":"Do you work in newer Chino communities like The Preserve and College Park?","a":"Yes — we serve all of Chino, including The Preserve, College Park, Downtown Chino, and the Airport Area. We're experienced with the plumbing systems in both new construction and older homes."},
            {"q":"What causes slab leaks in newer Chino homes?","a":"Even newer homes can develop slab leaks. High water pressure, soil settlement, and manufacturing defects in copper fittings can all cause pipe failures beneath a concrete slab. Early detection with our electronic equipment prevents costly damage."},
            {"q":"Can you replace a water heater same-day in Chino?","a":"In most cases, yes. We carry common water heater models on our service vehicles and can complete standard tank replacements same-day in Chino. Tankless installations may require a scheduled appointment."},
            {"q":"Is 24/7 plumbing service available in Chino?","a":"Yes — we offer 24/7 emergency plumbing service throughout Chino. Call (909) 600-4561 any time, day or night, and a real person will answer."}
        ],
        "cta_heading": "Need a Plumber in Chino? We're Ready Now",
        "cta_sub": "24/7 emergency and same-day service throughout Chino, CA"
    },
    {
        "file": "corona-ca.json", "prefix": "co",
        "title": "Plumber in Corona CA",
        "seo_title": "Plumber in Corona, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Licensed plumbing in Corona, CA. Serving South Corona, Eagle Glen, and all neighborhoods. 24/7 emergency response. Call (909) 600-4561.",
        "city": "Corona",
        "h1": "Plumber in Corona, CA",
        "sub": "Licensed, professional plumbing for Corona homes and businesses — 24/7 emergency response and same-day appointments available.",
        "map_p1": "Corona is a fast-growing Inland Empire city with neighborhoods spanning from <strong>South Corona</strong> to <strong>Eagle Glen</strong> and beyond. The city's mix of newer developments and established communities creates diverse plumbing needs — from hard water filtration in master-planned subdivisions to aging sewer line repairs in older Corona neighborhoods closer to the 91 freeway corridor.",
        "map_p2": "Regal Plumbing &amp; Rooter serves all of Corona from our Ontario base. We're experienced with Corona's water quality challenges, which are similar to the broader Inland Empire hard water issues, as well as the pressurized plumbing systems in Corona's newer hillside developments. Our team responds 24/7 for all Corona plumbing emergencies.",
        "service_descs": [
            "From South Corona to Eagle Glen, our emergency plumbers respond 24/7 — dispatching fast to stop burst pipes, sewage backups, and major leaks.",
            "Corona's hard water creates scale buildup in drain lines. We clear kitchen, bathroom, and main sewer lines professionally with snaking and hydrojetting.",
            "Corona's sewer lines in older neighborhoods are prone to root intrusion and cracking. We diagnose with camera inspection and offer trenchless repair options.",
            "We handle all water heater types throughout Corona — from traditional tank replacements to tankless installations in newer hillside homes. Same-day service often available.",
            "Corona's slab homes face copper pipe corrosion beneath concrete foundations. Our electronic detection locates leaks precisely without unnecessary excavation.",
            "Hard water scale and grease buildup in Corona pipes call for professional hydrojetting. We scour pipe walls completely clean for lasting results.",
            "Gas line detection and repair in Corona requires licensed professionals. We use advanced equipment to locate leaks precisely and make code-compliant repairs.",
            "Corona's hard water is tough on appliances and plumbing. We install whole-home softeners and filtration systems that extend the life of your pipes and fixtures."
        ],
        "why_heading": "Why Corona Residents Choose Regal",
        "why_cards": [
            {"title":"Hard Water Specialists","desc":"We understand Corona's water quality challenges — high mineral content that damages pipes, appliances, and fixtures — and install solutions that address the root cause."},
            {"title":"Fast Corona Response","desc":"From our Ontario base, we reach all Corona neighborhoods quickly. South Corona, Eagle Glen, and every area of the city are within our rapid-response range."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Corona job is performed by licensed plumbers with full liability coverage and transparent, upfront pricing."}
        ],
        "seo_heading": "Trusted Plumber in Corona CA",
        "seo_paragraphs": [
            "For a dependable <strong>plumber in Corona CA</strong>, Regal Plumbing &amp; Rooter is the trusted choice for homeowners and businesses throughout the city. From <strong>South Corona</strong> to <strong>Eagle Glen</strong>, we've built a reputation for fast response, accurate diagnosis, and lasting repairs.",
            "As your <strong>emergency plumber Corona CA</strong>, we're available 24 hours a day, 7 days a week. Burst pipes, sewage backups, and gas leaks in Corona get our fastest dispatch — any time, day or night.",
            "<strong>Drain cleaning Corona CA</strong> is a frequent service need throughout the city. Corona's hard water builds up mineral scale inside pipes, accelerating blockages in kitchen and bathroom drains. Our professional snaking and hydrojetting services restore full flow reliably.",
            "For <strong>slab leak Corona</strong> detection and <strong>water heater repair Corona CA</strong>, we bring the same precision equipment and upfront pricing that Corona residents count on. Every job is backed by our commitment to quality and satisfaction."
        ],
        "faq_items": [
            {"q":"How quickly can you reach my Corona home in an emergency?","a":"We typically reach Corona locations within 45–60 minutes of your call. Our Ontario base provides quick access to all Corona neighborhoods, including South Corona, Eagle Glen, and the areas near the 91 freeway."},
            {"q":"Do you serve all of Corona, including newer developments?","a":"Yes — we serve all of Corona, including new master-planned communities, established neighborhoods, and everything in between. No part of Corona is outside our service area."},
            {"q":"What makes hard water such a problem in Corona?","a":"Corona's water supply, like much of the Inland Empire, contains elevated calcium and magnesium levels. Over time, these minerals coat pipe interiors, clog drains, damage water heaters, and leave white deposits on fixtures. A whole-home water softener is the most effective solution."},
            {"q":"Do you handle both residential and commercial plumbing in Corona?","a":"Yes — we serve both residential homeowners and commercial properties throughout Corona. From single-family homes to multi-unit buildings and businesses, our licensed team handles all plumbing needs."},
            {"q":"Is emergency plumbing service available in Corona on weekends?","a":"Absolutely. We offer 24/7 emergency plumbing service in Corona, including weekends and holidays. Call (909) 600-4561 any time."}
        ],
        "cta_heading": "Need a Plumber in Corona? We're Ready Now",
        "cta_sub": "24/7 emergency and same-day service throughout Corona, CA"
    },
    {
        "file": "upland-ca.json", "prefix": "up",
        "title": "Plumber in Upland CA",
        "seo_title": "Plumber in Upland, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Licensed plumbing in Upland, CA. Serving North Upland, San Antonio Heights, Upland Village, Cable. 24/7 emergency response. Call (909) 600-4561.",
        "city": "Upland",
        "h1": "Plumber in Upland, CA",
        "sub": "Licensed plumbing service for Upland homes and businesses — emergency response 24/7 and same-day service available.",
        "map_p1": "Upland is a charming Inland Empire city with tree-lined streets and a mix of historic homes and newer developments. Neighborhoods like <strong>North Upland</strong>, <strong>San Antonio Heights</strong>, <strong>Upland Village</strong>, and the <strong>Cable</strong> area span a range of housing eras — from early 20th-century craftsman homes to modern subdivisions. Older Upland neighborhoods frequently face root intrusion in sewer lines and aging supply pipes, while newer areas deal with hard water and pressure issues.",
        "map_p2": "Regal Plumbing &amp; Rooter serves all of Upland from our Ontario base, just minutes away. We're experienced with Upland's specific plumbing challenges — particularly root intrusion from the city's mature tree canopy and the corrosion issues common in older homes throughout North Upland and San Antonio Heights.",
        "service_descs": [
            "Upland plumbing emergencies get immediate response — from San Antonio Heights to Cable, we dispatch 24/7 to stop burst pipes and backups fast.",
            "Upland's mature trees and older pipes create persistent drain and sewer blockages. We clear all drain types professionally with snaking and hydrojetting.",
            "Upland's established neighborhoods have mature trees whose roots regularly invade aging sewer lines. We use camera inspection to diagnose and trenchless methods to repair.",
            "We handle all water heater types throughout Upland — from traditional tank replacements in established neighborhoods to tankless upgrades in newer homes.",
            "Upland's older slab homes face copper pipe corrosion beneath concrete. Our electronic leak detection pinpoints the exact location with minimal floor disruption.",
            "Root intrusion and hard water scale in Upland's older pipes require powerful hydrojetting to clear completely. We restore full flow for lasting results.",
            "Gas line issues in Upland require licensed, careful response. We locate and repair gas leaks safely throughout the city with advanced detection equipment.",
            "Upland's hard water affects pipes, water heaters, and appliances. We install whole-home water softeners and filtration systems for cleaner, softer water."
        ],
        "why_heading": "Why Upland Residents Choose Regal",
        "why_cards": [
            {"title":"Root Intrusion Experts","desc":"We specialize in the root intrusion problems common in Upland's tree-lined neighborhoods — from initial camera diagnosis to permanent repair with minimal yard disruption."},
            {"title":"Fast Upland Response","desc":"Our Ontario base is minutes from Upland. We reach North Upland, San Antonio Heights, Upland Village, and Cable quickly for any plumbing need."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every Upland job is performed by licensed plumbers with full liability coverage and upfront, transparent pricing."}
        ],
        "seo_heading": "Trusted Plumber in Upland CA",
        "seo_paragraphs": [
            "For a dependable <strong>plumber in Upland CA</strong>, Regal Plumbing &amp; Rooter knows this city's unique infrastructure. From the established homes in <strong>North Upland</strong> and <strong>San Antonio Heights</strong> to the communities in <strong>Upland Village</strong> and the <strong>Cable</strong> area, we've worked throughout Upland.",
            "As your <strong>emergency plumber Upland CA</strong>, we respond 24 hours a day. Upland plumbing emergencies receive our immediate dispatch — including nights, weekends, and holidays.",
            "<strong>Drain cleaning Upland CA</strong> and sewer line work are two of our most common Upland services. The city's mature tree canopy means root intrusion is a frequent cause of sewer line problems. We diagnose with camera inspection and provide targeted, cost-effective repair.",
            "Our <strong>slab leak Upland</strong> detection and <strong>water heater repair Upland CA</strong> services bring the same quality and upfront pricing that Upland homeowners expect. Every job is backed by our satisfaction guarantee and CA License #1097482."
        ],
        "faq_items": [
            {"q":"How fast can you reach Upland in a plumbing emergency?","a":"We typically reach Upland locations within 45–60 minutes of your call. Our Ontario base provides quick access to all Upland neighborhoods, including North Upland, San Antonio Heights, and Upland Village."},
            {"q":"Why is root intrusion such a common problem in Upland?","a":"Upland's beautiful tree-lined streets are home to mature trees with root systems that actively seek water sources. Aging clay and cast iron sewer pipes are particularly vulnerable — roots enter through small cracks and quickly grow to block the entire pipe."},
            {"q":"Do you serve all of Upland, including San Antonio Heights?","a":"Yes — we serve all of Upland, including North Upland, San Antonio Heights, Upland Village, the Cable area, and every neighborhood throughout the city."},
            {"q":"Can you repair a sewer line without digging up my Upland yard?","a":"In many cases, yes. We offer trenchless sewer repair options including pipe lining and pipe bursting that allow us to fix or replace damaged Upland sewer lines with minimal excavation."},
            {"q":"Is emergency plumbing service available in Upland on weekends?","a":"Absolutely — our 24/7 emergency line is always staffed. Call (909) 600-4561 any time, including weekends and holidays, for Upland plumbing emergencies."}
        ],
        "cta_heading": "Need a Plumber in Upland? We're Ready Now",
        "cta_sub": "24/7 emergency and same-day service throughout Upland, CA"
    },
    {
        "file": "west-covina-ca.json", "prefix": "wc",
        "title": "Plumber in West Covina CA",
        "seo_title": "Plumber in West Covina, CA — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "Licensed plumbing in West Covina, CA. Serving Shadow Oak, Merced Heights, Sunset, Monte Vista. 24/7 emergency response. Call (909) 600-4561.",
        "city": "West Covina",
        "h1": "Plumber in West Covina, CA",
        "sub": "Professional plumbing for West Covina homes and businesses — 24/7 emergency response and same-day service available.",
        "map_p1": "West Covina is a well-established San Gabriel Valley city with residential neighborhoods spanning from <strong>Shadow Oak</strong> to <strong>Merced Heights</strong>, <strong>Sunset</strong>, and <strong>Monte Vista</strong>. Much of West Covina's housing stock was built in the 1950s through 1970s, creating widespread aging infrastructure — galvanized pipes, clay sewer lines, and older water heater setups that need updated solutions.",
        "map_p2": "Regal Plumbing &amp; Rooter serves West Covina from our Ontario base, reaching the city efficiently through I-10. Our team is well-versed in the plumbing challenges typical of West Covina's mid-century homes — including corroded water supply lines, slab leak detection, and main sewer line clearing. We're on call 24/7 for all West Covina plumbing needs.",
        "service_descs": [
            "West Covina emergencies get immediate response — from Shadow Oak to Monte Vista, we dispatch 24/7 to stop burst pipes, backups, and major leaks fast.",
            "West Covina's older pipes and hard water create persistent drain blockages. We clear all drain types professionally with snaking and hydrojetting throughout the city.",
            "West Covina's aging clay sewer lines are prone to root intrusion and cracking. We diagnose with camera inspection and provide trenchless repair options when possible.",
            "We handle all water heater types throughout West Covina — traditional tank replacements to tankless upgrades in older homes. Same-day service often available.",
            "West Covina's slab homes have copper pipes that corrode over decades. Our electronic detection finds slab leaks precisely without unnecessary floor demolition.",
            "Decades of hard water buildup in West Covina's older pipes call for powerful hydrojetting. We scour pipe walls completely clean for lasting results throughout the city.",
            "Gas line problems in West Covina's older homes require licensed response. We locate and repair leaks safely with advanced detection equipment and pressure testing.",
            "West Covina's hard water affects appliances and plumbing throughout the city. We install whole-home softeners and filtration to protect your home's plumbing investment."
        ],
        "why_heading": "Why West Covina Residents Choose Regal",
        "why_cards": [
            {"title":"Old-Home Specialists","desc":"We specialize in the aging infrastructure challenges common in West Covina's mid-century homes — galvanized pipes, clay sewers, and corroded slab plumbing."},
            {"title":"Fast West Covina Response","desc":"Our Ontario base provides direct access to West Covina via I-10. We reach Shadow Oak, Merced Heights, Sunset, and Monte Vista quickly for any plumbing emergency."},
            {"title":"Licensed & Insured","desc":"CA License #1097482. Every West Covina job is performed by licensed plumbers with full liability coverage and transparent, upfront pricing."}
        ],
        "seo_heading": "Trusted Plumber in West Covina CA",
        "seo_paragraphs": [
            "When you need a reliable <strong>plumber in West Covina CA</strong>, Regal Plumbing &amp; Rooter brings specialized expertise to this established San Gabriel Valley city. West Covina neighborhoods like <strong>Shadow Oak</strong>, <strong>Merced Heights</strong>, <strong>Sunset</strong>, and <strong>Monte Vista</strong> are home to decades-old plumbing infrastructure that requires experienced hands.",
            "As your <strong>emergency plumber West Covina CA</strong>, we respond 24 hours a day. West Covina plumbing emergencies receive our immediate dispatch — our Ontario base provides fast access to the entire city.",
            "<strong>Drain cleaning West Covina CA</strong> is one of our most frequent service calls in the city. West Covina's older drain lines accumulate decades of mineral scale, grease, and debris. We use professional snaking for everyday clogs and hydrojetting for deep pipe cleaning.",
            "Our <strong>slab leak West Covina</strong> detection uses advanced electronic equipment to locate pipe failures beneath concrete foundations. We also handle all <strong>water heater repair West Covina CA</strong> needs with upfront pricing and licensed technicians on every job."
        ],
        "faq_items": [
            {"q":"How quickly can you reach West Covina for a plumbing emergency?","a":"We typically reach West Covina within 45–60 minutes of your call. Our Ontario base provides efficient access via I-10 to all West Covina neighborhoods including Shadow Oak, Merced Heights, and Monte Vista."},
            {"q":"Do you serve all of West Covina?","a":"Yes — we serve all of West Covina, including Shadow Oak, Merced Heights, Sunset, Monte Vista, and every residential and commercial area throughout the city."},
            {"q":"Why do older West Covina homes have so many plumbing problems?","a":"Many West Covina homes built in the 1950s through 1970s used galvanized steel supply pipes and clay sewer lines. These materials have a limited lifespan, and decades of hard water use accelerates their deterioration. We diagnose accurately and provide lasting repairs."},
            {"q":"Can you clear a clogged main sewer line in West Covina?","a":"Yes — main sewer line clearing is one of our most common West Covina services. We use professional snaking and hydrojetting to clear blockages thoroughly, and camera inspection to diagnose any underlying damage."},
            {"q":"Is same-day plumbing service available in West Covina?","a":"Yes — for most plumbing services including drain cleaning, water heater repair, and leak detection, same-day service is available in West Covina. Call (909) 600-4561 and we'll confirm availability."}
        ],
        "cta_heading": "Need a Plumber in West Covina? We're Ready",
        "cta_sub": "24/7 emergency and same-day service throughout West Covina, CA"
    }
]

for cp in city_pages:
    p = cp["prefix"]
    doc = {
        "version": "0.4",
        "title": cp["title"],
        "type": "page",
        "page_settings": {
            "seo_title": cp["seo_title"],
            "seo_description": cp["seo_desc"]
        },
        "content": [
            emerg_bar(p),
            header_container(p),
            hero_container(p, cp["h1"], cp["sub"]),
            map_intro_container(p, cp["city"], "", "", cp["map_p1"], cp["map_p2"]),
            trust_bar(p),
            services_section(p, cp["city"], cp["service_descs"]),
            why_section(p, cp["city"], cp["why_heading"], cp["why_cards"]),
            seo_section(p, cp["city"], cp["seo_heading"], cp["seo_paragraphs"]),
            faq_section(p, cp["city"], cp["faq_items"]),
            cta_container(p, cp["cta_heading"], cp["cta_sub"]),
            footer_container(p)
        ]
    }
    out_path = os.path.join(base_dir, cp["file"])
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"Written: {cp['file']}")

print("All 8 city pages done.")
