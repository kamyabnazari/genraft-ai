<script lang="ts">
	import ActionCards from '$lib/components/ActionCards.svelte';
	import ProjectTable from '$lib/components/ProjectTable.svelte';
	import StatsBar from '$lib/components/StatsBar.svelte';
</script>

<div class="mx-auto flex min-h-full max-w-7xl flex-col gap-8">
	<div class="flex flex-col gap-8">
		<div class="flex justify-center">
			<h1 class="text-2xl font-bold md:text-3xl">Dashboard</h1>
		</div>
		<div class="flex">
			<StatsBar />
		</div>
		<div class="flex">
			<ActionCards />
		</div>
		<div class="flex">
			<ProjectTable />
		</div>
	</div>
</div>
