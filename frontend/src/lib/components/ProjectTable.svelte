<script lang="ts">
	// Icons imports
	import IconDownload from '~icons/solar/download-square-outline';
	import IconBin from '~icons/solar/trash-bin-trash-outline';
	import IconHistory from '~icons/solar/history-2-outline';

	// Essential imports
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import type { Project } from '$lib/models';

	let loading: boolean;

	let projectList: Project[] = [];

	onMount(async () => {
		await getProjects();
	});

	async function getProjects() {
		loading = true;
		projectList = [];

		try {
			const response = await fetch(`/api/projects`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			const results: Project[] = await response.json();
			projectList = results.map((element) => ({
				id: element.id,
				name: element.name,
				idea_initial: element.idea_initial,
				idea_final: element.idea_final,
				folder_path: element.folder_path,
				created_at: element.created_at
			}));
		} catch (error) {
			console.error('Error fetching projects:', error);
		} finally {
			loading = false;
		}
	}

	async function openProject(id: string) {
		goto(`/dashboard/project-create/${id}`);
	}

	async function deleteProject(id: string) {
		try {
			const response = await fetch(`/api/project/${id}`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			projectList = projectList.filter((project) => project.id !== id);
		} catch (error) {
			console.error('Error fetching projects:', error);
		} finally {
			loading = false;
		}
	}

	async function downloadProject(id: string) {
		try {
			const response = await fetch(`/api/project/${id}/download`, {
				method: 'GET'
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			// Handle the download
			const blob = await response.blob();
			const downloadUrl = window.URL.createObjectURL(blob);

			// Extract filename from Content-Disposition header or use a default
			const contentDisposition = response.headers.get('Content-Disposition');
			const filenameMatch = contentDisposition?.match(/filename="?(.+)"/);
			const filename = filenameMatch ? filenameMatch[1] : `project_${id}.zip`;

			// Create an anchor element and download the file
			const a = document.createElement('a');
			a.href = downloadUrl;
			a.download = filename;
			document.body.appendChild(a);
			a.click();

			// Cleanup
			window.URL.revokeObjectURL(downloadUrl);
			a.remove();
		} catch (error) {
			console.error('Error downloading project:', error);
		} finally {
			loading = false;
		}
	}
</script>

<div class="bg-base-200 w-full overflow-x-auto rounded-lg shadow-lg">
	<table class="table w-full">
		<!-- Table Head -->
		<thead>
			<tr>
				<th class="w-0/12" />
				<th class="w-3/12">Name</th>
				<th class="w-4/12">Idea</th>
				<th class="w-3/12">Creation Date</th>
				<th class="w-2/12">Actions</th>
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
						{project.idea_initial.length > 40
							? `${project.idea_initial.slice(0, 40)}...`
							: project.idea_initial}
					</td>
					<td>{project.created_at.split('.')[0].replace('T', ' at ')}</td>
					<th>
						<div class="flex flex-row gap-4">
							<button class="btn btn-square btn-primary" on:click={() => openProject(project.id)}>
								<IconHistory style="font-size: x-large;" />
							</button>
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
