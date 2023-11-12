<script lang="ts">
	// Icons imports
	import IconProject from '~icons/solar/clapperboard-text-outline';
	import IconFile from '~icons/solar/file-text-outline';
	import IconAsset from '~icons/solar/file-smile-outline';

	// Essential imports
	import { onMount } from 'svelte';
	import type { ProjectStats } from '$lib/models';

	let loading: boolean;
	let result: ProjectStats = {
		total_projects: 0,
		total_files: 0,
		total_assets: 0
	};

	onMount(async () => {
		await getProjectsStatistics();
	});

	async function getProjectsStatistics() {
		loading = true;

		try {
			const response = await fetch(`/api/stats/projects`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			result = await response.json();
		} catch (error) {
			console.error('Error fetching projects:', error);
		} finally {
			loading = false;
		}
	}

	function formatNumber(num: number) {
		if (num >= 1000000) {
			return (num / 1000000).toFixed(1).replace(/\.0$/, '') + 'M';
		}
		if (num >= 1000) {
			return (num / 1000).toFixed(1).replace(/\.0$/, '') + 'K';
		}
		return num;
	}
</script>

<div class="stats bg-base-200 flex-auto flex-nowrap shadow-lg">
	<div class="stat">
		<div class="stat-figure text-secondary">
			<IconProject style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Created projects</div>
		<div class="stat-value">{formatNumber(result.total_projects ?? 0)}</div>
	</div>
	<div class="stat">
		<div class="stat-figure text-secondary">
			<IconFile style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Created files</div>
		<div class="stat-value">{formatNumber(result.total_files ?? 0)}</div>
	</div>
	<div class="stat">
		<div class="stat-figure text-secondary">
			<IconAsset style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Created assets</div>
		<div class="stat-value">{formatNumber(result.total_assets ?? 0)}</div>
	</div>
</div>
