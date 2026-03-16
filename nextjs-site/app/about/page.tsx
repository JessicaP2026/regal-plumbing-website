import Image from 'next/image'
import Link from 'next/link'
import { BUSINESS, CITIES } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import { generateBreadcrumbSchema } from '@/lib/schema'
import SchemaMarkup from '@/components/SchemaMarkup'
import HeroSection from '@/components/HeroSection'
import EmergencyCTABanner from '@/components/EmergencyCTABanner'

export const metadata = generatePageMetadata({
  title: 'About Us - Regal Plumbing & Rooter',
  description: 'Family-owned plumbing company in Ontario, CA. Licensed, insured, and serving 32+ cities across the Inland Empire & San Gabriel Valley since 2022.',
  path: '/about',
})

const TEAM = [
  { name: 'Brayden', role: 'Plumbing Technician', image: '/images/regal-plumber-brayden-ontario-ca.webp' },
  { name: 'Tony', role: 'Plumbing Technician', image: '/images/regal-plumber-tony-ontario-ca.webp' },
  { name: 'Ashton', role: 'Plumbing Technician', image: '/images/regal-plumber-ashton-ontario-ca.webp' },
  { name: 'Nick', role: 'Plumbing Technician', image: '/images/regal-plumber-nick-ontario-ca.webp' },
  { name: 'Natalie', role: 'Office Manager', image: '/images/regal-plumbing-office-natalie-ontario-ca.webp' },
]

const VALUES = [
  { icon: '\uD83E\uDD1D', title: 'Honesty & Transparency', desc: 'We believe every customer deserves clear, upfront pricing and honest advice - even when that means recommending a less expensive solution. We never upsell work that isn\u2019t needed.' },
  { icon: '\uD83D\uDD27', title: 'Quality Craftsmanship', desc: 'We take pride in doing the job right the first time. Our work is done to last, using quality materials and proven techniques. We stand behind everything we install or repair.' },
  { icon: '\u2764\uFE0F', title: 'Community Commitment', desc: 'We\u2019re not just serving homes - we\u2019re building relationships in the communities where we live and work. Supporting our neighbors is at the heart of everything Regal does.' },
]

const CREDENTIALS = [
  { icon: '\uD83D\uDCCB', title: "California Contractor's License #1097482", desc: 'Fully licensed by the California Contractors State License Board (CSLB). Our license number is verifiable at cslb.ca.gov. We maintain all required continuing education and renewals.' },
  { icon: '\uD83D\uDEE1\uFE0F', title: 'Fully Insured & Bonded', desc: 'Regal Plumbing & Rooter carries comprehensive general liability insurance and workers\u2019 compensation coverage, protecting you and your property on every job.' },
  { icon: '\uD83D\uDC68\u200D\uD83D\uDC69\u200D\uD83D\uDC67', title: 'Family Owned & Operated', desc: 'We are a locally owned, family-operated business - not a franchise or corporate chain. Every decision is made with our customers and community in mind, not shareholder returns.' },
  { icon: '\u23F0', title: '24/7 Emergency Availability', desc: 'Plumbing emergencies don\u2019t follow business hours. Our team is on-call around the clock, every day of the year, ready to respond when you need help most.' },
  { icon: '\uD83D\uDCCD', title: 'Locally Based in Ontario, CA', desc: 'Our shop is located at 2141 E Philadelphia St, Suite R, Ontario, CA 91761 - right in the heart of the Inland Empire. Local means fast response and community accountability.' },
  { icon: '\u2B50', title: '4+ Years of Proven Service', desc: 'Since our founding, we\u2019ve built a track record of five-star reviews and satisfied customers across Southern California. Our reputation is built one job at a time.' },
]

