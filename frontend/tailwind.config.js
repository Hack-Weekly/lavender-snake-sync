/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}", "./src/**/*.{html,js,jsx}"],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["Roboto", "sans"],
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
