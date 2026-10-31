/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        aicte: {
          navy: '#002147',
          navylight: '#0d325e',
          saffron: '#FF9933',
          green: '#138808',
        }
      }
    },
  },
  plugins: [],
}
