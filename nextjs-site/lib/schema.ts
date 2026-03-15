import { BUSINESS, SERVICES, type City } from './constants'

export function generateLocalBusinessSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Plumber',
    name: BUSINESS.name,
    image: `${BUSINESS.url}/images/regal-plumbing-logo.png`,
    telephone: BUSINESS.phone,
    email: BUSINESS.email,
    url: BUSINESS.url,
    address: {
      '@type': 'PostalAddress',
      streetAddress: BUSINESS.address.street,
      addressLocality: BUSINESS.address.city,
      addressRegion: BUSINESS.address.state,
      postalCode: BUSINESS.address.zip,
      addressCountry: 'US',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: BUSINESS.geo.lat,
      longitude: BUSINESS.geo.lng,
    },
    openingHoursSpecification: [
      {
        '@type': 'OpeningHoursSpecification',
        dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        opens: '07:00',
        closes: '19:00',
      },
      {
        '@type': 'OpeningHoursSpecification',
        dayOfWeek: 'Sunday',
        opens: '00:00',
        closes: '23:59',
        description: 'Emergency service only',
      },
    ],
    priceRange: '$$',
    areaServed: {
      '@type': 'State',
      name: 'California',
    },
  }
}

export function generateWebsiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: BUSINESS.name,
    url: BUSINESS.url,
  }
}

export function generateServiceSchema(serviceSlug: string) {
  const service = SERVICES.find((s) => s.slug === serviceSlug)
  if (!service) return null
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: service.name,
    description: service.description,
    provider: {
      '@type': 'Plumber',
      name: BUSINESS.name,
      telephone: BUSINESS.phone,
      url: BUSINESS.url,
    },
    areaServed: {
      '@type': 'State',
      name: 'California',
    },
    url: `${BUSINESS.url}/${service.slug}`,
  }
}

export function generateCitySchema(city: City) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Plumber',
    name: `${BUSINESS.name} \u2014 ${city.name}, CA`,
    telephone: BUSINESS.phone,
    url: `${BUSINESS.url}/service-area/${city.slug}`,
    address: {
      '@type': 'PostalAddress',
      addressLocality: city.name,
      addressRegion: 'CA',
      addressCountry: 'US',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: city.mapLat || BUSINESS.geo.lat,
      longitude: city.mapLng || BUSINESS.geo.lng,
    },
    areaServed: {
      '@type': 'City',
      name: city.name,
    },
  }
}

export function generateFAQSchema(faqs: readonly { question: string; answer: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  }
}

export function generateBreadcrumbSchema(items: { name: string; url: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      item: item.url,
    })),
  }
}
