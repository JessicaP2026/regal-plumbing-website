import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Slab Leak Detection \u2014 Non-Invasive | Regal Plumbing & Rooter',
  description: 'Electronic slab leak detection with minimal disruption. Spot repair, re-routing & epoxy lining. Call (909) 600-4561.',
  path: '/slab-leak-detection',
})

export default function SlabLeakDetectionPage() {
  return (
    <ServicePageTemplate
      slug="slab-leak-detection"
      heroTitle="Slab Leak Detection"
      heroSubtitle="Non-invasive electronic leak detection beneath concrete slabs \u2014 saving your home from hidden water damage"
      badge="Non-Invasive Technology"
      heroImage="/images/leak-repair-wall-open-ontario-ca.webp"
      overviewEyebrow="Find It Fast, Fix It Right"
      overviewTitle="Slab Leak Detection & Repair"
      overviewBody="Slab leaks are among the most damaging \u2014 and hardest to find \u2014 plumbing problems a homeowner can face. We use electronic detection equipment to precisely locate leaks beneath your concrete slab without unnecessary excavation, saving you time, money, and the headache of major property disruption."
      overviewFeatures={[
        'Electronic leak detection \u2014 no guesswork',
        'Spot repair and re-routing options',
        'Epoxy pipe lining (non-invasive)',
        'Post-repair pressure testing',
        'Foundation damage assessment',
        'Insurance documentation assistance',
      ]}
      overviewImage="/images/pipe-repair-leak-detection-chino-hills-ca.webp"
      overviewImageAlt="Slab leak detection equipment"
      covers={[
        { icon: '\uD83D\uDD0D', title: 'Electronic Detection', description: 'Using sensitive acoustic and electronic equipment, we pinpoint the exact location of leaks beneath your slab without breaking concrete.' },
        { icon: '\uD83D\uDD27', title: 'Spot Repair', description: 'Once located, we access the leak through a targeted opening, repair the pipe, and restore your floor with minimal disruption.' },
        { icon: '\uD83C\uDFE0', title: 'Re-Routing & Lining', description: 'For severely damaged pipes, we offer re-routing through walls or ceilings, or epoxy pipe lining to restore flow without excavation.' },
      ]}
      ctaHeading="Suspect a Slab Leak? Act Fast"
      ctaSubtext="Early detection saves thousands in foundation and water damage repair"
    />
  )
}
