import Link from 'next/link'
import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'west-covina-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in West Covina, CA - 24/7 Service ',
  description: 'Licensed plumber in West Covina CA. Emergency plumbing, drain cleaning, sewer repair & water heaters. Call (909) 600-4561.',
  path: '/service-area/west-covina-ca',
})

export default function WestCovinaCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "West Covina is a vibrant San Gabriel Valley city with a diverse mix of residential neighborhoods, from the established areas near the Eastland Shopping Center to the hillside homes in South Hills and the Galster Park area. The city's varied housing stock - ranging from 1950s-era ranch homes to modern developments - creates a broad range of plumbing service needs.",
        <>Regal Plumbing &amp; Rooter provides professional plumbing services throughout West Covina. Our Ontario base allows us to respond to all West Covina neighborhoods with the speed and expertise homeowners expect &mdash; covering{' '}<Link href="/water-heater-services" className="text-red font-medium hover:underline">water heater services</Link>,{' '}<Link href="/drain-cleaning" className="text-red font-medium hover:underline">drain cleaning</Link>,{' '}<Link href="/emergency-plumbing" className="text-red font-medium hover:underline">emergency plumbing</Link>, and{' '}<Link href="/water-filtration" className="text-red font-medium hover:underline">water filtration</Link>.</>,
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'West Covina emergency plumbing - rapid 24/7 response to burst pipes, sewage backups, and major water leaks.' },
        { slug: 'drain-cleaning', description: "West Covina's aging drain systems and hard water make professional drain cleaning essential. We clear all residential blockages." },
        { slug: 'sewer-line-repair', description: "Many West Covina homes have decades-old sewer lines. We diagnose issues with camera inspection and provide repair options." },
        { slug: 'water-heater-services', description: 'Water heater services for West Covina - installation, repair, and replacement of tank and tankless systems.' },
        { slug: 'slab-leak-detection', description: 'Electronic slab leak detection for West Covina homes - precise location with minimal property disruption.' },
        { slug: 'hydrojetting', description: 'High-pressure hydrojetting for West Covina drain and sewer lines - clearing grease, scale, and root intrusion.' },
        { slug: 'gas-leak-detection', description: 'Licensed gas leak detection and repair for West Covina homes - professional equipment and safety testing.' },
        { slug: 'water-filtration', description: "Improve West Covina's hard water with professionally installed softeners and filtration systems." },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Quick West Covina Response', description: 'We serve West Covina from our Ontario base, providing reliable response times across all neighborhoods.' },
        { icon: '\uD83D\uDD27', title: 'West Covina Expertise', description: "We understand the plumbing needs of West Covina's diverse housing stock - from mid-century homes to modern developments." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Every West Covina job comes with transparent pricing and full insurance protection.' },
      ]}
      seoContent={[
        'For dependable <strong>plumbing services in West Covina CA</strong>, homeowners trust Regal Plumbing & Rooter. We serve all West Covina neighborhoods, from <strong>South Hills</strong> and the <strong>Galster Park</strong> area to the commercial corridors near <strong>Eastland Shopping Center</strong>.',
        'Our <a href="/emergency-plumbing" class="text-red font-medium hover:underline"><strong>emergency plumber in West Covina</strong></a> service is available around the clock. Burst pipes, sewer backups, and water heater failures don\'t wait for business hours - and neither do we.',
        'West Covina\'s diverse housing stock means varied plumbing needs. We handle <a href="/drain-cleaning" class="text-red font-medium hover:underline"><strong>drain cleaning</strong></a> in homes with aging pipes, <a href="/slab-leak-detection" class="text-red font-medium hover:underline"><strong>slab leak detection</strong></a> in properties with shifting foundations, and <a href="/water-heater-services" class="text-red font-medium hover:underline"><strong>water heater installation</strong></a> in both older and newer West Covina homes. We also offer <a href="/water-filtration" class="text-red font-medium hover:underline">water filtration systems</a> to improve the area\'s notoriously hard water.',
        'Call <strong>(909) 600-4561</strong> for professional plumbing service in West Covina - same-day appointments and 24/7 emergency response available.',
      ]}
      faqs={[
        { question: 'How fast can you get to West Covina?', answer: 'We typically reach West Covina locations within 40\u201355 minutes from our Ontario base. Emergency calls are always prioritized.' },
        { question: 'Do you serve all West Covina neighborhoods?', answer: 'Yes - we cover all of West Covina, including South Hills, the Eastland area, Galster Park, and every neighborhood throughout the city.' },
        { question: 'What plumbing problems are common in West Covina?', answer: 'Aging sewer lines, drain blockages from hard water, slab leaks, and water heater issues are the most common plumbing calls we receive from West Covina residents.' },
        { question: 'Do you serve nearby cities like Covina and Azusa?', answer: 'Yes. We serve West Covina, Covina, Azusa, Glendora, and 28+ other cities throughout the San Gabriel Valley and Inland Empire.' },
        { question: 'Is 24/7 emergency service available in West Covina?', answer: 'Yes. Our emergency line is staffed around the clock. Call (909) 600-4561 any time for plumbing emergencies in West Covina.' },
      ]}
      ctaHeading="Need a Plumber in West Covina? We're Ready"
      ctaSubtext="24/7 emergency and same-day plumbing service throughout West Covina, CA"
    />
  )
}
