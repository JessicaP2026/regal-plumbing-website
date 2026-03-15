import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Gas Leak Detection \u2014 Safety Critical | Regal Plumbing & Rooter',
  description: 'Licensed gas leak detection, repair, and pressure testing. If you smell gas, call 911 first, then call us at (909) 600-4561.',
  path: '/gas-leak-detection',
})

export default function GasLeakDetectionPage() {
  return (
    <ServicePageTemplate
      slug="gas-leak-detection"
      heroTitle="Gas Leak Detection"
      heroSubtitle="Licensed gas line detection, repair, and safety testing for homes and businesses"
      badge="Safety Critical"
      heroImage="/images/camera-inspection-drain-cleaning-san-bernardino-ca.webp"
      overviewEyebrow="Safety First, Always"
      overviewTitle="Gas Leak Detection & Repair"
      overviewBody="A gas leak is a serious safety emergency. If you smell gas, leave the building immediately and call 911 first. Then call us. Our licensed plumbers perform precise gas leak detection and repair, ensuring your home or business is safe before restoring service. Never ignore a suspected gas leak."
      overviewFeatures={[
        'Electronic gas leak detection equipment',
        'Gas line repair and re-piping',
        'Pressure testing after repair',
        'Licensed for natural gas and propane systems',
        'Appliance gas line connections',
        'Gas line installation for new appliances',
      ]}
      overviewImage="/images/pipe-replacement-copper-ontario-ca.webp"
      overviewImageAlt="Gas line repair"
      covers={[
        { icon: '\uD83D\uDD0D', title: 'Leak Location', description: 'Using advanced electronic gas detectors, we pinpoint the exact location of gas leaks in your home\'s piping system.' },
        { icon: '\uD83D\uDD27', title: 'Line Repair & Repiping', description: 'Once located, we repair or replace the damaged section of gas line to restore safe operation to your home.' },
        { icon: '\uD83D\uDCCA', title: 'Pressure Testing', description: 'After every repair, we perform a pressure test to verify the integrity of your entire gas line system before restoring service.' },
      ]}
      ctaHeading="Gas Leak? Safety First. Then Call Us"
      ctaSubtext="If you smell gas, evacuate and call 911. Then call us for professional detection and repair."
    />
  )
}
