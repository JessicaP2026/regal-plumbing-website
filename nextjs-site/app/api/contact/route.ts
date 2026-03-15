import { NextResponse } from 'next/server'

export async function POST(request: Request) {
  try {
    const data = await request.json()

    // Honeypot check
    if (data.honeypot) {
      return NextResponse.json({ success: true })
    }

    const { fullName, phone, email, city, service, message } = data

    if (!fullName || !phone || !city || !service) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 })
    }

    // If RESEND_API_KEY is configured, send email
    if (process.env.RESEND_API_KEY && process.env.RESEND_API_KEY !== 'your_resend_api_key_here') {
      const { Resend } = await import('resend')
      const resend = new Resend(process.env.RESEND_API_KEY)

      // Business notification
      await resend.emails.send({
        from: 'Regal Website <onboarding@resend.dev>',
        to: ['info@regalplumbingservices.com'],
        subject: `New Lead: ${fullName} — ${service}`,
        html: `
          <h2>New Contact Form Submission</h2>
          <p><strong>Name:</strong> ${fullName}</p>
          <p><strong>Phone:</strong> ${phone}</p>
          <p><strong>Email:</strong> ${email || 'Not provided'}</p>
          <p><strong>City:</strong> ${city}</p>
          <p><strong>Service:</strong> ${service}</p>
          <p><strong>Message:</strong> ${message || 'No message'}</p>
        `,
      })

      // Auto-reply if email provided
      if (email) {
        await resend.emails.send({
          from: 'Regal Plumbing & Rooter <onboarding@resend.dev>',
          to: [email],
          subject: 'Thank You — Regal Plumbing & Rooter',
          html: `
            <h2>Thanks for reaching out, ${fullName}!</h2>
            <p>We received your message and will get back to you shortly.</p>
            <p>For immediate assistance, call us at <strong>(909) 600-4561</strong> — we answer 24/7.</p>
            <p>Best regards,<br>The Regal Plumbing & Rooter Team</p>
          `,
        })
      }
    }

    return NextResponse.json({ success: true })
  } catch (error) {
    console.error('Contact form error:', error)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}
