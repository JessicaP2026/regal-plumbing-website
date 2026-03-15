import Link from 'next/link'
import { BUSINESS } from '@/lib/constants'

export default function NotFound() {
  return (
    <section className="py-24 px-6 bg-white text-center min-h-[60vh] flex items-center">
      <div className="max-w-[600px] mx-auto">
        <div className="font-oswald font-bold text-[120px] text-red leading-none mb-4">404</div>
        <h1 className="font-oswald font-bold text-[clamp(24px,3vw,36px)] uppercase tracking-wide text-dark-grey mb-4">
          Page Not Found
        </h1>
        <p className="text-base text-gray-500 mb-8 leading-relaxed">
          Sorry, the page you&apos;re looking for doesn&apos;t exist or has been moved. Let us help you find what you need.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link
            href="/"
            className="inline-flex items-center justify-center gap-2 bg-red text-white font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-3 rounded hover:bg-red-dark transition-colors"
          >
            Go to Homepage
          </Link>
          <Link
            href="/services"
            className="inline-flex items-center justify-center gap-2 bg-transparent text-red border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-3 rounded hover:bg-red hover:text-white transition-colors"
          >
            View Services
          </Link>
          <a
            href={`tel:${BUSINESS.phoneTel}`}
            className="inline-flex items-center justify-center gap-2 bg-navy text-white font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-3 rounded hover:bg-navy/90 transition-colors"
          >
            Call {BUSINESS.phone}
          </a>
        </div>
      </div>
    </section>
  )
}
