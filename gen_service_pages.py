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
            "settings": {"editor": "<p style=\"text-align:center;color:#ffffff;font-size:13.5px;font-weight:600;\">24/7 Emergency Service Available - Call <a href=\"tel:9096004561\" style=\"color:#fca5a5;\">(909) 600-4561</a></p>"}
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

def hero_container(p, hero_img, hero_alt, badge, h1, sub):
    return {
        "id": f"{p}ac01", "elType": "container",
        "settings": {
            "background_background": "classic",
            "background_image": {"url": IMG+hero_img, "alt": hero_alt},
            "background_size": "cover", "background_position": "center center",
            "min_height": {"unit":"px","size":320},
            "flex_align_items": "center"
        },
        "elements": [
            {
                "id": f"{p}ac02", "elType": "container",
                "settings": {
                    "background_background": "classic",
                    "background_color": "rgba(0,0,0,0.75)",
                    "content_width": "full",
                    "padding": {"unit":"px","top":"72","right":"24","bottom":"72","left":"24","isLinked":False}
                },
                "elements": [
                    {
                        "id": f"{p}ac03", "elType": "widget", "widgetType": "heading",
                        "settings": {
                            "title": badge, "header_size": "p",
                            "background_background": "classic", "background_color": "#B91C1C",
                            "typography_font_family": "Oswald", "typography_font_weight": "600",
                            "typography_font_size": {"unit":"px","size":12},
                            "typography_letter_spacing": {"unit":"px","size":1.5},
                            "typography_text_transform": "uppercase",
                            "title_color": "#FFFFFF",
                            "padding": {"unit":"px","top":"5","right":"14","bottom":"5","left":"14","isLinked":False},
                            "_margin": {"unit":"px","top":"0","right":"0","bottom":"16","left":"0","isLinked":False}
                        }
                    },
                    {
                        "id": f"{p}ac04", "elType": "widget", "widgetType": "heading",
                        "settings": {
                            "title": h1, "header_size": "h1",
                            "typography_font_family": "Oswald", "typography_font_weight": "700",
                            "typography_font_size": {"unit":"px","size":52},
                            "typography_text_transform": "uppercase",
                            "title_color": "#FFFFFF"
                        }
                    },
                    {
                        "id": f"{p}ac05", "elType": "widget", "widgetType": "text-editor",
                        "settings": {
                            "editor": f"<p style=\"font-size:17px;color:#D1D5DB;max-width:600px;line-height:1.6;\">{sub}</p>"
                        }
                    }
                ]
            }
        ]
    }

def overview_container(p, eyebrow, heading, body_text, features, cta_text, cta_url, right_img, right_alt):
    feat_items = "".join(f"<li>{f}</li>" for f in features)
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
                    "flex_align_items": "center", "gap": {"unit":"px","size":72},
                    "_element_width": "initial"
                },
                "elements": [
                    {
                        "id": f"{p}ad03", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"50%"},
                        "elements": [
                            {
                                "id": f"{p}ad04", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": eyebrow, "header_size": "p",
                                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                                    "typography_font_size": {"unit":"px","size":12},
                                    "typography_letter_spacing": {"unit":"px","size":3},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#B91C1C"
                                }
                            },
                            {
                                "id": f"{p}ad05", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": heading, "header_size": "h2",
                                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                                    "typography_font_size": {"unit":"px","size":38},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#2D2D2D"
                                }
                            },
                            {
                                "id": f"{p}ad06", "elType": "widget", "widgetType": "divider",
                                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":15}}
                            },
                            {
                                "id": f"{p}ad07", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor": f"<p style=\"font-size:15.5px;color:#4B5563;line-height:1.8;\">{body_text}</p>"}
                            },
                            {
                                "id": f"{p}ad08", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor": f"<ul style=\"list-style:none;padding:0;margin:0 0 28px;\">{feat_items}</ul>"}
                            },
                            {
                                "id": f"{p}ad09", "elType": "widget", "widgetType": "button",
                                "settings": {
                                    "text": cta_text, "link": {"url": cta_url},
                                    "background_color": "#B91C1C", "button_text_color": "#FFFFFF",
                                    "typography_font_family": "Oswald", "typography_font_weight": "600",
                                    "typography_font_size": {"unit":"px","size":14},
                                    "border_radius": {"unit":"px","top":4,"right":4,"bottom":4,"left":4,"isLinked":True}
                                }
                            }
                        ]
                    },
                    {
                        "id": f"{p}ad10", "elType": "widget", "widgetType": "image",
                        "settings": {
                            "image": {"url": IMG+right_img, "alt": right_alt},
                            "image_size": "full",
                            "width": {"unit":"%","size":100},
                            "border_radius": {"unit":"px","top":10,"right":10,"bottom":10,"left":10,"isLinked":True}
                        }
                    }
                ]
            }
        ]
    }

