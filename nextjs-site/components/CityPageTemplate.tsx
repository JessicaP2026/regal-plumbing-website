import type { ReactNode } from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { BUSINESS, SERVICES, CITIES, type City } from '@/lib/constants'
import { generateCitySchema, generateBreadcrumbSchema, generateFAQSchema } from '@/lib/schema'
import SchemaMarkup from './SchemaMarkup'
import HeroSection from './HeroSection'
import TrustBar from './TrustBar'
import FAQAccordion from './FAQAccordion'
import EmergencyCTABanner from './EmergencyCTABanner'

interface CityServiceDesc {
  slug: string
  description: string
}

interface CityFAQ {
  question: string
  answer: string
}

interface WhyCard {
  icon: string
  title: string
  description: string
}

interface CityPageTemplateProps {
  city: City
  introText: ReactNode[]
  serviceDescriptions: CityServiceDesc[]
  whyCards: WhyCard[]
  seoContent: string[]
  faqs: CityFAQ[]
  ctaHeading: string
  ctaSubtext: string
}

export default function CityPageTemplate({
  city,
  introText,
  serviceDescriptions,
  whyCards,
  seoContent,
  faqs,
  ctaHeading,
  ctaSubtext,
}: CityPageTemplateProps) {
  const servicesWithCityDesc = SERVICES.map((s) => {
    const cityDesc = serviceDescriptions.find((sd) => sd.slug === s.slug)
    return { ...s, description: cityDesc?.description || s.description }
  })

  return (
    <>
      <SchemaMarkup
        schema={[
          generateCitySchema(city),
          generateBreadcrumbSchema([
            { name: 'Home', url: BUSINESS.url },
            { name: 'Service Area', url: `${BUSINESS.url}/service-area` },
            { name: `${city.name} CA`, url: `${BUSINESS.url}/service-area/${city.slug}` },
          ]),
          generateFAQSchema(faqs),
        ]}
      />

      <HeroSection
        title={city.hero}
        subtitle={`Licensed, local plumbing services for ${city.name} homeowners and businesses - available 24/7 for emergencies and same-day scheduled work.`}
        breadcrumbs={[
          { label: 'Home', href: '/' },
          { label: 'Service Area', href: '/service-area' },
          { label: `${city.name} CA` },
        ]}
        navyBg
      />

      {/* Map + Intro */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-[1.2fr_1fr] gap-14 items-start">
            <div className="rounded-lg overflow-hidden shadow-lg h-[420px]">
              <iframe
                src={`https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d84000!2d${city.mapLng || BUSINESS.geo.lng}!3d${city.mapLat || BUSINESS.geo.lat}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1`}
                className="w-full h-full border-0"
                allowFullScreen
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                title={`Plumber in ${city.name} CA - Regal Plumbing Service Area`}
              />
            </div>
            <div>
              <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Your Local Plumber</p>
              <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
                Serving All of {city.name}, CA
              </h2>
              <div className="w-14 h-1 bg-red rounded mb-5" />
              {introText.map((p, i) => (
                <p key={i} className="text-[15.5px] text-gray-600 leading-relaxed mb-4">{p}</p>
              ))}
            </div>
          </div>
        </div>
      </section>

      <TrustBar />

      {/* Services */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">What We Do</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
              Plumbing Services in {city.name}, CA
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-[15px] text-gray-500 max-w-[520px] mx-auto mt-4 leading-relaxed">
              Full-service plumbing for every situation &mdash; from routine maintenance to major repairs throughout {city.name}.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {servicesWithCityDesc.map((s) => (
              <Link
                key={s.slug}
                href={`/${s.slug}`}
                className="group bg-white border border-gray-200 rounded-lg overflow-hidden transition-all duration-300 hover:-translate-y-1.5 hover:shadow-xl block"
              >
                <div className="h-[180px] overflow-hidden relative">
                  <Image
                    src={s.image}
                    alt={s.alt}
                    fill
                    className="object-cover transition-transform duration-400 group-hover:scale-105"
                    sizes="(max-width: 640px) 50vw, (max-width: 900px) 50vw, 25vw"
                    loading="lazy"
                  />
                </div>
                <div className="p-4 pb-5">
                  <h3 className="font-oswald font-semibold text-[17px] tracking-wide text-dark-grey mb-1.5">
                    {s.name} in {city.name}
                  </h3>
                  <p className="text-[13.5px] text-gray-500 leading-relaxed mb-3.5">{s.description}</p>
                  <span className="font-oswald font-medium text-[13px] tracking-wider uppercase text-red inline-flex items-center gap-1.5">
                    Learn More &rarr;
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose */}
      <section className="py-20 px-6 bg-navy">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red-light mb-2">Our Promise</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide text-white mb-3">
              Why {city.name} Residents Choose Regal
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {whyCards.map((card, i) => (
              <div key={i} className="text-center p-9 bg-white/[0.06] border border-white/10 rounded-lg hover:bg-white/10 hover:-translate-y-1 transition-all">
                <span className="text-[42px] block mb-4">{card.icon}</span>
                <h3 className="font-oswald font-semibold text-xl text-white uppercase tracking-wide mb-3">{card.title}</h3>
                <p className="text-[14.5px] text-blue-300 leading-relaxed">{card.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* SEO Content */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-[860px] mx-auto">
          <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Local Expertise</p>
          <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
            Trusted Plumber in {city.name} CA
          </h2>
          <div className="w-14 h-1 bg-red rounded mb-7" />
          <div className="text-[15.5px] text-gray-600 leading-relaxed space-y-4">
            {seoContent.map((p, i) => (
              <p key={i} dangerouslySetInnerHTML={{ __html: p }} />
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Common Questions</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
              {city.name} Plumbing FAQs
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <FAQAccordion faqs={faqs} />
        </div>
      </section>

      {/* Nearby Cities We Serve */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-10">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Service Area</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
              Nearby Cities We Serve
            </h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-[15px] text-gray-500 max-w-[500px] mx-auto mt-4 leading-relaxed">
              We cover the entire Inland Empire and San Gabriel Valley &mdash; with fast response times throughout the region.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {CITIES.filter((c) => c.slug !== city.slug).map((c) => (
              <Link
                key={c.slug}
                href={`/service-area/${c.slug}`}
                className="flex items-center gap-2.5 bg-white border border-gray-200 px-4 py-3 rounded hover:bg-red hover:border-red transition-colors group"
              >
                <div className="w-2 h-2 bg-red rounded-full flex-shrink-0 group-hover:bg-white transition-colors" />
                <span className="font-oswald font-medium text-[14.5px] tracking-wide text-dark-grey group-hover:text-white transition-colors">
                  Plumber in {c.name}, CA
                </span>
              </Link>
            ))}
          </div>
          <div className="text-center mt-8">
            <Link
              href="/service-area"
              className="inline-flex items-center gap-2 font-oswald font-semibold text-sm tracking-wider uppercase text-red border-b-2 border-transparent hover:border-red transition-all"
            >
              View Full Service Area &rarr;
            </Link>
          </div>
        </div>
      </section>

      <EmergencyCTABanner heading={ctaHeading} subtext={ctaSubtext} />
    </>
  )
}
