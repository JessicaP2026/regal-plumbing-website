import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Sewer Line Repair - Camera Inspection & Trenchless ',
  description: 'Expert sewer line repair with camera inspection and trenchless options. Root intrusion, cracked pipes & more. Call (909) 600-4561.',
  path: '/sewer-line-repair',
})

export default function SewerLineRepairPage() {
  return (
    <ServicePageTemplate
      slug="sewer-line-repair"
      heroTitle="Sewer Line Repair"
      heroSubtitle="Expert sewer line diagnosis, repair, and replacement for Southern California homes and businesses"
      badge="Camera Diagnosis"
      heroImage="/images/sewer-line-repair-excavation-fontana-ca.webp"
      overviewEyebrow="Expert Diagnosis & Repair"
      overviewTitle="Sewer Line Repair & Replacement"
      overviewBody="Sewer line problems can cause serious damage if left untreated. We use camera inspection technology to accurately diagnose sewer line issues - root intrusion, cracks, bellied pipes, and more - then provide the most cost-effective repair solution, including trenchless options when available."
      overviewFeatures={[
        'Camera video inspection and diagnosis',
        'Pipe bursting and trenchless repair',
        'Root intrusion removal',
        'Full sewer line replacement when needed',
        'Bellied pipe correction',
        'Post-repair camera verification',
      ]}
      overviewImage="/images/sewer-line-excavation-ontario-ca.webp"
      overviewImageAlt="Sewer line excavation repair"
      covers={[
        { icon: '\uD83D\uDCF9', title: 'Camera Inspection', description: 'We use high-definition sewer cameras to locate the exact problem - root intrusion, cracks, offsets, or collapse - before we start any work.' },
        { icon: '\uD83C\uDF33', title: 'Root Intrusion', description: 'Tree roots penetrate sewer lines through joints and cracks. We remove root masses and repair the pipe to prevent re-entry.' },
        { icon: '\uD83D\uDD27', title: 'Trenchless Options', description: 'When possible, we use trenchless pipe bursting or lining to repair sewer lines without tearing up your yard or driveway.' },
      ]}
      ctaHeading="Sewer Problems? Get a Camera Inspection"
      ctaSubtext="Know exactly what's wrong before you spend a dollar on repairs"
    />
  )
}
