import { BUSINESS } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import HeroSection from '@/components/HeroSection'

export const metadata = generatePageMetadata({
  title: 'Privacy Policy \u2014 Regal Plumbing & Rooter',
  description: 'Privacy policy for Regal Plumbing & Rooter. Learn how we collect, use, and protect your personal information.',
  path: '/privacy-policy',
})

export default function PrivacyPolicyPage() {
  return (
    <>
      <HeroSection
        title="Privacy Policy"
        subtitle="How we collect, use, and protect your personal information."
        breadcrumbs={[{ label: 'Home', href: '/' }, { label: 'Privacy Policy' }]}
      />

      <section className="py-20 px-6 bg-white">
        <div className="max-w-[860px] mx-auto prose prose-gray max-w-none">
          <p className="text-sm text-gray-500 mb-8">Last updated: January 1, 2025</p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">1. Introduction</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            {BUSINESS.name} (&ldquo;we,&rdquo; &ldquo;us,&rdquo; or &ldquo;our&rdquo;) respects your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or use our services.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">2. Information We Collect</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We may collect personal information that you voluntarily provide when using our website, including your name, phone number, email address, city, and service details when you submit our contact form.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">3. Contact Forms</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            When you submit a contact form on our website, we collect your name, phone number, email (if provided), city, service needed, and message. This information is used solely to respond to your inquiry and provide plumbing services.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">4. Cookies & Tracking</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            Our website may use cookies and similar tracking technologies to improve your browsing experience and analyze site traffic. You can control cookies through your browser settings.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">5. Google Analytics</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We may use Google Analytics to analyze website traffic and usage patterns. Google Analytics collects anonymous data about how visitors use our site. For more information, see Google&apos;s Privacy Policy.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">6. How We Use Your Information</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We use collected information to: respond to your inquiries and service requests, provide and maintain our plumbing services, communicate with you about appointments and service updates, improve our website and services, and comply with legal obligations.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">7. Information Sharing</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We do not sell, trade, or rent your personal information to third parties. We may share information with service providers who assist us in operating our website and conducting our business, provided they agree to keep this information confidential.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">8. Data Security</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We implement reasonable security measures to protect your personal information. However, no method of transmission over the internet or electronic storage is 100% secure.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">9. Your Rights</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            You have the right to access, correct, or delete your personal information. To exercise these rights, contact us at {BUSINESS.email} or call {BUSINESS.phone}.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">10. California Privacy Rights (CCPA)</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            California residents have additional rights under the California Consumer Privacy Act (CCPA), including the right to know what personal information we collect, the right to delete personal information, and the right to opt-out of the sale of personal information. We do not sell personal information.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">11. Children&apos;s Privacy</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            Our website is not directed to children under 13. We do not knowingly collect personal information from children under 13.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">12. Changes to This Policy</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            We may update this Privacy Policy from time to time. Changes will be posted on this page with an updated revision date.
          </p>

          <h2 className="font-oswald font-bold text-xl uppercase tracking-wide text-dark-grey mt-10 mb-4">13. Contact Us</h2>
          <p className="text-[15px] text-gray-600 leading-relaxed mb-4">
            If you have questions about this Privacy Policy, contact us at:
          </p>
          <p className="text-[15px] text-gray-600 leading-relaxed">
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
