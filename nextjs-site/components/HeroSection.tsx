import Image from 'next/image'
import Link from 'next/link'
import BreadCrumb from './BreadCrumb'

interface BreadcrumbItem {
  label: string
  href?: string
}

interface HeroSectionProps {
  title: string
  subtitle: string
  breadcrumbs: BreadcrumbItem[]
  bgImage?: string
  navyBg?: boolean
  badge?: string
  ctaText?: string
  ctaHref?: string
}

export default function HeroSection({
  title,
  subtitle,
  breadcrumbs,
  bgImage,
  navyBg,
  badge,
  ctaText,
  ctaHref,
}: HeroSectionProps) {
  if (bgImage) {
    return (
      <div className="relative overflow-hidden min-h-[320px] flex items-center">
        <div className="absolute inset-0">
          <Image
            src={bgImage}
            alt={title}
            fill
            className="object-cover"
            priority
            sizes="100vw"
          />
        </div>
        <div className="absolute inset-0 bg-gradient-to-r from-black/85 via-navy/65 to-red/25" />
        <div className="relative z-10 max-w-content mx-auto px-6 py-[72px] w-full">
          <BreadCrumb items={breadcrumbs} />
          {badge && (
            <span className="inline-block bg-red text-white font-oswald font-semibold text-xs tracking-widest uppercase px-3.5 py-1.5 rounded mb-4">
              {badge}
            </span>
          )}
          <h1 className="font-oswald font-bold text-[clamp(30px,4vw,52px)] text-white uppercase tracking-wider mb-3">
            {title}
          </h1>
          <p className="text-[17px] text-gray-300 max-w-[600px] leading-relaxed">{subtitle}</p>
          {ctaText && ctaHref && (
            <Link
              href={ctaHref}
              className="inline-flex items-center gap-1.5 mt-6 bg-red text-white border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red-dark hover:border-red-dark hover:-translate-y-0.5 transition-all"
            >
              {ctaText}
            </Link>
          )}
        </div>
      </div>
    )
  }

  const bgClass = navyBg ? 'bg-navy' : 'bg-dark-grey'

  return (
    <div className={`${bgClass} relative overflow-hidden py-16 px-6`}>
      <div className="absolute inset-0 bg-[repeating-linear-gradient(45deg,transparent,transparent_2px,rgba(255,255,255,0.015)_2px,rgba(255,255,255,0.015)_4px)]" />
      <div className="relative z-10 max-w-content mx-auto">
        <BreadCrumb items={breadcrumbs} />
        {badge && (
          <span className="inline-block bg-red text-white font-oswald font-semibold text-xs tracking-widest uppercase px-3.5 py-1.5 rounded mb-4">
            {badge}
          </span>
        )}
        <h1 className="font-oswald font-bold text-[clamp(30px,4vw,48px)] text-white uppercase tracking-wider mb-3">
          {title}
        </h1>
        <p className={`text-base max-w-[580px] ${navyBg ? 'text-blue-300' : 'text-gray-300'}`}>
          {subtitle}
        </p>
        {ctaText && ctaHref && (
          <Link
            href={ctaHref}
            className="inline-flex items-center gap-1.5 mt-6 bg-red text-white border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red-dark hover:border-red-dark hover:-translate-y-0.5 transition-all"
          >
            {ctaText}
          </Link>
        )}
      </div>
    </div>
  )
}
