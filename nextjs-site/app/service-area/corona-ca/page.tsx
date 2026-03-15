import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'corona-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Corona, CA \u2014 24/7 Service | Regal Plumbing & Rooter',
  description: 'Licensed plumber in Corona CA. Emergency plumbing, drain cleaning, sewer repair & water heaters. Call (909) 600-4561.',
  path: '/service-area/corona-ca',
})

export default function CoronaCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Corona, known as the Circle City, is a thriving Riverside County community with diverse residential areas ranging from the historic homes near Grand Boulevard to newer developments in South Corona and the Skyline area. The city's rapid growth has created demand for reliable, licensed plumbing services that understand both new and established infrastructure.",
        'Regal Plumbing & Rooter brings fast, professional plumbing service to all Corona neighborhoods. From our Ontario base, we serve Corona with emergency and scheduled plumbing covering everything from drain cleaning to complete sewer line replacement.',
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'Corona emergency plumbing \u2014 burst pipes, sewage backups, and major leaks handled 24/7 with rapid response.' },
        { slug: 'drain-cleaning', description: "Corona's water quality contributes to drain buildup over time. We clear all types of residential and commercial drain blockages." },
        { slug: 'sewer-line-repair', description: 'Camera inspection and sewer repair throughout Corona \u2014 from the older Grand Boulevard homes to newer South Corona developments.' },
        { slug: 'water-heater-services', description: 'Tank and tankless water heater services for Corona homes \u2014 installation, repair, and replacement.' },
        { slug: 'slab-leak-detection', description: 'Electronic slab leak detection for Corona properties \u2014 finding hidden leaks beneath foundations without unnecessary damage.' },
        { slug: 'hydrojetting', description: 'Professional hydrojetting services for Corona \u2014 clearing stubborn grease, scale, and root intrusion from drain lines.' },
        { slug: 'gas-leak-detection', description: 'Licensed gas leak detection and repair in Corona \u2014 keeping your home safe with professional equipment and testing.' },
        { slug: 'water-filtration', description: 'Corona water benefits greatly from filtration and softening. We install whole-home systems for cleaner, softer water.' },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Corona Response', description: 'We reach Corona quickly from our Ontario base, providing fast response for both emergencies and scheduled service.' },
        { icon: '\uD83D\uDD27', title: 'Circle City Experts', description: "We know Corona's plumbing landscape from the historic Grand Boulevard area to the newer Skyline and South Corona communities." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Full insurance coverage and honest, upfront pricing on every Corona job.' },
      ]}
      seoContent={[
        'For professional <strong>plumbing services in Corona CA</strong>, Regal Plumbing & Rooter is your trusted local choice. We serve all Corona neighborhoods, from the <strong>historic Grand Boulevard</strong> corridor to <strong>South Corona</strong> and the <strong>Skyline</strong> area developments.',
        'Our <strong>emergency plumber Corona CA</strong> service operates 24/7. When plumbing emergencies strike \u2014 burst pipes, sewer backups, or gas leaks \u2014 we respond fast and arrive prepared.',
        'Corona homeowners rely on us for <strong>drain cleaning</strong>, <strong>water heater repair</strong>, <strong>slab leak detection</strong>, and more. Our licensed technicians understand the plumbing needs of both newer and older Corona homes.',
        'Call <strong>(909) 600-4561</strong> for same-day plumbing service or 24/7 emergency response in Corona, CA.',
      ]}
      faqs={[
        { question: 'How fast can you reach Corona?', answer: 'We typically reach Corona locations within 40\u201360 minutes from our Ontario base. Emergency calls are given top priority.' },
        { question: 'Do you serve all Corona neighborhoods?', answer: 'Yes \u2014 we serve all of Corona, including Grand Boulevard, South Corona, Skyline, and every neighborhood throughout the city.' },
        { question: 'What plumbing issues are common in Corona?', answer: 'Hard water drain buildup, sewer line problems in older homes, water heater failures, and slab leaks are common Corona plumbing issues.' },
        { question: 'Do you handle both residential and commercial plumbing in Corona?', answer: 'Yes. We provide plumbing services for homes and commercial properties throughout Corona.' },
        { question: 'Is 24/7 emergency service available in Corona?', answer: 'Yes. Call (909) 600-4561 any time for emergency plumbing service in Corona \u2014 we answer around the clock.' },
      ]}
      ctaHeading="Need a Plumber in Corona? We're Ready"
      ctaSubtext="24/7 emergency and same-day plumbing service throughout Corona, CA"
    />
  )
}
