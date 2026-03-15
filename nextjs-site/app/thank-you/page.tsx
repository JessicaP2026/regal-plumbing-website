import Link from 'next/link'
import { BUSINESS } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'

export const metadata = generatePageMetadata({
  title: 'Thank You - Regal Plumbing & Rooter',
  description: 'Thank you for contacting Regal Plumbing & Rooter. We will be in touch shortly.',
  path: '/thank-you',
  noindex: true,
})

export default function ThankYouPage() {
  return (
    <section className="py-24 px-6 bg-white text-center min-h-[60vh] flex items-center">
      <div className="max-w-[600px] mx-auto">
        <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-8">
          <svg className="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M5 13l4 4L19 7" />
          </svg>
        </div>

        <h1 className="font-oswald font-bold text-[clamp(28px,4vw,42px)] uppercase tracking-wide text-dark-grey mb-4">
          Thank You &mdash; We&apos;ll Be In Touch Shortly
        </h1>

        <p className="text-base text-gray-500 mb-10 leading-relaxed">
          Your message has been received. A member of our team will respond within 1 business hour during operating hours.
        </p>

        <div className="bg-light-grey rounded-lg p-8 mb-10">
          <h2 className="font-oswald font-semibold text-lg uppercase tracking-wide text-dark-grey mb-6">What Happens Next</h2>
          <div className="flex flex-col gap-5 text-left max-w-[400px] mx-auto">
            <div className="flex items-start gap-4">
              <div className="w-8 h-8 bg-red text-white rounded-full flex items-center justify-center font-oswald font-bold text-sm flex-shrink-0">1</div>
              <div>
                <div className="font-oswald font-semibold text-sm text-dark-grey">We Review Your Request</div>
                <p className="text-[13px] text-gray-500">Our team reads your message and assigns the right technician.</p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="w-8 h-8 bg-red text-white rounded-full flex items-center justify-center font-oswald font-bold text-sm flex-shrink-0">2</div>
              <div>
                <div className="font-oswald font-semibold text-sm text-dark-grey">We Call or Text You Back</div>
                <p className="text-[13px] text-gray-500">Expect a call or text within 1 business hour to discuss your needs.</p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="w-8 h-8 bg-red text-white rounded-full flex items-center justify-center font-oswald font-bold text-sm flex-shrink-0">3</div>
              <div>
                <div className="font-oswald font-semibold text-sm text-dark-grey">We Schedule & Solve</div>
                <p className="text-[13px] text-gray-500">We book a convenient time and arrive ready to fix your plumbing problem.</p>
              </div>
            </div>
          </div>
        </div>

        <p className="text-base text-gray-500 mb-6">
          Need immediate help? Call us directly:
        </p>
        <a
          href={`tel:${BUSINESS.phoneTel}`}
          className="inline-flex items-center gap-2 bg-red text-white font-oswald font-bold text-xl uppercase tracking-wider px-8 py-4 rounded hover:bg-red-dark transition-colors"
        >
          {BUSINESS.phone}
        </a>

        <div className="mt-10">
          <Link href="/" className="font-oswald font-medium text-sm tracking-wider uppercase text-red hover:text-red-dark transition-colors">
            &larr; Return to Homepage
          </Link>
        </div>
      </div>
    </section>
  )
}
