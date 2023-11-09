<script lang="ts">
	import IconFile from '~icons/solar/file-text-outline';
	import IconNewFile from '~icons/solar/pen-new-square-outline';
	import IconWord from '~icons/solar/chat-square-outline';
	import IconPage from '~icons/solar/documents-outline';

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
			<IconFile style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Created projects</div>
		<div class="stat-value">{formatNumber(20 ?? 0)}</div>
	</div>
	<div class="stat">
		<div class="stat-figure text-secondary">
			<IconNewFile style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Created files</div>
		<div class="stat-value">{formatNumber(25 ?? 0)}</div>
	</div>
	<div class="stat">
		<div class="stat-figure text-secondary">
			<IconPage style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Total assets</div>
		<div class="stat-value">{formatNumber(30 ?? 0)}</div>
	</div>
	<div class="stat">
		<div class="stat-figure text-secondary">
			<IconWord style="font-size: x-large;" class="text-primary" />
		</div>
		<div class="stat-title">Total lines of code</div>
		<div class="stat-value">{formatNumber(35 ?? 0)}</div>
	</div>
</div>
