# Regal Plumbing & Rooter — Master Project Context

## PRIME DIRECTIVES
1. Always use the FASTEST approach possible
2. Always read this entire file before writing any code
3. Always read all existing project files before starting any task
4. Never repeat work that has already been done
5. Always use TypeScript
6. Always use native Next.js patterns — no shortcuts
7. Every decision must prioritize SEO, map pack rankings, and phone call conversions
8. Never suggest a slow method when a fast one exists

---

## Business Details
- **Company:** Regal Plumbing & Rooter
- **Phone:** (909) 600-4561 — always link as tel:9096004561
- **Address:** 2141 E Philadelphia St, Suite R, Ontario, CA 91761
- **Email:** info@regalplumbingservices.com
- **CA License:** #1097482
- **Type:** Family-owned, 24/7 emergency service
- **Founded:** ~4 years ago
- **Tagline:** Honest, professional plumbing & rooter services
- **Live site:** https://regalplumbingservices.com
- **GitHub repo:** https://github.com/JessicaP2026/regal-plumbing-website
- **Vercel project:** regal-website.vercel.app

---

## Brand Colors
| Variable | Hex | Usage |
|----------|-----|-------|
| red | #B91C1C | CTAs, buttons, highlights |
| red-dark | #991B1B | Button hover states |
| navy | #1E3A6E | Hero backgrounds, accents |
| dark-grey | #2D2D2D | Emergency bar, footer, dark sections |
| light-grey | #F3F4F6 | Alternate section backgrounds |
| white | #FFFFFF | Base background |
| red-light | #fca5a5 | Phone links on dark backgrounds |

## Typography
- **Headlines:** Oswald — weights 400, 500, 600, 700
- **Body:** Open Sans — weights 400, 500, 600
- **Both loaded via next/font/google — never use @import or link tags**

---

## Tech Stack
- **Framework:** Next.js 14 with App Router
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Fonts:** next/font/google
- **Images:** next/image
- **Forms:** React Hook Form
- **Email:** Resend
- **Animations:** Framer Motion
- **Analytics:** Google Analytics 4 (to be added)
- **Hosting:** Vercel
- **Branch:** nextjs (never touch main branch)
- **Next.js app location:** nextjs-site/ folder

---

## Services (8 total)
1. Emergency Plumbing — /emergency-plumbing/
2. Drain Cleaning — /drain-cleaning/
3. Sewer Line Repair — /sewer-line-repair/
4. Water Heater Installation & Repair — /water-heater-services/
5. Slab Leak Detection & Repair — /slab-leak-detection/
6. Hydrojetting — /hydrojetting/
7. Gas Leak Detection — /gas-leak-detection/
8. Water Filtration & Softener Systems — /water-filtration/

---

## Service Area
### Primary 8 Cities (footer + nav)
1. Ontario, CA — /service-area/ontario-ca/ (HEADQUARTERS)
2. Rancho Cucamonga, CA — /service-area/rancho-cucamonga-ca/
3. Fontana, CA — /service-area/fontana-ca/
4. Pomona, CA — /service-area/pomona-ca/
5. Chino, CA — /service-area/chino-ca/
6. Corona, CA — /service-area/corona-ca/
7. Upland, CA — /service-area/upland-ca/
8. West Covina, CA — /service-area/west-covina-ca/

### Full 32 City Coverage
Azusa, Bloomington, Brea, Charter Oak, Chino, Chino Hills, Citrus, Claremont,
Colton, Corona, Covina, Diamond Bar, Eastvale, Fontana, Glendora, Highgrove,
Jurupa Valley, La Verne, Loma Linda, Mira Loma, Montclair, Muscoy, Norco,
Ontario, Pomona, Rancho Cucamonga, Rowland Heights, San Dimas, Upland,
Walnut, West Covina, Yorba Linda

---

