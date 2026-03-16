import Image from 'next/image'
import Link from 'next/link'
import { BUSINESS } from '@/lib/constants'
import { generatePageMetadata } from '@/lib/metadata'
import { generateBreadcrumbSchema } from '@/lib/schema'
import SchemaMarkup from '@/components/SchemaMarkup'
import HeroSection from '@/components/HeroSection'
import EmergencyCTABanner from '@/components/EmergencyCTABanner'

export const metadata = generatePageMetadata({
  title: 'Plumbing Services - Regal Plumbing & Rooter',
  description: 'Comprehensive residential and commercial plumbing services - emergency plumbing, drain cleaning, sewer repair, water heaters & more. Available 24/7.',
  path: '/services',
})

const SERVICE_DETAILS = [
  {
    slug: 'emergency-plumbing',
    name: 'Emergency Plumbing',
    badge: '24/7 Available',
    image: '/images/pipe-repair-leak-detection-chino-hills-ca.webp',
    alt: 'Emergency plumbing service',
    description: 'Plumbing emergencies don\u2019t wait for business hours, and neither do we. Regal Plumbing & Rooter provides rapid-response emergency plumbing services around the clock. Whether it\u2019s a burst pipe, severe water leak, or overflowing fixture - our team mobilizes fast to minimize damage and restore your home.',
    features: ['Rapid response - typically on-site within the hour', 'Burst pipe repair and water shut-off', 'Severe clog and overflow emergencies', '24/7 availability, including holidays'],
    isEmergency: true,
  },
  {
    slug: 'drain-cleaning',
    name: 'Drain Cleaning',
    badge: 'Residential & Commercial',
    image: '/images/drain-cleaning-shower-upland-ca.webp',
    alt: 'Drain cleaning service',
    description: 'Slow or blocked drains are more than an inconvenience - they can signal deeper plumbing issues. Our drain cleaning services clear everything from minor kitchen clogs to severe main line blockages, using professional-grade equipment to restore full flow and prevent future buildup.',
    features: ['Kitchen and bathroom drain clearing', 'Main sewer line snaking', 'Floor drain and utility sink cleaning', 'Preventative maintenance plans available'],
  },
  {
    slug: 'sewer-line-repair',
    name: 'Sewer Line Repair',
    badge: 'Expert Diagnosis',
    image: '/images/sewer-line-repair-excavation-fontana-ca.webp',
    alt: 'Sewer line repair',
    description: 'Sewer line problems can cause serious damage if left untreated. We use camera inspection technology to accurately diagnose sewer line issues - root intrusion, cracks, bellied pipes, and more - then provide the most cost-effective repair solution, including trenchless options when available.',
    features: ['Camera video inspection and diagnosis', 'Pipe bursting and trenchless repair', 'Root intrusion removal', 'Full sewer line replacement when needed'],
  },
  {
    slug: 'water-heater-services',
    name: 'Water Heater Install & Repair',
    badge: 'All Types & Brands',
    image: '/images/water-heater-installation-ontario-ca.webp',
    alt: 'Water heater installation Ontario CA - Regal Plumbing & Rooter',
    description: 'No hot water? We install and repair all types of water heaters - traditional tank units, tankless (on-demand) systems, and hybrid heat pump models. Our technicians are experienced with all major brands and can help you choose the right system for your household\u2019s needs and budget.',
    features: ['Traditional tank water heater install & repair', 'Tankless water heater installation', 'Heat pump water heater systems', 'Anode rod replacement and flushing'],
  },
  {
    slug: 'slab-leak-detection',
    name: 'Slab Leak Detection',
    badge: 'Non-Invasive Technology',
    image: '/images/leak-repair-wall-open-ontario-ca.webp',
    alt: 'Slab leak detection',
    description: 'Slab leaks are among the most damaging - and hardest to find - plumbing problems a homeowner can face. We use electronic detection equipment to precisely locate leaks beneath your concrete slab without unnecessary excavation, saving you time, money, and the headache of major property disruption.',
    features: ['Electronic leak detection - no guesswork', 'Spot repair and re-routing options', 'Epoxy pipe lining (non-invasive)', 'Post-repair pressure testing'],
  },
  {
    slug: 'hydrojetting',
    name: 'Hydrojetting',
    badge: 'High-Pressure Cleaning',
    image: '/images/hydro-jetting-roof-rancho-cucamonga-ca.webp',
    alt: 'Hydrojetting service',
    description: 'When snaking isn\u2019t enough, hydrojetting is the most effective method for clearing stubborn grease, scale, and root intrusion from drain and sewer lines. Using water at up to 4,000 PSI, hydrojetting scours pipe walls clean and restores full pipe capacity - ideal for commercial properties and recurring residential blockages.',
    features: ['Clears grease, scale, and hardened buildup', 'Removes tree root intrusion', 'Ideal for commercial kitchens and restaurants', 'Extends the life of your plumbing system'],
  },
  {
    slug: 'gas-leak-detection',
    name: 'Gas Leak Detection',
    badge: 'Safety Critical',
    image: '/images/camera-inspection-drain-cleaning-san-bernardino-ca.webp',
    alt: 'Gas leak detection',
    description: 'A gas leak is a serious safety emergency. If you smell gas, leave the building immediately and call 911 first. Then call us. Our licensed plumbers perform precise gas leak detection and repair, ensuring your home or business is safe before restoring service. Never ignore a suspected gas leak.',
    features: ['Electronic gas leak detection equipment', 'Gas line repair and re-piping', 'Pressure testing after repair', 'Licensed for natural gas and propane systems'],
    isEmergency: true,
  },
  {
    slug: 'water-filtration',
    name: 'Water Filtration & Softeners',
    badge: 'Cleaner, Softer Water',
    image: '/images/pipe-replacement-copper-ontario-ca.webp',
    alt: 'Water filtration systems',
    description: 'Southern California water is notoriously hard. Mineral buildup damages appliances, leaves residue on fixtures, and affects the taste and quality of your water. We install whole-home water softeners, under-sink filters, and reverse osmosis systems to give you cleaner, softer water throughout your home.',
    features: ['Whole-home water softener installation', 'Under-sink reverse osmosis systems', 'Carbon filtration and UV purification', 'Filter cartridge replacement service'],
  },
]

