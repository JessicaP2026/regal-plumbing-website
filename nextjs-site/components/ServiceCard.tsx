import Image from 'next/image'
import Link from 'next/link'

interface ServiceCardProps {
  name: string
  slug: string
  description: string
  image: string
  alt: string
}

export default function ServiceCard({ name, slug, description, image, alt }: ServiceCardProps) {
  return (
    <Link
      href={`/${slug}`}
      className="group bg-white border border-gray-200 rounded-lg overflow-hidden transition-all duration-300 hover:-translate-y-1.5 hover:shadow-xl block"
    >
      <div className="h-[180px] overflow-hidden relative">
        <Image
          src={image}
          alt={alt}
          fill
          className="object-cover transition-transform duration-400 group-hover:scale-105"
          sizes="(max-width: 640px) 50vw, (max-width: 900px) 50vw, 25vw"
        />
      </div>
      <div className="p-4 pb-5">
        <h3 className="font-oswald font-semibold text-[17px] tracking-wide text-dark-grey mb-1.5">
          {name}
        </h3>
        <p className="text-[13.5px] text-gray-500 leading-relaxed mb-3.5">{description}</p>
        <span className="font-oswald font-medium text-[13px] tracking-wider uppercase text-red inline-flex items-center gap-1.5">
          Learn More &rarr;
        </span>
      </div>
    </Link>
  )
}
