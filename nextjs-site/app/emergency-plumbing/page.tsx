import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Emergency Plumbing Services - 24/7 | Regal Plumbing & Rooter',
  description: 'Rapid-response 24/7 emergency plumbing for the Inland Empire. Burst pipes, sewage backups, major leaks. Call (909) 600-4561 now.',
  path: '/emergency-plumbing',
})

export default function EmergencyPlumbingPage() {
  return (
    <ServicePageTemplate
      slug="emergency-plumbing"
      heroTitle="Emergency Plumbing"
      heroSubtitle="Rapid-response emergency plumbing for the Inland Empire - we're on call around the clock"
      badge="24/7 Available"
      heroImage="/images/pipe-repair-leak-detection-chino-hills-ca.webp"
      overviewEyebrow="When Every Minute Counts"
      overviewTitle="24/7 Emergency Plumbing Response"
      overviewBody="When a plumbing emergency strikes - a burst pipe, major leak, or sewage backup - every minute matters. Regal Plumbing & Rooter provides rapid-response emergency service around the clock, 365 days a year. We mobilize fast, arrive with the right equipment, and get the problem under control before it causes serious damage to your home or property."
      overviewFeatures={[
        'Typically on-site within the hour',
        'Burst pipe detection and emergency shutoff',
        'Sewage backup and overflow response',
        'Major leak control and repair',
        '24/7 availability including holidays',
        'Upfront pricing even in emergencies',
      ]}
      overviewImage="/images/sewer-repair-service-truck-inland-empire.webp"
      overviewImageAlt="Emergency plumbing response"
      covers={[
        { icon: '\uD83D\uDCA5', title: 'Burst Pipes', description: 'Immediate shutoff and repair of burst or frozen pipes before water damage spreads to walls, floors, and structural elements.' },
        { icon: '\uD83D\uDEBF', title: 'Sewage Backups', description: 'Emergency response to sewage backups and overflow situations that require immediate containment and clearance.' },
        { icon: '\uD83D\uDCA7', title: 'Major Leaks', description: 'Rapid detection and repair of active leaks - under sinks, behind walls, or at the main line - stopping damage fast.' },
      ]}
      ctaHeading="Plumbing Emergency? Call Right Now"
      ctaSubtext="Our emergency team is standing by 24/7 - including weekends and holidays"
    />
  )
}
