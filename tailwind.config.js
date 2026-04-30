/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        cyber: {
          dark: '#020617',
          card: '#0f172a',
          border: '#1e293b',
          accent: '#0ea5e9',
          danger: '#ef4444',
          warning: '#f59e0b',
          success: '#10b981'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
