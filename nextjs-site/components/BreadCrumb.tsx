import Link from 'next/link'

interface BreadcrumbItem {
  label: string
  href?: string
}

interface BreadCrumbProps {
  items: BreadcrumbItem[]
}

export default function BreadCrumb({ items }: BreadCrumbProps) {
  return (
    <nav className="flex items-center gap-2 text-[13px] text-gray-400 mb-3.5">
      {items.map((item, i) => (
        <span key={i} className="flex items-center gap-2">
          {i > 0 && <span className="text-gray-600">&rsaquo;</span>}
          {item.href ? (
            <Link href={item.href} className="hover:text-white transition-colors">
              {item.label}
            </Link>
          ) : (
            <span className="text-red-light">{item.label}</span>
          )}
        </span>
      ))}
    </nav>
  )
}
