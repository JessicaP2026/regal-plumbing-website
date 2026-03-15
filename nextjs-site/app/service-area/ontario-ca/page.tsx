import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'ontario-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Ontario, CA - 24/7 Emergency Service | Regal Plumbing & Rooter',
  description: 'Expert plumber in Ontario CA - drain cleaning, slab leak detection & water heater repair. 24/7 emergency service available. Call (909) 600-4561.',
  path: '/service-area/ontario-ca',
})

export default function OntarioCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Ontario, CA is one of the Inland Empire's fastest-growing cities, home to neighborhoods like Ontario Ranch, Gramercy, Creekside, and the bustling corridor near Ontario International Airport. As the region expands, plumbing demands have grown alongside it - from brand-new subdivisions facing high water pressure issues to older homes near downtown contending with aging cast iron pipes and galvanized supply lines.",
        'Regal Plumbing & Rooter is based right here in Ontario at 2141 E Philadelphia St, Suite R - which means we respond faster than anyone else when emergencies strike. Whether you\'re dealing with a slab leak in Ontario Ranch, a clogged main sewer near Gramercy, or a failed water heater near the airport corridor, our licensed technicians are on the road within the hour.',
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'When a burst pipe or sewage backup strikes your Ontario home, we dispatch immediately - day or night - to stop damage fast.' },
        { slug: 'drain-cleaning', description: "Ontario's hard water accelerates buildup in drains. We clear kitchen, bathroom, and main sewer lines with professional snaking and hydrojetting." },
        { slug: 'sewer-line-repair', description: 'Older Ontario neighborhoods near Euclid Ave have aging clay sewer pipes prone to cracking. We offer camera inspection and trenchless repair.' },
        { slug: 'water-heater-services', description: 'From tankless installations in new Ontario Ranch homes to traditional tank replacements near Mountain Ave, we handle all water heater work in Ontario.' },
        { slug: 'slab-leak-detection', description: "Ontario's clay-heavy soil causes pipes beneath concrete slabs to shift and crack. Our electronic detection pinpoints the exact leak with minimal disruption." },
        { slug: 'hydrojetting', description: "Hard water scale and grease coat Ontario's pipe walls over time. Our high-pressure hydrojetting scours lines clean and restores full flow capacity." },
        { slug: 'gas-leak-detection', description: "Ontario's mix of older homes and new construction creates diverse gas line risks. Our licensed team uses advanced sensors to locate and repair leaks safely." },
        { slug: 'water-filtration', description: 'Ontario tap water carries high mineral content. We install whole-home softeners and reverse osmosis systems to protect your appliances and improve taste.' },
      ]}
      whyCards={[
        { icon: '\uD83D\uDCCD', title: 'Based in Ontario', description: 'Our shop is in Ontario at 2141 E Philadelphia St. When you call, we\'re already nearby - reaching most Ontario locations in under an hour.' },
        { icon: '\uD83D\uDD27', title: 'Ontario Experts', description: "We know Ontario's soil conditions, water quality challenges, and infrastructure age across neighborhoods like Ontario Ranch, Gramercy, and Creekside." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Every Ontario job is covered by full liability insurance, and every quote is upfront with no hidden fees.' },
      ]}
      seoContent={[
        'When you need a reliable <strong>plumber in Ontario CA</strong>, Regal Plumbing & Rooter is your local choice. Based in Ontario, we understand the specific plumbing challenges homeowners and businesses face throughout this growing city. From the sprawling <strong>Ontario Ranch</strong> master-planned community to the established <strong>Gramercy</strong> and <strong>Creekside</strong> neighborhoods near the heart of town, we\'ve seen and solved every type of plumbing problem Ontario has to offer.',
        'As your trusted <strong>emergency plumber Ontario CA</strong>, our team is on call around the clock. Whether it\'s a slab leak beneath a concrete foundation in an older Ontario home, a broken water main along Euclid Avenue, or a sewage backup in a commercial property - we dispatch fast and arrive with the tools to fix it right.',
        '<strong>Drain cleaning Ontario CA</strong> is one of our most frequent services. Ontario\'s water supply carries heavy mineral content from the local groundwater system, which accelerates scale buildup inside pipes. We use professional snaking and high-pressure hydrojetting to restore full function - not a temporary fix, but a lasting clear that protects your pipes long-term.',
        '<strong>Slab leak Ontario</strong> detection is particularly important here because the clay-heavy soil under many Ontario properties shifts seasonally, putting stress on copper supply pipes embedded in concrete. If you notice warm spots on your floor, unexplained spikes in your water bill, or the sound of running water with nothing in use, call us immediately.',
      ]}
      faqs={[
        { question: 'How fast can Regal Plumbing get to my Ontario, CA home?', answer: 'Because we\'re based in Ontario at 2141 E Philadelphia St, our technicians can typically reach most parts of Ontario within 45\u201360 minutes of your call. For plumbing emergencies, we prioritize the fastest possible dispatch - including nights and weekends.' },
        { question: 'Do you serve all neighborhoods in Ontario, CA?', answer: 'Yes - we serve all of Ontario, including Ontario Ranch, Gramercy, Creekside, the Airport District, downtown Ontario, and every area in between. No part of the city is outside our service range.' },
        { question: 'What are the most common plumbing problems in Ontario, CA?', answer: 'The most frequent calls we get from Ontario residents involve slab leaks - especially in older neighborhoods where copper pipes sit in calcium-heavy soil - drain blockages from hard water buildup, and water heater failures. We handle all of these daily.' },
        { question: 'Does Regal Plumbing work on new construction homes in Ontario Ranch?', answer: 'Yes - we work on both new construction and established homes throughout Ontario. For Ontario Ranch properties, we\'re familiar with current building standards and frequently handle water heater upgrades, whole-home filtration installations, and pressure regulator replacements.' },
        { question: 'Is emergency plumbing service available on weekends in Ontario?', answer: 'Absolutely. Our emergency plumbing line is staffed 24 hours a day, 7 days a week - including weekends and holidays. Call (909) 600-4561 any time and a real person will answer.' },
      ]}
      ctaHeading="Need a Plumber in Ontario? We're Ready Now"
      ctaSubtext="24/7 emergency and same-day service throughout Ontario, CA"
    />
  )
}
