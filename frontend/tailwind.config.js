/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {}
	},
	plugins: [require('@tailwindcss/typography'), require('daisyui')],
	daisyui: {
		themes: false,
		styled: true,
		base: true,
		utils: true,
		logs: false,
		prefix: '',
		darkTheme: 'dark',
		themeRoot: ":root"
	}
};
