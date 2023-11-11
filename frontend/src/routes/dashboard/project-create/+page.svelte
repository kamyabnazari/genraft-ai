<script lang="ts">
	// Icons imports
	import IconClose from '~icons/solar/alt-arrow-left-bold';

	// Essential imports
	import { goto } from '$app/navigation';

	let loading: boolean;
	let name: string = '';
	let idea: string = '';

	// Function to handle the form submission
	async function handleSubmit() {
		loading = true;

		const payload = {
			name: name,
			idea: idea
		};

		try {
			const response = await fetch('/api/project/step-idea-submit', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(payload)
			});

			const result = await response.json();

			if (result.id) {
				// Redirect to the project-create page with the new project's ID
				goto(`/dashboard/project-create/${result.id}`);
			} else {
				throw new Error('No project ID returned from server.');
			}
		} catch (error) {
			console.error('Submission failed:', error);
		} finally {
			loading = false;
		}
	}
</script>

<div class="mx-auto flex min-h-full max-w-7xl flex-col gap-8">
	<div class="flex items-start">
		<button
			class="btn btn-link text-primary"
			on:click={() => goto('/dashboard')}
			style="max-width: 150px;"
		>
			<IconClose style="font-size: x-large;" /> close
		</button>
	</div>
	<div class="self-center">
		<h1 class="mb-8 text-2xl font-bold md:text-3xl">Create a new project!</h1>
	</div>
	<div class="flex flex-col justify-center gap-8 lg:flex-row">
		<div
			class="bg-base-200 mx-auto flex max-w-md flex-1 flex-col justify-between gap-8 rounded-lg p-8 shadow-lg"
		>
			<div class="flex flex-row justify-center">
				<h1 class="text-l mb-8 font-bold md:text-xl">Your new idea?</h1>
			</div>
			<div class="flex w-full flex-row justify-center">
				<div class="flex w-full justify-center">
					<div class="form-control w-full">
						<label for="idea" class="label">
							<span class="label-text">What is your project's name?</span>
						</label>
						<input
							class="input input-bordered w-full rounded-md border-2"
							placeholder="Project name..."
							type="text"
							id="name"
							name="name"
							disabled={loading}
							bind:value={name}
						/>
					</div>
				</div>
			</div>
			<div class="flex w-full flex-row justify-center">
				<div class="flex w-full justify-center">
					<div class="form-control w-full">
						<label for="idea" class="label">
							<span class="label-text">What project do you want to generate?</span>
						</label>
						<textarea
							class="textarea textarea-bordered h-56 w-full rounded-md border-2"
							placeholder="I want a personal portfolio website..."
							id="idea"
							name="idea"
							disabled={loading}
							bind:value={idea}
						/>
					</div>
				</div>
			</div>
			<div class="mt-8 flex flex-row justify-center">
				<div class="flex-auto">
					<button class="btn btn-ghost" on:click={() => goto('/dashboard')} disabled={loading}>
						Cancel
					</button>
				</div>
				<button
					class="btn btn-primary"
					type="button"
					on:click={handleSubmit}
					disabled={loading || idea === '' || name === ''}
				>
					{#if loading}
						<span class="loading loading-spinner"></span>
					{/if}
					Start
				</button>
			</div>
		</div>
	</div>
</div>