def cards_container(p, section_eyebrow, section_heading, cards):
    card_els = []
    for i, c in enumerate(cards):
        card_els.append({
            "id": f"{p}ae{i+10:02d}", "elType": "container",
            "settings": {
                "background_background": "classic", "background_color": "#FFFFFF",
                "border_border": "solid", "border_width": {"unit":"px","top":3,"right":0,"bottom":0,"left":0,"isLinked":False},
                "border_color": "#B91C1C",
                "border_radius": {"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},
                "box_shadow_box_shadow_type": "yes",
                "box_shadow_box_shadow": {"horizontal":0,"vertical":2,"blur":12,"spread":0,"color":"rgba(0,0,0,0.06)"},
                "padding": {"unit":"px","top":"28","right":"24","bottom":"28","left":"24","isLinked":False},
                "flex_direction": "column"
            },
            "elements": [
                {
                    "id": f"{p}ae{i+20:02d}", "elType": "widget", "widgetType": "heading",
                    "settings": {
                        "title": c["icon"], "header_size": "p",
                        "typography_font_size": {"unit":"px","size":28},
                        "_margin": {"unit":"px","top":"0","right":"0","bottom":"14","left":"0","isLinked":False}
                    }
                },
                {
                    "id": f"{p}ae{i+30:02d}", "elType": "widget", "widgetType": "heading",
                    "settings": {
                        "title": c["title"], "header_size": "h3",
                        "typography_font_family": "Oswald", "typography_font_weight": "600",
                        "typography_font_size": {"unit":"px","size":16},
                        "typography_text_transform": "uppercase",
                        "title_color": "#2D2D2D",
                        "_margin": {"unit":"px","top":"0","right":"0","bottom":"8","left":"0","isLinked":False}
                    }
                },
                {
                    "id": f"{p}ae{i+40:02d}", "elType": "widget", "widgetType": "text-editor",
                    "settings": {"editor": f"<p style=\"font-size:14px;color:#6B7280;line-height:1.7;\">{c['desc']}</p>"}
                }
            ]
        })

    return {
        "id": f"{p}ae01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#F3F4F6",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ae02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": section_eyebrow, "header_size": "p", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                    "typography_font_size": {"unit":"px","size":12},
                    "typography_letter_spacing": {"unit":"px","size":3},
                    "typography_text_transform": "uppercase",
                    "title_color": "#B91C1C"
                }
            },
            {
                "id": f"{p}ae03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": section_heading, "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":38},
                    "typography_text_transform": "uppercase",
                    "title_color": "#2D2D2D"
                }
            },
            {
                "id": f"{p}ae04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}
            },
            {
                "id": f"{p}ae05", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "gap": {"unit":"px","size":28},
                    "_element_width": "initial"
                },
                "elements": card_els
            }
        ]
    }

def why_container(p):
    why_cards = [
        {"icon":"💰","title":"Honest Pricing","desc":"Upfront, transparent quotes before any work begins. No hidden fees, no surprises — even in emergencies."},
        {"icon":"⚡","title":"Fast Response","desc":"24/7 availability for emergencies. We arrive quickly and work efficiently to minimize damage."},
        {"icon":"🔧","title":"Quality Workmanship","desc":"Every job backed by our commitment to premium craftsmanship and lasting results."}
    ]
    card_els = []
    for i, c in enumerate(why_cards):
        card_els.append({
            "id": f"{p}af{i+10:02d}", "elType": "widget", "widgetType": "icon-box",
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
        "id": f"{p}af01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#1E3A6E",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}af02", "elType": "widget", "widgetType": "heading",
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
                "id": f"{p}af03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "Why Choose Regal?", "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":38},
                    "typography_text_transform": "uppercase",
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}af04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}
            },
            {
                "id": f"{p}af05", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "gap": {"unit":"px","size":32},
                    "_element_width": "initial"
                },
                "elements": card_els
            }
        ]
    }

