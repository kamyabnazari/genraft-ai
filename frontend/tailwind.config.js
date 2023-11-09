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
				lofi: {
					...require('daisyui/src/theming/themes')['[data-theme=lofi]'],
					'--rounded-box': '0.25rem',
					'--rounded-btn': '0.25rem',
					'--rounded-badge': '0.15rem',
					'--animation-btn': '0.25s',
					'--animation-input': '0.25s',
					'--btn-text-case': 'uppercase',
					'--btn-focus-scale': '0.95',
					'--border-btn': '1px',
					'--tab-border': '1px',
					'--tab-radius': '0.5rem'
				},
				business: {
					...require('daisyui/src/theming/themes')['[data-theme=business]'],
					'--rounded-box': '0.25rem',
					'--rounded-btn': '0.25rem',
					'--rounded-badge': '0.15rem',
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
		darkTheme: 'business'
	}
};
