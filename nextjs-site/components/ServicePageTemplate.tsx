import type { ReactNode } from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { BUSINESS, SERVICES, CITIES } from '@/lib/constants'
import SchemaMarkup from './SchemaMarkup'
import HeroSection from './HeroSection'
import EmergencyCTABanner from './EmergencyCTABanner'
import { generateServiceSchema, generateBreadcrumbSchema } from '@/lib/schema'

interface CoverCard {
  icon: string
  title: string
  description: string
}

interface GalleryPhoto {
  src: string
  alt: string
  caption: string
}

interface ServicePageTemplateProps {
  slug: string
  heroTitle: string
  heroSubtitle: string
  badge: string
  heroImage: string
  overviewEyebrow: string
  overviewTitle: string
  overviewBody: ReactNode
  overviewFeatures: string[]
  overviewImage: string
  overviewImageAlt: string
  covers: CoverCard[]
  galleryHeading?: string
  photoGallery?: GalleryPhoto[]
  ctaHeading: string
  ctaSubtext: string
}

export default function ServicePageTemplate({
  slug,
  heroTitle,
  heroSubtitle,
  badge,
  heroImage,
  overviewEyebrow,
  overviewTitle,
  overviewBody,
  overviewFeatures,
  overviewImage,
  overviewImageAlt,
  covers,
  galleryHeading,
  photoGallery,
  ctaHeading,
  ctaSubtext,
}: ServicePageTemplateProps) {
  const otherServices = SERVICES.filter((s) => s.slug !== slug)

  return (
    <>
      <SchemaMarkup
        schema={[
          generateServiceSchema(slug)!,
          generateBreadcrumbSchema([
            { name: 'Home', url: BUSINESS.url },
            { name: 'Services', url: `${BUSINESS.url}/services` },
            { name: heroTitle, url: `${BUSINESS.url}/${slug}` },
          ]),
        ]}
      />

      <HeroSection
        title={heroTitle}
        subtitle={heroSubtitle}
        badge={badge}
        bgImage={heroImage}
        breadcrumbs={[
          { label: 'Home', href: '/' },
          { label: 'Services', href: '/services' },
          { label: heroTitle },
        ]}
      />

      {/* Overview */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">{overviewEyebrow}</p>
              <h2 className="font-oswald font-bold text-[clamp(24px,3vw,38px)] uppercase tracking-wide mb-3">{overviewTitle}</h2>
              <div className="w-14 h-1 bg-red rounded mb-6" />
              <p className="text-[15.5px] text-gray-600 leading-relaxed mb-5">{overviewBody}</p>
              <ul className="flex flex-col gap-2.5 mb-7">
                {overviewFeatures.map((f, i) => (
                  <li key={i} className="flex items-start gap-2.5 text-[15px] text-dark-grey">
                    <span className="text-red font-bold flex-shrink-0 mt-0.5">&#x2713;</span>
                    {f}
                  </li>
                ))}
              </ul>
              <a
                href={`tel:${BUSINESS.phoneTel}`}
                className="inline-flex items-center gap-2 bg-red text-white border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red-dark hover:border-red-dark transition-all"
              >
                Call Now &mdash; {BUSINESS.phone}
              </a>
            </div>
            <div className="relative rounded-lg overflow-hidden shadow-xl h-[420px]">
              <Image
                src={overviewImage}
                alt={overviewImageAlt}
                fill
                className="object-cover"
                sizes="(max-width: 900px) 100vw, 50vw"
              />
            </div>
          </div>
        </div>
      </section>

      {/* What We Cover */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">What We Cover</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Services We Provide</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-7">
            {covers.map((c, i) => (
              <div key={i} className="bg-white rounded-lg p-7 border-t-[3px] border-t-red shadow-sm">
                <span className="text-[28px] block mb-3.5">{c.icon}</span>
                <h3 className="font-oswald font-semibold text-base uppercase tracking-wide text-dark-grey mb-2">{c.title}</h3>
                <p className="text-sm text-gray-500 leading-relaxed">{c.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Photo Gallery (optional) */}
      {photoGallery && photoGallery.length > 0 && (
        <section className="py-20 px-6 bg-light-grey">
          <div className="max-w-content mx-auto">
            <div className="text-center mb-12">
              <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Recent Work</p>
              <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide text-dark-grey mb-3">
                {galleryHeading || 'Our Recent Work'}
              </h2>
              <div className="w-14 h-1 bg-red rounded mx-auto" />
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
              {photoGallery.map((photo, i) => (
                <div key={i} className="group rounded-lg overflow-hidden bg-white border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all">
                  <div className="overflow-hidden">
                    <Image
                      src={photo.src}
                      alt={photo.alt}
                      width={600}
                      height={400}
                      className="w-full object-cover transition-transform duration-500 group-hover:scale-105"
                    />
                  </div>
                  <div className="px-5 py-3.5 flex items-center gap-2.5 border-t-[3px] border-t-red">
                    <p className="font-oswald font-medium text-[14.5px] text-dark-grey tracking-wide">{photo.caption}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Why Choose Regal */}
      <section className="py-20 px-6 bg-navy">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red-light mb-2">Our Promise</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide text-white mb-3">Why Choose Regal?</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-8">
              <span className="text-[36px] block mb-4">&#x1F4B0;</span>
              <h3 className="font-oswald font-semibold text-lg text-white uppercase tracking-wide mb-2.5">Honest Pricing</h3>
              <p className="text-sm text-blue-300 leading-relaxed">Upfront, transparent quotes before any work begins. No hidden fees, no surprises &mdash; even in emergencies.</p>
            </div>
            <div className="text-center p-8">
              <span className="text-[36px] block mb-4">&#x26A1;</span>
              <h3 className="font-oswald font-semibold text-lg text-white uppercase tracking-wide mb-2.5">Fast Response</h3>
              <p className="text-sm text-blue-300 leading-relaxed">24/7 availability for emergencies. We arrive quickly and work efficiently to minimize damage.</p>
            </div>
            <div className="text-center p-8">
              <span className="text-[36px] block mb-4">&#x1F527;</span>
              <h3 className="font-oswald font-semibold text-lg text-white uppercase tracking-wide mb-2.5">Quality Workmanship</h3>
              <p className="text-sm text-blue-300 leading-relaxed">Every job backed by our commitment to premium craftsmanship and lasting results.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Other Services */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Explore</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Other Services We Offer</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-5">
            {otherServices.map((s) => (
              <Link
                key={s.slug}
                href={`/${s.slug}`}
                className="bg-light-grey border border-gray-200 rounded-lg p-5 hover:shadow-lg hover:border-red transition-all block"
              >
                <h3 className="font-oswald font-semibold text-[15px] uppercase tracking-wide text-dark-grey mb-1.5">{s.name}</h3>
                <p className="text-[13px] text-gray-500 leading-relaxed mb-3">{s.description}</p>
                <span className="font-oswald font-medium text-xs tracking-wider uppercase text-red">Learn More &rarr;</span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Cities We Serve */}
      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-10">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Service Coverage</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Cities We Serve</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-[15px] text-gray-500 max-w-[500px] mx-auto mt-4 leading-relaxed">
              We provide fast, local plumbing service throughout the Inland Empire and San Gabriel Valley.
            </p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {CITIES.map((city) => (
              <Link
                key={city.slug}
                href={`/service-area/${city.slug}`}
                className="flex items-center gap-2.5 bg-white border border-gray-200 px-4 py-3 rounded hover:bg-red hover:border-red hover:text-white transition-colors group"
              >
                <div className="w-2 h-2 bg-red rounded-full flex-shrink-0 group-hover:bg-white transition-colors" />
                <span className="font-oswald font-medium text-[14.5px] tracking-wide text-dark-grey group-hover:text-white transition-colors">
                  Plumber in {city.name}, CA
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      <EmergencyCTABanner heading={ctaHeading} subtext={ctaSubtext} />
    </>
  )
}
