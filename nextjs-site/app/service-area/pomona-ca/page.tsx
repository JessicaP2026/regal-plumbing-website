import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'pomona-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Pomona, CA - 24/7 Service | Regal Plumbing & Rooter',
  description: 'Licensed plumber in Pomona CA. Emergency plumbing, drain cleaning, sewer repair & more. Call (909) 600-4561.',
  path: '/service-area/pomona-ca',
})

export default function PomonaCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Pomona is a historic San Gabriel Valley city with a diverse mix of residential neighborhoods, from the tree-lined streets near Ganesha Park to the growing developments in Phillips Ranch and Diamond Bar adjacent areas. Many Pomona homes feature older plumbing systems that require specialized knowledge to maintain and repair.",
        'Regal Plumbing & Rooter serves all of Pomona with fast, professional plumbing services. Our Ontario-based team knows the area well and responds quickly to both emergency and scheduled service calls throughout the city.',
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'Emergency plumbing for Pomona - we respond to burst pipes, sewage backups, and major leaks day or night.' },
        { slug: 'drain-cleaning', description: "Pomona's aging drain systems benefit from professional cleaning. We clear blockages in kitchens, bathrooms, and main lines." },
        { slug: 'sewer-line-repair', description: "Many Pomona homes have older sewer infrastructure. We provide camera inspection and cost-effective repair solutions." },
        { slug: 'water-heater-services', description: 'Water heater repair and installation throughout Pomona - tank, tankless, and heat pump systems.' },
        { slug: 'slab-leak-detection', description: "Pomona's clay soil conditions put stress on underground pipes. Our electronic detection finds slab leaks with minimal disruption." },
        { slug: 'hydrojetting', description: 'High-pressure pipe cleaning for Pomona homes and businesses - clearing grease, roots, and mineral scale.' },
        { slug: 'gas-leak-detection', description: "Licensed gas leak detection and repair for Pomona's diverse housing stock - from older homes to newer construction." },
        { slug: 'water-filtration', description: 'Improve your Pomona home\'s water quality with whole-home softeners and filtration systems.' },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Quick Pomona Response', description: 'Our Ontario base gives us fast response times to all Pomona neighborhoods, including Phillips Ranch and downtown.' },
        { icon: '\uD83D\uDD27', title: 'Pomona Specialists', description: "We understand Pomona's older infrastructure and the specific plumbing challenges that come with historic and modern homes alike." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Full insurance coverage and upfront pricing on every Pomona job.' },
      ]}
      seoContent={[
        'When you need a dependable <strong>plumber in Pomona CA</strong>, Regal Plumbing & Rooter delivers licensed, professional service. We serve all Pomona neighborhoods, from <strong>Phillips Ranch</strong> and <strong>Ganesha Park</strong> area to <strong>downtown Pomona</strong> and the surrounding communities.',
        'Our <strong>emergency plumbing Pomona</strong> team is on call around the clock. Whether it\'s a weekend sewage backup or a midnight burst pipe, we dispatch fast and arrive prepared to resolve the problem.',
        'Many Pomona homes have older plumbing infrastructure that requires experienced hands. Our technicians regularly handle <strong>sewer line repair</strong>, <strong>drain cleaning</strong>, and <strong>slab leak detection</strong> in homes throughout the city, using modern techniques to solve problems in aging systems.',
        'For reliable <strong>plumbing services in Pomona CA</strong>, call <strong>(909) 600-4561</strong>. We provide same-day appointments and 24/7 emergency response.',
      ]}
      faqs={[
        { question: 'How fast can you reach my Pomona home?', answer: 'Our Ontario-based team typically reaches Pomona locations within 35\u201350 minutes. Emergency calls receive priority dispatch.' },
        { question: 'Do you serve all Pomona neighborhoods?', answer: 'Yes - we serve all of Pomona, including Phillips Ranch, downtown, Ganesha Park area, and every neighborhood in between.' },
        { question: 'What are common plumbing issues in Pomona?', answer: 'Aging sewer lines, drain blockages, slab leaks, and water heater failures are the most common issues we address in Pomona homes.' },
        { question: 'Do you offer same-day service in Pomona?', answer: 'Yes. We offer same-day scheduled service for most plumbing needs in Pomona, subject to availability.' },
        { question: 'Is emergency plumbing available 24/7 in Pomona?', answer: 'Yes. Call (909) 600-4561 any time for emergency plumbing service in Pomona - including nights, weekends, and holidays.' },
      ]}
      ctaHeading="Need a Plumber in Pomona? Call Us Now"
      ctaSubtext="24/7 emergency and same-day plumbing service throughout Pomona, CA"
    />
  )
}
