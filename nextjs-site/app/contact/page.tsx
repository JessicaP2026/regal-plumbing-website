import { BUSINESS } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import { generateBreadcrumbSchema } from '@/lib/schema'
import SchemaMarkup from '@/components/SchemaMarkup'
import HeroSection from '@/components/HeroSection'
import ContactForm from '@/components/ContactForm'
import EmergencyCTABanner from '@/components/EmergencyCTABanner'
import Link from 'next/link'

export const metadata = generatePageMetadata({
  title: 'Contact Us \u2014 Regal Plumbing & Rooter | Call (909) 600-4561',
  description: 'Contact Regal Plumbing & Rooter for 24/7 emergency plumbing or schedule service. Call (909) 600-4561 or fill out our contact form.',
  path: '/contact',
})

export default function ContactPage() {
  return (
    <>
      <SchemaMarkup
        schema={generateBreadcrumbSchema([
          { name: 'Home', url: BUSINESS.url },
          { name: 'Contact Us', url: `${BUSINESS.url}/contact` },
        ])}
      />

      <HeroSection
        title="Contact Regal Plumbing & Rooter"
        subtitle="Call now for immediate service or fill out the form below \u2014 we'll get back to you fast."
        breadcrumbs={[{ label: 'Home', href: '/' }, { label: 'Contact Us' }]}
      />

      <section className="py-20 px-6 bg-white">
        <div className="max-w-content mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-[1.1fr_1fr] gap-16 items-start">
            {/* Form Side */}
            <div>
              <h2 className="font-oswald font-bold text-[28px] text-dark-grey uppercase tracking-wide mb-1.5">
                Send Us a Message
              </h2>
              <p className="text-[15px] text-gray-500 mb-8 leading-relaxed">
                Fill out the form and we&apos;ll respond promptly. For emergencies, call us directly at{' '}
                <a href={`tel:${BUSINESS.phoneTel}`} className="text-red font-semibold">{BUSINESS.phone}</a>.
              </p>
              <ContactForm />
            </div>

            {/* Info Side */}
            <div>
              {/* Phone Box */}
              <div className="bg-navy rounded-lg p-8 text-center mb-7">
                <div className="font-oswald text-[13px] font-medium tracking-widest uppercase text-blue-300 mb-2">
                  For Fastest Service &mdash; Call Us
                </div>
                <a href={`tel:${BUSINESS.phoneTel}`} className="font-oswald font-bold text-[36px] text-white tracking-wider block mb-4">
                  {BUSINESS.phone}
                </a>
                <a
                  href={`tel:${BUSINESS.phoneTel}`}
                  className="flex items-center justify-center gap-2 w-full bg-red text-white font-oswald font-semibold text-[15px] uppercase tracking-wider py-3 rounded hover:bg-red-dark transition-colors"
                >
                  Call Now &mdash; We Answer 24/7
                </a>
              </div>

              {/* Info Blocks */}
              <div className="flex flex-col gap-4">
                <div className="flex gap-3.5 items-start p-4.5 bg-light-grey rounded-md border-l-4 border-l-red">
                  <span className="text-xl flex-shrink-0 mt-0.5">&#x1F4CD;</span>
                  <div>
                    <div className="font-oswald font-semibold text-sm uppercase tracking-wide text-dark-grey mb-1">Our Location</div>
                    <div className="text-[13.5px] text-gray-600 leading-relaxed">{BUSINESS.address.street}<br />{BUSINESS.address.city}, {BUSINESS.address.state} {BUSINESS.address.zip}</div>
                  </div>
                </div>
                <div className="flex gap-3.5 items-start p-4.5 bg-light-grey rounded-md border-l-4 border-l-red">
                  <span className="text-xl flex-shrink-0 mt-0.5">&#x2709;&#xFE0F;</span>
                  <div>
                    <div className="font-oswald font-semibold text-sm uppercase tracking-wide text-dark-grey mb-1">Email Us</div>
                    <div className="text-[13.5px] text-gray-600"><a href={`mailto:${BUSINESS.email}`} className="text-red hover:underline">{BUSINESS.email}</a></div>
                  </div>
                </div>
                <div className="flex gap-3.5 items-start p-4.5 bg-light-grey rounded-md border-l-4 border-l-red">
                  <span className="text-xl flex-shrink-0 mt-0.5">&#x1F550;</span>
                  <div>
                    <div className="font-oswald font-semibold text-sm uppercase tracking-wide text-dark-grey mb-1">Hours of Operation</div>
                    <div className="text-[13.5px] text-gray-600 leading-relaxed">
                      <strong>Emergency Line:</strong> {BUSINESS.hours.emergency}<br />
                      <strong>Office Hours:</strong> {BUSINESS.hours.office}<br />
                      <strong>Sunday:</strong> {BUSINESS.hours.sunday}
                    </div>
                  </div>
                </div>
                <div className="flex gap-3.5 items-start p-4.5 bg-light-grey rounded-md border-l-4 border-l-red">
                  <span className="text-xl flex-shrink-0 mt-0.5">&#x1F4CD;</span>
                  <div>
                    <div className="font-oswald font-semibold text-sm uppercase tracking-wide text-dark-grey mb-1">Service Area</div>
                    <div className="text-[13.5px] text-gray-600">
                      Serving 32+ cities across the Inland Empire &amp; San Gabriel Valley.{' '}
                      <Link href="/service-area" className="text-red hover:underline">View full list &rarr;</Link>
                    </div>
                  </div>
                </div>
                <div className="flex gap-3.5 items-start p-4.5 bg-light-grey rounded-md border-l-4 border-l-red">
                  <span className="text-xl flex-shrink-0 mt-0.5">&#x2705;</span>
                  <div>
                    <div className="font-oswald font-semibold text-sm uppercase tracking-wide text-dark-grey mb-1">License & Insurance</div>
                    <div className="text-[13.5px] text-gray-600">CA Contractor License {BUSINESS.license}<br />Fully licensed, bonded &amp; insured</div>
                  </div>
                </div>
              </div>

              {/* Mini Map */}
              <div className="rounded-md overflow-hidden mt-5 shadow-md h-[200px]">
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3308.5!2d-117.6!3d34.07!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMzTCsDA0JzE4LjAiTiAxMTfCsDM2JzAwLjAiVw!5e0!3m2!1sen!2sus!4v1"
                  className="w-full h-full border-0"
                  allowFullScreen
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Regal Plumbing location"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      <EmergencyCTABanner
        heading="Plumbing Emergency? Don't Wait \u2014 Call Now"
        subtext="We're available 24/7 for emergency plumbing across Southern California"
      />
    </>
  )
}
