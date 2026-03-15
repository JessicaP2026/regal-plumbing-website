import { BUSINESS } from '@/lib/constants'

interface EmergencyCTABannerProps {
  heading: string
  subtext: string
}

export default function EmergencyCTABanner({ heading, subtext }: EmergencyCTABannerProps) {
  return (
    <section className="bg-red py-16 px-6 text-center relative overflow-hidden">
      <div className="absolute inset-0 bg-[repeating-linear-gradient(-45deg,transparent,transparent_8px,rgba(0,0,0,0.04)_8px,rgba(0,0,0,0.04)_10px)]" />
      <div className="relative z-10 max-w-[700px] mx-auto">
        <h2 className="font-oswald font-bold text-[clamp(26px,4vw,42px)] text-white tracking-wider uppercase mb-3">
          {heading}
        </h2>
        <p className="text-base text-white/85 mb-6">{subtext}</p>
        <a
          href={`tel:${BUSINESS.phoneTel}`}
          className="font-oswald font-bold text-[clamp(30px,5vw,50px)] text-white tracking-widest block mb-7"
        >
          {BUSINESS.phone}
        </a>
        <a
          href={`tel:${BUSINESS.phoneTel}`}
          className="inline-flex items-center justify-center gap-1.5 bg-white text-red border-2 border-white font-oswald font-semibold text-[15px] uppercase tracking-wider px-8 py-3.5 rounded hover:bg-transparent hover:text-white hover:-translate-y-0.5 transition-all"
        >
          Call Now
        </a>
      </div>
    </section>
  )
}
