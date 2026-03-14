# Regal Plumbing & Rooter Website Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a conversion-focused, SEO-dominant 5-page WordPress + Elementor Pro website for Regal Plumbing & Rooter at regalplumbingservices.com.

**Architecture:** Hello Elementor child theme provides the base; all page layouts are built with Elementor Pro widgets and templates. Global design tokens (colors, fonts) are set in Elementor's Site Settings so every page inherits them automatically. A single Elementor Header template and Footer template are applied globally, keeping layout consistent and DRY.

**Tech Stack:** WordPress 6.x, Elementor Pro, Hello Elementor (parent theme), RankMath SEO, WPForms Pro (dynamic population is a native Pro feature — no add-on required), WP Mail SMTP, WP Rocket, Google Site Kit (GA4), Wordfence, UpdraftPlus, Widgets for Google Reviews

**Spec:** `docs/superpowers/specs/2026-03-13-regal-plumbing-website-design.md`

---

## File Structure

```
wp-content/
  themes/
    hello-elementor/                  ← Parent theme (do not modify)
    regal-plumbing-child/             ← All custom code lives here
      style.css                       ← Theme declaration + typography overrides
      functions.php                   ← Enqueue child styles, register Google Fonts
      assets/
        css/
          custom.css                  ← Mobile sticky CTA bar, utility overrides
        js/
          custom.js                   ← Mobile sticky bar show/hide on scroll
        images/
          logo.png                    ← Client logo (transparent background)
          [hero-*.jpg]                ← Client-provided hero photos
```

Elementor templates and page content are stored in the WordPress database. Export JSON backups after completing each page:
```
docs/elementor-exports/
  global-settings.json
  header-template.json
  footer-template.json
  page-home.json
  page-services.json
  page-about.json
  page-contact.json
  page-service-area.json
  page-thank-you.json
```

---

## Chunk 1: Foundation — WordPress, Plugins, Child Theme, Global Styles

### Task 1: Install WordPress

- [ ] **Step 1: Install WordPress**

  Install WordPress on your hosting environment (cPanel, WP Engine, Kinsta, etc.) via one-click installer or manual upload.

  Verify: WordPress admin accessible at `yourdomain.com/wp-admin`

- [ ] **Step 2: Verify SSL and set HTTPS URLs**

  Before any other settings: confirm your hosting has an active SSL certificate. Then:
  - WP Admin → Settings → General
  - Set both **WordPress Address (URL)** and **Site Address (URL)** to `https://regalplumbingservices.com`
  - Confirm the site loads on HTTPS with a valid padlock icon
  - In your hosting control panel or `.htaccess`, ensure HTTP → HTTPS redirects are active

- [ ] **Step 3: Configure basic WordPress settings**

  In WP Admin → Settings:
  - **General:** Site Title = `Regal Plumbing & Rooter`, Tagline = `Licensed Plumbers — Available 24/7`
  - **Permalinks:** Set to `Post name` (`/%postname%/`)
  - **Reading:** Set a static front page (create a blank page called "Home" first, assign it)
  - **Discussion:** Disable comments site-wide (uncheck "Allow people to post comments on new articles")

- [ ] **Step 4: Delete default content**

  Delete default posts, pages (except the "Home" page you just created), and comments. Delete the "Hello World" post. Delete "Sample Page".

- [ ] **Step 4: Set favicon**

  WP Admin → Appearance → Customize → Site Identity → Site Icon:
  - Upload the Regal Plumbing logo (square crop, minimum 512×512px)
  - This sets the browser tab favicon and mobile homescreen icon

- [ ] **Step 5: Create `.gitignore` for WordPress**

  In the site root, create a `.gitignore` file to exclude WordPress core from version control (track only your custom code):

  ```gitignore
  # WordPress core — managed by hosting/updates, not git
  /wp-admin/
  /wp-includes/
  /wp-*.php
  /index.php
  /xmlrpc.php
  /license.txt
  /readme.html

  # Uploads (large files, managed separately)
  /wp-content/uploads/

  # Track only our custom code
  !/wp-content/themes/regal-plumbing-child/
  !/wp-content/plugins/
  ```

- [ ] **Step 6: Commit**

  ```bash
  git add .gitignore
  git commit -m "chore: fresh WordPress install, basic settings, gitignore configured"
  ```

---

### Task 2: Install and Activate Required Plugins

- [ ] **Step 1: Install plugins**

  **Step 1a: Install Hello Elementor parent theme first**

  WP Admin → Appearance → Themes → Add New → search "Hello Elementor" → Install → Do NOT activate yet (the child theme created in Task 3 will be activated instead).

  **Step 1b: Install plugins via WP Admin → Plugins → Add New:**

  | Plugin | Notes |
  |--------|-------|
  | Elementor Pro | Upload the Pro zip file via Plugins → Add New → Upload |
  | RankMath SEO | Free version from plugin directory |
  | WPForms Pro | **Pro version required** for URL parameter dynamic population (the `?service=` pre-fill feature). Purchase at wpforms.com. The free Lite version does not support this feature. |
  | WP Mail SMTP | Free version |
  | WP Rocket | Upload the purchased zip |
  | Wordfence Security | Free version |
  | UpdraftPlus | Free version |
  | Widgets for Google Reviews | Search plugin directory |

- [ ] **Step 2: Configure WP Mail SMTP**

  WP Admin → WP Mail SMTP → Settings:
  - From Email: `info@regalplumbingservices.com`
  - From Name: `Regal Plumbing & Rooter`
  - Mailer: Connect to your email provider (Gmail/G Suite recommended — follow the plugin wizard)
  - Send a test email to confirm delivery

- [ ] **Step 3: Configure UpdraftPlus**

  WP Admin → Settings → UpdraftPlus:
  - Set automatic backups: Daily for files, Daily for database
  - Connect remote storage (Google Drive or Dropbox)
  - Run a manual backup now

- [ ] **Step 4: Configure Wordfence**

  WP Admin → Wordfence → Dashboard:
  - Run initial scan
  - Enable login security (2FA optional but recommended)
  - Enable firewall

- [ ] **Step 5: Commit**

  ```bash
  git add .
  git commit -m "chore: all required plugins installed and configured"
  ```

---

### Task 3: Install Hello Elementor Child Theme

- [ ] **Step 1: Create child theme directory and files**

  On the server (via FTP or File Manager), create:
  ```
  wp-content/themes/regal-plumbing-child/
  ```

- [ ] **Step 2: Create `style.css`**

  Create `wp-content/themes/regal-plumbing-child/style.css`:

  ```css
  /*
  Theme Name: Regal Plumbing Child
  Theme URI: https://regalplumbingservices.com
  Description: Child theme for Regal Plumbing & Rooter
  Author: Your Name
  Template: hello-elementor
  Version: 1.0.0
  */

  /* ─── TYPOGRAPHY OVERRIDES ─── */
  body {
    font-family: 'Open Sans', sans-serif;
    color: #2D2D2D;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: 'Oswald', sans-serif;
  }
  ```

- [ ] **Step 3: Create `functions.php`**

  Create `wp-content/themes/regal-plumbing-child/functions.php`:

  ```php
  <?php
  /**
   * Regal Plumbing Child Theme Functions
   */

  // Enqueue parent and child theme stylesheets + Google Fonts
  add_action( 'wp_enqueue_scripts', 'regal_enqueue_styles' );
  function regal_enqueue_styles() {
      wp_enqueue_style(
          'hello-elementor',
          get_template_directory_uri() . '/style.css'
      );
      wp_enqueue_style(
          'regal-child-style',
          get_stylesheet_directory_uri() . '/style.css',
          [ 'hello-elementor' ],
          wp_get_theme()->get( 'Version' )
      );
      wp_enqueue_style(
          'regal-custom-style',
          get_stylesheet_directory_uri() . '/assets/css/custom.css',
          [ 'regal-child-style' ]
      );
      wp_enqueue_style(
          'google-fonts-oswald-opensans',
          'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Oswald:wght@400;500;700&display=swap',
          [],
          null
      );
      wp_enqueue_script(
          'regal-custom-js',
          get_stylesheet_directory_uri() . '/assets/js/custom.js',
          [],
          '1.0.0',
          true  // load in footer
      );
  }
  ```

