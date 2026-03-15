import { BUSINESS } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import HeroSection from '@/components/HeroSection'

export const metadata = generatePageMetadata({
  title: 'Terms of Service - Regal Plumbing & Rooter',
  description: 'Terms of service for Regal Plumbing & Rooter. Read about our service agreements, warranties, and policies.',
  path: '/terms-of-service',
})

export default function TermsOfServicePage() {
  return (
    <>
      <HeroSection
        title="Terms of Service"
        subtitle="Please read these terms carefully before using our services."
        breadcrumbs={[{ label: 'Home', href: '/' }, { label: 'Terms of Service' }]}
      />

      <section className="py-20 px-6 bg-white">
        <div className="max-w-[860px] mx-auto">
          <p className="text-sm text-gray-500 mb-8">Last updated: January 1, 2025</p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">1. Acceptance of Terms</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            By accessing our website or using our plumbing services, you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use our website or services.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">2. Services</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            {BUSINESS.name} provides residential and commercial plumbing services throughout the Inland Empire and San Gabriel Valley regions of Southern California. All services are performed by licensed, insured plumbing professionals.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">3. Service Agreements</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            Specific service terms, pricing, and scope of work are agreed upon between {BUSINESS.name} and the customer prior to commencing work. Any changes to the agreed scope require mutual consent.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">4. Estimates & Pricing</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We provide upfront pricing before beginning any work. Estimates are based on our assessment of the work required. If additional work is discovered during service, we will inform you and obtain approval before proceeding.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">5. Payment</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            Payment is due upon completion of services unless otherwise agreed in writing. We accept cash, checks, and all major credit cards.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">6. Warranties</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We stand behind our work. Specific warranty terms vary by service type and will be communicated at the time of service. Warranties cover workmanship and may include parts warranties from manufacturers.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">7. Limitation of Liability</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            {BUSINESS.name}&apos;s liability is limited to the cost of the services provided. We are not liable for pre-existing conditions, consequential damages, or issues arising from factors beyond our control.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">8. Property Access</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            By scheduling service, you grant our technicians access to the areas of your property necessary to perform the requested work. You are responsible for clearing access to work areas and informing us of any known hazards.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">9. Cancellation</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            Appointments can be cancelled or rescheduled with reasonable notice. Emergency service cancellations may be subject to a service call fee if a technician has already been dispatched.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">10. Governing Law</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            These terms are governed by the laws of the State of California. Any disputes shall be resolved in the courts of San Bernardino County, California.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">11. Website Use</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            The content on this website is for informational purposes only. While we strive to keep information current and accurate, we make no warranties about the completeness, reliability, or accuracy of this information.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">12. Changes to Terms</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We reserve the right to update these Terms of Service at any time. Changes will be posted on this page with an updated date.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">13. Contact</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed">
            For questions about these Terms of Service, contact us at:<br /><br />
            {BUSINESS.name}<br />
            {BUSINESS.address.street}<br />
            {BUSINESS.address.city}, {BUSINESS.address.state} {BUSINESS.address.zip}<br />
            Phone: {BUSINESS.phone}<br />
            Email: {BUSINESS.email}
          </p>
        </div>
      </section>
    </>
  )
}
