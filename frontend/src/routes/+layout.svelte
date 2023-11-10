<script lang="ts">
	// Essential imports
	import '../app.css';
	import Navbar from '$lib/components/MainNavbar.svelte';
	import Footer from '$lib/components/MainFooter.svelte';
	import { page } from '$app/stores';
</script>

<div class="drawer xl:drawer-open">
	<input id="application-drawer" type="checkbox" class="drawer-toggle" />
	<div class="drawer-content flex min-h-screen flex-col overflow-x-auto">
		<div class="flex-none">
			<Navbar />
		</div>
		<div class="flex-grow p-8 py-16">
			<slot />
		</div>
		<div class="flex-none">
			<Footer />
		</div>
	</div>
	<div class="drawer-side z-50">
		<label for="application-drawer" class="drawer-overlay" />
		<ul class="menu bg-base-200 text-base-content h-full w-80 gap-2 p-4">
			<li>
				<a href="/dashboard" class:active={$page.url.pathname === '/dashboard'}> Dashboard </a>
			</li>
			<li>
				<a href="/documentation" class:active={$page.url.pathname === '/documentation'}>
					Documentation
				</a>
			</li>
			<li><a href="/about-us" class:active={$page.url.pathname === '/about-us'}> About us </a></li>
		</ul>
	</div>
</div>