- [ ] **Step 4: Create `assets/css/custom.css`**

  Create `wp-content/themes/regal-plumbing-child/assets/css/custom.css`:

  ```css
  /* ─── MOBILE STICKY CTA BAR ─── */
  .mobile-sticky-cta {
    display: none;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    background-color: #B91C1C;
    padding: 12px 20px;
    text-align: center;
  }

  .mobile-sticky-cta a {
    color: #ffffff;
    font-family: 'Oswald', sans-serif;
    font-size: 18px;
    font-weight: 700;
    text-decoration: none;
    letter-spacing: 0.5px;
  }

  @media (max-width: 768px) {
    .mobile-sticky-cta {
      display: block;
    }
    /* Add bottom padding to body so sticky bar doesn't overlap content */
    body {
      padding-bottom: 56px;
    }
  }

  /* ─── UTILITY CLASSES ─── */
  .text-red    { color: #B91C1C; }
  .text-navy   { color: #1E3A6E; }
  .bg-red      { background-color: #B91C1C; }
  .bg-navy     { background-color: #1E3A6E; }
  .bg-darkgrey { background-color: #2D2D2D; }
  .bg-lightgrey{ background-color: #F3F4F6; }
  ```

- [ ] **Step 5: Create `assets/js/custom.js`**

  Create `wp-content/themes/regal-plumbing-child/assets/js/custom.js`:

  ```js
  // Mobile sticky CTA bar — inject into DOM (guard against duplicate injection)
  document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('.mobile-sticky-cta')) return;
    var bar = document.createElement('div');
    bar.className = 'mobile-sticky-cta';
    bar.innerHTML = '<a href="tel:9096004561">Call Now: (909) 600-4561</a>';
    document.body.appendChild(bar);
  });
  ```

- [ ] **Step 6: Activate child theme**

  WP Admin → Appearance → Themes → Activate "Regal Plumbing Child"

- [ ] **Step 7: Verify**

  - Site loads without errors
  - Open browser DevTools → Network tab → confirm `custom.css` and `custom.js` are loading
  - On a mobile viewport (< 768px), confirm the red sticky CTA bar appears at the bottom

- [ ] **Step 8: Commit**

  ```bash
  git add wp-content/themes/regal-plumbing-child/
  git commit -m "feat: add Hello Elementor child theme with fonts, mobile sticky CTA"
  ```

---

### Task 4: Configure Elementor Global Design Settings

- [ ] **Step 1: Open Elementor Site Settings**

  WP Admin → Elementor → Site Settings (or open any page in Elementor editor → hamburger menu → Site Settings)

- [ ] **Step 2: Set Global Colors**

  Under **Global Colors**, add:

  | Label | Hex |
  |-------|-----|
  | Primary Red | `#B91C1C` |
  | Dark Red (Hover) | `#991B1B` |
  | Navy Blue | `#1E3A6E` |
  | Dark Grey | `#2D2D2D` |
  | Light Grey | `#F3F4F6` |
  | White | `#FFFFFF` |

- [ ] **Step 3: Set Global Fonts**

  Under **Global Fonts**, configure. Elementor has 4 slots — map them as follows (the Label is what appears in the Elementor font picker when building widgets):

  | Elementor Label | Font | Weight | Maps to spec role |
  |-----------------|------|--------|-------------------|
  | Primary | Oswald | 700 | Main headlines (H1/H2) |
  | Secondary | Oswald | 500 | Accent labels ("24/7 Emergency", section labels) |
  | Text | Open Sans | 400 | Body copy |
  | Accent | Open Sans | 600 | Bold body text, subheadings |

  When building widgets in later tasks: use **Primary** for main headlines, **Secondary** for accent labels like trust badges and nav items, **Text** for paragraph copy.

- [ ] **Step 4: Set Typography defaults**

  Under **Theme Style → Typography**:
  - Body: Open Sans, 16px, Regular (400)
  - H1: Oswald, 52px, Bold (700)
  - H2: Oswald, 40px, Bold (700)
  - H3: Oswald, 28px, Medium (500)
  - H4: Oswald, 22px, Medium (500)

- [ ] **Step 5: Set Button defaults**

  Under **Theme Style → Buttons**:
  - Background Color: `#B91C1C`
  - Text Color: `#FFFFFF`
  - Font: Oswald, 16px, Medium (500)
  - Border Radius: 4px
  - Padding: 14px 28px
  - Hover Background: `#991B1B`

- [ ] **Step 6: Save and verify**

  Click Save. Open a test page in Elementor to confirm colors and fonts appear in the global pickers.

- [ ] **Step 7: Export global settings**

  Elementor → Tools → Export Kit → export Global Settings only.
  Save to `docs/elementor-exports/global-settings.json`

- [ ] **Step 8: Commit**

  ```bash
  git add docs/elementor-exports/global-settings.json
  git commit -m "feat: Elementor global colors, fonts, and button styles configured"
  ```

---

## Chunk 2: Global Templates — Header, Footer, Thank You Page

### Task 5: Build the Sticky Header Template

The header is built as an Elementor Pro **Header** template and applied site-wide via Theme Builder.

**Sections:**
1. Top Emergency Bar (dark grey strip)
2. Main Header (logo, nav, phone CTA)

- [ ] **Step 1: Create the Header template**

  WP Admin → Templates → Theme Builder → Add New → Select "Header" → name it "Regal Global Header" → Edit with Elementor

- [ ] **Step 2: Build the Emergency Bar row**

  Add a Section with:
  - Background: `#2D2D2D`
  - Padding: 8px top/bottom

  Add a single-column Inner Section. Add a **Text Editor** widget:
  - Content: `24/7 Emergency Service Available — Call <a href="tel:9096004561" style="color:#ffffff;font-weight:700;">(909) 600-4561</a>`
  - Alignment: Center
  - Font: Open Sans, 13px, color `#FFFFFF`

- [ ] **Step 3: Build the Main Header row**

  Add a new Section below with:
  - Background: `#FFFFFF`
  - Box Shadow: 0 2px 8px rgba(0,0,0,0.1)
  - Padding: 12px top/bottom

  Add a 3-column layout:

  **Column 1 (Logo):**
  - Add **Image** widget → upload `logo.png`
  - Link: Homepage URL
  - Width: 120px max
  - Alignment: Left

  **Column 2 (Navigation):**
  - Add **Nav Menu** widget → select your site's primary menu
  - Layout: Horizontal
  - Font: Oswald, 15px, Medium, color `#2D2D2D`
  - Hover color: `#B91C1C`
  - Active color: `#B91C1C`

  **Column 3 (Phone CTA):**
  - Add a **Text** widget: `(909) 600-4561`
    - Font: Oswald, 18px, Bold, color `#2D2D2D`
    - Link: `tel:9096004561`
  - Add a **Button** widget below it:
    - Text: `Call Now`
    - Link: `tel:9096004561`
    - Background: `#B91C1C`, Hover: `#991B1B`
    - Alignment: Right

- [ ] **Step 4: Configure sticky behavior**

  The **emergency bar** (top dark grey strip) is NOT sticky — it scrolls away naturally.
  The **main header row** (logo/nav/phone) IS sticky — it pins to the top on scroll.

  Click the main header Section → Advanced → Motion Effects:
  - Sticky: Top
  - Sticky on: Desktop + Tablet + Mobile

  Leave the emergency bar Section with no sticky setting.

