import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Drain Cleaning Services \u2014 Regal Plumbing & Rooter',
  description: 'Professional drain cleaning for kitchen, bathroom, and main sewer lines. Residential & commercial. Call (909) 600-4561.',
  path: '/drain-cleaning',
})

export default function DrainCleaningPage() {
  return (
    <ServicePageTemplate
      slug="drain-cleaning"
      heroTitle="Drain Cleaning"
      heroSubtitle="Professional drain clearing for residential and commercial properties across Southern California"
      badge="Residential & Commercial"
      heroImage="/images/drain-cleaning-shower-upland-ca.webp"
      overviewEyebrow="Restore Full Flow"
      overviewTitle="Professional Drain Cleaning Services"
      overviewBody="Slow or blocked drains are more than an inconvenience \u2014 they can signal deeper plumbing issues. Our drain cleaning services clear everything from minor kitchen clogs to severe main line blockages, using professional-grade equipment to restore full flow and prevent future buildup."
      overviewFeatures={[
        'Kitchen and bathroom drain clearing',
        'Main sewer line snaking',
        'Floor drain and utility sink cleaning',
        'Preventative maintenance plans available',
        'Camera inspection to identify root causes',
        'Same-day service in most areas',
      ]}
      overviewImage="/images/drain-cleaning-bathtub-rialto-ca.webp"
      overviewImageAlt="Drain cleaning service"
      covers={[
        { icon: '\uD83C\uDF73', title: 'Kitchen Drains', description: 'Grease, food particles, and soap scum build up over time. We clear kitchen drain clogs and restore proper flow.' },
        { icon: '\uD83D\uDEC1', title: 'Bathroom Drains', description: 'Hair, soap residue, and mineral deposits cause slow bathroom drains. We clear them completely and prevent future issues.' },
        { icon: '\uD83C\uDFE0', title: 'Main Sewer Line', description: 'When multiple drains slow down simultaneously, the main sewer line may be blocked. We snake and clear main lines efficiently.' },
      ]}
      ctaHeading="Ready for Clear Drains?"
      ctaSubtext="Call now for professional drain cleaning service across Southern California"
    />
  )
}
