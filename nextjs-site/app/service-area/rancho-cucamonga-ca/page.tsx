import { generatePageMetadata } from '@/lib/metadata'
import { CITIES } from '@/lib/constants'
import CityPageTemplate from '@/components/CityPageTemplate'

const city = CITIES.find((c) => c.slug === 'rancho-cucamonga-ca')!

export const metadata = generatePageMetadata({
  title: 'Plumber in Rancho Cucamonga, CA \u2014 24/7 Service | Regal Plumbing & Rooter',
  description: 'Licensed plumber in Rancho Cucamonga CA. Emergency plumbing, drain cleaning, slab leak detection & water heater repair. Call (909) 600-4561.',
  path: '/service-area/rancho-cucamonga-ca',
})

export default function RanchoCucamongaCityPage() {
  return (
    <CityPageTemplate
      city={city}
      introText={[
        "Rancho Cucamonga is one of the Inland Empire's most desirable communities, with neighborhoods ranging from the established homes near Foothill Boulevard to newer developments along Day Creek and Victoria Gardens. The city's diverse housing stock brings a wide range of plumbing challenges \u2014 from aging galvanized pipes in older neighborhoods to high water pressure issues in hillside homes near the foothills.",
        'Regal Plumbing & Rooter is based just minutes away in Ontario, giving us fast response times to all Rancho Cucamonga neighborhoods. Whether you need emergency plumbing at 2 AM or a scheduled water heater installation, our licensed technicians arrive quickly and get the job done right.',
      ]}
      serviceDescriptions={[
        { slug: 'emergency-plumbing', description: 'Burst pipe or sewage backup in Rancho Cucamonga? We dispatch immediately \u2014 our Ontario base means we reach most RC locations in under an hour.' },
        { slug: 'drain-cleaning', description: 'Hard water buildup is common in Rancho Cucamonga homes. We clear slow drains in kitchens, bathrooms, and main sewer lines fast.' },
        { slug: 'sewer-line-repair', description: 'Older homes near Foothill Blvd often have aging clay sewer lines. We provide camera inspection and trenchless repair options.' },
        { slug: 'water-heater-services', description: 'From tankless upgrades in newer homes to tank replacements in established neighborhoods, we handle all water heater work in Rancho Cucamonga.' },
        { slug: 'slab-leak-detection', description: 'The shifting soil beneath Rancho Cucamonga properties can stress underground pipes. Our electronic detection locates slab leaks with precision.' },
        { slug: 'hydrojetting', description: 'Mineral scale and grease buildup in Rancho Cucamonga pipes respond to our high-pressure hydrojetting \u2014 restoring full flow capacity.' },
        { slug: 'gas-leak-detection', description: "Rancho Cucamonga's mix of home ages creates varied gas line conditions. Our licensed team uses advanced equipment to locate and fix leaks safely." },
        { slug: 'water-filtration', description: 'Rancho Cucamonga water is high in minerals. We install whole-home softeners and RO systems to improve water quality throughout your home.' },
      ]}
      whyCards={[
        { icon: '\u26A1', title: 'Fast Response', description: "Located in nearby Ontario, we reach most Rancho Cucamonga locations in under an hour \u2014 faster for emergencies." },
        { icon: '\uD83D\uDD27', title: 'RC Experts', description: "We know Rancho Cucamonga's neighborhoods, soil conditions, and water quality challenges from Day Creek to Victoria Gardens." },
        { icon: '\u2705', title: 'Licensed & Insured', description: 'CA License #1097482. Every Rancho Cucamonga job is fully insured with upfront, honest pricing.' },
      ]}
      seoContent={[
        'Looking for a reliable <strong>plumber in Rancho Cucamonga CA</strong>? Regal Plumbing & Rooter serves all of Rancho Cucamonga with professional, licensed plumbing services. From the established neighborhoods near <strong>Foothill Boulevard</strong> to the newer communities along <strong>Day Creek</strong> and near <strong>Victoria Gardens</strong>, we understand the unique plumbing needs of RC homeowners.',
        'Our <strong>emergency plumbing Rancho Cucamonga</strong> service is available 24/7. Whether it\'s a burst pipe in the middle of the night or a sewage backup on a holiday weekend, our team dispatches fast from our Ontario base to get your plumbing emergency under control.',
        '<strong>Drain cleaning Rancho Cucamonga</strong> is one of our most common services. The hard water throughout the Inland Empire accelerates mineral buildup inside drain pipes, leading to slow flow and eventual blockages. Our professional snaking and hydrojetting services restore full drain function.',
        'For <strong>slab leak detection</strong> and <strong>water heater services in Rancho Cucamonga</strong>, trust the local experts who know the area. Call <strong>(909) 600-4561</strong> for same-day service or 24/7 emergency response.',
      ]}
      faqs={[
        { question: 'How quickly can you reach Rancho Cucamonga?', answer: 'Based in nearby Ontario, our technicians can reach most Rancho Cucamonga locations within 30\u201350 minutes. Emergency calls are prioritized for fastest possible dispatch.' },
        { question: 'Do you serve all neighborhoods in Rancho Cucamonga?', answer: 'Yes \u2014 we serve all of Rancho Cucamonga, including Day Creek, Victoria Gardens area, Foothill corridor, Etiwanda, Terra Vista, and every neighborhood in between.' },
        { question: 'What plumbing issues are common in Rancho Cucamonga?', answer: 'We frequently handle drain blockages from hard water buildup, water heater failures, slab leaks in homes with shifting soil, and sewer line issues in older neighborhoods near Foothill Boulevard.' },
        { question: 'Can you install a tankless water heater in my Rancho Cucamonga home?', answer: 'Absolutely. We install all major brands of tankless water heaters and can evaluate whether your home\'s gas and electrical systems can support the upgrade.' },
        { question: 'Is weekend emergency service available in Rancho Cucamonga?', answer: 'Yes. Our emergency line is staffed 24/7/365. Call (909) 600-4561 any time for emergency plumbing service in Rancho Cucamonga.' },
      ]}
      ctaHeading="Need a Plumber in Rancho Cucamonga? Call Now"
      ctaSubtext="24/7 emergency and same-day service throughout Rancho Cucamonga, CA"
    />
  )
}