export default function AboutPage() {
  return (
    <>
      <SchemaMarkup
        schema={generateBreadcrumbSchema([
          { name: 'Home', url: BUSINESS.url },
          { name: 'About Us', url: `${BUSINESS.url}/about` },
        ])}
      />

      <HeroSection
        title="About Regal Plumbing & Rooter"
        subtitle="A family-owned plumbing company built on honesty, craftsmanship, and community service across Southern California."
        breadcrumbs={[{ label: 'Home', href: '/' }, { label: 'About Us' }]}
        navyBg
      />

      {/* Our Story */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-[1fr_1.4fr] gap-16 items-center">
            <div>
              <Image
                src="/images/regal-plumbing-rooter-office-ontario-ca.webp"
                alt="Regal Plumbing & Rooter - Ontario, CA Office"
                width={600}
                height={400}
                className="rounded-lg shadow-xl w-full"
              />
              <div className="grid grid-cols-3 gap-4 mt-6">
                <div className="bg-light-grey border border-gray-200 border-t-[3px] border-t-red rounded-md p-4 text-center">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none mb-1">32+</div>
                  <div className="text-[11.5px] text-gray-500">Cities Served</div>
                </div>
                <div className="bg-light-grey border border-gray-200 border-t-[3px] border-t-red rounded-md p-4 text-center">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none mb-1">4+</div>
                  <div className="text-[11.5px] text-gray-500">Years in Business</div>
                </div>
                <div className="bg-light-grey border border-gray-200 border-t-[3px] border-t-red rounded-md p-4 text-center">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none mb-1">24/7</div>
                  <div className="text-[11.5px] text-gray-500">Emergency Service</div>
                </div>
              </div>
            </div>
            <div>
              <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Our Story</p>
              <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Who We Are</h2>
              <div className="w-14 h-1 bg-red rounded mb-6" />
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-4">
                Regal Plumbing &amp; Rooter was founded with one clear goal: to bring honesty, professionalism, and premium craftsmanship to every customer we serve. We saw a gap in the market &mdash; too many homeowners were being overcharged, under-informed, and left frustrated by plumbers who didn&apos;t treat them with respect. We set out to change that.
              </p>
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-4">
                As a family-owned business based in Ontario, CA, we take pride in building real relationships with our customers. When you call Regal, you&apos;re not calling a call center &mdash; you&apos;re calling a local team that genuinely cares about your home and your family&apos;s wellbeing. We treat every job as if it were our own home.
              </p>
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-4">
                Licensed, insured, and serving over 32 cities across the Inland Empire and San Gabriel Valley, Regal Plumbing &amp; Rooter has become a trusted name in Southern California plumbing. From routine drain cleaning to complex slab leak repairs, we bring the same dedication to quality to every call.
              </p>
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-6">
                We proudly serve{' '}
                {CITIES.slice(0, 4).map((city, i) => (
                  <span key={city.slug}>
                    <Link href={`/service-area/${city.slug}`} className="text-red font-medium hover:underline">
                      {city.name}
                    </Link>
                    {i < 3 ? ', ' : ''}
                  </span>
                ))}
                {' '}and dozens more communities across Southern California. Visit our{' '}
                <Link href="/service-area" className="text-red font-medium hover:underline">
                  full service area page
                </Link>{' '}
                to find your city.
              </p>
              <div className="flex flex-wrap items-center gap-4">
                <a
                  href={`tel:${BUSINESS.phoneTel}`}
                  className="inline-flex items-center gap-2 bg-red text-white border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red-dark hover:border-red-dark hover:-translate-y-0.5 transition-all"
                >
                  Call Us Today
                </a>
                <Link
                  href="/services"
                  className="font-oswald font-medium text-sm tracking-wider uppercase text-red inline-flex items-center gap-1.5 border-b-2 border-transparent hover:border-red transition-all"
                >
                  View Our Services &rarr;
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Core Values */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">What Drives Us</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Our Core Values</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-base text-gray-500 max-w-[500px] mx-auto mt-4 leading-relaxed">
              Everything we do is guided by three foundational principles that we&apos;ve never compromised on.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-7">
            {VALUES.map((v, i) => (
              <div key={i} className="bg-white rounded-lg border border-gray-200 p-9 text-center hover:-translate-y-1.5 hover:shadow-lg transition-all">
                <span className="text-[48px] block mb-4">{v.icon}</span>
                <h3 className="font-oswald font-semibold text-[19px] text-dark-grey mb-2.5">{v.title}</h3>
                <p className="text-sm text-gray-500 leading-relaxed">{v.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Credentials */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Verified & Trusted</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Our Credentials</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {CREDENTIALS.map((c, i) => (
              <div key={i} className="flex items-start gap-5 bg-light-grey border border-gray-200 border-l-[5px] border-l-red rounded-lg p-6 hover:shadow-md transition-shadow">
                <span className="text-[32px] flex-shrink-0">{c.icon}</span>
                <div>
                  <h3 className="font-oswald font-semibold text-base text-dark-grey mb-1">{c.title}</h3>
                  <p className="text-[13.5px] text-gray-500 leading-relaxed">{c.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Meet the Team */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">The People Behind the Work</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Meet Our Team</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-base text-gray-500 max-w-[500px] mx-auto mt-4 leading-relaxed">
              Skilled, licensed, and genuinely committed to doing right by every customer.
            </p>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-8">
            {TEAM.map((member) => (
              <div key={member.name} className="text-center">
                <div className="relative w-full aspect-[3/4] rounded-lg overflow-hidden mb-3.5">
                  <Image
                    src={member.image}
                    alt={`${member.name} - ${member.role}`}
                    fill
                    className="object-cover object-top"
                    sizes="(max-width: 640px) 50vw, (max-width: 900px) 33vw, 20vw"
                  />
                </div>
                <div className="font-oswald font-semibold text-[17px] text-dark-grey uppercase tracking-wide">
                  {member.name}
                </div>
                <div className="text-[13px] text-gray-500 mt-0.5">{member.role}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* The Regal Promise */}
      <section className="py-20 px-6 bg-dark-grey">
        <div className="max-w-content mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red-light mb-2">Our Commitment to You</p>
              <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide text-white mb-3">The Regal Promise</h2>
              <div className="w-14 h-1 bg-red rounded mb-7" />
              <ul className="flex flex-col gap-5">
                {[
                  { icon: '\uD83D\uDCB0', title: 'Upfront Pricing - Always', desc: 'You\u2019ll know the full cost before we begin any work. No hidden fees, no surprise invoices. Our quotes are clear and honest.' },
                  { icon: '\uD83C\uDFAF', title: 'First-Time Fixes', desc: 'We properly diagnose problems before starting work, so we fix it right the first time - saving you time and money.' },
                  { icon: '\uD83E\uDDF9', title: 'Respect for Your Home', desc: 'Our technicians wear shoe covers, protect your floors, and leave the work area cleaner than we found it. Always.' },
                  { icon: '\uD83D\uDCDE', title: 'Real People, Real Answers', desc: 'When you call us, a real person answers. We communicate clearly at every step and follow up after the job is done.' },
                ].map((item, i) => (
                  <li key={i} className="flex items-start gap-4">
                    <span className="text-[28px] flex-shrink-0 mt-0.5">{item.icon}</span>
                    <div>
                      <h3 className="font-oswald font-semibold text-[17px] text-white mb-1">{item.title}</h3>
                      <p className="text-sm text-gray-400 leading-relaxed">{item.desc}</p>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
            <div className="bg-white/[0.04] border border-white/[0.08] rounded-lg p-10">
              <h3 className="font-oswald font-bold text-[22px] text-white tracking-wide mb-5">A Note From Our Family</h3>
              <p className="text-[17px] text-gray-300 leading-relaxed italic pl-5 border-l-4 border-red">
                &ldquo;When we started Regal Plumbing &amp; Rooter, we made a promise to every customer: we would treat your home the way we treat our own. That means honest advice, quality work, and being there when you need us most. That promise hasn&apos;t changed &mdash; and it never will.&rdquo;
              </p>
              <div className="mt-6 font-oswald font-medium text-[15px] text-red-light tracking-wide">
                &mdash; The Regal Plumbing &amp; Rooter Team
              </div>
            </div>
          </div>
        </div>
      </section>

      <EmergencyCTABanner
        heading="Ready to Work With Us?"
        subtext="Call now for a free quote - or reach out anytime for emergency service"
      />
    </>
  )
}
