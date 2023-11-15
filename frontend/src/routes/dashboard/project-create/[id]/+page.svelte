<script lang="ts">
	// Icons imports
	import IconClose from '~icons/solar/alt-arrow-left-bold';
	import IconArrow from '~icons/solar/alt-arrow-right-bold';
	import IconChecked from '~icons/solar/check-circle-bold';
	import IconClock from '~icons/solar/clock-square-outline';

	// Essential imports
	import { writable } from 'svelte/store';
	import { goto } from '$app/navigation';
	import { onMount, tick } from 'svelte';
	import { page } from '$app/stores';
	import type { Phase, Phases, Project, Stage } from '$lib/models';
	import { phases } from '$lib/utils';

	let project: Project = {
		id: '',
		name: '',
		idea_initial: '',
		idea_final: '',
		folder_path: '',
		created_at: ''
	};

	let chatContainer: HTMLDivElement;
	let messages = writable<string[]>([]);
	let messagesArray: string[] = [];
	let messagesArrayString: string = '';

	// Reactive declaration for projectId
	let projectId: string = '';
	$: projectId = $page.params.id;

	onMount(async () => {
		if (projectId) {
			await getProjectById();
		}
	});

	// Function to fetch project details by ID
	async function getProjectById() {
		loading = true;

		try {
			const response = await fetch(`/api/projects/${projectId}`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			const result = await response.json();
			project = result;
		} catch (error) {
			console.error('Error fetching project idea:', error);
		} finally {
			loading = false;
		}
	}

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

	// Stages and Phases

	const currentPhaseIndex = writable(0);
	const currentStageIndex = writable(0);
	let automaticMode = writable(false);
	let phasesDone: boolean = false;
	let stagesDone: boolean = false;
	let loading: boolean = false;

	async function callStageApi(stage: Stage) {
		try {
			const response = await fetch(stage.endpoint, {
				method: stage.method || 'GET'
				// Include other necessary configurations like headers, body, etc.
			});
			if (!response.ok) {
				throw new Error(`API call for stage ${stage.name} failed`);
			}
			return response.json();
		} catch (error) {
			console.error('Error calling stage API:', error);
		}
	}

	function delay(ms: number) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	// Function to replace ${id} in endpoint with actual project id
	function updatePhaseEndpoints(phases: Phases, projectId: string) {
		return phases.map((phase: Phase) => {
			return {
				...phase,
				stages: phase.stages.map((stage: Stage) => {
					return {
						...stage,
						endpoint: stage.endpoint.replace('{id}', projectId)
					};
				})
			};
		});
	}

	// Function to start a specific phase
	async function startPhase(phaseIndex: number) {
		loading = true; // Start loading when a phase starts

		const updatedPhases = updatePhaseEndpoints(phases, projectId);
		const phase = updatedPhases[phaseIndex];
		for (let i = 0; i < phase.stages.length; i++) {
			currentStageIndex.set(i);
			const stage = phase.stages[i];
			if (phase.key === 'preparation') {
				await callStageApi(stage);
			}
			await delay(1000);
		}
		stagesDone = true;

		// Check if all phases are completed
		if (phaseIndex === phases.length - 1) {
			phasesDone = true;
			loading = false; // Stop loading only after all phases are done
		} else if ($automaticMode) {
			// If not the last phase and in automatic mode, proceed to next phase
			currentPhaseIndex.update((n) => n + 1);
			currentStageIndex.set(0);
			stagesDone = false;
			await startPhase(phaseIndex + 1);
		} else {
			loading = false; // If in manual mode, stop loading after each phase
		}
	}

	// Handle the start of a phase
	async function handleStart() {
		await startPhase($currentPhaseIndex);
	}

	// Handle the start of a phase
	async function handleNext() {
		currentPhaseIndex.update((n) => n + 1);
		currentStageIndex.set(0);
		stagesDone = false;
	}

	async function handleDashboard() {
		goto('/dashboard');
	}

	function getResultWithProjectData(stage: Stage) {
		let resultWithProjectData = stage.result;

		if (stage.result.includes('{project.idea_initial}')) {
			resultWithProjectData = resultWithProjectData.replace(
				'{project.idea_initial}',
				project.idea_initial
			);
		}
		if (stage.result.includes('{project.idea_final}')) {
			resultWithProjectData = resultWithProjectData.replace(
				'{project.idea_final}',
				project.idea_final
			);
		}

		return resultWithProjectData;
	}
</script>

<div class="mx-auto flex min-h-full max-w-7xl flex-col gap-8">
	<div class="flex items-start">
		<button class="btn btn-link text-primary" on:click={handleDashboard} style="max-width: 150px;">
			<IconClose style="font-size: x-large;" /> close
		</button>
	</div>
	<div class="self-center">
		<h1 class="mb-8 text-2xl font-bold md:text-3xl">Project Creation Assistant</h1>
	</div>
	<div class="flex flex-col justify-center gap-8 lg:flex-row">
		<div class="flex flex-col justify-center gap-8">
			<div class="overflow-x-auto">
				<ul class="steps steps-horizontal lg:steps-vertical">
					{#each phases as phase, index (phase.key)}
						<li class={index <= $currentPhaseIndex ? 'step step-primary' : 'step'}>
							{phase.name}
						</li>
					{/each}
				</ul>
			</div>
			<div class="divider divider-vertical lg:divider-vertical" />
			<div>
				<div class="form-control w-52">
					<label class="label cursor-pointer">
						<span class="label-text">AUTOMATIC</span>
						<input
							type="checkbox"
							class="toggle toggle-accent"
							bind:checked={$automaticMode}
							disabled={loading || stagesDone || phasesDone}
						/>
					</label>
				</div>
			</div>
		</div>
		<div class="divider divider-vertical lg:divider-horizontal">
			<IconArrow style="font-size: xx-large;" />
		</div>
		<div class="bg-base-200 flex flex-1 flex-col justify-between rounded-lg p-8 shadow-lg">
			<div class="flex flex-row justify-center">
				<h1 class="text-l mb-8 font-bold md:text-xl">
					{phases[$currentPhaseIndex].title}
				</h1>
			</div>
			<div class="justify-left flex flex-row">
				<div class="max-h-[400px] w-full overflow-auto">
					<ul class="timeline timeline-vertical timeline-compact">
						{#each phases[$currentPhaseIndex].stages as stage, index (stage.key)}
							<li>
								<div class="timeline-start">{stage.name}</div>
								<div class="timeline-middle">
									<IconChecked
										style="font-size: x-large;"
										class={index <= $currentStageIndex ? 'text-primary' : ''}
									/>
								</div>
								<div class="timeline-end timeline-box">
									{#if index === $currentStageIndex && loading}
										<span class="loading loading-spinner"></span>
									{:else if index < $currentStageIndex}
										<p>{getResultWithProjectData(stage)}</p>
									{:else if index === $currentStageIndex && stage.key === 'done'}
										<p>{getResultWithProjectData(stage)}</p>
									{:else}
										<IconClock
											style="font-size: large;"
											class={index < $currentStageIndex ? 'text-primary' : ''}
										/>
									{/if}
								</div>
								{#if index < $currentStageIndex}
									<hr class="bg-primary" />
								{:else if stage.key !== 'done'}
									<hr />
								{/if}
							</li>
						{/each}
					</ul>
				</div>
			</div>
			<div class="mt-8 flex flex-row justify-center">
				{#if stagesDone === false}
					<button
						class="btn btn-warning btn-wide"
						type="button"
						on:click={handleStart}
						disabled={loading}
					>
						{#if loading}
							<span class="loading loading-spinner"></span>
						{:else}
							Start
						{/if}
					</button>
				{:else if phasesDone === false}
					<button
						class="btn btn-neutral btn-wide"
						type="button"
						on:click={handleNext}
						disabled={loading}
					>
						{#if loading}
							<span class="loading loading-spinner"></span>
						{:else}
							Next
						{/if}
					</button>
				{/if}
				{#if phasesDone}
					<button
						class="btn btn-primary btn-wide"
						type="button"
						on:click={handleDashboard}
						disabled={loading}
					>
						{#if loading}
							<span class="loading loading-spinner"></span>
						{:else}
							Done
						{/if}
					</button>
				{/if}
			</div>
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
