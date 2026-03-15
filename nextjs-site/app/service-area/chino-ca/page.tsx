import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'chino-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Chino, CA \u2014 24/7 Service | Regal Plumbing & Rooter',
  description: 'Licensed plumber in Chino CA. Emergency plumbing, drain cleaning, sewer repair & water heaters. Call (909) 600-4561.',
  path: '/service-area/chino-ca',
})

export default function ChinoCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Chino is a growing city in San Bernardino County known for its family-friendly neighborhoods and mix of established and new construction homes. Areas like The Preserve, College Park, and neighborhoods near Chino Airport each present unique plumbing considerations \u2014 from newer homes with high-efficiency systems to older properties with aging copper and galvanized pipes.",
        'Regal Plumbing & Rooter provides fast, reliable plumbing services to all Chino neighborhoods from our Ontario home base. We understand the local water conditions and infrastructure challenges that Chino homeowners face.',
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'Emergency plumbing in Chino \u2014 rapid response to burst pipes, sewage backups, and leaks around the clock.' },
        { slug: 'drain-cleaning', description: "Chino's hard water contributes to drain buildup. We professionally clear kitchen, bathroom, and main sewer line blockages." },
        { slug: 'sewer-line-repair', description: 'Camera inspection and trenchless sewer repair for Chino homes \u2014 addressing root intrusion, cracks, and deterioration.' },
        { slug: 'water-heater-services', description: 'Water heater installation and repair throughout Chino \u2014 tank, tankless, and hybrid systems for every home.' },
        { slug: 'slab-leak-detection', description: "Chino's soil conditions can cause underground pipe stress. Our non-invasive detection locates slab leaks accurately." },
        { slug: 'hydrojetting', description: 'Professional hydrojetting clears stubborn clogs and buildup in Chino residential and commercial plumbing systems.' },
        { slug: 'gas-leak-detection', description: 'Licensed gas leak detection and repair for Chino homes and businesses \u2014 safety is our top priority.' },
        { slug: 'water-filtration', description: 'Chino water benefits from softening and filtration. We install systems that protect your plumbing and improve quality.' },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Quick Chino Response', description: 'Based in neighboring Ontario, we reach Chino locations fast \u2014 often within 30\u201340 minutes for emergencies.' },
        { icon: '\uD83D\uDD27', title: 'Chino Experts', description: "We know Chino's neighborhoods from The Preserve to College Park, and the plumbing challenges each area presents." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Transparent pricing and full insurance on every Chino plumbing job.' },
      ]}
      seoContent={[
        'Searching for a quality <strong>plumber in Chino CA</strong>? Regal Plumbing & Rooter delivers expert plumbing services throughout Chino. Whether you live in <strong>The Preserve</strong>, <strong>College Park</strong>, or near <strong>Chino Airport</strong>, our licensed technicians handle every plumbing need with professionalism and care.',
        'Our <strong>emergency plumbing Chino</strong> service is available 24 hours a day, 7 days a week. From burst pipes to sewer backups, we respond quickly from our nearby Ontario location.',
        'Chino homeowners frequently call us for <strong>drain cleaning</strong>, <strong>water heater services</strong>, and <strong>slab leak detection</strong>. The area\'s hard water and soil conditions create recurring plumbing challenges that we\'re well-equipped to handle.',
        'Trust the local experts for your <strong>Chino plumbing needs</strong>. Call <strong>(909) 600-4561</strong> for same-day or emergency service.',
      ]}
      faqs={[
        { question: 'How fast can you get to Chino?', answer: 'From our Ontario base, we reach most Chino locations within 30\u201340 minutes. Emergency calls are prioritized.' },
        { question: 'Do you serve all of Chino, CA?', answer: 'Yes \u2014 we serve all Chino neighborhoods, including The Preserve, College Park, and the areas near Chino Airport.' },
        { question: 'What plumbing issues are common in Chino?', answer: 'Hard water-related drain buildup, slab leaks, water heater failures, and sewer line issues are the most frequent Chino plumbing calls.' },
        { question: 'Do you also serve Chino Hills?', answer: 'Yes. We serve both Chino and Chino Hills, along with 30+ other cities in the Inland Empire and San Gabriel Valley.' },
        { question: 'Can I schedule same-day service in Chino?', answer: 'Yes. We offer same-day appointments for most services in Chino. Call (909) 600-4561 to schedule.' },
      ]}
      ctaHeading="Need a Plumber in Chino? Call Us Today"
      ctaSubtext="24/7 emergency and same-day plumbing service throughout Chino, CA"
    />
  )
}
