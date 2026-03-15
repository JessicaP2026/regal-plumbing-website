import { BUSINESS } from '@/lib/constants'

export default function EmergencyBar() {
  return (
    <div className="bg-dark-grey text-white text-center py-2.5 px-4 text-[13.5px] font-semibold tracking-wide">
      24/7 Emergency Service Available &mdash; Call{' '}
      <a
        href={`tel:${BUSINESS.phoneTel}`}
        className="text-red-light underline underline-offset-2 hover:text-white transition-colors"
      >
        {BUSINESS.phone}
      </a>
    </div>
  )
}