export default function ServicesPage() {
  return (
    <>
      <SchemaMarkup
        schema={generateBreadcrumbSchema([
          { name: 'Home', url: BUSINESS.url },
          { name: 'Services', url: `${BUSINESS.url}/services` },
        ])}
      />

      <HeroSection
        title="Plumbing Services"
        subtitle="Comprehensive residential and commercial plumbing solutions - available 24/7 across Southern California."
        breadcrumbs={[{ label: 'Home', href: '/' }, { label: 'Services' }]}
        navyBg
      />

      <section className="py-20 px-6 bg-light-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-14">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Full Service Plumbing</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">Everything We Offer</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
            <p className="text-base text-gray-500 max-w-[520px] mx-auto mt-4 leading-relaxed">
              From emergency repairs to planned installations &mdash; our licensed technicians handle it all.
            </p>
          </div>

          <div className="flex flex-col gap-14">
            {SERVICE_DETAILS.map((svc, i) => (
              <div
                key={svc.slug}
                className={`grid grid-cols-1 lg:grid-cols-[1fr_1.8fr] gap-12 items-start p-10 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-lg transition-shadow ${i % 2 !== 0 ? 'lg:grid-cols-[1.8fr_1fr]' : ''}`}
              >
                <div className={`relative rounded-lg overflow-hidden min-h-[260px] ${i % 2 !== 0 ? 'lg:order-2' : ''}`}>
                  <Image
                    src={svc.image}
                    alt={svc.alt}
                    fill
                    className="object-cover"
                    sizes="(max-width: 900px) 100vw, 40vw"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/55 to-transparent" />
                  <span className="absolute bottom-3.5 left-3.5 bg-red text-white font-oswald font-bold text-[15px] tracking-wider uppercase px-2.5 py-1 rounded text-xs">
                    {svc.name}
                  </span>
                </div>
                <div className={i % 2 !== 0 ? 'lg:order-1' : ''}>
                  <h3 className="font-oswald font-bold text-2xl text-dark-grey tracking-wide mb-1.5">{svc.name}</h3>
                  <span className="inline-block bg-red-50 text-red font-oswald font-medium text-[11px] tracking-widest uppercase px-2.5 py-0.5 rounded mb-3.5">
                    {svc.badge}
                  </span>
                  <p className="text-[15px] text-gray-600 leading-relaxed mb-5">{svc.description}</p>
                  <ul className="flex flex-col gap-2 mb-6">
                    {svc.features.map((f, fi) => (
                      <li key={fi} className="flex items-start gap-2.5 text-sm text-gray-700">
                        <span className="w-5 h-5 bg-red text-white rounded-full flex items-center justify-center text-[11px] font-bold flex-shrink-0 mt-0.5">&#x2713;</span>
                        {f}
                      </li>
                    ))}
                  </ul>
                  {svc.isEmergency ? (
                    <a
                      href={`tel:${BUSINESS.phoneTel}`}
                      className="inline-flex items-center gap-2 bg-red text-white border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red-dark hover:border-red-dark transition-all"
                    >
                      Call for Emergency Service
                    </a>
                  ) : (
                    <Link
                      href={`/${svc.slug}`}
                      className="inline-flex items-center gap-2 bg-transparent text-red border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red hover:text-white transition-all"
                    >
                      Learn More &rarr;
                    </Link>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Regal */}
      <section className="py-20 px-6 bg-dark-grey">
        <div className="max-w-content mx-auto">
          <div className="text-center mb-12">
            <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red-light mb-2">Our Promise</p>
            <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide text-white mb-3">Why Choose Regal?</h2>
            <div className="w-14 h-1 bg-red rounded mx-auto" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-9 bg-white/[0.04] border border-white/[0.08] rounded-lg hover:bg-white/[0.08] hover:-translate-y-1 transition-all">
              <span className="text-[40px] block mb-3.5">&#x1F4B0;</span>
              <h3 className="font-oswald font-semibold text-[19px] text-white mb-2.5">Honest Pricing</h3>
              <p className="text-sm text-gray-400 leading-relaxed">Upfront, transparent quotes before any work begins. No hidden fees, no surprises.</p>
            </div>
            <div className="text-center p-9 bg-white/[0.04] border border-white/[0.08] rounded-lg hover:bg-white/[0.08] hover:-translate-y-1 transition-all">
              <span className="text-[40px] block mb-3.5">&#x26A1;</span>
              <h3 className="font-oswald font-semibold text-[19px] text-white mb-2.5">Fast Response</h3>
              <p className="text-sm text-gray-400 leading-relaxed">24/7 availability for emergencies. We arrive quickly and work efficiently.</p>
            </div>
            <div className="text-center p-9 bg-white/[0.04] border border-white/[0.08] rounded-lg hover:bg-white/[0.08] hover:-translate-y-1 transition-all">
              <span className="text-[40px] block mb-3.5">&#x1F527;</span>
              <h3 className="font-oswald font-semibold text-[19px] text-white mb-2.5">Quality Workmanship</h3>
              <p className="text-sm text-gray-400 leading-relaxed">Every job backed by our commitment to premium craftsmanship and lasting results.</p>
            </div>
          </div>
        </div>
      </section>

      <EmergencyCTABanner
        heading="Ready to Get Started?"
        subtext="Call now for a free quote or immediate emergency service"
      />
    </>
  )
}
