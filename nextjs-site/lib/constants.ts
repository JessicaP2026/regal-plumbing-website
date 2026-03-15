export const BUSINESS = {
  name: 'Regal Plumbing & Rooter',
  phone: '(909) 600-4561',
  phoneTel: '9096004561',
  email: 'info@regalplumbingservices.com',
  address: {
    street: '2141 E Philadelphia St, Suite R',
    city: 'Ontario',
    state: 'CA',
    zip: '91761',
  },
  license: '#1097482',
  url: process.env.NEXT_PUBLIC_SITE_URL || 'https://regalplumbingservices.com',
  hours: {
    office: 'Mon\u2013Sat: 7am\u20137pm',
    emergency: '24/7, 365 days',
    sunday: 'Emergency service only',
  },
  tagline: 'Honest, professional plumbing & rooter services for the Inland Empire & San Gabriel Valley.',
  founded: '2022',
  geo: { lat: 34.0633, lng: -117.6509 },
} as const

export interface Service {
  name: string
  slug: string
  description: string
  image: string
  alt: string
  badge?: string
  heroImage?: string
}

export const SERVICES: Service[] = [
  {
    name: 'Emergency Plumbing',
    slug: 'emergency-plumbing',
    description: 'Rapid-response emergency plumbing for the Inland Empire \u2014 we\u2019re on call around the clock.',
    image: '/images/pipe-repair-leak-detection-chino-hills-ca.webp',
    alt: 'Emergency plumbing service',
    badge: '24/7 Available',
    heroImage: '/images/pipe-repair-leak-detection-chino-hills-ca.webp',
  },
  {
    name: 'Drain Cleaning',
    slug: 'drain-cleaning',
    description: 'Professional clearing of kitchen, bathroom, and main sewer line blockages.',
    image: '/images/drain-cleaning-shower-upland-ca.webp',
    alt: 'Drain cleaning service',
    badge: 'Residential & Commercial',
    heroImage: '/images/drain-cleaning-shower-upland-ca.webp',
  },
  {
    name: 'Sewer Line Repair',
    slug: 'sewer-line-repair',
    description: 'Camera inspection, trenchless repair, and full sewer line replacement.',
    image: '/images/sewer-line-repair-excavation-fontana-ca.webp',
    alt: 'Sewer line repair',
    badge: 'Camera Diagnosis',
    heroImage: '/images/sewer-line-repair-excavation-fontana-ca.webp',
  },
  {
    name: 'Water Heater Services',
    slug: 'water-heater-services',
    description: 'Installation and repair of tank, tankless, and heat pump water heaters.',
    image: '/images/sink-faucet-installation-ontario-ca.webp',
    alt: 'Water heater installation',
    badge: 'All Types & Brands',
    heroImage: '/images/sink-faucet-installation-ontario-ca.webp',
  },
  {
    name: 'Slab Leak Detection',
    slug: 'slab-leak-detection',
    description: 'Electronic leak detection beneath concrete slabs with minimal disruption.',
    image: '/images/leak-repair-wall-open-ontario-ca.webp',
    alt: 'Slab leak detection',
    badge: 'Non-Invasive Technology',
    heroImage: '/images/leak-repair-wall-open-ontario-ca.webp',
  },
  {
    name: 'Hydrojetting',
    slug: 'hydrojetting',
    description: 'High-pressure water jetting to scour pipe walls and restore full flow.',
    image: '/images/hydro-jetting-roof-rancho-cucamonga-ca.webp',
    alt: 'Hydrojetting service',
    badge: 'High-Pressure Cleaning',
    heroImage: '/images/hydro-jetting-roof-rancho-cucamonga-ca.webp',
  },
  {
    name: 'Gas Leak Detection',
    slug: 'gas-leak-detection',
    description: 'Licensed gas line detection, repair, and pressure testing for safety.',
    image: '/images/camera-inspection-drain-cleaning-san-bernardino-ca.webp',
    alt: 'Gas leak detection',
    badge: 'Safety Critical',
    heroImage: '/images/camera-inspection-drain-cleaning-san-bernardino-ca.webp',
  },
  {
    name: 'Water Filtration',
    slug: 'water-filtration',
    description: 'Whole-home softeners, reverse osmosis, and filtration systems installed.',
    image: '/images/pipe-replacement-copper-ontario-ca.webp',
    alt: 'Water filtration systems',
    badge: 'Cleaner, Softer Water',
    heroImage: '/images/pipe-replacement-copper-ontario-ca.webp',
  },
]

export interface City {
  name: string
  slug: string
  hero: string
  mapLat?: number
  mapLng?: number
}

