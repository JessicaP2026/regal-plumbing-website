import { NextResponse } from 'next/server'

export async function GET() {
  const apiKey = process.env.GOOGLE_PLACES_API_KEY
  const placeId = process.env.NEXT_PUBLIC_GOOGLE_PLACE_ID

  if (!apiKey || !placeId) {
    return NextResponse.json({ error: 'Missing configuration' }, { status: 500 })
  }

  try {
    const url = `https://maps.googleapis.com/maps/api/place/details/json?place_id=${placeId}&fields=name,rating,user_ratings_total,reviews&key=${apiKey}`

    const res = await fetch(url, { next: { revalidate: 3600 } })
    if (!res.ok) throw new Error('Network error')

    const data = await res.json()

    if (data.status !== 'OK') {
      return NextResponse.json({ error: data.status, message: data.error_message, fullResponse: data }, { status: 502 })
    }

    const { rating, user_ratings_total, reviews = [] } = data.result

    const filtered = (reviews as Array<{ rating: number; time: number }>)
      .filter((r) => r.rating >= 4)
      .sort((a, b) => b.time - a.time)
      .slice(0, 5)

    return NextResponse.json({
      rating,
      totalReviews: user_ratings_total,
      reviews: filtered,
      googleMapsUrl: `https://www.google.com/maps/place/?q=place_id:${placeId}`,
    })
  } catch (error) {
    return NextResponse.json({ error: 'Failed to fetch reviews', details: String(error) }, { status: 500 })
  }
}