## Project File Structure
```
regal-plumbing-website/
├── claude.md                      # This file — read first always
├── preview/                       # HTML prototype — source of truth for design
├── images/                        # All 20 website images (.webp)
├── docs/                          # Design spec documents
├── wp-content/                    # WordPress child theme (separate project)
└── nextjs-site/                   # NEXT.JS APP — build everything here
    ├── app/
    │   ├── layout.tsx
    │   ├── page.tsx
    │   ├── not-found.tsx
    │   ├── about/page.tsx
    │   ├── contact/page.tsx
    │   ├── services/page.tsx
    │   ├── service-area/page.tsx
    │   ├── emergency-plumbing/page.tsx
    │   ├── drain-cleaning/page.tsx
    │   ├── sewer-line-repair/page.tsx
    │   ├── water-heater-services/page.tsx
    │   ├── slab-leak-detection/page.tsx
    │   ├── hydrojetting/page.tsx
    │   ├── gas-leak-detection/page.tsx
    │   ├── water-filtration/page.tsx
    │   ├── service-area/ontario-ca/page.tsx
    │   ├── service-area/rancho-cucamonga-ca/page.tsx
    │   ├── service-area/fontana-ca/page.tsx
    │   ├── service-area/pomona-ca/page.tsx
    │   ├── service-area/chino-ca/page.tsx
    │   ├── service-area/corona-ca/page.tsx
    │   ├── service-area/upland-ca/page.tsx
    │   ├── service-area/west-covina-ca/page.tsx
    │   ├── privacy-policy/page.tsx
    │   ├── terms-of-service/page.tsx
    │   ├── thank-you/page.tsx
    │   └── api/contact/route.ts
    ├── components/
    │   ├── EmergencyBar.tsx
    │   ├── Header.tsx
    │   ├── Footer.tsx
    │   ├── MobileStickyCTA.tsx
    │   ├── EmergencyCTABanner.tsx
    │   ├── HeroSection.tsx
    │   ├── TrustBar.tsx
    │   ├── ServiceCard.tsx
    │   ├── StatCounter.tsx
    │   ├── FAQAccordion.tsx
    │   ├── ReviewCard.tsx
    │   ├── BreadCrumb.tsx
    │   ├── SchemaMarkup.tsx
    │   └── ContactForm.tsx
    ├── lib/
    │   ├── schema.ts
    │   ├── metadata.ts
    │   └── constants.ts
    ├── public/images/
    ├── next.config.ts
    ├── tailwind.config.ts
    └── tsconfig.json
```

---

## Image Library
All images in /images/ — copy to nextjs-site/public/images/
Always use next/image — never img tags

| Filename | Usage | Alt Text |
|----------|-------|----------|
| regal-plumbing-logo.png | Logo | Regal Plumbing and Rooter logo |
| sewer-repair-service-truck-inland-empire.webp | Emergency/Hero | Emergency plumber service truck Inland Empire CA |
| drain-cleaning-shower-upland-ca.webp | Drain Cleaning | Drain cleaning shower service Upland CA |
| drain-cleaning-bathtub-rialto-ca.webp | Drain Cleaning alt | Drain cleaning bathtub service Rialto CA |
| sewer-line-excavation-ontario-ca.webp | Sewer Line | Sewer line excavation repair Ontario CA |
| sewer-line-repair-excavation-fontana-ca.webp | Sewer Line alt | Sewer line repair excavation Fontana CA |
| sink-faucet-installation-ontario-ca.webp | Water Heater | Sink faucet installation Ontario CA |
| pipe-repair-leak-detection-chino-hills-ca.webp | Slab Leak | Pipe repair leak detection Chino Hills CA |
| leak-repair-wall-open-ontario-ca.webp | Slab Leak alt | Leak repair wall open Ontario CA |
| hydro-jetting-roof-rancho-cucamonga-ca.webp | Hydrojetting | Hydrojetting drain cleaning Rancho Cucamonga CA |
| camera-inspection-drain-cleaning-san-bernardino-ca.webp | Gas Leak | Camera inspection drain cleaning San Bernardino CA |
| copper-pipe-installation-chino-ca.webp | Water Filtration | Copper pipe installation Chino CA |
| pipe-replacement-copper-ontario-ca.webp | Pipe replacement | Copper pipe replacement Ontario CA |
| regal-plumbing-rooter-office-ontario-ca.webp | About/Office | Regal Plumbing Rooter office Ontario CA |
| regal-plumbing-office-natalie-ontario-ca.webp | About/Team | Regal Plumbing office team member Ontario CA |
| regal-plumber-ashton-ontario-ca.webp | Team | Licensed plumber Ashton Regal Plumbing Ontario CA |
| regal-plumber-brayden-ontario-ca.webp | Team | Licensed plumber Brayden Regal Plumbing Ontario CA |
| regal-plumber-nick-ontario-ca.webp | Team | Licensed plumber Nick Regal Plumbing Ontario CA |
| regal-plumber-tony-ontario-ca.webp | Team | Licensed plumber Tony Regal Plumbing Ontario CA |

