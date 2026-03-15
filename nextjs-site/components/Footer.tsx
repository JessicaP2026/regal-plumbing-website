import Link from 'next/link'
import { BUSINESS, SERVICES, CITIES } from '@/lib/constants'

export default function Footer() {
  return (
    <footer className="bg-dark-grey text-white pt-16 px-6">
      <div className="max-w-content mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-[1.6fr_1fr_1fr_1.3fr] gap-12 pb-12 border-b border-white/10">
        {/* Brand */}
        <div>
          <div className="font-oswald font-bold text-lg text-white tracking-wider uppercase mb-1.5">
            {BUSINESS.name}
          </div>
          <p className="text-[13px] text-gray-400 mb-4 leading-relaxed">{BUSINESS.tagline}</p>
          <span className="inline-block bg-red/20 border border-red/40 text-red-light text-[11.5px] font-oswald tracking-wider px-2.5 py-1 rounded">
            CA License {BUSINESS.license}
          </span>
        </div>

        {/* Services */}
        <div>
          <h4 className="font-oswald font-semibold text-sm tracking-widest uppercase text-white mb-4 pb-2.5 border-b-2 border-red inline-block">
            Services
          </h4>
          <ul className="flex flex-col gap-2">
            {SERVICES.map((s) => (
              <li key={s.slug}>
                <Link
                  href={`/${s.slug}`}
                  className="text-[13.5px] text-gray-400 hover:text-white hover:pl-1 transition-all flex items-center gap-1.5"
                >
                  <span className="text-red text-base">&rsaquo;</span>
                  {s.name}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        {/* Service Area */}
        <div>
          <h4 className="font-oswald font-semibold text-sm tracking-widest uppercase text-white mb-4 pb-2.5 border-b-2 border-red inline-block">
            Service Area
          </h4>
          <ul className="flex flex-col gap-2">
            {CITIES.map((c) => (
              <li key={c.slug}>
                <Link
                  href={`/service-area/${c.slug}`}
                  className="text-[13.5px] text-gray-400 hover:text-white hover:pl-1 transition-all flex items-center gap-1.5"
                >
                  <span className="text-red text-base">&rsaquo;</span>
                  {c.name}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        {/* Contact */}
        <div>
          <h4 className="font-oswald font-semibold text-sm tracking-widest uppercase text-white mb-4 pb-2.5 border-b-2 border-red inline-block">
            Contact Us
          </h4>
          <ul className="flex flex-col gap-3">
            <li className="flex gap-2.5 text-[13.5px] text-gray-400 leading-relaxed">
              <span className="text-[15px] flex-shrink-0 mt-0.5">&#x1F4CD;</span>
              <span>
                {BUSINESS.address.street}
                <br />
                {BUSINESS.address.city}, {BUSINESS.address.state} {BUSINESS.address.zip}
              </span>
            </li>
            <li className="flex gap-2.5 text-[13.5px] text-gray-400">
              <span className="text-[15px] flex-shrink-0">&#x1F4DE;</span>
              <a href={`tel:${BUSINESS.phoneTel}`} className="hover:text-white transition-colors">
                {BUSINESS.phone}
              </a>
            </li>
            <li className="flex gap-2.5 text-[13.5px] text-gray-400">
              <span className="text-[15px] flex-shrink-0">&#x2709;&#xFE0F;</span>
              <a href={`mailto:${BUSINESS.email}`} className="hover:text-white transition-colors">
                {BUSINESS.email}
              </a>
            </li>
            <li className="flex gap-2.5 text-[13.5px] text-gray-400 leading-relaxed">
              <span className="text-[15px] flex-shrink-0 mt-0.5">&#x1F550;</span>
              <span>
                24/7 Emergency
                <br />
                {BUSINESS.hours.office}
              </span>
            </li>
          </ul>
        </div>
      </div>

      {/* Bottom */}
      <div className="max-w-content mx-auto py-4 flex flex-col sm:flex-row justify-between items-center gap-2 text-[12.5px] text-gray-500">
        <span>&copy; {new Date().getFullYear()} {BUSINESS.name}. All Rights Reserved. CA License {BUSINESS.license}</span>
        <div className="flex gap-5">
          <Link href="/privacy-policy" className="hover:text-gray-400 transition-colors">Privacy Policy</Link>
          <Link href="/terms-of-service" className="hover:text-gray-400 transition-colors">Terms of Service</Link>
        </div>
      </div>
    </footer>
  )
}
