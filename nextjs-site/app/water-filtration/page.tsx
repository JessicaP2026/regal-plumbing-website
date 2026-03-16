import Link from 'next/link'
import { generatePageMetadata } from '@/lib/metadata'
import ServicePageTemplate from '@/components/ServicePageTemplate'

export const metadata = generatePageMetadata({
  title: 'Water Filtration & Softeners - Regal Plumbing & Rooter',
  description: 'Whole-home water softeners, reverse osmosis, and filtration systems. Cleaner, softer water for your home. Call (909) 600-4561.',
  path: '/water-filtration',
})

export default function WaterFiltrationPage() {
  return (
    <ServicePageTemplate
      slug="water-filtration"
      heroTitle="Water Filtration"
      heroSubtitle="Cleaner, softer water for your entire home - water softeners, reverse osmosis, and whole-home filtration systems"
      badge="Cleaner, Softer Water"
      heroImage="/images/pipe-replacement-copper-ontario-ca.webp"
      overviewEyebrow="Better Water, Better Living"
      overviewTitle="Water Filtration & Softener Installation"
      overviewBody={<>Southern California water is notoriously hard. Mineral buildup damages appliances, leaves residue on fixtures, and affects the taste and quality of your water. We install whole-home water softeners, under-sink filters, and reverse osmosis systems to give you cleaner, softer water throughout your home.{' '}Hard water affects the entire region &mdash; we install filtration systems in{' '}<Link href="/service-area/ontario-ca" className="text-red font-medium hover:underline">Ontario</Link>,{' '}<Link href="/service-area/rancho-cucamonga-ca" className="text-red font-medium hover:underline">Rancho Cucamonga</Link>,{' '}<Link href="/service-area/fontana-ca" className="text-red font-medium hover:underline">Fontana</Link>,{' '}<Link href="/service-area/pomona-ca" className="text-red font-medium hover:underline">Pomona</Link>,{' '}<Link href="/service-area/chino-ca" className="text-red font-medium hover:underline">Chino</Link>,{' '}<Link href="/service-area/corona-ca" className="text-red font-medium hover:underline">Corona</Link>,{' '}<Link href="/service-area/upland-ca" className="text-red font-medium hover:underline">Upland</Link>, and{' '}<Link href="/service-area/west-covina-ca" className="text-red font-medium hover:underline">West Covina</Link>.</>}
      overviewFeatures={[
        'Whole-home water softener installation',
        'Under-sink reverse osmosis systems',
        'Carbon filtration and UV purification',
        'Filter cartridge replacement service',
        'Water quality testing',
        'Custom solutions for your water needs',
      ]}
      overviewImage="/images/copper-pipe-installation-chino-ca.webp"
      overviewImageAlt="Water filtration system installation"
      covers={[
        { icon: '\uD83D\uDCA7', title: 'Water Softeners', description: 'Whole-home water softeners remove calcium and magnesium, protecting your appliances and leaving skin and hair feeling softer.' },
        { icon: '\uD83E\uDDEA', title: 'Reverse Osmosis', description: 'Under-sink RO systems provide pure, great-tasting drinking water by removing contaminants, chlorine, and dissolved solids.' },
        { icon: '\uD83C\uDFE0', title: 'Whole-Home Filtration', description: 'Comprehensive filtration systems that treat all water entering your home - every faucet, shower, and appliance gets clean water.' },
      ]}
      ctaHeading="Better Water Starts with One Call"
      ctaSubtext="Free water quality assessment and expert filtration recommendations"
    />
  )
}
