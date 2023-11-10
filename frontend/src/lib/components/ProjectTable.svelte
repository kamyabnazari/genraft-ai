<script lang="ts">
	// Icons imports
	import IconDownload from '~icons/solar/download-square-outline';
	import IconBin from '~icons/solar/trash-bin-trash-outline';
	import IconHistory from '~icons/solar/history-2-outline';

	interface Project {
		id: string;
		name: string;
		type: string;
		created: string;
	}

	let projectList: Project[] = [
		{ id: '1', name: 'Project Alpha', type: 'Type 1', created: '2023-01-01T12:00:00' },
		{ id: '2', name: 'Project Beta', type: 'Type 2', created: '2023-01-02T13:00:00' }
	];

	async function deleteProject(projectID: string) {
		console.log('Delete Project!');
	}

	async function downloadProject(projectID: string) {
		console.log('Download Project!');
	}
</script>

<div class="bg-base-200 w-full overflow-x-auto rounded-lg shadow-lg">
	<table class="table w-full">
		<!-- Table Head -->
		<thead>
			<tr>
				<th class="w-0/12" />
				<th class="w-3/12">Name</th>
				<th class="w-2/12">Type</th>
				<th class="w-3/12">Create Date</th>
				<th class="w-1/12">Actions</th>
			</tr>
		</thead>
		<!-- Table Body -->
		<tbody class="bg-base-100">
			{#if projectList.length === 0}
				<tr>
					<td colspan="5" class="text-center">No projects found! Create a new project.</td>
				</tr>
			{/if}
			{#each projectList as project, index}
				<tr class="hover">
					<td>
						<div class="text-md">
							{index + 1}
						</div>
					</td>
					<td>
						<div class="flex items-center space-x-3">
							<div class="text-md font-bold">{project.name}</div>
						</div>
					</td>
					<td>
						<span class="badge badge-ghost badge-sm">{project.type}</span>
					</td>
					<td>{project.created.slice(0, 19)}</td>
					<th>
						<div class="flex flex-row gap-4">
							<a href={`/dashboard/project-history/${project.id}`}>
								<button class="btn btn-square btn-primary">
									<IconHistory style="font-size: x-large;" />
								</button>
							</a>
							<button class="btn btn-square btn-info" on:click={() => downloadProject(project.id)}>
								<IconDownload style="font-size: x-large;" />
							</button>
							<button class="btn btn-square btn-error" on:click={() => deleteProject(project.id)}>
								<IconBin style="font-size: x-large;" />
							</button>
						</div>
					</th>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
