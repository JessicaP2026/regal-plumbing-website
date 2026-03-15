import Link from 'next/link'
import { BUSINESS, ALL_CITIES, CITIES } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import { generateBreadcrumbSchema } from '@/lib/schema'
import SchemaMarkup from '@/components/SchemaMarkup'
import HeroSection from '@/components/HeroSection'
import EmergencyCTABanner from '@/components/EmergencyCTABanner'

export const metadata = generatePageMetadata({
  title: 'Service Area \u2014 Regal Plumbing & Rooter | Inland Empire & San Gabriel Valley',
  description: 'Regal Plumbing serves 32+ cities in the Inland Empire & San Gabriel Valley. Fast, local plumbers available 24/7. Call (909) 600-4561.',
  path: '/service-area',
})

export default function ServiceAreaPage() {
  return (
    <>
      <SchemaMarkup
        schema={generateBreadcrumbSchema([
          { name: 'Home', url: BUSINESS.url },
          { name: 'Service Area', url: `${BUSINESS.url}/service-area` },
        ])}
      />

      <HeroSection
        title="Plumbing Services Across Southern California"
        subtitle="Serving 32+ cities in the Inland Empire and San Gabriel Valley \u2014 fast, local plumbers available 24/7."
        breadcrumbs={[{ label: 'Home', href: '/' }, { label: 'Service Area' }]}
        navyBg
      />

      {/* Map + Intro */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-[1.2fr_1fr] gap-14 items-start">
            <div className="rounded-lg overflow-hidden shadow-lg h-[420px]">
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d422147!2d-117.55!3d34.0!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1"
                className="w-full h-full border-0"
                allowFullScreen
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                title="Regal Plumbing Service Area"
              />
            </div>
            <div>
              <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Our Coverage</p>
              <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Your Local Plumbing Experts</h2>
              <div className="w-14 h-1 bg-red rounded mb-5" />
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-4">
                Regal Plumbing &amp; Rooter is based in Ontario, CA and serves a wide coverage area spanning the Inland Empire and San Gabriel Valley. Whether you&apos;re in Rancho Cucamonga, Pomona, Chino Hills, or anywhere in between &mdash; we have a technician near you.
              </p>
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-7">
                Our service area covers everything from emergency plumbing and drain cleaning to slab leak detection and water heater installation across 32 cities in Southern California.
              </p>
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-light-grey border-l-4 border-l-red rounded px-4.5 py-3.5">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none">32+</div>
                  <div className="text-xs text-gray-500 uppercase tracking-wide mt-0.5">Cities Covered</div>
                </div>
                <div className="bg-light-grey border-l-4 border-l-red rounded px-4.5 py-3.5">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none">24/7</div>
                  <div className="text-xs text-gray-500 uppercase tracking-wide mt-0.5">Emergency Service</div>
                </div>
                <div className="bg-light-grey border-l-4 border-l-red rounded px-4.5 py-3.5">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none">60<span className="text-lg">min</span></div>
                  <div className="text-xs text-gray-500 uppercase tracking-wide mt-0.5">Avg. Response Time</div>
                </div>
                <div className="bg-light-grey border-l-4 border-l-red rounded px-4.5 py-3.5">
                  <div className="font-oswald font-bold text-[28px] text-red leading-none">500+</div>
                  <div className="text-xs text-gray-500 uppercase tracking-wide mt-0.5">Jobs Completed</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Cities Grid */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Full Coverage List</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Cities We Serve</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-[15px] text-gray-500 max-w-[500px] mx-auto mt-4 leading-relaxed">
              Don&apos;t see your city? Call us &mdash; our service area is always expanding.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4">
            {ALL_CITIES.map((city) => {
              const cityData = CITIES.find((c) => c.name === city)
              const content = (
                <div className="flex items-center gap-2.5 bg-white border border-gray-200 px-4.5 py-3.5 hover:bg-red-50 hover:border-red-light transition-colors">
                  <div className="w-2 h-2 bg-red rounded-full flex-shrink-0" />
                  <span className="font-oswald font-medium text-[15px] text-dark-grey tracking-wide">{city}</span>
                </div>
              )
              return cityData ? (
                <Link key={city} href={`/service-area/${cityData.slug}`}>
                  {content}
                </Link>
              ) : (
                <div key={city}>{content}</div>
              )
            })}
          </div>
        </div>
      </section>

      {/* SEO Content */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-[860px] mx-auto">
          <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Fast, Local Plumbing</p>
          <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Fast, Local Plumbing You Can Count On</h2>
          <div className="w-14 h-1 bg-red rounded mb-7" />
          <div className="text-[15.5px] text-gray-600 leading-relaxed space-y-4">
            <p>When a plumbing problem strikes, the last thing you want is to wait hours for a technician from across the county. That&apos;s why <strong className="text-dark-grey">Regal Plumbing &amp; Rooter</strong> built our team around fast, local response &mdash; with technicians positioned throughout the <strong className="text-dark-grey">Inland Empire and San Gabriel Valley</strong> to reach you quickly, whether you&apos;re in <strong className="text-dark-grey">Rancho Cucamonga, Fontana, Ontario, Pomona</strong>, or any of the 32 cities we serve.</p>
            <p>Our services cover the full range of residential and commercial plumbing needs across Southern California. From <strong className="text-dark-grey">24/7 emergency plumbing</strong> and <strong className="text-dark-grey">drain cleaning</strong> to <strong className="text-dark-grey">slab leak detection</strong>, <strong className="text-dark-grey">water heater installation</strong>, and <strong className="text-dark-grey">hydrojetting</strong> &mdash; we bring expert, licensed service directly to your door.</p>
            <p>As a <strong className="text-dark-grey">family-owned, CA licensed business (License {BUSINESS.license})</strong>, we&apos;re deeply invested in the communities we serve. We know the plumbing challenges specific to Southern California &mdash; hard water buildup, aging infrastructure, and the unique demands of high-density residential areas.</p>
            <p>Need a plumber near you? <strong className="text-dark-grey">Call {BUSINESS.phone}</strong> &mdash; we&apos;re available 24 hours a day, 7 days a week, for emergencies and scheduled service alike.</p>
          </div>
        </div>
      </section>

      <EmergencyCTABanner
        heading="Need a Plumber in Your Area? We're Ready Now"
        subtext="Available 24/7 for emergency and scheduled service across 32+ cities"
      />
    </>
  )
}
