'use client'

import { useState } from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { motion, AnimatePresence } from 'framer-motion'
import { BUSINESS, SERVICES } from '@/lib/constants'

const NAV_LINKS = [
  { label: 'Home', href: '/' },
  { label: 'Services', href: '/services', hasDropdown: true },
  { label: 'About', href: '/about' },
  { label: 'Service Area', href: '/service-area' },
  { label: 'Contact', href: '/contact' },
]

export default function Header() {
  const [mobileOpen, setMobileOpen] = useState(false)
  const [servicesOpen, setServicesOpen] = useState(false)

  return (
    <header className="sticky top-0 z-[1000] bg-white shadow-md">
      <div className="max-w-content mx-auto px-6 flex items-center justify-between gap-6 h-[72px]">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-3 flex-shrink-0">
          <Image
            src="/images/regal-plumbing-logo.png"
            alt="Regal Plumbing & Rooter"
            width={160}
            height={56}
            className="h-14 w-auto"
            priority
          />
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden lg:flex items-center gap-1.5">
          {NAV_LINKS.map((link) => (
            <div key={link.href} className="relative group">
              <Link
                href={link.href}
                className="font-oswald font-medium text-sm tracking-widest uppercase text-dark-grey px-3 py-2 rounded hover:text-red hover:bg-red-50 transition-colors"
                onMouseEnter={() => link.hasDropdown && setServicesOpen(true)}
                onMouseLeave={() => link.hasDropdown && setServicesOpen(false)}
              >
                {link.label}
              </Link>
              {link.hasDropdown && (
                <div
                  onMouseEnter={() => setServicesOpen(true)}
                  onMouseLeave={() => setServicesOpen(false)}
                >
                  <AnimatePresence>
                    {servicesOpen && (
                      <motion.div
                        initial={{ opacity: 0, y: -4 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -4 }}
                        transition={{ duration: 0.15 }}
                        className="absolute top-full left-0 bg-white border border-gray-200 rounded-md shadow-lg py-2 min-w-[220px] z-50"
                      >
                        {SERVICES.map((s) => (
                          <Link
                            key={s.slug}
                            href={`/${s.slug}`}
                            className="block px-4 py-2 text-sm text-dark-grey hover:bg-red-50 hover:text-red transition-colors"
                          >
                            {s.name}
                          </Link>
                        ))}
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              )}
            </div>
          ))}
        </nav>

        {/* Right side */}
        <div className="flex items-center gap-3.5 flex-shrink-0">
          <a
            href={`tel:${BUSINESS.phoneTel}`}
            className="hidden sm:block font-oswald font-semibold text-base text-navy tracking-wide"
          >
            {BUSINESS.phone}
          </a>
          <a
            href={`tel:${BUSINESS.phoneTel}`}
            className="hidden md:inline-flex items-center justify-center gap-1.5 bg-red text-white border-2 border-red font-oswald font-semibold text-sm tracking-wider uppercase px-5 py-2.5 rounded hover:bg-red-dark hover:border-red-dark hover:-translate-y-0.5 transition-all"
          >
            Call Now
          </a>
          {/* Mobile hamburger */}
          <button
            className="lg:hidden flex flex-col gap-1.5 p-2"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle menu"
          >
            <span className={`block w-6 h-0.5 bg-dark-grey transition-transform ${mobileOpen ? 'rotate-45 translate-y-2' : ''}`} />
            <span className={`block w-6 h-0.5 bg-dark-grey transition-opacity ${mobileOpen ? 'opacity-0' : ''}`} />
            <span className={`block w-6 h-0.5 bg-dark-grey transition-transform ${mobileOpen ? '-rotate-45 -translate-y-2' : ''}`} />
          </button>
        </div>
      </div>

      {/* Mobile drawer */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="lg:hidden overflow-hidden bg-white border-t border-gray-200"
          >
            <nav className="flex flex-col py-4 px-6 gap-1">
              {NAV_LINKS.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  className="font-oswald font-medium text-base tracking-wider uppercase text-dark-grey py-3 border-b border-gray-100 hover:text-red transition-colors"
                  onClick={() => setMobileOpen(false)}
                >
                  {link.label}
                </Link>
              ))}
              <a
                href={`tel:${BUSINESS.phoneTel}`}
                className="mt-3 flex items-center justify-center gap-2 bg-red text-white font-oswald font-semibold text-base uppercase tracking-wider py-3 rounded"
              >
                Call {BUSINESS.phone}
              </a>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  )
}