## Hero Image Assignments
| Page | Hero Image |
|------|-----------|
| Homepage | sewer-repair-service-truck-inland-empire.webp |
| About | regal-plumbing-rooter-office-ontario-ca.webp |
| Services | camera-inspection-drain-cleaning-san-bernardino-ca.webp |
| Service Area | sewer-repair-service-truck-inland-empire.webp |
| Contact | regal-plumbing-office-natalie-ontario-ca.webp |
| Emergency Plumbing | sewer-repair-service-truck-inland-empire.webp |
| Drain Cleaning | drain-cleaning-shower-upland-ca.webp |
| Sewer Line Repair | sewer-line-excavation-ontario-ca.webp |
| Water Heater Services | sink-faucet-installation-ontario-ca.webp |
| Slab Leak Detection | pipe-repair-leak-detection-chino-hills-ca.webp |
| Hydrojetting | hydro-jetting-roof-rancho-cucamonga-ca.webp |
| Gas Leak Detection | camera-inspection-drain-cleaning-san-bernardino-ca.webp |
| Water Filtration | copper-pipe-installation-chino-ca.webp |
| Ontario | sewer-repair-service-truck-inland-empire.webp |
| Rancho Cucamonga | hydro-jetting-roof-rancho-cucamonga-ca.webp |
| Fontana | sewer-line-repair-excavation-fontana-ca.webp |
| Pomona | sewer-repair-service-truck-inland-empire.webp |
| Chino | copper-pipe-installation-chino-ca.webp |
| Corona | sewer-repair-service-truck-inland-empire.webp |
| Upland | drain-cleaning-shower-upland-ca.webp |
| West Covina | sewer-repair-service-truck-inland-empire.webp |

---

## SEO Strategy

### Primary Keywords
- plumber Ontario CA
- emergency plumber Inland Empire
- drain cleaning Ontario CA
- slab leak detection Inland Empire
- water heater repair Ontario CA
- plumber Rancho Cucamonga CA
- plumber Fontana CA
- 24/7 emergency plumber Southern California
- licensed plumber Inland Empire
- family owned plumber Ontario CA

### Meta Title Format
[Primary Keyword] — [Secondary Info] | Regal Plumbing & Rooter

### Meta Description Format
[Action phrase] in [City] CA? [Company] offers [services]. Licensed, local, 24/7. Call (909) 600-4561.
Keep under 160 characters always.

### Page SEO Targets
| Page | H1 | Primary Keyword |
|------|----|----------------|
| Homepage | Your Trusted Local Plumbers — Available 24/7 | plumber Inland Empire CA |
| Emergency | 24/7 Emergency Plumber — Inland Empire | emergency plumber Inland Empire |
| Drain Cleaning | Professional Drain Cleaning — Inland Empire CA | drain cleaning Inland Empire |
| Sewer Line | Sewer Line Repair & Replacement | sewer line repair Ontario CA |
| Water Heater | Water Heater Installation & Repair | water heater repair Inland Empire |
| Slab Leak | Slab Leak Detection & Repair | slab leak detection Inland Empire |
| Hydrojetting | Hydrojetting Service — Inland Empire CA | hydrojetting service Inland Empire |
| Gas Leak | Gas Leak Detection & Repair | gas leak detection Inland Empire |
| Water Filtration | Water Filtration & Softener Systems | water filtration Inland Empire |
| Ontario | Plumber in Ontario, CA | plumber Ontario CA |
| Rancho Cucamonga | Plumber in Rancho Cucamonga, CA | plumber Rancho Cucamonga CA |
| Fontana | Plumber in Fontana, CA | plumber Fontana CA |
| Pomona | Plumber in Pomona, CA | plumber Pomona CA |
| Chino | Plumber in Chino, CA | plumber Chino CA |
| Corona | Plumber in Corona, CA | plumber Corona CA |
| Upland | Plumber in Upland, CA | plumber Upland CA |
| West Covina | Plumber in West Covina, CA | plumber West Covina CA |

---

## Schema Markup (CRITICAL FOR MAP PACK)

