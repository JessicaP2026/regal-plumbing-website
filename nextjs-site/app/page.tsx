import Image from 'next/image'
import Link from 'next/link'
import { BUSINESS, SERVICES, REVIEWS, FAQS_HOME } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import { generateFAQSchema } from '@/lib/schema'
import SchemaMarkup from '@/components/SchemaMarkup'
import TrustBar from '@/components/TrustBar'
import ServiceCard from '@/components/ServiceCard'
import ReviewCard from '@/components/ReviewCard'
import FAQAccordion from '@/components/FAQAccordion'
import EmergencyCTABanner from '@/components/EmergencyCTABanner'

export const metadata = generatePageMetadata({
  title: `${BUSINESS.name} \u2014 24/7 Plumber | Inland Empire & San Gabriel Valley`,
  description: 'Licensed 24/7 plumber serving 32+ cities in the Inland Empire & San Gabriel Valley. Emergency plumbing, drain cleaning, slab leak detection & more. Call (909) 600-4561.',
  path: '/',
})

export default function HomePage() {
  return (
    <>
      <SchemaMarkup schema={generateFAQSchema(FAQS_HOME)} />

      {/* Hero */}
      <section className="relative overflow-hidden min-h-[480px] flex items-center">
        <Image
          src="/images/sewer-repair-service-truck-inland-empire.webp"
          alt="Regal Plumbing service truck"
          fill
          className="object-cover"
          priority
          sizes="100vw"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-black/85 via-navy/65 to-red/25" />
        <div className="relative z-10 max-w-content mx-auto px-6 py-20 w-full">
          <span className="inline-block bg-red text-white font-oswald font-semibold text-xs tracking-widest uppercase px-3.5 py-1.5 rounded mb-4">
            24/7 Emergency Service
          </span>
          <h1 className="font-oswald font-bold text-[clamp(32px,5vw,56px)] text-white uppercase tracking-wider mb-4 max-w-[700px] leading-tight">
            Your Trusted Local Plumber in Southern California
          </h1>
          <p className="text-lg text-gray-300 max-w-[550px] mb-8 leading-relaxed">
            Licensed, family-owned plumbing for the Inland Empire &amp; San Gabriel Valley. Fast response, honest pricing, quality work &mdash; every time.
          </p>
          <div className="flex flex-wrap gap-3">
            <a
              href={`tel:${BUSINESS.phoneTel}`}
              className="inline-flex items-center gap-2 bg-red text-white border-2 border-red font-oswald font-semibold text-[15px] uppercase tracking-wider px-7 py-3 rounded hover:bg-red-dark hover:border-red-dark hover:-translate-y-0.5 transition-all"
            >
              Call Now &mdash; {BUSINESS.phone}
            </a>
            <Link
              href="/contact"
              className="inline-flex items-center gap-2 bg-transparent text-white border-2 border-white font-oswald font-semibold text-[15px] uppercase tracking-wider px-7 py-3 rounded hover:bg-white hover:text-red hover:-translate-y-0.5 transition-all"
            >
              Get a Free Quote
            </Link>
          </div>
        </div>
      </section>

      {/* Trust Bar */}
      <TrustBar />

      {/* Services Grid */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">
              What We Do
            </p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
              Our Plumbing Services
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-base text-gray-500 max-w-[520px] mx-auto mt-4 leading-relaxed">
              From emergency repairs to planned installations &mdash; our licensed technicians handle it all.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {SERVICES.map((s) => (
              <ServiceCard key={s.slug} {...s} />
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Regal */}
      <section className="py-20 px-6 bg-dark-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red-light mb-2">
              Our Promise
            </p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide text-white mb-3">
              Why Choose Regal?
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-9 bg-white/[0.04] border border-white/[0.08] rounded-lg hover:bg-white/[0.08] hover:-translate-y-1 transition-all">
              <span className="text-[40px] block mb-3.5">&#x1F4B0;</span>
              <h3 className="font-oswald font-semibold text-[19px] text-white mb-2.5">Honest Pricing</h3>
              <p className="text-sm text-gray-400 leading-relaxed">Upfront, transparent quotes before any work begins. No hidden fees, no surprises.</p>
            </div>
            <div className="text-center p-9 bg-white/[0.04] border border-white/[0.08] rounded-lg hover:bg-white/[0.08] hover:-translate-y-1 transition-all">
              <span className="text-[40px] block mb-3.5">&#x26A1;</span>
              <h3 className="font-oswald font-semibold text-[19px] text-white mb-2.5">Fast Response</h3>
              <p className="text-sm text-gray-400 leading-relaxed">24/7 availability for emergencies. We arrive quickly and work efficiently.</p>
            </div>
            <div className="text-center p-9 bg-white/[0.04] border border-white/[0.08] rounded-lg hover:bg-white/[0.08] hover:-translate-y-1 transition-all">
              <span className="text-[40px] block mb-3.5">&#x1F527;</span>
              <h3 className="font-oswald font-semibold text-[19px] text-white mb-2.5">Quality Workmanship</h3>
              <p className="text-sm text-gray-400 leading-relaxed">Every job backed by our commitment to premium craftsmanship and lasting results.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Reviews */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">
              Customer Reviews
            </p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
              What Our Customers Say
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {REVIEWS.map((r, i) => (
              <ReviewCard key={i} {...r} />
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">
              Common Questions
            </p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
              Frequently Asked Questions
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <FAQAccordion faqs={FAQS_HOME} />
        </div>
      </section>

      {/* Emergency CTA */}
      <EmergencyCTABanner
        heading="Plumbing Emergency? Don't Wait"
        subtext="Our emergency team is standing by 24/7 \u2014 including weekends and holidays"
      />
    </>
  )
}
