import Link from 'next/link'
import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Water Heater Services - Install & Repair ',
  description: 'Water heater installation and repair - tank, tankless & heat pump models. All major brands. Call (909) 600-4561.',
  path: '/water-heater-services',
})

export default function WaterHeaterServicesPage() {
  return (
    <ServicePageTemplate
      slug="water-heater-services"
      heroTitle="Water Heater Services"
      heroSubtitle="Installation and repair of all water heater types - tank, tankless, and heat pump systems"
      badge="All Types & Brands"
      heroImage="/images/water-heater-installation-ontario-ca.webp"
      overviewEyebrow="Hot Water When You Need It"
      overviewTitle="Water Heater Install & Repair"
      overviewBody={<>No hot water? We install and repair all types of water heaters &mdash; traditional tank units, tankless (on-demand) systems, and hybrid heat pump models. Our technicians are experienced with all major brands and can help you choose the right system for your household&apos;s needs and budget.{' '}We serve homeowners in{' '}<Link href="/service-area/rancho-cucamonga-ca" className="text-red font-medium hover:underline">Rancho Cucamonga</Link>,{' '}<Link href="/service-area/west-covina-ca" className="text-red font-medium hover:underline">West Covina</Link>, and{' '}<Link href="/service-area/corona-ca" className="text-red font-medium hover:underline">Corona</Link>, as well as throughout Southern California.</>}
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
        { icon: '\uD83C\uDFED', title: 'Tank Water Heaters', description: 'Installation, repair, and replacement of traditional tank water heaters in all sizes - 40, 50, and 75+ gallon units.' },
        { icon: '\u26A1', title: 'Tankless Systems', description: 'On-demand hot water with tankless systems. We size, install, and service all major tankless brands.' },
        { icon: '\uD83D\uDD27', title: 'Repairs & Tune-Ups', description: 'Thermostat issues, pilot lights, anode rods, and sediment buildup - we diagnose and repair all water heater problems.' },
      ]}
      recentWorkHeading="Our Recent Water Heater Work"
      recentWork={[
        {
          src: '/images/water-heater-installation-ontario-ca.webp',
          alt: 'Tank water heater installation Ontario CA - Regal Plumbing & Rooter',
          title: 'Tank Water Heater Installation',
          description: 'New 50-gallon gas water heater installed for a homeowner in Ontario, CA. Replaced a failing 15-year-old unit with same-day service.',
        },
        {
          src: '/images/water-heater-installation-rancho-cucamonga-ca.webp',
          alt: 'Water heater replacement Rancho Cucamonga CA - Regal Plumbing & Rooter',
          title: 'Water Heater Replacement',
          description: 'Full water heater replacement in Rancho Cucamonga, CA. Old unit removed and new energy-efficient model installed within hours.',
        },
        {
          src: '/images/water-heater-repair-upland-ca.webp',
          alt: 'Emergency water heater repair Upland CA - Regal Plumbing & Rooter',
          title: 'Emergency Water Heater Repair',
          description: 'Emergency repair call in Upland, CA. Diagnosed a failed heating element and restored hot water the same day.',
        },
        {
          src: '/images/water-heater-replacement-fontana-ca.webp',
          alt: 'Water heater replacement Fontana CA - Regal Plumbing & Rooter',
          title: 'Water Heater Replacement — Fontana',
          description: 'Water heater replacement in Fontana, CA. Customer had no hot water — we arrived within the hour and completed the job same day.',
        },
      ]}
      ctaHeading="No Hot Water? We Can Help Today"
      ctaSubtext="Same-day water heater repair and installation across Southern California"
    />
  )
}