def other_services_container(p, exclude_slug):
    all_services = [
        {"name":"Emergency Plumbing","slug":"emergency-plumbing"},
        {"name":"Drain Cleaning","slug":"drain-cleaning"},
        {"name":"Sewer Line Repair","slug":"sewer-line-repair"},
        {"name":"Water Heater Services","slug":"water-heater-services"},
        {"name":"Slab Leak Detection","slug":"slab-leak-detection"},
        {"name":"Hydrojetting","slug":"hydrojetting"},
        {"name":"Gas Leak Detection","slug":"gas-leak-detection"},
        {"name":"Water Filtration","slug":"water-filtration"},
    ]
    services = [s for s in all_services if s["slug"] != exclude_slug]
    btn_els = []
    for i, s in enumerate(services):
        btn_els.append({
            "id": f"{p}ag{i+10:02d}", "elType": "widget", "widgetType": "button",
            "settings": {
                "text": s["name"], "link": {"url": f"/{s['slug']}/"},
                "background_color": "#F3F4F6", "button_text_color": "#2D2D2D",
                "border_border": "solid", "border_width": {"unit":"px","top":1,"right":1,"bottom":1,"left":1,"isLinked":True},
                "border_color": "#E5E7EB",
                "typography_font_family": "Oswald", "typography_font_weight": "600",
                "typography_font_size": {"unit":"px","size":14},
                "border_radius": {"unit":"px","top":8,"right":8,"bottom":8,"left":8,"isLinked":True},
                "size": "lg"
            }
        })
    return {
        "id": f"{p}ag01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#FFFFFF",
            "padding": {"unit":"px","top":"80","right":"24","bottom":"80","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ag02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "Explore", "header_size": "p", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "500",
                    "typography_font_size": {"unit":"px","size":12},
                    "typography_letter_spacing": {"unit":"px","size":3},
                    "typography_text_transform": "uppercase",
                    "title_color": "#B91C1C"
                }
            },
            {
                "id": f"{p}ag03", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "Other Services We Offer", "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":38},
                    "typography_text_transform": "uppercase",
                    "title_color": "#2D2D2D"
                }
            },
            {
                "id": f"{p}ag04", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"#B91C1C","weight":{"unit":"px","size":4},"width":{"unit":"%","size":8},"align":"center"}
            },
            {
                "id": f"{p}ag05", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "flex_wrap": "wrap",
                    "gap": {"unit":"px","size":20}, "_element_width": "initial"
                },
                "elements": btn_els
            }
        ]
    }