### Every Page — LocalBusiness + Plumber Schema
```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "Plumber"],
  "name": "Regal Plumbing & Rooter",
  "image": "https://regalplumbingservices.com/images/regal-plumbing-logo.png",
  "logo": "https://regalplumbingservices.com/images/regal-plumbing-logo.png",
  "telephone": "(909) 600-4561",
  "email": "info@regalplumbingservices.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2141 E Philadelphia St, Suite R",
    "addressLocality": "Ontario",
    "addressRegion": "CA",
    "postalCode": "91761",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 34.0633,
    "longitude": -117.6508
  },
  "url": "https://regalplumbingservices.com",
  "priceRange": "$$",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  },
  "areaServed": [
    {"@type": "City", "name": "Ontario", "addressRegion": "CA"},
    {"@type": "City", "name": "Rancho Cucamonga", "addressRegion": "CA"},
    {"@type": "City", "name": "Fontana", "addressRegion": "CA"},
    {"@type": "City", "name": "Pomona", "addressRegion": "CA"},
    {"@type": "City", "name": "Chino", "addressRegion": "CA"},
    {"@type": "City", "name": "Corona", "addressRegion": "CA"},
    {"@type": "City", "name": "Upland", "addressRegion": "CA"},
    {"@type": "City", "name": "West Covina", "addressRegion": "CA"}
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Plumbing Services",
    "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Emergency Plumbing"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Drain Cleaning"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Sewer Line Repair"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Water Heater Installation & Repair"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Slab Leak Detection & Repair"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Hydrojetting"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Gas Leak Detection"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Water Filtration & Softeners"}}
    ]
  },
  "sameAs": [
    "https://www.facebook.com/regalplumbing",
    "https://www.instagram.com/regalplumbing"
  ]
}
```

---

## NAP Consistency (CRITICAL)
Use EXACTLY this format everywhere:
- **Name:** Regal Plumbing & Rooter
- **Address:** 2141 E Philadelphia St, Suite R, Ontario, CA 91761
- **Phone:** (909) 600-4561

---

## Google Business Profile
- Status: Active
- Category: Plumber
- Location: Ontario, CA
- Google Maps embed on contact and all city pages
- Maps coordinates: lat 34.0633, lng -117.6508

---

## Social Media
- Facebook: linked in footer and schema
- Instagram: linked in footer and schema
- Both in OpenGraph metadata

---

## Analytics & Tracking
- Google Analytics 4: add placeholder with env var NEXT_PUBLIC_GA_ID
- Vercel Analytics: add @vercel/analytics
- Track form submissions and phone clicks as GA4 events

---

## Contact Form
- Fields: Full Name, Phone (required), Email, City (32 cities), Service (8 services), Message
- Submit to: info@regalplumbingservices.com via Resend
- Success: Redirect to /thank-you/
- Spam protection: Honeypot field + rate limiting
- Auto-reply confirmation email to customer

---

## Performance Targets
- Lighthouse: 95+ all metrics
- LCP: Under 2.5 seconds
- All pages statically generated
- Images via next/image
- Fonts via next/font — zero layout shift

---

## Internal Linking Rules
Always use Next.js Link component — never anchor tags for internal links

---

## Environment Variables
```
RESEND_API_KEY=
NEXT_PUBLIC_GA_ID=
NEXT_PUBLIC_SITE_URL=https://regalplumbingservices.com
```

---

## Git Workflow
```bash
git pull
git checkout nextjs
git add .
git commit -m "description"
git push
```
NEVER push to main without partner approval

---

## Partner Info
- Partner: Jessica (JessicaP2026 on GitHub)
- She built the HTML prototype in preview/ folder
- Always git pull before starting work
- Always commit and push after completing work

---

## Competitor Reference
- rooterhero.com
- allcity4uplumbing.com

---

## Completed
- HTML prototype for all 25 pages
- All 20 images in images/ folder
- Design spec in docs/ folder
- GitHub repo with nextjs branch
- Vercel project connected

## Still To Do
- Build Next.js app in nextjs-site/
- Set up Resend API key
- Set up Google Analytics 4
- Connect domain to Vercel
- Set up Google Search Console
- Submit sitemap to Google
- Optimize Google Business Profile
- Build blog section
- Set up local citations

## Post Launch SEO Checklist
- [ ] Google Business Profile fully filled out
- [ ] Add photos to Google Business Profile
- [ ] Get 10+ Google reviews
- [ ] List on Yelp, BBB, Angi, HomeAdvisor, Thumbtack
- [ ] NAP consistent on all listings
- [ ] Submit sitemap to Google Search Console
- [ ] Build citations on local directories
- [ ] Create service area posts on Google Business Profile
