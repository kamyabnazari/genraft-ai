/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {}
	},
	plugins: [require('@tailwindcss/typography'), require('daisyui')],
	daisyui: {
		themes: [
			{
				light: {
					...require('daisyui/src/theming/themes')['[data-theme=light]'],
					'--rounded-box': '0.30rem',
					'--rounded-btn': '0.30rem',
					'--rounded-badge': '0.20rem',
					'--animation-btn': '0.25s',
					'--animation-input': '0.25s',
					'--btn-text-case': 'uppercase',
					'--btn-focus-scale': '0.95',
					'--border-btn': '1px',
					'--tab-border': '1px',
					'--tab-radius': '0.5rem'
				},
				dark: {
					...require('daisyui/src/theming/themes')['[data-theme=dark]'],
					'--rounded-box': '0.30rem',
					'--rounded-btn': '0.30rem',
					'--rounded-badge': '0.20rem',
					'--animation-btn': '0.25s',
					'--animation-input': '0.25s',
					'--btn-text-case': 'uppercase',
					'--btn-focus-scale': '0.95',
					'--border-btn': '1px',
					'--tab-border': '1px',
					'--tab-radius': '0.5rem'
				}
			}
		],
		styled: true,
		base: true,
		utils: true,
		logs: false,
		rtl: false,
		prefix: '',
		darkTheme: 'dark'
	}
};
