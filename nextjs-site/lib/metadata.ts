import type { Metadata } from 'next'
import { BUSINESS } from './constants'

interface PageMetadataOptions {
  title: string
  description: string
  path: string
  noindex?: boolean
}

export function generatePageMetadata({ title, description, path, noindex }: PageMetadataOptions): Metadata {
  const url = `${BUSINESS.url}${path}`
  return {
    title,
    description,
    alternates: { canonical: url },
    openGraph: {
      title,
      description,
      url,
      siteName: BUSINESS.name,
      locale: 'en_US',
      type: 'website',
      images: [
        {
          url: `${BUSINESS.url}/images/regal-plumbing-logo.png`,
          width: 600,
          height: 600,
          alt: BUSINESS.name,
        },
      ],
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description,
    },
    ...(noindex ? { robots: { index: false, follow: false } } : {}),
  }
}
