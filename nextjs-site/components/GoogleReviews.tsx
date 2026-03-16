'use client'

import { useEffect, useState } from 'react'

interface Review {
  author_name: string
  profile_photo_url: string
  rating: number
  relative_time_description: string
  text: string
  author_url: string
}

interface ReviewsData {
  rating: number
  totalReviews: number
  reviews: Review[]
  googleMapsUrl: string
}

function getInitials(name: string): string {
  const parts = name.trim().split(' ')
  if (parts.length === 1) return parts[0][0].toUpperCase()
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase()
}

function StarRow({ rating }: { rating: number }) {
  return (
    <div className="flex gap-0.5">
      {[1, 2, 3, 4, 5].map((s) => (
        <svg
          key={s}
          className={`w-4 h-4 ${s <= rating ? 'text-yellow-400' : 'text-gray-200'}`}
          fill="currentColor"
          viewBox="0 0 20 20"
          aria-hidden="true"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
      ))}
    </div>
  )
}

function BigStarRow({ rating }: { rating: number }) {
  return (
    <div className="flex gap-1">
      {[1, 2, 3, 4, 5].map((s) => (
        <svg
          key={s}
          className={`w-7 h-7 ${s <= Math.round(rating) ? 'text-yellow-400' : 'text-gray-300'}`}
          fill="currentColor"
          viewBox="0 0 20 20"
          aria-hidden="true"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
      ))}
    </div>
  )
}

function ReviewSkeleton() {
  return (
    <div className="animate-pulse bg-white rounded-lg p-6 shadow-sm border border-gray-100 border-t-[3px] border-t-gray-200">
      <div className="flex items-center gap-3 mb-4">
        <div className="w-11 h-11 bg-gray-200 rounded-full flex-shrink-0" />
        <div className="flex-1 min-w-0">
          <div className="h-4 bg-gray-200 rounded w-28 mb-2" />
          <div className="h-3 bg-gray-200 rounded w-20" />
        </div>
      </div>
      <div className="h-3 bg-gray-200 rounded w-16 mb-3" />
      <div className="space-y-2 mt-3">
        <div className="h-3 bg-gray-200 rounded" />
        <div className="h-3 bg-gray-200 rounded" />
        <div className="h-3 bg-gray-200 rounded w-3/4" />
      </div>
    </div>
  )
}

export default function GoogleReviews({ bgClass = 'bg-white' }: { bgClass?: string }) {
  const [data, setData] = useState<ReviewsData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  useEffect(() => {
    fetch('/api/reviews')
      .then((r) => r.json())
      .then((json) => {
        if (json.error) throw new Error()
        setData(json)
      })
      .catch(() => setError(true))
      .finally(() => setLoading(false))
  }, [])

  return (
    <section className={`py-20 px-6 ${bgClass}`}>
      <div className="max-w-content mx-auto">

        {/* Section heading */}
        <div className="text-center mb-12">
          <p className="font-oswald font-medium text-xs tracking-[3px] uppercase text-red mb-2">Customer Reviews</p>
          <h2 className="font-oswald font-bold text-[clamp(26px,3.5vw,38px)] uppercase tracking-wide mb-3">
            What Our Customers Say
          </h2>
          <div className="w-14 h-1 bg-red rounded mx-auto" />
        </div>

        {/* Overall rating summary */}
        {data && (
          <div className="flex flex-col items-center mb-12">
            <div className="text-[56px] font-oswald font-bold text-dark-grey leading-none mb-2">
              {data.rating.toFixed(1)}
            </div>
            <BigStarRow rating={data.rating} />
            <p className="text-[13.5px] text-gray-500 mt-2">
              Based on {data.totalReviews.toLocaleString()} Google reviews
            </p>
          </div>
        )}

        {/* Loading skeletons */}
        {loading && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[...Array(3)].map((_, i) => <ReviewSkeleton key={i} />)}
          </div>
        )}

        {/* Error fallback */}
        {error && !loading && (
          <div className="text-center py-10">
            <p className="text-gray-500 text-[15px] mb-5">
              Couldn&apos;t load reviews right now &mdash; see what our customers are saying on Google.
            </p>
            <a
              href="https://www.google.com/maps/search/Regal+Plumbing+%26+Rooter+Ontario+CA"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 bg-red text-white font-oswald font-semibold text-sm uppercase tracking-wider px-6 py-2.5 rounded hover:bg-red-dark transition-colors"
            >
              View Reviews on Google &rarr;
            </a>
          </div>
        )}

        {/* Review cards */}
        {data && (
          <>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
              {data.reviews.map((review, i) => {
                const truncated = review.text.length > 200
                const displayText = truncated
                  ? review.text.slice(0, 200).trimEnd() + '\u2026'
                  : review.text

                return (
                  <div
                    key={i}
                    className="bg-white rounded-lg p-6 shadow-sm border border-gray-100 border-t-[3px] border-t-red flex flex-col"
                  >
                    {/* Reviewer info */}
                    <div className="flex items-center gap-3 mb-3">
                      {review.profile_photo_url ? (
                        // eslint-disable-next-line @next/next/no-img-element
                        <img
                          src={review.profile_photo_url}
                          alt={review.author_name}
                          width={44}
                          height={44}
                          className="w-11 h-11 rounded-full object-cover flex-shrink-0"
                        />
                      ) : (
                        <div className="w-11 h-11 rounded-full bg-navy text-white flex items-center justify-center font-oswald font-bold text-[15px] flex-shrink-0">
                          {getInitials(review.author_name)}
                        </div>
                      )}
                      <div className="min-w-0">
                        <div className="font-oswald font-semibold text-[15px] text-dark-grey truncate">
                          {review.author_name}
                        </div>
                        <div className="text-[12px] text-gray-400">
                          {review.relative_time_description}
                        </div>
                      </div>
                    </div>

                    {/* Stars */}
                    <StarRow rating={review.rating} />

                    {/* Review text */}
                    <p className="text-[13.5px] text-gray-600 leading-relaxed mt-3 flex-1">
                      {displayText}
                      {truncated && (
                        <a
                          href={review.author_url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-red font-medium ml-1 hover:underline"
                        >
                          Read more
                        </a>
                      )}
                    </p>
                  </div>
                )
              })}
            </div>

            {/* CTA */}
            <div className="text-center">
              <a
                href={data.googleMapsUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 bg-transparent text-red border-2 border-red font-oswald font-semibold text-sm uppercase tracking-wider px-7 py-2.5 rounded hover:bg-red hover:text-white transition-all"
              >
                Read All Reviews on Google &rarr;
              </a>
            </div>
          </>
        )}

      </div>
    </section>
  )
}