- [ ] **Step 5: Configure mobile responsive**

  Switch to Mobile view in the Elementor editor:
  - Column 2 (Nav): Advanced → Responsive → Hide on Mobile ✓
  - Column 3 (Phone CTA): Advanced → Responsive → Hide on Mobile ✓
  - Column 1 (Logo): set width to 100%, alignment centered on mobile

  Add a 4th column (far right, mobile-only) in the main header row:
  - Add a **Nav Menu** widget → Content → Layout: Dropdown
  - Toggle: set Hamburger icon to display
  - Advanced → Responsive → Hide on Desktop and Tablet ✓ (show on Mobile only)
  - Position this column so the hamburger icon appears to the right of the logo

  Breakpoint: Elementor's default mobile breakpoint is 768px, matching the CSS in `custom.css`. No change needed to the breakpoint setting.

- [ ] **Step 6: Create WordPress navigation menu**

  WP Admin → Appearance → Menus → Create New Menu → name "Primary Navigation":
  - Add pages: Home, Services, About, Service Area, Contact
  - Assign to: Primary Menu location
  - Save

- [ ] **Step 7: Apply Header template site-wide**

  In Elementor template editor → Publish → Conditions:
  - Add condition: **Entire Site**
  - Save & Close

- [ ] **Step 8: Verify**

  Visit the front-end. Confirm:
  - [ ] Emergency bar shows with phone number link
  - [ ] Logo, nav, and phone CTA visible on desktop
  - [ ] Header is sticky (stays at top on scroll)
  - [ ] Hamburger menu appears on mobile
  - [ ] All nav links go to correct pages

- [ ] **Step 9: Export and commit**

  Export header template JSON → save to `docs/elementor-exports/header-template.json`

  ```bash
  git add docs/elementor-exports/header-template.json
  git commit -m "feat: build global sticky header with emergency bar"
  ```

---

### Task 6: Build the Global Footer Template

- [ ] **Step 1: Create Footer template**

  Templates → Theme Builder → Add New → "Footer" → name "Regal Global Footer" → Edit with Elementor

- [ ] **Step 2: Build the 4-column footer content section**

  Add a Section:
  - Background: `#2D2D2D`
  - Padding: 60px top/bottom

  Add a 4-column inner layout:

  **Column 1 — Logo + Tagline:**
  - Image widget: logo (white version or standard logo)
  - Text widget below: *"Honest, professional plumbing & rooter services across Southern California."*
    - Font: Open Sans, 14px, color `#AAAAAA`

  **Column 2 — Services:**
  - Heading widget: "Our Services" — Oswald, 18px, `#FFFFFF`
  - Icon List widget with links:
    - Emergency Plumbing → `/services/`
    - Drain Cleaning → `/services/`
    - Sewer Line Repair → `/services/`
    - Water Heater → `/services/`
    - Slab Leak Detection → `/services/`
    - Hydrojetting → `/services/`
    - Gas Leak Detection → `/services/`
    - Water Filtration → `/services/`
  - Font: Open Sans, 13px, color `#AAAAAA`, hover `#FFFFFF`

  **Column 3 — Service Area:**
  - Heading widget: "Service Area" — Oswald, 18px, `#FFFFFF`
  - **Icon List** widget with 8 key cities, each linked to its city page slug:
    - Rancho Cucamonga → `/service-area/rancho-cucamonga/`
    - Ontario → `/service-area/ontario/`
    - Pomona → `/service-area/pomona/`
    - Fontana → `/service-area/fontana/`
    - Chino → `/service-area/chino/`
    - Corona → `/service-area/corona/`
    - Upland → `/service-area/upland/`
    - Claremont → `/service-area/claremont/`
  - Font: Open Sans, 13px, color `#AAAAAA`, hover `#FFFFFF`
  - Note: These city pages don't exist in Phase 1 — the links are SEO-intentional placeholders
  - Text link below: "View All Cities →" → `/service-area/`, color `#B91C1C`

  **Column 4 — Contact:**
  - Heading widget: "Contact Us" — Oswald, 18px, `#FFFFFF`
  - Icon List:
    - Phone: (909) 600-4561 (linked `tel:9096004561`)
    - Email: info@regalplumbingservices.com
    - Address: 2141 E Philadelphia St, Suite R, Ontario, CA 91761
    - Hours: Available 24/7
  - Font: Open Sans, 13px, color `#AAAAAA`

- [ ] **Step 3: Build the bottom footer bar**

  Add a new Section below:
  - Background: `#1A1A1A`
  - Padding: 16px top/bottom

  Two columns:
  - Left: Text widget — use Elementor's dynamic copyright year tag so it updates automatically:
    `© [Elementor dynamic tag: Current Year] Regal Plumbing & Rooter. All Rights Reserved. CA License #1097482`
    In the Elementor text widget, type `©`, then click the dynamic tag icon (lightning bolt), select **Site** → **Current Year**, then type the rest of the text.
    - Font: Open Sans, 12px, color `#777777`
  - Right: Text widget — `regalplumbingservices.com`
    - Alignment: Right, color `#777777`

- [ ] **Step 4: Apply Footer template site-wide**

  Publish → Conditions → Entire Site

- [ ] **Step 5: Verify**

  - [ ] Footer appears on all pages
  - [ ] All 4 columns display correctly on desktop
  - [ ] Footer collapses to single column on mobile
  - [ ] Phone number and email links are functional
  - [ ] License number visible in bottom bar

- [ ] **Step 6: Export and commit**

  Export footer template JSON → `docs/elementor-exports/footer-template.json`

  ```bash
  git add docs/elementor-exports/footer-template.json
  git commit -m "feat: build global 4-column footer"
  ```

---

### Task 7: Create Thank You Page

- [ ] **Step 1: Create the Thank You page**

  WP Admin → Pages → Add New:
  - Title: `Thank You`
  - Slug: `thank-you`
  - Edit with Elementor

- [ ] **Step 2: Build the page**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 100px top/bottom, centered content

  Add:
  - Icon widget: checkmark icon, color `#B91C1C`, size 64px
  - Heading: "Thank You! We'll Be in Touch Soon." — Oswald, 40px, `#2D2D2D`
  - Text: "We've received your message and will contact you shortly. For urgent issues, call us directly at **(909) 600-4561**."
  - Button: "Return to Home" → link to homepage, red background

