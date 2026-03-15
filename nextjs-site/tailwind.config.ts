import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        red: {
          DEFAULT: '#B91C1C',
          dark: '#991B1B',
          light: '#fca5a5',
        },
        navy: '#1E3A6E',
        'dark-grey': '#2D2D2D',
        'light-grey': '#F3F4F6',
      },
      fontFamily: {
        oswald: ['var(--font-oswald)', 'sans-serif'],
        sans: ['var(--font-open-sans)', 'sans-serif'],
      },
      maxWidth: {
        content: '1200px',
      },
    },
  },
  plugins: [],
}

export default config
