import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'fontana-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Fontana, CA - 24/7 Service ',
  description: 'Licensed plumber in Fontana CA. Emergency plumbing, drain cleaning, sewer repair & water heaters. Call (909) 600-4561.',
  path: '/service-area/fontana-ca',
})

export default function FontanaCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Fontana is one of the largest cities in San Bernardino County, with rapid residential growth stretching from the older neighborhoods near downtown to the sprawling master-planned communities in the south. This growth brings plumbing challenges - new construction with high water pressure issues and older homes with aging galvanized and cast iron pipe systems.",
        "Regal Plumbing & Rooter serves all of Fontana from our nearby Ontario base, providing fast response times across the city. Whether it's a sewer line emergency near Sierra Avenue or a water heater replacement in Southridge Village, our licensed team is ready.",
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'Emergency plumbing in Fontana - burst pipes, sewage backups, and major leaks handled immediately, day or night.' },
        { slug: 'drain-cleaning', description: "Fontana's hard water leads to stubborn drain buildup. We clear all types of drain blockages with professional equipment." },
        { slug: 'sewer-line-repair', description: "Fontana's older neighborhoods have clay and cast iron sewer lines prone to root intrusion and collapse. We diagnose and repair them." },
        { slug: 'water-heater-services', description: 'Tank and tankless water heater installation and repair throughout Fontana - all major brands serviced.' },
        { slug: 'slab-leak-detection', description: "Fontana's expansive clay soil puts stress on underground pipes. Our electronic detection finds slab leaks without tearing up your home." },
        { slug: 'hydrojetting', description: 'High-pressure hydrojetting clears grease, scale, and roots from Fontana drain and sewer lines - residential and commercial.' },
        { slug: 'gas-leak-detection', description: "From older Fontana homes to new construction, we provide licensed gas leak detection and repair services for safety." },
        { slug: 'water-filtration', description: 'Fontana water quality benefits from whole-home softeners and filtration. We install systems that protect pipes and improve taste.' },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Fast Fontana Response', description: 'Based in nearby Ontario, we reach all Fontana neighborhoods quickly - from downtown to Southridge Village.' },
        { icon: '\uD83D\uDD27', title: 'Fontana Expertise', description: "We understand Fontana's unique plumbing landscape - from new construction challenges to aging infrastructure in established areas." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Every Fontana job is backed by full insurance and transparent, upfront pricing.' },
      ]}
      seoContent={[
        'Need a trusted <strong>plumber in Fontana CA</strong>? Regal Plumbing & Rooter provides licensed, professional plumbing services throughout Fontana. From the established neighborhoods near <strong>Sierra Avenue</strong> and <strong>Foothill Boulevard</strong> to the newer communities in <strong>Southridge Village</strong> and surrounding areas, we handle every type of plumbing challenge.',
        'Our <strong>emergency plumbing Fontana</strong> service runs 24/7. Burst pipes, sewage backups, and major leaks are handled with urgency - we dispatch fast from our Ontario base to minimize damage and get your home back to normal.',
        '<strong>Sewer line repair in Fontana</strong> is a frequent need, especially in older neighborhoods where clay and cast iron pipes have deteriorated over decades. We use camera inspection to diagnose problems accurately and offer trenchless repair options to minimize yard disruption.',
        'For all your Fontana plumbing needs - from <strong>drain cleaning</strong> and <strong>water heater installation</strong> to <strong>slab leak detection</strong> - call <strong>(909) 600-4561</strong> for fast, honest service.',
      ]}
      faqs={[
        { question: 'How fast can you get to my Fontana home?', answer: 'From our Ontario base, we typically reach Fontana locations within 30\u201345 minutes. Emergency calls receive top priority dispatch.' },
        { question: 'Do you serve all parts of Fontana?', answer: 'Yes - we serve all of Fontana, from the downtown area to Southridge Village, the Sierra corridor, and all surrounding neighborhoods.' },
        { question: 'What plumbing problems are common in Fontana?', answer: 'Sewer line issues in older neighborhoods, drain blockages from hard water, slab leaks due to expansive soil, and water heater failures are the most common calls we receive from Fontana.' },
        { question: 'Do you handle commercial plumbing in Fontana?', answer: 'Yes. We serve both residential and commercial customers throughout Fontana, including restaurants, offices, and multi-unit properties.' },
        { question: 'Is emergency service available on holidays in Fontana?', answer: 'Absolutely. We are available 24/7/365 for plumbing emergencies in Fontana. Call (909) 600-4561 any time.' },
      ]}
      ctaHeading="Need a Plumber in Fontana? We're On Our Way"
      ctaSubtext="24/7 emergency and same-day plumbing service throughout Fontana, CA"
    />
  )
}
