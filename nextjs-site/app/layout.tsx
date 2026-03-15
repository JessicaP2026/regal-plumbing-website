import type { Metadata } from 'next'
import { Oswald, Open_Sans } from 'next/font/google'
import { Analytics } from '@vercel/analytics/react'
import SchemaMarkup from '@/components/SchemaMarkup'
import EmergencyBar from '@/components/EmergencyBar'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import MobileStickyCTA from '@/components/MobileStickyCTA'
import { generateLocalBusinessSchema, generateWebsiteSchema } from '@/lib/schema'
import { BUSINESS } from '@/lib/constants'
import './globals.css'

const oswald = Oswald({
  subsets: ['latin'],
  variable: '--font-oswald',
  display: 'swap',
})

const openSans = Open_Sans({
  subsets: ['latin'],
  variable: '--font-open-sans',
  display: 'swap',
})

export const metadata: Metadata = {
  title: {
    default: `${BUSINESS.name} \u2014 24/7 Plumber | Inland Empire & San Gabriel Valley`,
    template: `%s | ${BUSINESS.name}`,
  },
  description: 'Licensed 24/7 plumber serving 32+ cities in the Inland Empire & San Gabriel Valley. Emergency plumbing, drain cleaning, slab leak detection & more. Call (909) 600-4561.',
  metadataBase: new URL(BUSINESS.url),
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={`${oswald.variable} ${openSans.variable}`}>
      <body className="font-sans text-dark-grey leading-relaxed antialiased">
        <SchemaMarkup schema={[generateLocalBusinessSchema(), generateWebsiteSchema()]} />
        <EmergencyBar />
        <Header />
        <main>{children}</main>
        <Footer />
        <MobileStickyCTA />
        <Analytics />
      </body>
    </html>
  )
}