def cta_container(p, heading, subtext):
    return {
        "id": f"{p}ah01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#B91C1C",
            "padding": {"unit":"px","top":"64","right":"24","bottom":"64","left":"24","isLinked":False},
            "text_align": "center"
        },
        "elements": [
            {
                "id": f"{p}ah02", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": heading, "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":42},
                    "typography_text_transform": "uppercase",
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}ah03", "elType": "widget", "widgetType": "text-editor",
                "settings": {"editor": f"<p style=\"text-align:center;font-size:16px;color:rgba(255,255,255,0.85);\">{subtext}</p>"}
            },
            {
                "id": f"{p}ah04", "elType": "widget", "widgetType": "heading",
                "settings": {
                    "title": "<a href=\"tel:9096004561\" style=\"color:#FFFFFF;\">(909) 600-4561</a>",
                    "header_size": "h2", "align": "center",
                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                    "typography_font_size": {"unit":"px","size":50},
                    "title_color": "#FFFFFF"
                }
            },
            {
                "id": f"{p}ah05", "elType": "widget", "widgetType": "button",
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
        "id": f"{p}ai01", "elType": "container",
        "settings": {
            "background_background": "classic", "background_color": "#2D2D2D",
            "padding": {"unit":"px","top":"64","right":"24","bottom":"24","left":"24","isLinked":False}
        },
        "elements": [
            {
                "id": f"{p}ai02", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row", "flex_wrap": "wrap",
                    "gap": {"unit":"px","size":48}, "_element_width": "initial"
                },
                "elements": [
                    {
                        "id": f"{p}ai03", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"25%"},
                        "elements": [
                            {
                                "id": f"{p}ai04", "elType": "widget", "widgetType": "heading",
                                "settings": {
                                    "title": "Regal Plumbing &amp; Rooter",
                                    "typography_font_family": "Oswald", "typography_font_weight": "700",
                                    "typography_font_size": {"unit":"px","size":18},
                                    "typography_text_transform": "uppercase",
                                    "title_color": "#FFFFFF"
                                }
                            },
                            {
                                "id": f"{p}ai05", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<p style=\"font-size:13px;color:#9CA3AF;line-height:1.6;\">Honest, professional plumbing &amp; rooter services for the Inland Empire &amp; San Gabriel Valley.</p>"}
                            },
                            {
                                "id": f"{p}ai06", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<p style=\"display:inline-block;background:rgba(185,28,28,0.2);border:1px solid rgba(185,28,28,0.4);color:#fca5a5;font-size:11.5px;font-family:Oswald,sans-serif;letter-spacing:1px;padding:4px 10px;border-radius:3px;\">CA License #1097482</p>"}
                            }
                        ]
                    },
                    {
                        "id": f"{p}ai07", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"15%"},
                        "elements": [
                            {
                                "id": f"{p}ai08", "elType": "widget", "widgetType": "heading",
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
                                "id": f"{p}ai09", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;\"><li><a href=\"/emergency-plumbing/\" style=\"font-size:13.5px;color:#9CA3AF;\">Emergency Plumbing</a></li><li><a href=\"/drain-cleaning/\" style=\"font-size:13.5px;color:#9CA3AF;\">Drain Cleaning</a></li><li><a href=\"/sewer-line-repair/\" style=\"font-size:13.5px;color:#9CA3AF;\">Sewer Line Repair</a></li><li><a href=\"/water-heater-services/\" style=\"font-size:13.5px;color:#9CA3AF;\">Water Heater Services</a></li><li><a href=\"/slab-leak-detection/\" style=\"font-size:13.5px;color:#9CA3AF;\">Slab Leak Detection</a></li><li><a href=\"/hydrojetting/\" style=\"font-size:13.5px;color:#9CA3AF;\">Hydrojetting</a></li><li><a href=\"/gas-leak-detection/\" style=\"font-size:13.5px;color:#9CA3AF;\">Gas Leak Detection</a></li><li><a href=\"/water-filtration/\" style=\"font-size:13.5px;color:#9CA3AF;\">Water Filtration</a></li></ul>"}
                            }
                        ]
                    },
                    {
                        "id": f"{p}ai10", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"15%"},
                        "elements": [
                            {
                                "id": f"{p}ai11", "elType": "widget", "widgetType": "heading",
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
                                "id": f"{p}ai12", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;\"><li><a href=\"/service-area/rancho-cucamonga-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Rancho Cucamonga</a></li><li><a href=\"/service-area/ontario-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Ontario</a></li><li><a href=\"/service-area/fontana-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Fontana</a></li><li><a href=\"/service-area/pomona-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Pomona</a></li><li><a href=\"/service-area/chino-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Chino</a></li><li><a href=\"/service-area/corona-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Corona</a></li><li><a href=\"/service-area/upland-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">Upland</a></li><li><a href=\"/service-area/west-covina-ca/\" style=\"font-size:13.5px;color:#9CA3AF;\">West Covina</a></li></ul>"}
                            }
                        ]
                    },
                    {
                        "id": f"{p}ai13", "elType": "container",
                        "settings": {"flex_direction":"column","_element_width":"20%"},
                        "elements": [
                            {
                                "id": f"{p}ai14", "elType": "widget", "widgetType": "heading",
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
                                "id": f"{p}ai15", "elType": "widget", "widgetType": "text-editor",
                                "settings": {"editor":"<ul style=\"list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:12px;\"><li style=\"font-size:13.5px;color:#9CA3AF;\">2141 E Philadelphia St, Suite R<br>Ontario, CA 91761</li><li><a href=\"tel:9096004561\" style=\"font-size:13.5px;color:#9CA3AF;\">(909) 600-4561</a></li><li><a href=\"mailto:info@regalplumbingservices.com\" style=\"font-size:13.5px;color:#9CA3AF;\">info@regalplumbingservices.com</a></li><li style=\"font-size:13.5px;color:#9CA3AF;\">24/7 Emergency | Mon\u2013Sat: 7am\u20137pm</li></ul>"}
                            }
                        ]
                    }
                ]
            },
            {
                "id": f"{p}ai16", "elType": "widget", "widgetType": "divider",
                "settings": {"color":"rgba(255,255,255,0.10)","weight":{"unit":"px","size":1},"width":{"unit":"%","size":100}}
            },
            {
                "id": f"{p}ai17", "elType": "container",
                "settings": {
                    "content_width": "full", "flex_direction": "row",
                    "flex_justify_content": "space-between", "flex_align_items": "center",
                    "padding": {"unit":"px","top":"18","right":"0","bottom":"18","left":"0","isLinked":False}
                },
                "elements": [
                    {
                        "id": f"{p}ai18", "elType": "widget", "widgetType": "text-editor",
                        "settings": {"editor":"<p style=\"font-size:12.5px;color:#6B7280;\">&copy; 2025 Regal Plumbing &amp; Rooter. All Rights Reserved. CA License #1097482</p>"}
                    },
                    {
                        "id": f"{p}ai19", "elType": "widget", "widgetType": "text-editor",
                        "settings": {"editor":"<p style=\"font-size:12.5px;color:#6B7280;\"><a href=\"/privacy-policy/\" style=\"color:#6B7280;\">Privacy Policy</a> &nbsp; <a href=\"/terms-of-service/\" style=\"color:#6B7280;\">Terms of Service</a></p>"}
                    }
                ]
            }
        ]
    }

