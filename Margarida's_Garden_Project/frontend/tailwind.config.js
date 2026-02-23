/** Margarida's Garden - Tailwind config (cores do design system) */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        sky: { blue: '#F0F9FC', light: '#E0F2F7' },
        grass: { green: '#5FDD4D', dark: '#4BA639' },
        flower: {
          pink: '#ff54a9',
          yellow: '#FFD700',
          purple: '#9966CC',
          rose: '#fd0389',
          peach: '#fd6b36',
          lavender: '#875dd4',
        },
        text: { dark: '#4a4a4a' },
      },
      fontFamily: {
        sans: ['Segoe UI', 'Georgia', 'serif'],
      },
    },
  },
  plugins: [],
}