export const CITIES: City[] = [
  { name: 'Ontario', slug: 'ontario-ca', hero: 'Plumber in Ontario, CA', mapLat: 34.0633, mapLng: -117.6509 },
  { name: 'Rancho Cucamonga', slug: 'rancho-cucamonga-ca', hero: 'Plumber in Rancho Cucamonga, CA', mapLat: 34.1064, mapLng: -117.5931 },
  { name: 'Fontana', slug: 'fontana-ca', hero: 'Plumber in Fontana, CA', mapLat: 34.0922, mapLng: -117.4350 },
  { name: 'Pomona', slug: 'pomona-ca', hero: 'Plumber in Pomona, CA', mapLat: 34.0551, mapLng: -117.7523 },
  { name: 'Chino', slug: 'chino-ca', hero: 'Plumber in Chino, CA', mapLat: 34.0122, mapLng: -117.6889 },
  { name: 'Corona', slug: 'corona-ca', hero: 'Plumber in Corona, CA', mapLat: 33.8753, mapLng: -117.5664 },
  { name: 'Upland', slug: 'upland-ca', hero: 'Plumber in Upland, CA', mapLat: 34.0975, mapLng: -117.6484 },
  { name: 'West Covina', slug: 'west-covina-ca', hero: 'Plumber in West Covina, CA', mapLat: 34.0686, mapLng: -117.9390 },
]

export const ALL_CITIES: string[] = [
  'Azusa', 'Bloomington', 'Brea', 'Charter Oak', 'Chino', 'Chino Hills',
  'Citrus', 'Claremont', 'Colton', 'Corona', 'Covina', 'Diamond Bar',
  'Eastvale', 'Fontana', 'Glendora', 'Highgrove', 'Jurupa Valley', 'La Verne',
  'Loma Linda', 'Mira Loma', 'Montclair', 'Muscoy', 'Norco', 'Ontario',
  'Pomona', 'Rancho Cucamonga', 'Rowland Heights', 'San Dimas', 'Upland',
  'Walnut', 'West Covina', 'Yorba Linda',
]

export const TRUST_ITEMS = [
  { icon: '\u23F0', label: '24/7 Emergency', sub: 'Always Available' },
  { icon: '\uD83D\uDC68\u200D\uD83D\uDC69\u200D\uD83D\uDC67', label: 'Family Owned & Operated', sub: 'Community Focused' },
  { icon: '\u2705', label: 'CA Licensed #1097482', sub: 'Fully Insured' },
  { icon: '\u2B50', label: '4+ Years Experience', sub: 'Proven Track Record' },
  { icon: '\uD83D\uDCCD', label: '32+ Cities Served', sub: 'Southern California' },
] as const

export const REVIEWS = [
  {
    name: 'Maria G.',
    city: 'Ontario, CA',
    rating: 5,
    text: 'Regal Plumbing came out within an hour for our emergency. They were professional, upfront about pricing, and fixed our burst pipe quickly. Highly recommend!',
  },
  {
    name: 'David R.',
    city: 'Rancho Cucamonga, CA',
    rating: 5,
    text: 'We called them for a slab leak and they found it with zero damage to our floor. Fair pricing and great communication throughout the whole process.',
  },
  {
    name: 'Jennifer T.',
    city: 'Fontana, CA',
    rating: 5,
    text: 'Amazing team! They installed our new tankless water heater and even took the time to explain maintenance tips. Clean, professional, and reasonably priced.',
  },
] as const

export const FAQS_HOME = [
  {
    question: 'Do you offer 24/7 emergency plumbing service?',
    answer: 'Yes. Our emergency plumbing line is staffed 24 hours a day, 7 days a week, 365 days a year. Call (909) 600-4561 any time \u2014 a real person will answer and dispatch a technician.',
  },
  {
    question: 'How fast can you get to my home?',
    answer: 'For emergencies, we typically arrive within 60 minutes. For scheduled service, we offer same-day appointments in most cities across our coverage area.',
  },
  {
    question: 'What areas do you serve?',
    answer: 'We serve 32+ cities across the Inland Empire and San Gabriel Valley, including Ontario, Rancho Cucamonga, Fontana, Pomona, Chino, Corona, Upland, West Covina, and more.',
  },
  {
    question: 'Are you licensed and insured?',
    answer: 'Yes. Regal Plumbing & Rooter holds California Contractor License #1097482. We are fully insured and bonded for your protection.',
  },
  {
    question: 'Do you provide free estimates?',
    answer: 'We provide upfront pricing before any work begins. For most services, we offer free estimates after an on-site evaluation. No hidden fees, ever.',
  },
  {
    question: 'What payment methods do you accept?',
    answer: 'We accept cash, checks, and all major credit cards. For larger jobs, we can discuss payment plan options.',
  },
] as const
