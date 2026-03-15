import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Water Heater Services \u2014 Install & Repair | Regal Plumbing & Rooter',
  description: 'Water heater installation and repair \u2014 tank, tankless & heat pump models. All major brands. Call (909) 600-4561.',
  path: '/water-heater-services',
})

export default function WaterHeaterServicesPage() {
  return (
    <ServicePageTemplate
      slug="water-heater-services"
      heroTitle="Water Heater Services"
      heroSubtitle="Installation and repair of all water heater types \u2014 tank, tankless, and heat pump systems"
      badge="All Types & Brands"
      heroImage="/images/sink-faucet-installation-ontario-ca.webp"
      overviewEyebrow="Hot Water When You Need It"
      overviewTitle="Water Heater Install & Repair"
      overviewBody="No hot water? We install and repair all types of water heaters \u2014 traditional tank units, tankless (on-demand) systems, and hybrid heat pump models. Our technicians are experienced with all major brands and can help you choose the right system for your household's needs and budget."
      overviewFeatures={[
        'Traditional tank water heater install & repair',
        'Tankless water heater installation',
        'Heat pump water heater systems',
        'Anode rod replacement and flushing',
        'Temperature and pressure valve service',
        'All major brands serviced',
      ]}
      overviewImage="/images/copper-pipe-installation-chino-ca.webp"
      overviewImageAlt="Water heater installation"
      covers={[
        { icon: '\uD83C\uDFED', title: 'Tank Water Heaters', description: 'Installation, repair, and replacement of traditional tank water heaters in all sizes \u2014 40, 50, and 75+ gallon units.' },
        { icon: '\u26A1', title: 'Tankless Systems', description: 'On-demand hot water with tankless systems. We size, install, and service all major tankless brands.' },
        { icon: '\uD83D\uDD27', title: 'Repairs & Tune-Ups', description: 'Thermostat issues, pilot lights, anode rods, and sediment buildup \u2014 we diagnose and repair all water heater problems.' },
      ]}
      ctaHeading="No Hot Water? We Can Help Today"
      ctaSubtext="Same-day water heater repair and installation across Southern California"
    />
  )
}
