<script lang="ts">
	// Icons imports
	import IconCreate from '~icons/solar/clipboard-add-outline';
</script>

<div class="flex w-full flex-col gap-8 md:flex-row">
	<div class="card bg-base-200 flex-1 shadow-lg">
		<div class="card-body">
			<h2 class="card-title">Create a new project</h2>
			<p>Gather your ideas and create software!</p>
			<div class="card-actions justify-end py-4">
				<a href="/dashboard/project-create">
					<button class="btn btn-primary gap-4">
						<IconCreate style="font-size: x-large" class="text-primary-content" />
						<span class="hidden sm:inline">Create</span>
					</button>
				</a>
			</div>
		</div>
	</div>
</div>