service_pages = [
    {
        "file": "emergency-plumbing.json", "prefix": "ep",
        "title": "Emergency Plumbing Services",
        "seo_title": "Emergency Plumbing Services — Regal Plumbing & Rooter | (909) 600-4561",
        "seo_desc": "24/7 emergency plumbing for the Inland Empire. Burst pipes, sewage backups, major leaks — we respond fast. Call (909) 600-4561.",
        "hero_img": "pipe-repair-leak-detection-chino-hills-ca.webp", "hero_alt": "Emergency plumbing service",
        "badge": "24/7 Available", "h1": "Emergency Plumbing",
        "sub": "Rapid-response emergency plumbing for the Inland Empire — we're on call around the clock",
        "ov_eyebrow": "When Every Minute Counts", "ov_heading": "24/7 Emergency Plumbing Response",
        "ov_body": "When a plumbing emergency strikes — a burst pipe, major leak, or sewage backup — every minute matters. Regal Plumbing &amp; Rooter provides rapid-response emergency service around the clock, 365 days a year. We mobilize fast, arrive with the right equipment, and get the problem under control before it causes serious damage to your home or property.",
        "ov_features": ["Typically on-site within the hour","Burst pipe detection and emergency shutoff","Sewage backup and overflow response","Major leak control and repair","24/7 availability including holidays","Upfront pricing even in emergencies"],
        "ov_cta_text": "Call Now — (909) 600-4561", "ov_cta_url": "tel:9096004561",
        "ov_right_img": "sewer-repair-service-truck-inland-empire.webp", "ov_right_alt": "Emergency plumbing response",
        "cards_eyebrow": "What We Cover", "cards_heading": "Emergency Services We Provide",
        "cards": [
            {"icon":"💥","title":"Burst Pipes","desc":"Immediate shutoff and repair of burst or frozen pipes before water damage spreads to walls, floors, and structural elements."},
            {"icon":"🚿","title":"Sewage Backups","desc":"Emergency response to sewage backups and overflow situations that require immediate containment and clearance."},
            {"icon":"💧","title":"Major Leaks","desc":"Rapid detection and repair of active leaks — under sinks, behind walls, or at the main line — stopping damage fast."}
        ],
        "cta_heading": "Plumbing Emergency? Call Right Now",
        "cta_sub": "Our emergency team is standing by 24/7 — including weekends and holidays",
        "slug": "emergency-plumbing"
    },
    {
        "file": "drain-cleaning.json", "prefix": "dc",
        "title": "Drain Cleaning Services",
        "seo_title": "Drain Cleaning Services — Regal Plumbing & Rooter | Ontario, CA",
        "seo_desc": "Professional drain cleaning for kitchen, bathroom, and main sewer line blockages. Serving the Inland Empire. Call (909) 600-4561.",
        "hero_img": "drain-cleaning-shower-upland-ca.webp", "hero_alt": "Drain cleaning service",
        "badge": "Residential & Commercial", "h1": "Drain Cleaning",
        "sub": "Professional drain clearing for kitchen, bathroom, and main sewer line blockages throughout Southern California",
        "ov_eyebrow": "Restore Full Flow", "ov_heading": "Professional Drain Cleaning Service",
        "ov_body": "Slow or blocked drains are more than an inconvenience — they can signal deeper plumbing issues and lead to pipe damage or backups if left untreated. Regal Plumbing &amp; Rooter uses professional-grade equipment to clear everything from minor bathroom clogs to severe main line blockages, restoring full flow and preventing future buildup.",
        "ov_features": ["Kitchen drain and grease trap clearing","Bathroom sink, tub, and shower drain cleaning","Main sewer line snaking and clearing","Floor drain and utility sink service","Camera inspection to diagnose root causes","Preventative maintenance plans available"],
        "ov_cta_text": "Get a Free Quote", "ov_cta_url": "/contact/",
        "ov_right_img": "drain-cleaning-bathtub-rialto-ca.webp", "ov_right_alt": "Drain cleaning service",
        "cards_eyebrow": "What We Cover", "cards_heading": "Drain Types We Service",
        "cards": [
            {"icon":"🍳","title":"Kitchen Drains","desc":"Clear grease, food buildup, and soap scum that accumulates in kitchen sink drains. We also service garbage disposals and grease traps."},
            {"icon":"🛁","title":"Bathroom Drains","desc":"Remove hair, soap residue, and debris from tub, shower, and sink drains. Fast clearing with minimal disruption."},
            {"icon":"🔩","title":"Main Sewer Line","desc":"Professional snaking and clearing of main line blockages before they cause sewage backup. Camera inspection available to find root causes."}
        ],
        "cta_heading": "Ready for Clear Drains?",
        "cta_sub": "Call for a free quote — same-day service often available",
        "slug": "drain-cleaning"
    },
    {
        "file": "sewer-line-repair.json", "prefix": "sl",
        "title": "Sewer Line Repair",
        "seo_title": "Sewer Line Repair & Replacement — Regal Plumbing & Rooter | Ontario, CA",
        "seo_desc": "Expert sewer line camera inspection, trenchless repair, and full replacement in the Inland Empire. Call (909) 600-4561.",
        "hero_img": "sewer-line-repair-excavation-fontana-ca.webp", "hero_alt": "Sewer line repair service",
        "badge": "Camera Diagnosis", "h1": "Sewer Line Repair",
        "sub": "Expert sewer line inspection, repair, and trenchless replacement — accurate diagnosis before any work begins",
        "ov_eyebrow": "Accurate Diagnosis First", "ov_heading": "Sewer Line Repair & Replacement",
        "ov_body": "Sewer line problems can cause serious property damage and health hazards if left untreated. We use camera inspection technology to accurately locate and diagnose sewer line issues — root intrusion, cracks, bellied pipes, and more — then recommend the most cost-effective solution. Trenchless repair options are available when applicable to minimize disruption to your yard.",
        "ov_features": ["Video camera inspection and diagnosis","Trenchless pipe bursting and lining","Root intrusion clearing and prevention","Partial repair and full line replacement","Excavation work with proper permits","Post-repair pressure testing and verification"],
        "ov_cta_text": "Get a Free Quote", "ov_cta_url": "/contact/",
        "ov_right_img": "sewer-line-excavation-ontario-ca.webp", "ov_right_alt": "Sewer line excavation",
        "cards_eyebrow": "What We Cover", "cards_heading": "Sewer Line Solutions",
        "cards": [
            {"icon":"📷","title":"Camera Inspection","desc":"We run a video camera through your sewer line to see exactly what's causing the problem before recommending any repair — no guessing, no unnecessary work."},
            {"icon":"🌱","title":"Root Intrusion","desc":"Tree roots are the #1 cause of sewer line damage in Southern California. We remove roots and repair or line the affected section to prevent regrowth."},
            {"icon":"🔄","title":"Trenchless Options","desc":"Where conditions allow, we offer trenchless pipe bursting and CIPP lining — restoring your sewer line without digging up your entire yard."}
        ],
        "cta_heading": "Sewer Problems? Get a Camera Inspection",
        "cta_sub": "We diagnose before we repair — no surprise charges",
        "slug": "sewer-line-repair"
    },
    {
        "file": "water-heater-services.json", "prefix": "wh",
        "title": "Water Heater Services",
        "seo_title": "Water Heater Services — Installation & Repair | Regal Plumbing & Rooter",
        "seo_desc": "Tank, tankless, and heat pump water heater installation and repair in Ontario, CA and the Inland Empire. Call (909) 600-4561.",
        "hero_img": "sink-faucet-installation-ontario-ca.webp", "hero_alt": "Water heater services",
        "badge": "All Types & Brands", "h1": "Water Heater Services",
        "sub": "Installation and repair of tank, tankless, and heat pump water heaters — all major brands serviced",
        "ov_eyebrow": "Hot Water Experts", "ov_heading": "Water Heater Install & Repair",
        "ov_body": "No hot water is never convenient. Regal Plumbing &amp; Rooter installs and repairs all types of water heaters — traditional tank units, tankless (on-demand) systems, and hybrid heat pump models. Whether your current unit needs a repair or it's time for an upgrade, our licensed technicians will assess your needs and provide the right solution for your home and budget.",
        "ov_features": ["Traditional tank water heater installation and repair","Tankless (on-demand) water heater installation","Hybrid heat pump water heater systems","All major brands serviced","Anode rod replacement and tank flushing","Emergency water heater service available"],
        "ov_cta_text": "Get a Free Quote", "ov_cta_url": "/contact/",
        "ov_right_img": "copper-pipe-installation-chino-ca.webp", "ov_right_alt": "Water heater installation",
        "cards_eyebrow": "What We Cover", "cards_heading": "Water Heater Types We Service",
        "cards": [
            {"icon":"🪣","title":"Tank Water Heaters","desc":"Service, repair, and replacement of traditional 30-80 gallon tank water heaters. We carry units from all major brands and can install same-day in most cases."},
            {"icon":"⚡","title":"Tankless Systems","desc":"Install or repair tankless water heaters that provide on-demand hot water and last significantly longer than tank units. Ideal for efficiency-focused homeowners."},
            {"icon":"🔧","title":"Repairs & Tune-Ups","desc":"Diagnose and fix water heater issues including pilot light failures, anode rod corrosion, sediment buildup, thermostat problems, and pressure relief valve issues."}
        ],
        "cta_heading": "No Hot Water? We Can Help Today",
        "cta_sub": "Same-day service often available — call for availability",
        "slug": "water-heater-services"
    },
    {
        "file": "slab-leak-detection.json", "prefix": "sd",
        "title": "Slab Leak Detection",
        "seo_title": "Slab Leak Detection & Repair — Regal Plumbing & Rooter | Ontario, CA",
        "seo_desc": "Electronic slab leak detection and repair in Ontario, CA. Precise leak location with minimal excavation. Call (909) 600-4561.",
        "hero_img": "leak-repair-wall-open-ontario-ca.webp", "hero_alt": "Slab leak detection",
        "badge": "Non-Invasive Technology", "h1": "Slab Leak Detection",
        "sub": "Precise electronic leak location beneath your concrete slab — we find it before we dig",
        "ov_eyebrow": "Find It. Fix It Right.", "ov_heading": "Slab Leak Detection & Repair",
        "ov_body": "A slab leak — a water line leak beneath your concrete foundation — is one of the most serious plumbing problems a homeowner can face. Left untreated, it can damage your foundation, cause mold growth, and lead to significant structural issues. Regal Plumbing &amp; Rooter uses electronic detection equipment to precisely locate slab leaks without unnecessary excavation, minimizing disruption and repair costs.",
        "ov_features": ["Electronic acoustic leak detection","Thermal imaging available","Spot repair with minimal concrete cutting","Pipe re-routing to avoid damaged section","Epoxy pipe lining (trenchless option)","Post-repair pressure testing"],
        "ov_cta_text": "Get a Free Quote", "ov_cta_url": "/contact/",
        "ov_right_img": "pipe-repair-leak-detection-chino-hills-ca.webp", "ov_right_alt": "Slab leak detection equipment",
        "cards_eyebrow": "What We Cover", "cards_heading": "Slab Leak Solutions",
        "cards": [
            {"icon":"🔍","title":"Electronic Detection","desc":"We use acoustic and electronic equipment to precisely locate the leak beneath your slab — not a general area, but the exact spot — before any concrete is cut."},
            {"icon":"🏠","title":"Spot Repair","desc":"Once located, we make a targeted, minimal-disruption repair — cutting only what's necessary to access and fix the leak, then properly restoring the concrete."},
            {"icon":"🔄","title":"Re-Routing & Lining","desc":"When a pipe section is too damaged for spot repair, we offer re-routing (running a new line through the attic or walls) or epoxy lining as non-invasive alternatives."}
        ],
        "cta_heading": "Suspect a Slab Leak? Act Fast",
        "cta_sub": "Signs include warm floors, high water bills, or the sound of running water with everything off",
        "slug": "slab-leak-detection"
    },
    {
        "file": "hydrojetting.json", "prefix": "hj",
        "title": "Hydrojetting",
        "seo_title": "Hydrojetting Service — Regal Plumbing & Rooter | Ontario & Inland Empire",
        "seo_desc": "High-pressure hydrojetting to scour pipes clean of grease, scale, and root intrusion. Serving the Inland Empire. Call (909) 600-4561.",
        "hero_img": "hydro-jetting-roof-rancho-cucamonga-ca.webp", "hero_alt": "Hydrojetting service",
        "badge": "High-Pressure Cleaning", "h1": "Hydrojetting",
        "sub": "Up to 4,000 PSI water jetting scours pipe walls clean — eliminating what snaking can't remove",
        "ov_eyebrow": "When Snaking Isn't Enough", "ov_heading": "Professional Hydrojetting Service",
        "ov_body": "Drain snaking breaks through clogs, but hydrojetting eliminates them — and the buildup on the pipe walls that caused them. Using water pressure up to 4,000 PSI, our hydrojetting service scours drain and sewer lines completely clean, removing grease accumulation, mineral scale, hardened debris, and even root intrusion. It's the most thorough drain cleaning method available, and ideal for commercial properties or homes with recurring blockages.",
        "ov_features": ["Removes grease, scale, and mineral buildup","Clears root intrusion from pipe walls","Restores full pipe capacity and flow","Extends the life of your plumbing system","Ideal for commercial kitchens and restaurants","Pre-jetting camera inspection recommended"],
        "ov_cta_text": "Get a Free Quote", "ov_cta_url": "/contact/",
        "ov_right_img": "camera-inspection-drain-cleaning-san-bernardino-ca.webp", "ov_right_alt": "Hydrojetting equipment",
        "cards_eyebrow": "What We Cover", "cards_heading": "Hydrojetting Applications",
        "cards": [
            {"icon":"💨","title":"Grease & Scale","desc":"Grease buildup in commercial kitchens and mineral scale in hard-water areas can reduce pipe diameter dramatically. Hydrojetting removes it completely, restoring full flow."},
            {"icon":"🌿","title":"Root Intrusion","desc":"Tree roots that have penetrated pipe walls can be blasted out with hydrojetting — often avoiding the need for more invasive repairs."},
            {"icon":"🏢","title":"Commercial Use","desc":"Restaurants, food service, and commercial properties benefit most from regular hydrojetting maintenance to keep drains clear and meet health code requirements."}
        ],
        "cta_heading": "Clear Pipes. Better Flow. Call Today",
        "cta_sub": "Hydrojetting is available for both residential and commercial properties",
        "slug": "hydrojetting"
    },
    {
        "file": "gas-leak-detection.json", "prefix": "gl",
        "title": "Gas Leak Detection",
        "seo_title": "Gas Leak Detection & Repair — Regal Plumbing & Rooter | Ontario, CA",
        "seo_desc": "Licensed gas leak detection and repair in Ontario, CA. If you smell gas, leave and call 911 first. Then call (909) 600-4561.",
        "hero_img": "camera-inspection-drain-cleaning-san-bernardino-ca.webp", "hero_alt": "Gas leak detection",
        "badge": "Safety Critical", "h1": "Gas Leak Detection",
        "sub": "Licensed gas line detection and repair — if you smell gas, leave the building and call 911 first",
        "ov_eyebrow": "Safety First", "ov_heading": "Gas Leak Detection & Repair",
        "ov_body": "A gas leak is a life-safety emergency. If you smell gas, leave the building immediately and call 911 before anything else. Once the property is safe, call Regal Plumbing &amp; Rooter. Our licensed technicians use professional gas detection equipment to locate leaks precisely, make code-compliant repairs, and perform pressure testing to verify the system is fully sealed before restoring service.",
        "ov_features": ["Electronic gas detection equipment","Natural gas and propane line service","Gas line repair and re-piping","Pressure testing after every repair","Code-compliant work — permits pulled when required","Licensed for residential and commercial gas systems"],
        "ov_cta_text": "Call Now — (909) 600-4561", "ov_cta_url": "tel:9096004561",
        "ov_right_img": "pipe-replacement-copper-ontario-ca.webp", "ov_right_alt": "Gas line repair",
        "cards_eyebrow": "What We Cover", "cards_heading": "Gas Line Services",
        "cards": [
            {"icon":"🔬","title":"Leak Location","desc":"We use electronic combustible gas detectors to locate the exact source of a leak — not a general area — before any repair work begins."},
            {"icon":"🔧","title":"Line Repair & Repiping","desc":"Repair of cracked, corroded, or damaged gas lines. When a section is compromised, we can repipe the affected run with new materials to code."},
            {"icon":"✅","title":"Pressure Testing","desc":"After every repair, we perform a full pressure test of the gas system to confirm it holds and is completely sealed before turning service back on."}
        ],
        "cta_heading": "Gas Leak? Safety First. Then Call Us",
        "cta_sub": "Leave the building, call 911, then call us at (909) 600-4561",
        "slug": "gas-leak-detection"
    },
    {
        "file": "water-filtration.json", "prefix": "wf",
        "title": "Water Filtration & Softeners",
        "seo_title": "Water Filtration & Softener Installation — Regal Plumbing & Rooter | Ontario, CA",
        "seo_desc": "Whole-home water softeners, reverse osmosis, and filtration systems for Southern California's hard water. Call (909) 600-4561.",
        "hero_img": "pipe-replacement-copper-ontario-ca.webp", "hero_alt": "Water filtration systems",
        "badge": "Cleaner, Softer Water", "h1": "Water Filtration &amp; Softeners",
        "sub": "Whole-home water softeners, reverse osmosis systems, and filtration for Southern California's hard water",
        "ov_eyebrow": "Better Water for Your Home", "ov_heading": "Water Filtration & Softener Installation",
        "ov_body": "Southern California water is notoriously hard — high in calcium and magnesium that causes scale buildup in pipes, damages appliances, leaves residue on fixtures, and affects the taste of your drinking water. Regal Plumbing &amp; Rooter installs whole-home water softeners, reverse osmosis drinking water systems, and whole-house carbon filtration to give your household the clean, soft water it deserves.",
        "ov_features": ["Whole-home water softener installation","Under-sink reverse osmosis (RO) systems","Whole-house carbon and sediment filtration","UV purification for bacteria and viruses","Filter cartridge replacement service","Water quality testing available"],
        "ov_cta_text": "Get a Free Quote", "ov_cta_url": "/contact/",
        "ov_right_img": "copper-pipe-installation-chino-ca.webp", "ov_right_alt": "Water filtration installation",
        "cards_eyebrow": "What We Cover", "cards_heading": "Water Treatment Systems",
        "cards": [
            {"icon":"💎","title":"Water Softeners","desc":"Whole-home salt-based and salt-free water softeners that remove hardness minerals, protect your pipes and appliances, and eliminate scale buildup throughout your home."},
            {"icon":"🚰","title":"Reverse Osmosis","desc":"Under-sink RO systems that remove up to 99% of contaminants from your drinking water — including lead, chlorine, fluoride, and dissolved solids."},
            {"icon":"🌊","title":"Whole-Home Filtration","desc":"Carbon and sediment filtration systems that treat all the water entering your home, protecting every faucet, shower, and appliance from chlorine and particulates."}
        ],
        "cta_heading": "Better Water Starts with One Call",
        "cta_sub": "Free consultation — we'll recommend the right system for your home and budget",
        "slug": "water-filtration"
    }
]

for sp in service_pages:
    p = sp["prefix"]
    doc = {
        "version": "0.4",
        "title": sp["title"],
        "type": "page",
        "page_settings": {
            "seo_title": sp["seo_title"],
            "seo_description": sp["seo_desc"]
        },
        "content": [
            emerg_bar(p),
            header_container(p),
            hero_container(p, sp["hero_img"], sp["hero_alt"], sp["badge"], sp["h1"], sp["sub"]),
            overview_container(p, sp["ov_eyebrow"], sp["ov_heading"], sp["ov_body"],
                               sp["ov_features"], sp["ov_cta_text"], sp["ov_cta_url"],
                               sp["ov_right_img"], sp["ov_right_alt"]),
            cards_container(p, sp["cards_eyebrow"], sp["cards_heading"], sp["cards"]),
            why_container(p),
            other_services_container(p, sp["slug"]),
            cta_container(p, sp["cta_heading"], sp["cta_sub"]),
            footer_container(p)
        ]
    }
    out_path = os.path.join(base_dir, sp["file"])
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"Written: {sp['file']}")

print("All 8 service pages done.")
