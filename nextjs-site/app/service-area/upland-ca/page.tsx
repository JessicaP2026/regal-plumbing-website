import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'upland-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Upland, CA - 24/7 Service ',
  description: 'Licensed plumber in Upland CA. Emergency plumbing, drain cleaning, sewer repair & water heaters. Call (909) 600-4561.',
  path: '/service-area/upland-ca',
})

export default function UplandCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Upland is a charming foothill community known for its tree-lined streets, historic downtown along Euclid Avenue, and family-oriented neighborhoods. From the older Craftsman-style homes near downtown to the newer developments in the northern foothills, Upland's housing variety creates diverse plumbing service needs.",
        "Regal Plumbing & Rooter serves all of Upland with professional, licensed plumbing services. Our Ontario base means fast response times to every Upland neighborhood, whether you're dealing with a plumbing emergency or scheduling routine maintenance.",
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'Emergency plumbing for Upland homes - 24/7 response to burst pipes, sewage backups, and water damage emergencies.' },
        { slug: 'drain-cleaning', description: "Upland's older homes often have drain systems prone to buildup. We clear blockages in all types of residential drains." },
        { slug: 'sewer-line-repair', description: "Historic Upland homes near Euclid Avenue often have aging sewer lines. We provide camera inspection and modern repair solutions." },
        { slug: 'water-heater-services', description: 'Water heater installation and repair throughout Upland - from downtown Craftsman homes to foothill developments.' },
        { slug: 'slab-leak-detection', description: "Electronic slab leak detection for Upland properties - finding hidden leaks in older and newer foundations alike." },
        { slug: 'hydrojetting', description: 'Professional hydrojetting to clear stubborn buildup from Upland residential and commercial drain systems.' },
        { slug: 'gas-leak-detection', description: 'Licensed gas leak detection and repair in Upland - ensuring safety for older and newer home gas systems.' },
        { slug: 'water-filtration', description: "Improve Upland's hard water with whole-home softeners and filtration systems installed by our licensed team." },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Fast Upland Response', description: 'Based in nearby Ontario, we reach Upland homes quickly - typically within 25\u201340 minutes for emergency calls.' },
        { icon: '\uD83D\uDD27', title: 'Upland Specialists', description: "We know Upland's housing stock from the historic downtown homes to the foothill developments, and the plumbing each requires." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Transparent pricing and full insurance coverage on every Upland plumbing job.' },
      ]}
      seoContent={[
        'Looking for a reliable <strong>plumber in Upland CA</strong>? Regal Plumbing & Rooter provides expert plumbing service throughout Upland. From the <strong>historic downtown</strong> along Euclid Avenue to the <strong>northern foothill</strong> neighborhoods, we handle all residential and commercial plumbing needs.',
        'Our <strong>emergency plumber Upland CA</strong> service runs 24/7. When a plumbing crisis hits your Upland home, we dispatch immediately from our nearby Ontario base.',
        'Upland\'s mix of historic and modern homes creates unique plumbing challenges. Our team regularly handles <strong>sewer line repair</strong> in older downtown homes, <strong>water heater upgrades</strong> in foothill properties, and <strong>drain cleaning</strong> throughout the city.',
        'Call <strong>(909) 600-4561</strong> for fast, honest plumbing service in Upland, CA - available 24 hours a day.',
      ]}
      faqs={[
        { question: 'How fast can you reach Upland?', answer: 'From our Ontario base, we reach most Upland locations within 25\u201340 minutes. Emergency calls receive priority dispatch.' },
        { question: 'Do you serve all Upland neighborhoods?', answer: 'Yes - we serve all of Upland, including the downtown historic district, the Euclid corridor, foothill neighborhoods, and everywhere in between.' },
        { question: 'What plumbing issues are common in Upland?', answer: 'Older sewer lines near downtown, hard water drain buildup, water heater failures, and slab leaks are the most common Upland plumbing issues we handle.' },
        { question: 'Can you work on older homes in Upland?', answer: 'Absolutely. Our technicians are experienced with the plumbing systems found in Upland\'s historic and mid-century homes, including galvanized pipes and older drain systems.' },
        { question: 'Do you offer 24/7 emergency service in Upland?', answer: 'Yes. Call (909) 600-4561 any time for emergency plumbing in Upland - we answer around the clock.' },
      ]}
      ctaHeading="Need a Plumber in Upland? Call Today"
      ctaSubtext="24/7 emergency and same-day plumbing service throughout Upland, CA"
    />
  )
}
