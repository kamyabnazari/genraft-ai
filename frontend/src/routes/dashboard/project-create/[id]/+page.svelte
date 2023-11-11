<script lang="ts">
	// Icons imports
	import IconClose from '~icons/solar/alt-arrow-left-bold';
	import IconArrow from '~icons/solar/alt-arrow-right-bold';
	import IconSend from '~icons/solar/square-arrow-up-bold';

	// Essential imports
	import { writable } from 'svelte/store';
	import { goto } from '$app/navigation';
	import { onMount, tick } from 'svelte';
	import { page } from '$app/stores';

	const phases = [
		{ key: 'preparation', name: 'Preparation' },
		{ key: 'ideaCreation', name: 'Idea Creation' },
		{ key: 'companyCreation', name: 'Company Creation' },
		{ key: 'designing', name: 'Designing' },
		{ key: 'coding', name: 'Coding' },
		{ key: 'testing', name: 'Testing' },
		{ key: 'documenting', name: 'Documenting' },
		{ key: 'done', name: 'Done' }
	];
	const currentPhaseIndex = writable(0);

	let idea: string = '';
	let loading: boolean;
	let chatContainer: HTMLDivElement;
	let messagingNeeded: boolean = false;

	let messages = writable([]);
	let messagesArray = [];
	let messagesArrayString: string;
	let message: string;

	// Reactive declaration for projectId
	let projectId: string = '';
	$: projectId = $page.params.id;

	onMount(async () => {
		if (projectId) {
			await getProjectIdeaById();
		}
	});

	async function scrollToBottom() {
		await tick();
		if (chatContainer) {
			chatContainer.scrollTop = chatContainer.scrollHeight;
		}
	}

	messages.subscribe((value) => {
		messagesArray = value;
		messagesArrayString = JSON.stringify(value);
	});

	async function getProjectIdeaById() {
		loading = true;

		try {
			const response = await fetch(`/api/project/${projectId}/idea`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			const result = await response.json();
			idea = result.idea;
		} catch (error) {
			console.error('Error fetching project idea:', error);
		} finally {
			loading = false;
		}
	}

	async function handleNext() {
		currentPhaseIndex.update((n) => n + 1);
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
		<h1 class="mb-8 text-2xl font-bold md:text-3xl">Project Creation Assistant</h1>
	</div>
	<div class="flex flex-col justify-center gap-8 lg:flex-row">
		<div class="flex flex-row justify-center">
			<div class="overflow-x-auto">
				<ul class="steps steps-horizontal lg:steps-vertical">
					{#each phases as phase, index (phase.key)}
						<li class={index <= $currentPhaseIndex ? 'step step-primary' : 'step'}>
							{phase.name}
						</li>
					{/each}
				</ul>
			</div>
		</div>
		<div class="divider divider-vertical lg:divider-horizontal">
			<IconArrow style="font-size: xx-large;" />
		</div>
		<div class="bg-base-200 flex flex-1 flex-col justify-between rounded-lg p-8 shadow-lg">
			<!-- Content based on phase -->
			{#if $currentPhaseIndex === 0}
				<!-- Content for Idea creation phase -->
				<div class="flex flex-row justify-center">
					<h1 class="text-l mb-8 font-bold md:text-xl">Idea Creation Phase</h1>
				</div>
				<div class="flex flex-row justify-center">
					<h1 class="mb-8 text-base">Initial Idea: {idea}</h1>
				</div>
				<div class="mt-8 flex flex-row justify-center">
					<div class="flex-auto">
						<button class="btn btn-ghost" on:click={() => goto('/dashboard')} disabled={loading}>
							Cancel
						</button>
					</div>
					<button class="btn btn-primary" type="button" on:click={handleNext} disabled={loading}>
						Next
					</button>
				</div>
			{:else if $currentPhaseIndex === 1}
				<!-- Content for Idea Creation phase -->
				<div class="flex flex-row justify-center">
					<h1 class="text-l font-bold md:text-xl">Preparation Phase</h1>
				</div>
				<div class="mt-4 flex flex-row justify-center">
					<div class="flex-auto">
						<button class="btn btn-ghost" on:click={() => goto('/dashboard')} disabled={loading}>
							Cancel
						</button>
					</div>
					<button class="btn btn-primary" type="button" on:click={handleNext} disabled={loading}>
						Next
					</button>
				</div>
			{/if}
		</div>
		<div class="divider divider-vertical lg:divider-horizontal">
			<IconArrow style="font-size: xx-large;" />
		</div>
		<div class="bg-base-200 flex-1 rounded-md p-8 shadow-lg">
			<div class="flex h-full flex-col justify-between gap-8">
				<div
					class="form-control chat-container bg-base-100 border-rounded border-base-300 flex-grow overflow-y-auto rounded-lg border-2 p-2"
					bind:this={chatContainer}
				>
					{#each $messages as message (message)}
						<div class={0 === 0 ? 'chat chat-end my-4' : 'chat chat-start my-4'}>
							<div class="chat-image avatar">
								<div class="w-10 rounded-lg shadow-sm">
									{#if 0 === 0}
										<img
											src={true
												? `https://ui-avatars.com/api/?name=user`
												: `https://ui-avatars.com/api/?name=computer`}
											alt="user avatar"
											id="avatar-preview-navbar"
										/>
									{:else}
										<img src="/favicon.png" alt="ee avatar" />
									{/if}
								</div>
							</div>
							<div class="chat-header">
								{0 === 0 ? 'user' : 'computer'}
							</div>
							<div
								class={0 === 0
									? 'chat-bubble chat-bubble-primary shadow-sm'
									: 'chat-bubble chat-bubble-info shadow-sm'}
							>
								Text message
							</div>
						</div>
					{/each}
				</div>
				{#if messagingNeeded}
					<div class="flex flex-row gap-2">
						<div class="form-control w-full">
							<input
								type="text"
								class="input border-primary h-12 w-full rounded-md border-2"
								placeholder="What do you want to change..."
								id="message"
								name="message"
								bind:value={message}
								disabled={loading}
							/>
						</div>
						<button
							class="btn btn-primary btn-square btn-ghost"
							class:loading
							type="submit"
							disabled={loading}><IconSend style="font-size: xx-large;" /></button
						>
					</div>
				{/if}
			</div>
		</div>
	</div>
</div>

<style>
	.chat-container {
		height: calc(
			75vh - 20rem
		); /* Adjust the subtraction value according to your header and footer size */
	}
</style>
