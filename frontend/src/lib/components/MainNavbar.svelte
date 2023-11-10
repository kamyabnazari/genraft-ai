<script lang="ts">
	import IconMenu from '~icons/solar/hamburger-menu-outline';
	import IconMoon from '~icons/solar/moon-outline';
	import IconSun from '~icons/solar/sun-2-outline';
	import { onMount, onDestroy } from 'svelte';
	import { writable } from 'svelte/store';

	const theme = writable('light');

	const toggleTheme = () => {
		theme.update((currentTheme) => {
			const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
			document.documentElement.setAttribute('data-theme', newTheme);
			localStorage.setItem('theme', newTheme);
			return newTheme;
		});
	};

	onMount(() => {
		const savedTheme = localStorage.getItem('theme');
		if (savedTheme) {
			theme.set(savedTheme);
		} else {
			// Use browser's preference if no saved theme
			const prefersDark =
				window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
			const defaultTheme = prefersDark ? 'dark' : 'light';
			theme.set(defaultTheme);
		}
		document.documentElement.setAttribute('data-theme', $theme);
	});

	onDestroy(() => {
		theme.set('dark'); // Reset the theme to default on component destruction
	});

	$: isChecked = $theme === 'dark'; // Computed property for checkbox state

	function handleCheckboxChange() {
		isChecked;
		toggleTheme();
	}
</script>

<div class="navbar text-base-content bg-base-200 sticky left-0 top-0 z-10 px-6 py-4 shadow-sm">
	<div class="me-4 flex-none">
		<label for="application-drawer" class="btn btn-square btn-ghost drawer-button xl:hidden">
			<IconMenu style="font-size: x-large" class="text-primary" />
		</label>
	</div>
	<div class="flex-1">
		<a class="btn-link hidden text-left text-xl font-bold normal-case md:block" href="/"
			>Genraft AI</a
		>
		<a class="btn-link md:hidden" href="/">
			<img class="h-10 rounded-lg" src="/favicon.png" alt="user avatar" />
		</a>
	</div>
	<label class="swap swap-rotate px-4">
		<input type="checkbox" bind:checked={isChecked} on:change={handleCheckboxChange} />
		<IconSun class="swap-off text-primary fill-current" style="font-size: x-large" />
		<IconMoon class="swap-on text-warning fill-current" style="font-size: x-large" />
	</label>
</div>
