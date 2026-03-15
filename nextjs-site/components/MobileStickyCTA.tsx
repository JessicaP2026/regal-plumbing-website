'use client'

import { BUSINESS } from '@/lib/constants'

export default function MobileStickyCTA() {
  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 bg-red p-3 md:hidden pb-safe">
      <a
        href={`tel:${BUSINESS.phoneTel}`}
        className="flex items-center justify-center gap-2 w-full bg-white text-red font-oswald font-semibold text-[15px] uppercase tracking-wider py-3 rounded hover:bg-light-grey transition-colors"
      >
        Call Now &mdash; {BUSINESS.phone}
      </a>
    </div>
  )
}
