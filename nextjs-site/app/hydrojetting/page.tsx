import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Hydrojetting Services \u2014 High-Pressure Pipe Cleaning | Regal Plumbing & Rooter',
  description: 'High-pressure hydrojetting for drain and sewer lines. Clears grease, roots & scale buildup. Call (909) 600-4561.',
  path: '/hydrojetting',
})

export default function HydrojettingPage() {
  return (
    <ServicePageTemplate
      slug="hydrojetting"
      heroTitle="Hydrojetting"
      heroSubtitle="High-pressure water jetting to scour pipe walls clean and restore full flow capacity"
      badge="High-Pressure Cleaning"
      heroImage="/images/hydro-jetting-roof-rancho-cucamonga-ca.webp"
      overviewEyebrow="The Most Effective Pipe Cleaning"
      overviewTitle="Professional Hydrojetting Services"
      overviewBody="When snaking isn't enough, hydrojetting is the most effective method for clearing stubborn grease, scale, and root intrusion from drain and sewer lines. Using water at up to 4,000 PSI, hydrojetting scours pipe walls clean and restores full pipe capacity \u2014 ideal for commercial properties and recurring residential blockages."
      overviewFeatures={[
        'Clears grease, scale, and hardened buildup',
        'Removes tree root intrusion',
        'Ideal for commercial kitchens and restaurants',
        'Extends the life of your plumbing system',
        'Pre-jetting camera inspection included',
        'Environmentally friendly \u2014 water only',
      ]}
      overviewImage="/images/camera-inspection-drain-cleaning-san-bernardino-ca.webp"
      overviewImageAlt="Hydrojetting equipment"
      covers={[
        { icon: '\uD83E\uDDEA', title: 'Grease & Scale', description: 'Commercial kitchens and older residential pipes accumulate grease and mineral scale. Hydrojetting blasts it all away.' },
        { icon: '\uD83C\uDF33', title: 'Root Intrusion', description: 'Tree roots inside sewer lines are no match for 4,000 PSI water pressure. We cut through roots and clear the full line.' },
        { icon: '\uD83C\uDFED', title: 'Commercial Use', description: 'Restaurants, hotels, and commercial properties rely on hydrojetting for regular maintenance to prevent costly backups.' },
      ]}
      ctaHeading="Clear Pipes. Better Flow. Call Today"
      ctaSubtext="Professional hydrojetting for residential and commercial properties"
    />
  )
}
