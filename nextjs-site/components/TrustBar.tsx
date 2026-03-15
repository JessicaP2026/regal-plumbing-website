import { TRUST_ITEMS } from '@/lib/constants'

export default function TrustBar() {
  return (
    <div className="bg-light-grey py-7 px-6 border-b border-gray-200">
      <div className="max-w-content mx-auto flex flex-wrap justify-center">
        {TRUST_ITEMS.map((item, i) => (
          <div
            key={i}
            className="flex items-center gap-3 px-7 py-3 border-r border-gray-300 last:border-r-0 flex-1 min-w-[180px] justify-center max-md:border-r-0 max-md:border-b max-md:border-gray-300 max-md:last:border-b-0"
          >
            <span className="text-2xl flex-shrink-0">{item.icon}</span>
            <div className="font-oswald font-medium text-sm tracking-wide text-dark-grey leading-tight">
              {item.label}
              <span className="block font-sans font-normal text-[11.5px] text-gray-500 tracking-normal">
                {item.sub}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
