interface ReviewCardProps {
  name: string
  city: string
  rating: number
  text: string
}

export default function ReviewCard({ name, city, rating, text }: ReviewCardProps) {
  return (
    <div className="bg-white border border-gray-200 rounded-lg p-7 shadow-sm">
      <div className="flex gap-0.5 mb-3">
        {Array.from({ length: rating }).map((_, i) => (
          <span key={i} className="text-yellow-400 text-lg">&#9733;</span>
        ))}
      </div>
      <p className="text-[14.5px] text-gray-600 leading-relaxed mb-4 italic">&ldquo;{text}&rdquo;</p>
      <div className="font-oswald font-semibold text-[15px] text-dark-grey">{name}</div>
      <div className="text-[12.5px] text-gray-500">{city}</div>
    </div>
  )
}