- [ ] **Step 3: Exclude from search results**

  RankMath → Edit page → Advanced → Robots Meta → set to `noindex` (thank-you pages shouldn't be indexed)

- [ ] **Step 4: Export and commit**

  Export Thank You page Elementor template → `docs/elementor-exports/page-thank-you.json`

  ```bash
  git add docs/elementor-exports/page-thank-you.json
  git commit -m "feat: add /thank-you page for form submission redirect"
  ```

---

## Chunk 3: Homepage

### Task 8: Build the Homepage

Create all 8 sections as specified.

**Reusable component — Emergency CTA Banner:**
Used on every page. Build it once as an Elementor **Global Section**, then insert the global section on each page. This keeps it DRY — updating the global section updates it everywhere.

- [ ] **Step 1: Open the Home page in Elementor**

  WP Admin → Pages → Home → Edit with Elementor

- [ ] **Step 2: Build Section 1 — Hero**

  Add a Section:
  - Background: Type = Image → upload hero photo (client-provided)
  - Background Overlay: Color `#1A1A1A`, Opacity 0.6
  - Min Height: 85vh
  - Content Position: Middle

  Add a single column with:
  - **Heading** widget: `Your Trusted Local Plumbers — Available 24/7`
    - Tag: H1, Font: Oswald Bold, 60px desktop / 38px mobile, Color: `#FFFFFF`
  - **Text Editor** widget: `Honest, professional plumbing & rooter services across the Inland Empire and San Gabriel Valley`
    - Font: Open Sans, 20px, color `#F3F4F6`
  - **Button** widget (red): `Call (909) 600-4561` → `tel:9096004561`
    - Background: `#B91C1C`, Text: White, Oswald 16px
  - **Button** widget (outline): `Get a Free Quote` → `/contact/#contact-form`
    - Background: Transparent, Border: 2px `#1E3A6E`, Text: `#FFFFFF`
    - Hover: background `#1E3A6E`

  Arrange buttons side-by-side using an Inner Section (2-column).

- [ ] **Step 3: Build Section 2 — Trust Bar**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 30px top/bottom

  Add an **Icon List** widget with 5 items (icons from Elementor icon library):
  - 24/7 Emergency Service
  - Family Owned & Operated
  - CA Licensed #1097482
  - 4+ Years Experience
  - 32+ Cities Served

  Layout: Inline, centered. Font: Oswald, 14px, color `#2D2D2D`.

- [ ] **Step 4: Build Section 3 — Services Overview**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  Heading widget: "Our Plumbing Services" — H2, Oswald, centered, `#2D2D2D`

  Add an **Inner Section** with 4 columns, then duplicate for row 2 (4 more columns). In each column add an **Icon Box** widget:

  | Service | Icon suggestion |
  |---------|----------------|
  | Emergency Plumbing | fa-exclamation-circle |
  | Drain Cleaning | fa-tint |
  | Sewer Line Repair | fa-tools |
  | Water Heater Install & Repair | fa-fire |
  | Slab Leak Detection & Repair | fa-search |
  | Hydrojetting | fa-water |
  | Gas Leak Detection | fa-burn |
  | Water Filtration & Softener | fa-filter |

  Each Icon Box:
  - Icon color: `#B91C1C`, size: 40px
  - Title: service name — Oswald, 18px
  - Description: one-line description
  - Link: "Learn More →" → `/contact/?service=[slug]` (pre-populates the Service Needed dropdown on the Contact page)

- [ ] **Step 5: Build Section 4 — Why Choose Regal**

  Add a Section:
  - Background: `#2D2D2D`
  - Padding: 80px top/bottom

  Heading: "Why Homeowners Trust Regal Plumbing & Rooter" — H2, Oswald, `#FFFFFF`, centered

  Inner Section — 3 columns, each with **Icon Box**:
  - Honest Pricing — icon `fa-dollar-sign` — white icon, white text
  - Fast Response — icon `fa-clock`
  - Quality Workmanship — icon `fa-award`

  Support text under each: 2 sentences, Open Sans 14px, color `#AAAAAA`

- [ ] **Step 6: Build the Global Emergency CTA Banner (save as Global Section)**

  Add a Section:
  - Background: `#B91C1C`
  - Padding: 50px top/bottom

  2-column layout:
  - Left: Heading "Plumbing Emergency? We're Available 24/7" — Oswald, 36px, `#FFFFFF`
  - Right: Button "Call (909) 600-4561" — white background, `#B91C1C` text, large; + subtext "Available 24/7"

  Right-click the Section → Save as Global → name "Emergency CTA Banner"

- [ ] **Step 7: Build Section 6 — Service Area Teaser**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 60px top/bottom

  Heading: "Proudly Serving Southern California" — H2, Oswald, centered

  Text widget listing key cities (comma-separated, 2 lines):
  *Rancho Cucamonga, Ontario, Pomona, Fontana, Upland, Corona, Chino, Claremont, and many more...*

  Button: "View Full Service Area" → `/service-area/` — Navy background `#1E3A6E`

- [ ] **Step 8: Build Section 7 — About Snapshot**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  2-column layout:
  - Left (40%): Image widget → logo; Icon List below with trust badges (Licensed, Family Owned, 24/7)
  - Right (60%): Heading "About Regal Plumbing & Rooter"; Text widget with about copy; CA License #1097482 displayed in **Alert** or styled text box; Button "Learn More About Us" → `/about/`

- [ ] **Step 9: Build Section 8 — Reviews / Social Proof**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 80px top/bottom

  Heading: "What Our Customers Say" — H2, centered

  **Configure Widgets for Google Reviews plugin:**
  WP Admin → Google Reviews → Add New → connect your Google Business Profile → set to show 3 reviews, 5-star minimum → copy the shortcode → insert via **Shortcode** widget in Elementor

  Below the reviews: Text link "See More Reviews on Google" linking to the GMB profile URL.

  **Fallback if plugin connection cannot be established at launch:** Build 3 static review cards manually using a 3-column Inner Section. Each column contains:
  - Row of 5 gold star icons (Icon List widget, fa-star, color `#F59E0B`)
  - Text Editor with review text (1–3 sentences from a real Google review)
  - Bold text: Reviewer name — Open Sans, 14px, `#2D2D2D`
  - Subtext: "Google Review" — Open Sans, 12px, `#777777`

  Replace with the live plugin shortcode once the Google Business Profile connection is established.

- [ ] **Step 10: Set Homepage page template**

  In Elementor → Page Settings (gear icon bottom-left) → Page Layout: Elementor Full Width (hides default WordPress title)

- [ ] **Step 11: Verify Homepage**

  Check each section:
  - [ ] Hero displays photo with overlay, headline readable, both buttons visible
  - [ ] Trust bar icons align horizontally
  - [ ] 8 service cards display in 2 rows of 4 on desktop, stack on mobile
  - [ ] Why Choose section: dark background, 3 columns readable
  - [ ] Emergency CTA banner: red background, phone number visible
  - [ ] Service area teaser shows cities + button
  - [ ] About snapshot: logo and text in 2 columns
  - [ ] Google reviews appear (at least 3)
  - [ ] All CTAs link to correct destinations

- [ ] **Step 12: Export and commit**

  Export homepage Elementor template → `docs/elementor-exports/page-home.json`

  ```bash
  git add docs/elementor-exports/page-home.json
  git commit -m "feat: build homepage with all 8 sections"
  ```

---

## Chunk 4: Services Overview Page & About Us Page

### Task 9: Build the Services Overview Page

- [ ] **Step 1: Create the Services page**

  WP Admin → Pages → Add New:
  - Title: `Plumbing Services`
  - Slug: `services`
  - Edit with Elementor

- [ ] **Step 2: Build Section 1 — Page Hero**

  Add a Section:
  - Background: `#2D2D2D`
  - Padding: 80px top/bottom

  Add:
  - Breadcrumb text (Text widget): `Home > Services` — Open Sans, 13px, color `#AAAAAA`
    - Link "Home" to `/`
  - Heading: "Our Plumbing Services" — H1, Oswald Bold, 52px, `#FFFFFF`
  - Subheading text: "Professional plumbing solutions for every situation — available 24/7 across Southern California" — Open Sans, 18px, `#F3F4F6`

  Add a red left-border accent: Add a 4px `#B91C1C` left border to the section or a decorative divider widget.

- [ ] **Step 3: Build Section 2 — Services Grid**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  Build 8 service cards in a 2-column layout. Each row is an Inner Section with 2 columns. Create 4 rows.

  Each service card (column):
  - Add an **Icon Box** or build with **Image Box** widget:
    - Icon (same icons as homepage, larger — 50px)
    - **H3** heading: service name, Oswald, 26px, `#2D2D2D` (use H3 — this page has one H1 in the hero and section headings as H2; service cards are H3 for correct SEO/accessibility hierarchy)
    - Description: 2–3 sentences about the service
    - Border: 1px `#F3F4F6`, border-radius 6px, padding 30px
    - Hover: box shadow `0 4px 16px rgba(0,0,0,0.1)`
  - Button: "Learn More" → `/contact/?service=[service-slug]`
    - Background `#B91C1C`, small size
  - Text link below button: "Or call (909) 600-4561" → `tel:9096004561`
    - Font: Open Sans, 13px, color `#777777`

  Service slugs for URL parameters:
  ```
  emergency-plumbing, drain-cleaning, sewer-line-repair,
  water-heater, slab-leak, hydrojetting,
  gas-leak-detection, water-filtration
  ```

- [ ] **Step 4: Insert Emergency CTA Banner Global Section**

  Add a new section → Right-click → Add Global Section → select "Emergency CTA Banner"

  **Do NOT edit the global section content.** The Emergency CTA Banner uses the generic headline "Plumbing Emergency? We're Available 24/7" which works appropriately on all pages. Editing a global section updates it on every page simultaneously — do not customize per-page. The generic headline is intentional.

- [ ] **Step 5: Build Section 4 — Why Regal (condensed)**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 50px top/bottom

  3-column Icon List (condensed version):
  - Licensed & Insured — fa-certificate
  - Family Owned — fa-home
  - Honest Pricing — fa-dollar-sign

  Each: icon `#B91C1C`, title Oswald 20px, 1-sentence support text Open Sans 14px.

- [ ] **Step 5b: Set page template to Elementor Full Width**

  In Elementor editor → Page Settings (gear icon, bottom-left) → Page Layout: **Elementor Full Width**
  This hides the default WordPress page title and any sidebar, giving Elementor full control of the layout.

- [ ] **Step 6: Verify Services page**

  - [ ] Hero shows breadcrumb, H1 headline, subheadline on dark background
  - [ ] 8 service cards in 2-column grid, all have icons, descriptions, and "Learn More" buttons
  - [ ] "Learn More" links go to `/contact/?service=[slug]`
  - [ ] Emergency CTA banner visible
  - [ ] Why Regal condensed section visible

- [ ] **Step 7: Export and commit**

  Export → `docs/elementor-exports/page-services.json`

  ```bash
  git add docs/elementor-exports/page-services.json
  git commit -m "feat: build services overview page"
  ```

---

### Task 10: Build the About Us Page

- [ ] **Step 1: Create the About page**

  WP Admin → Pages → Add New:
  - Title: `About Us`
  - Slug: `about`
  - Edit with Elementor

- [ ] **Step 2: Build Section 1 — Page Hero**

  Add a Section:
  - Background: `#1E3A6E` (Dark Navy)
  - Padding: 80px top/bottom

  Add:
  - Breadcrumb: `Home > About Us`
  - H1 Heading: "About Regal Plumbing & Rooter" — Oswald Bold, 52px, `#FFFFFF`
  - Subheadline: "Family-owned and built on honesty, professionalism, and premium craftsmanship" — Open Sans, 18px, `#F3F4F6`

- [ ] **Step 3: Build Section 2 — Our Story**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  2-column layout (40/60 split):

  **Left column:**
  - Image widget: logo, max-width 200px, centered
  - Icon List widget: trust badges
    - CA Licensed #1097482 — fa-certificate
    - Family Owned & Operated — fa-users
    - 24/7 Emergency Service — fa-clock
    - 4+ Years in Business — fa-calendar

  **Right column:**
  - H2 Heading: "Our Story" — Oswald, `#2D2D2D`
  - Text Editor with full about copy:

    *"Regal Plumbing & Rooter was founded with one goal: to bring honesty, professionalism, and premium craftsmanship to every customer. As a family-owned business, we take pride in delivering reliable plumbing solutions backed by integrity.*

    *We understand that plumbing issues can be stressful. That's why we make it simple — transparent pricing, expert workmanship, and a team that treats your home like our own.*

    *Serving the Inland Empire and San Gabriel Valley, we're proud to be the plumbing partner families and businesses trust 24/7."*

  - Styled box below text (Alert widget or custom-styled Text widget):
    - Background: `#F3F4F6`, border-left: 4px `#B91C1C`, padding: 16px
    - Text: "**CA Contractor License #1097482** — Licensed, Bonded & Insured"

- [ ] **Step 4: Build Section 3 — Our Values**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 80px top/bottom

  H2 Heading: "What Sets Us Apart" — centered, Oswald, `#2D2D2D`

  3-column Icon Box layout:
  - **Honesty** — fa-handshake — "Upfront pricing with no hidden fees. You'll always know what you're paying before we start."
  - **Professionalism** — fa-id-badge — "Our technicians are licensed, trained, and respectful of your home and time."
  - **Quality** — fa-star — "Premium workmanship on every job, big or small. We don't cut corners."

  Icon color: `#B91C1C`. Title: Oswald 22px. Description: Open Sans 15px.

- [ ] **Step 5: Build Section 4 — By The Numbers**

  Add a Section:
  - Background: `#2D2D2D`
  - Padding: 80px top/bottom

  4-column layout using **Counter** widgets or styled **Heading + Text** pairs:

  | Number | Label |
  |--------|-------|
  | 4+ | Years in Business |
  | 32+ | Cities Served |
  | 24/7 | Emergency Availability |
  | #1097482 | CA License |

  Number: Oswald Bold 52px `#B91C1C`. Label: Oswald 18px `#FFFFFF`.

- [ ] **Step 6: Insert Emergency CTA Banner**

  Add a new Section (not a Global Section insert — add a regular styled section):
  - Background: `#B91C1C`, Padding: 50px top/bottom
  - Match the same layout as the homepage Global Section (2-column: headline left, button right)
  - Headline: "Ready to Experience the Regal Difference?" — Oswald, 36px, `#FFFFFF`
  - Button: "Call Us Today — (909) 600-4561" → `tel:9096004561` — white background, `#B91C1C` text

  Note: **Do not insert the Global Section here.** Because this page needs a different headline, build a regular styled section instead of inserting the Global Section (editing a Global Section updates it everywhere simultaneously).

- [ ] **Step 6b: Set page template to Elementor Full Width**

  Elementor editor → Page Settings → Page Layout: **Elementor Full Width**

- [ ] **Step 7: Verify About page**

  - [ ] Navy hero with breadcrumb and H1
  - [ ] 2-column Our Story: logo + trust badges left; about copy + license callout right
  - [ ] 3-column values section on light grey background
  - [ ] 4 stat tiles on dark grey background
  - [ ] Emergency CTA banner

- [ ] **Step 8: Export and commit**

  Export → `docs/elementor-exports/page-about.json`

  ```bash
  git add docs/elementor-exports/page-about.json
  git commit -m "feat: build about us page"
  ```

---

## Chunk 5: Contact Us Page & Service Area Page

### Task 11: Configure WPForms Contact Form

Build the contact form before building the Contact page so it can be embedded.

- [ ] **Step 1: Verify WPForms Pro is active**

  WP Admin → WPForms → All Forms — confirm the Pro version is active (Pro is required for the Dynamic Population feature used in Step 2). No additional addon needs to be installed — the URL parameter pre-population feature is built into WPForms Pro natively.

- [ ] **Step 2: Create the contact form**

  WP Admin → WPForms → Add New → name "Contact Us Form" → use Blank template

  Add these fields in order:
  1. **Name** field — label "Full Name", Required
  2. **Phone** field — label "Phone Number", Required
  3. **Email** field — label "Email Address", Required
  4. **Dropdown** field — label "Your City" — add all 32 cities as options (alphabetical order, same list as spec)
  5. **Dropdown** field — label "Service Needed" — add all 8 services as options. Then enable **Dynamic Population**:
     - Click the "Service Needed" field in the form builder → **Advanced** tab → toggle on "Enable Dynamic Population" → set Parameter Name to `service`
     - This allows `/contact/?service=drain-cleaning` to pre-select the matching option
     - Map display labels to URL parameter values:
     - Emergency Plumbing → `emergency-plumbing`
     - Drain Cleaning → `drain-cleaning`
     - Sewer Line Repair → `sewer-line-repair`
     - Water Heater Installation & Repair → `water-heater`
     - Slab Leak Detection & Repair → `slab-leak`
     - Hydrojetting → `hydrojetting`
     - Gas Leak Detection → `gas-leak-detection`
     - Water Filtration & Softener Systems → `water-filtration`
  6. **Paragraph Text** field — label "Describe Your Issue", Required

  Note: reCAPTCHA is NOT added as a form field — it is configured globally (see Step 2b below).

- [ ] **Step 2b: Configure reCAPTCHA globally**

  WP Admin → WPForms → Settings → reCAPTCHA:
  - Select reCAPTCHA type: **v3** (invisible, no user checkbox)
  - Register your site at `google.com/recaptcha`, select reCAPTCHA v3
  - Copy the Site Key and Secret Key into WPForms settings → Save
  - Then open your form → Settings → Spam Protection and Security → enable "Enable anti-spam protection" and "reCAPTCHA"
  - reCAPTCHA v3 will now apply silently to all form submissions

- [ ] **Step 3: Configure form notifications**

  WPForms → Settings → Notifications:
  - Send to: `info@regalplumbingservices.com`
  - Subject: `New Contact Form Submission — {field_id="5"}` (Service Needed field — verify field ID by opening the form, clicking the Service Needed field, and checking the Field ID shown in the field's Advanced tab; use that ID in the smart tag)
  - Email body: include all field values using smart tags

- [ ] **Step 4: Configure form confirmations**

  WPForms → Settings → Confirmations:
  - Type: Redirect
  - Redirect URL: `https://regalplumbingservices.com/thank-you/`

- [ ] **Step 5: Test the form**

  Submit a test entry. Verify:
  - [ ] Email received at info@regalplumbingservices.com
  - [ ] Redirect goes to `/thank-you/`
  - [ ] reCAPTCHA working (no spam submissions)

- [ ] **Step 6: Commit**

  ```bash
  git commit -m "feat: configure WPForms contact form with dynamic service dropdown"
  ```

---

### Task 12: Build the Contact Us Page

- [ ] **Step 1: Create the Contact page**

  WP Admin → Pages → Add New:
  - Title: `Contact Us`
  - Slug: `contact`
  - Edit with Elementor

- [ ] **Step 2: Build Section 1 — Page Hero**

  Add a Section:
  - Background: `#2D2D2D`
  - Padding: 80px top/bottom

  Add:
  - Breadcrumb: `Home > Contact Us`
  - H1: "Contact Regal Plumbing & Rooter" — Oswald Bold, 52px, `#FFFFFF`
  - Subheadline: "Available 24/7 for emergencies — call us now or send a message below" — Open Sans, 18px, `#F3F4F6`

- [ ] **Step 3: Build Section 2 — Contact Split Layout**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  Add an HTML anchor to this section for the "Get a Free Quote" button deep-link:
  - Section → Advanced → CSS ID: `contact-form`

  2-column layout (55/45 split):

  **Left column — Form:**
  - H2: "Send Us a Message" — Oswald, 28px
  - Large phone CTA: add a **Button** widget → "(909) 600-4561" → `tel:9096004561`
    - Full-width, large, red background, Oswald 20px
    - Subtext below: "Available 24/7 for Emergency Service" — Open Sans 13px, grey
  - **WPForms** widget → select "Contact Us Form"

  **Right column — Info:**
  - H3: "Get in Touch" — Oswald 24px
  - **Icon List** widget:
    - Phone: (909) 600-4561
    - Email: info@regalplumbingservices.com
    - Address: 2141 E Philadelphia St, Suite R, Ontario, CA 91761
    - Hours: 24/7 Emergency Available
    - License: CA #1097482
  - **Google Maps** widget (Elementor Pro):
    - Address: 2141 E Philadelphia St, Suite R, Ontario, CA 91761
    - Zoom: 13
    - Height: 300px

- [ ] **Step 4: Insert Emergency CTA Banner**

  Add a new Section (regular section, not the Global Section — this page needs a different headline):
  - Background: `#B91C1C`, Padding: 50px top/bottom
  - Headline: "Plumbing Emergency? Don't Wait — Call Now" — Oswald, 36px, `#FFFFFF`
  - Phone number prominent + Button: "Call Now" → `tel:9096004561`

- [ ] **Step 4b: Set page template to Elementor Full Width**

  Elementor editor → Page Settings → Page Layout: **Elementor Full Width**

- [ ] **Step 5: Verify Contact page**

  - [ ] `/contact/#contact-form` anchor scrolls directly to the form
  - [ ] Form displays all fields
  - [ ] Service dropdown accepts `?service=drain-cleaning` URL parameter and pre-selects "Drain Cleaning"
  - [ ] Submit form → redirects to `/thank-you/`
  - [ ] Email received at info@regalplumbingservices.com
  - [ ] Google Map shows correct address
  - [ ] Phone number is tappable on mobile

- [ ] **Step 6: Export and commit**

  Export → `docs/elementor-exports/page-contact.json`

  ```bash
  git add docs/elementor-exports/page-contact.json
  git commit -m "feat: build contact us page with embedded form and map"
  ```

---

### Task 13: Build the Service Area Page

- [ ] **Step 1: Create the Service Area page**

  WP Admin → Pages → Add New:
  - Title: `Service Area`
  - Slug: `service-area`
  - Edit with Elementor

- [ ] **Step 2: Build Section 1 — Page Hero**

  Add a Section:
  - Background: `#1E3A6E` (Navy)
  - Padding: 80px top/bottom

  Add:
  - Breadcrumb: `Home > Service Area`
  - H1: "Plumbing Services Across Southern California" — Oswald Bold, 52px, `#FFFFFF`
  - Subheadline: "Regal Plumbing & Rooter proudly serves homeowners and businesses across the Inland Empire and San Gabriel Valley" — Open Sans, 18px, `#F3F4F6`

- [ ] **Step 3: Build Section 2 — Map**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  H2: "Our Service Area" — Oswald, centered

  **Google Maps** widget (Elementor Pro):
  - Address: Ontario, CA (center of coverage area)
  - Zoom: 10 (shows full IE/SGV region)
  - Height: 450px

  Text widget below map: *"From Rancho Cucamonga to Yorba Linda, our licensed plumbers are ready to respond fast — including 24/7 emergency service throughout our entire service area."*

- [ ] **Step 4: Build Section 3 — Cities We Serve**

  Add a Section:
  - Background: `#F3F4F6`
  - Padding: 80px top/bottom

  H2: "Cities We Serve" — Oswald, centered

  Build a 4-column grid using **Text Editor** widgets or an **HTML** widget. List all 32 cities in alphabetical order, each city as a link to its future landing page `/service-area/[city-slug]/`:

  ```html
  <div class="cities-grid">
    <ul>
      <li><a href="/service-area/azusa/">Azusa</a></li>
      <li><a href="/service-area/bloomington/">Bloomington</a></li>
      <li><a href="/service-area/brea/">Brea</a></li>
      <li><a href="/service-area/charter-oak/">Charter Oak</a></li>
      <li><a href="/service-area/chino/">Chino</a></li>
      <li><a href="/service-area/chino-hills/">Chino Hills</a></li>
      <li><a href="/service-area/citrus/">Citrus</a></li>
      <li><a href="/service-area/claremont/">Claremont</a></li>
    </ul>
    <ul>
      <li><a href="/service-area/colton/">Colton</a></li>
      <li><a href="/service-area/corona/">Corona</a></li>
      <li><a href="/service-area/covina/">Covina</a></li>
      <li><a href="/service-area/diamond-bar/">Diamond Bar</a></li>
      <li><a href="/service-area/eastvale/">Eastvale</a></li>
      <li><a href="/service-area/fontana/">Fontana</a></li>
      <li><a href="/service-area/glendora/">Glendora</a></li>
      <li><a href="/service-area/highgrove/">Highgrove</a></li>
    </ul>
    <ul>
      <li><a href="/service-area/jurupa-valley/">Jurupa Valley</a></li>
      <li><a href="/service-area/la-verne/">La Verne</a></li>
      <li><a href="/service-area/loma-linda/">Loma Linda</a></li>
      <li><a href="/service-area/mira-loma/">Mira Loma</a></li>
      <li><a href="/service-area/montclair/">Montclair</a></li>
      <li><a href="/service-area/muscoy/">Muscoy</a></li>
      <li><a href="/service-area/norco/">Norco</a></li>
      <li><a href="/service-area/ontario/">Ontario</a></li>
    </ul>
    <ul>
      <li><a href="/service-area/pomona/">Pomona</a></li>
      <li><a href="/service-area/rancho-cucamonga/">Rancho Cucamonga</a></li>
      <li><a href="/service-area/rowland-heights/">Rowland Heights</a></li>
      <li><a href="/service-area/san-dimas/">San Dimas</a></li>
      <li><a href="/service-area/upland/">Upland</a></li>
      <li><a href="/service-area/walnut/">Walnut</a></li>
      <li><a href="/service-area/west-covina/">West Covina</a></li>
      <li><a href="/service-area/yorba-linda/">Yorba Linda</a></li>
    </ul>
  </div>
  ```

  Add this CSS to the widget's Custom CSS or to `custom.css`:
  ```css
  .cities-grid {
    display: flex;
    gap: 20px;
  }
  .cities-grid ul {
    list-style: none;
    padding: 0;
    flex: 1;
  }
  .cities-grid ul li {
    margin-bottom: 8px;
  }
  .cities-grid ul li a {
    color: #1E3A6E;
    font-family: 'Open Sans', sans-serif;
    font-size: 15px;
    text-decoration: none;
  }
  .cities-grid ul li a:hover {
    color: #B91C1C;
    text-decoration: underline;
  }
  @media (max-width: 768px) {
    .cities-grid {
      flex-wrap: wrap;
    }
    .cities-grid ul {
      flex: 0 0 48%;
    }
  }
  ```

  **Important — Placeholder pages required to avoid launch 404s:** Google will crawl all 32 city URLs immediately after Search Console submission. Create minimal stub pages for each city now to prevent crawl errors:

  WP Admin → Pages → Add New (repeat for each city):
  - Title: `[City Name] Plumber — Regal Plumbing & Rooter`
  - Slug: `service-area/[city-slug]` (e.g., `service-area/rancho-cucamonga`)
  - Content (same for all stubs): Add an Elementor section with a heading and text:
    - H1: "[City Name] Plumbing Services"
    - Text: "Regal Plumbing & Rooter proudly serves [City Name] and the surrounding area. For plumbing services in [City Name], call us 24/7 at (909) 600-4561. Full [City Name] service page coming soon."
    - Button: "Call (909) 600-4561" → `tel:9096004561`
  - Set page template: Elementor Full Width
  - RankMath: set a unique title/meta for each city

  This creates minimal but valid pages that avoid 404s and begin earning local SEO signals. Full city page content is Phase 2 scope.

- [ ] **Step 5: Build Section 4 — SEO Content Block**

  Add a Section:
  - Background: `#FFFFFF`
  - Padding: 80px top/bottom

  H2: "Fast, Local Plumbing You Can Count On" — Oswald, centered

  Text Editor widget with 3 SEO-optimized paragraphs:

  *"When plumbing problems strike, response time matters. Regal Plumbing & Rooter provides fast, reliable service to homeowners and businesses across the Inland Empire and San Gabriel Valley — from Rancho Cucamonga and Ontario to Pomona, Fontana, and Corona.*

  *Whether you need emergency drain cleaning in Upland, a water heater replacement in Chino Hills, or slab leak detection in Claremont, our licensed technicians are ready to respond 24/7. We serve 32 cities with the same commitment to honesty and quality workmanship.*

  *As a family-owned, CA-licensed plumbing company (License #1097482), we take pride in being the trusted local plumber for thousands of homeowners across the region. Call (909) 600-4561 — we're available around the clock."*

- [ ] **Step 6: Insert Emergency CTA Banner**

  Add a new Section (regular section, not the Global Section — this page needs a different headline):
  - Background: `#B91C1C`, Padding: 50px top/bottom
  - Headline: "Need a Plumber in Your Area? We're Ready Now" — Oswald, 36px, `#FFFFFF`
  - Phone number prominent + Button: "Call Now" → `tel:9096004561`

- [ ] **Step 7: Verify Service Area page**

  - [ ] Navy hero with breadcrumb and H1
  - [ ] Google Map centered on Ontario, CA, showing full IE/SGV region
  - [ ] All 32 cities listed in 4 columns, alphabetical
  - [ ] City links follow `/service-area/[city-slug]/` pattern
  - [ ] SEO content block contains natural keyword mentions
  - [ ] Emergency CTA banner visible

- [ ] **Step 8: Export and commit**

  Export → `docs/elementor-exports/page-service-area.json`

  ```bash
  git add docs/elementor-exports/page-service-area.json
  git commit -m "feat: build service area page with city grid and SEO content"
  ```

---

## Chunk 6: SEO Configuration & Launch Checklist

### Task 14: Configure RankMath SEO

- [ ] **Step 1: Run RankMath Setup Wizard**

  WP Admin → RankMath → Setup Wizard:
  - Business type: Local Business → Plumber
  - Business Name: Regal Plumbing & Rooter
  - Address: 2141 E Philadelphia St, Suite R, Ontario, CA 91761
  - Phone: (909) 600-4561
  - Business Hours: Open 24/7

- [ ] **Step 2: Set meta titles and descriptions for all 5 pages**

  Edit each page → RankMath meta box → General tab:

  **Homepage:**
  - Title: `Regal Plumbing & Rooter — 24/7 Plumber | Inland Empire & San Gabriel Valley`
  - Description: `Family-owned, licensed plumbers serving Rancho Cucamonga, Pomona, Ontario & 30+ cities. Emergency plumbing, drain cleaning, slab leak repair & more. Call (909) 600-4561.`
  - Focus keyword: `plumber Inland Empire`

  **Services Overview:**
  - Title: `Plumbing Services — Drain Cleaning, Water Heater, Slab Leak & More | Regal Plumbing`
  - Description: `Regal Plumbing & Rooter offers emergency plumbing, hydrojetting, sewer line repair, water heater installation, and more. Serving Southern California 24/7.`
  - Focus keyword: `plumbing services Inland Empire`
  - Schema: Use **LocalBusiness** schema only for this page (the global RankMath Local SEO setting covers this). Individual Service schema (one per service) will be added in Phase 2 when dedicated service pages are built. Do not attempt to add multiple Service schema blocks to this page — it is not supported in RankMath free and is out of scope for Phase 1.

  **About Us:**
  - Title: `About Regal Plumbing & Rooter — Family-Owned, CA Licensed Plumbers`
  - Description: `Learn about Regal Plumbing & Rooter — a family-owned plumbing company built on honesty and premium craftsmanship. CA License #1097482.`
  - Focus keyword: `Regal Plumbing Rooter Ontario CA`

  **Contact Us:**
  - Title: `Contact Regal Plumbing & Rooter — Call (909) 600-4561`
  - Description: `Get in touch with Regal Plumbing & Rooter. Available 24/7 for plumbing emergencies across the Inland Empire and San Gabriel Valley.`
  - Focus keyword: `contact plumber Ontario CA`

  **Service Area:**
  - Title: `Plumbing Service Area — Inland Empire & San Gabriel Valley | Regal Plumbing`
  - Description: `Regal Plumbing & Rooter serves 32 cities including Rancho Cucamonga, Fontana, Ontario, Pomona, Chino, Corona & more. Available 24/7.`
  - Focus keyword: `plumber service area Southern California`

- [ ] **Step 3: Configure Local SEO schema**

  RankMath → Titles & Meta → Local SEO:
  - Enable Local SEO
  - Business Type: Plumber
  - Business Name: Regal Plumbing & Rooter
  - Address: 2141 E Philadelphia St, Suite R, Ontario, CA 91761
  - Phone: +1-909-600-4561
  - Opening Hours: 24/7 (all days, 00:00–24:00)
  - Price Range: $$
  - Geo Coordinates: (get from Google Maps for the Ontario address)
  - **Service Area / areaServed:** Add all 32 cities — Azusa, Bloomington, Brea, Charter Oak, Chino, Chino Hills, Citrus, Claremont, Colton, Corona, Covina, Diamond Bar, Eastvale, Fontana, Glendora, Highgrove, Jurupa Valley, La Verne, Loma Linda, Mira Loma, Montclair, Muscoy, Norco, Ontario, Pomona, Rancho Cucamonga, Rowland Heights, San Dimas, Upland, Walnut, West Covina, Yorba Linda

- [ ] **Step 4: Configure per-page schema**

  For each page, set Schema in the RankMath sidebar:

  | Page | Schema Type |
  |------|-------------|
  | Homepage | WebSite + LocalBusiness |
  | Services Overview | Service (set service name/description for each; may need to use custom schema) |
  | About Us | Organization |
  | Contact Us | ContactPage |
  | Service Area | LocalBusiness with areaServed |

- [ ] **Step 5: Generate and submit sitemap**

  RankMath → Sitemap → enable sitemap → verify at `/sitemap_index.xml`

  Submit to Google Search Console:
  - Add property for `regalplumbingservices.com`
  - Verify ownership (HTML tag method via RankMath)
  - Submit sitemap URL

- [ ] **Step 6: Connect Google Search Console via RankMath Analytics**

  RankMath → Analytics → connect Google Search Console (this pulls keyword ranking data into the WP dashboard — it does NOT set up GA4 tracking).

  **GA4 tracking requires a separate step:** Install the **Google Site Kit** plugin (free, by Google):
  - WP Admin → Plugins → Add New → "Site Kit by Google" → Install & Activate
  - Follow the Site Kit wizard to connect your Google Analytics 4 property
  - Site Kit will inject the GA4 tracking code across the entire site automatically

- [ ] **Step 7: Commit**

  ```bash
  git commit -m "feat: configure RankMath SEO, schema markup, and sitemaps"
  ```

---

### Task 15: Performance Optimization

- [ ] **Step 1: Configure WP Rocket**

  WP Admin → WP Rocket → Settings:

  **Cache tab:**
  - Enable caching for mobile devices
  - Cache lifespan: 10 hours

  **File Optimization tab:**
  - Minify CSS files: ON
  - Combine CSS files: **OFF** (this frequently breaks Elementor Pro's CSS — leave off and only enable after a complete visual QA pass, and only if no layout regressions are found)
  - Minify JavaScript: ON
  - Defer JavaScript loading: ON
  - Delay JavaScript execution: ON — **after enabling, test all interactive elements**: sticky header, hamburger menu, contact form, Google Maps, and the mobile sticky CTA bar. If any break, add Elementor's scripts to the Delay exclusion list in WP Rocket → File Optimization → Delay JS Exclusions: add `elementor`

  **Media tab:**
  - LazyLoad images: ON
  - LazyLoad iframes/videos: ON
  - Add missing image dimensions: ON

  **Preload tab:**
  - Activate preloading: ON
  - Prefetch DNS requests: add `fonts.googleapis.com`, `fonts.gstatic.com`

- [ ] **Step 2: Optimize images**

  Upload all client-provided photos via WordPress Media Library. For each image used in hero sections:
  - Recommended dimensions: 1920×1080px minimum
  - Format: JPG, quality 80–85%
  - Use WP's built-in image compression or install **Smush** plugin for additional compression

- [ ] **Step 3: Test page speed**

  Run each page through Google PageSpeed Insights (`pagespeed.web.dev`):
  - Target: Mobile score ≥ 70, Desktop score ≥ 85
  - If scores are low, identify the heaviest assets and compress further

- [ ] **Step 4: Commit**

  ```bash
  git commit -m "feat: configure WP Rocket performance optimization"
  ```

---

### Task 16: Pre-Launch Checklist & Final Verification

- [ ] **Publishing checks (run first):**
  - [ ] All 5 main pages are Published (not Draft): Home, Services, About, Contact, Service Area
  - [ ] Thank You page is Published
  - [ ] All 32 city stub pages are Published
  - [ ] WP Admin → Settings → Reading → "Your homepage displays" is set to the static Home page

- [ ] **Cross-page checks:**
  - [ ] All 5 pages load without errors
  - [ ] Sticky header visible and functional on all pages
  - [ ] Footer visible on all pages, NAP information correct (address, phone, license number)
  - [ ] Mobile sticky CTA bar visible on mobile for all pages
  - [ ] No broken links (use a broken link checker plugin or `brokenlinkcheck.com`)
  - [ ] Thank You page (`/thank-you/`) loads correctly

- [ ] **SEO checks:**
  - [ ] RankMath shows green/orange score for all 5 pages (aim for 70+)
  - [ ] All pages have unique title tags and meta descriptions
  - [ ] Sitemap accessible at `/sitemap_index.xml`
  - [ ] Google Search Console property verified
  - [ ] Schema validated via Google's Rich Results Test (`search.google.com/test/rich-results`) — note: LocalBusiness and Plumber types are not rich-result eligible so "No results detected" is expected. Also validate at `validator.schema.org` to confirm the schema structure itself is correct.

- [ ] **Conversion checks:**
  - [ ] Contact form submits successfully → email received at info@regalplumbingservices.com → redirect to `/thank-you/`
  - [ ] WP Mail SMTP test: submit the contact form and confirm delivery (check spam folder too)
  - [ ] End-to-end `?service=` test: click "Learn More" on the Services page (e.g., Drain Cleaning) → verify Contact page opens with "Drain Cleaning" pre-selected in Service Needed dropdown
  - [ ] All "Call Now" and phone number links use `tel:9096004561` (tap on mobile to verify)
  - [ ] "Get a Free Quote" button on homepage scrolls to `#contact-form` on Contact page

- [ ] **Mobile checks (test on real device or BrowserStack):**
  - [ ] Homepage hero readable on mobile
  - [ ] Navigation hamburger menu works
  - [ ] Contact form usable on mobile
  - [ ] Mobile sticky CTA bar visible and functional
  - [ ] No horizontal scroll on any page

- [ ] **Security checks:**
  - [ ] Wordfence scan shows no malware
  - [ ] WordPress admin URL changed from `/wp-admin` (optional, security hardening)
  - [ ] Disable XML-RPC if not needed (WP Admin → Wordfence settings)

- [ ] **SSL check:**
  - [ ] Site loads on HTTPS with valid certificate
  - [ ] HTTP → HTTPS redirect active (no mixed content warnings)

- [ ] **Final backup:**
  - [ ] UpdraftPlus full backup completed before go-live

- [ ] **Go-live commit:**

  ```bash
  git add .
  git commit -m "feat: pre-launch checklist complete — site ready for go-live"
  ```

---

## Summary

| Phase | Tasks | Deliverable |
|-------|-------|-------------|
| Chunk 1 | 1–4 | WordPress foundation, child theme, global design system |
| Chunk 2 | 5–7 | Global header, footer, thank-you page |
| Chunk 3 | 8 | Homepage (all 8 sections) |
| Chunk 4 | 9–10 | Services Overview + About Us |
| Chunk 5 | 11–13 | Contact Us (with form) + Service Area |
| Chunk 6 | 14–16 | SEO config, performance, pre-launch checklist |
