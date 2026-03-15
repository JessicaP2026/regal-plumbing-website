'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { BUSINESS, ALL_CITIES, SERVICES } from '@/lib/constants'

interface FormData {
  fullName: string
  phone: string
  email: string
  city: string
  service: string
  message: string
  honeypot: string
}

export default function ContactForm() {
  const [status, setStatus] = useState<'idle' | 'submitting' | 'success' | 'error'>('idle')
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<FormData>()

  const onSubmit = async (data: FormData) => {
    if (data.honeypot) return
    setStatus('submitting')
    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
      if (res.ok) {
        setStatus('success')
        reset()
        window.location.href = '/thank-you'
      } else {
        setStatus('error')
      }
    } catch {
      setStatus('error')
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-4.5">
      {/* Honeypot */}
      <input type="text" {...register('honeypot')} className="hidden" tabIndex={-1} autoComplete="off" />

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4.5">
        <div className="flex flex-col gap-1.5">
          <label htmlFor="fullName" className="font-oswald font-medium text-[13px] tracking-widest uppercase text-dark-grey">
            Full Name *
          </label>
          <input
            id="fullName"
            type="text"
            placeholder="John Smith"
            {...register('fullName', { required: 'Name is required' })}
            className="w-full px-3.5 py-3 border-[1.5px] border-gray-300 rounded text-sm text-dark-grey bg-white focus:border-red focus:ring-2 focus:ring-red/10 outline-none transition-all"
          />
          {errors.fullName && <span className="text-red text-xs">{errors.fullName.message}</span>}
        </div>
        <div className="flex flex-col gap-1.5">
          <label htmlFor="phone" className="font-oswald font-medium text-[13px] tracking-widest uppercase text-dark-grey">
            Phone Number *
          </label>
          <input
            id="phone"
            type="tel"
            placeholder="(909) 000-0000"
            {...register('phone', { required: 'Phone is required' })}
            className="w-full px-3.5 py-3 border-[1.5px] border-gray-300 rounded text-sm text-dark-grey bg-white focus:border-red focus:ring-2 focus:ring-red/10 outline-none transition-all"
          />
          {errors.phone && <span className="text-red text-xs">{errors.phone.message}</span>}
        </div>
      </div>

      <div className="flex flex-col gap-1.5">
        <label htmlFor="email" className="font-oswald font-medium text-[13px] tracking-widest uppercase text-dark-grey">
          Email Address
        </label>
        <input
          id="email"
          type="email"
          placeholder="john@example.com"
          {...register('email')}
          className="w-full px-3.5 py-3 border-[1.5px] border-gray-300 rounded text-sm text-dark-grey bg-white focus:border-red focus:ring-2 focus:ring-red/10 outline-none transition-all"
        />
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4.5">
        <div className="flex flex-col gap-1.5">
          <label htmlFor="city" className="font-oswald font-medium text-[13px] tracking-widest uppercase text-dark-grey">
            City *
          </label>
          <select
            id="city"
            {...register('city', { required: 'City is required' })}
            className="w-full px-3.5 py-3 border-[1.5px] border-gray-300 rounded text-sm text-dark-grey bg-white focus:border-red focus:ring-2 focus:ring-red/10 outline-none transition-all appearance-none cursor-pointer"
          >
            <option value="">Select your city...</option>
            {ALL_CITIES.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
          {errors.city && <span className="text-red text-xs">{errors.city.message}</span>}
        </div>
        <div className="flex flex-col gap-1.5">
          <label htmlFor="service" className="font-oswald font-medium text-[13px] tracking-widest uppercase text-dark-grey">
            Service Needed *
          </label>
          <select
            id="service"
            {...register('service', { required: 'Service is required' })}
            className="w-full px-3.5 py-3 border-[1.5px] border-gray-300 rounded text-sm text-dark-grey bg-white focus:border-red focus:ring-2 focus:ring-red/10 outline-none transition-all appearance-none cursor-pointer"
          >
            <option value="">Select a service...</option>
            {SERVICES.map((s) => (
              <option key={s.slug} value={s.slug}>{s.name}</option>
            ))}
            <option value="other">Other / Not Sure</option>
          </select>
          {errors.service && <span className="text-red text-xs">{errors.service.message}</span>}
        </div>
      </div>

      <div className="flex flex-col gap-1.5">
        <label htmlFor="message" className="font-oswald font-medium text-[13px] tracking-widest uppercase text-dark-grey">
          Describe Your Issue
        </label>
        <textarea
          id="message"
          rows={5}
          placeholder="Tell us a bit about what's going on \u2014 the more detail, the better we can prepare..."
          {...register('message')}
          className="w-full px-3.5 py-3 border-[1.5px] border-gray-300 rounded text-sm text-dark-grey bg-white focus:border-red focus:ring-2 focus:ring-red/10 outline-none transition-all resize-y min-h-[120px]"
        />
      </div>

      <div className="mt-1.5">
        <button
          type="submit"
          disabled={status === 'submitting'}
          className="w-full bg-red text-white font-oswald font-semibold text-base uppercase tracking-wider py-3.5 rounded hover:bg-red-dark hover:-translate-y-0.5 transition-all disabled:opacity-60 disabled:cursor-not-allowed"
        >
          {status === 'submitting' ? 'Sending...' : 'Send Message \u2192'}
        </button>
      </div>

      {status === 'error' && (
        <p className="text-red text-sm text-center">Something went wrong. Please call us at {BUSINESS.phone}.</p>
      )}

      <p className="text-[12px] text-gray-400 text-center mt-2">
        Your information is private and will never be shared. We respond within 1 business hour during operating hours.
      </p>
    </form>
  )
}
