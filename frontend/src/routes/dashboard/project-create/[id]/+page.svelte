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
	import type { Phases, Project, Stage, ChatMessage } from '$lib/models';
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
	let stagesContainer: HTMLDivElement;
	let messages = writable<string[]>([]);

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
		}
	}

	let uniqueSenders = writable(new Set());
	let firstSender: string | unknown = '';

	uniqueSenders.subscribe((senders) => {
		firstSender = Array.from(senders)[0];
	});

	function determineAlignment(sender: string) {
		// Assign one style to the first sender and another to the second sender
		return sender === firstSender ? 'chat-end' : 'chat-start';
	}

	function determineBubbleStyle(sender: string) {
		// Similar logic for bubble style
		return sender === firstSender ? 'chat-bubble-primary' : 'chat-bubble-info';
	}

	async function scrollToBottomChatContainer() {
		await tick();
		if (chatContainer) {
			chatContainer.scrollTop = chatContainer.scrollHeight;
		}
	}

	async function scrollToBottomStagesContainer() {
		await tick(); // Wait for DOM updates
		if (stagesContainer) {
			// Find the element representing the current stage
			const currentStageElement = stagesContainer.querySelector(
				`.stage-item-${$currentStageIndex}`
			);

			if (currentStageElement && currentStageElement instanceof HTMLElement) {
				// Calculate the position to scroll to
				const topPos = currentStageElement.offsetTop;
				stagesContainer.scrollTop = topPos;
			}
		}
	}

	// Stages and Phases

	const currentPhaseIndex = writable(0);
	const currentStageIndex = writable(0);
	let automaticMode = writable(false);
	let previousStageIndex = 0;
	let phasesDone: boolean = false;
	let stagesDone: boolean = false;
	let loading: boolean = false;
	let hasPhaseStarted: boolean = false;
	let stageSuccessStatus: (boolean | null)[] = [];
	let chatId: string;

	async function callStageApi(stage: Stage, stageIndex: number) {
		try {
			if (!stage.endpoint) {
				console.warn(`No endpoint specified for stage ${stage.name}`);
				return { success: true, data: null }; // Assuming no endpoint means success by default
			}

			const requestOptions: RequestInit = {
				method: stage.method || 'GET',
				headers: { 'Content-Type': 'application/json' }
			};

			// Add body to request if it exists in the stage object and method is not GET
			if (stage.method !== 'GET' && stage.body) {
				requestOptions.body = JSON.stringify(stage.body);
			}

			const response = await fetch(stage.endpoint, requestOptions);

			if (!response.ok) {
				console.error(`API call for stage ${stage.name} failed`);
				stageSuccessStatus[stageIndex] = false;
				return { success: false, data: null };
			}

			const data = await response.json();
			stageSuccessStatus[stageIndex] = true;

			// Check if the response contains a chat_id and store it
			if (data.chat_id) {
				chatId = data.chat_id;
				fetchChatHistory(chatId);
			}

			return { success: true, data };
		} catch (error) {
			console.error('Error calling stage API:', error);
			stageSuccessStatus[stageIndex] = false;
			return { success: false, data: null };
		}
	}

	function delay(ms: number) {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	function updatePhaseEndpoints(phases: Phases, projectId: string) {
		return phases.map((phase) => {
			return {
				...phase,
				stages: phase.stages.map((stage) => {
					const updatedStage: Stage = { ...stage };

					if (stage.endpoint) {
						updatedStage.endpoint = stage.endpoint.replace('{id}', projectId);
					}

					if (stage.body && typeof stage.body === 'object') {
						updatedStage.body = Object.fromEntries(
							Object.entries(stage.body).map(([key, value]) => {
								return [key, value.toString().replace('{id}', projectId)];
							})
						);
					}

					return updatedStage;
				})
			};
		});
	}

	async function startPhase(phaseIndex: number) {
		loading = true;
		hasPhaseStarted = true;
		stageSuccessStatus = phases[phaseIndex].stages.map(() => null);

		const updatedPhases = updatePhaseEndpoints(phases, projectId);
		const phase = updatedPhases[phaseIndex];
		let allStagesSuccessful = true;

		for (let i = 0; i < phase.stages.length; i++) {
			currentStageIndex.set(i);
			const stage = phase.stages[i];

			if (previousStageIndex !== $currentStageIndex) {
				scrollToBottomStagesContainer();
			}
			previousStageIndex = $currentStageIndex;

			if (stage.endpoint) {
				const result = await callStageApi(stage, i);
				if (!result.success) {
					allStagesSuccessful = false;
					break; // Stop the phase if any stage fails
				}
			}

			if (stage.updatesProject) {
				await getProjectById();
			}
			await delay(1000);
		}

		if (allStagesSuccessful) {
			stagesDone = true;
			if (phaseIndex < phases.length - 1 && $automaticMode) {
				// Proceed to next phase in automatic mode
				currentPhaseIndex.update((n) => n + 1);
				await startPhase($currentPhaseIndex);
			}
		} else {
			stagesDone = false;
		}

		loading = false;
		phasesDone = phaseIndex === phases.length - 1 && stagesDone;
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
		hasPhaseStarted = false;
	}

	async function handleDashboard() {
		goto('/dashboard');
	}

	async function fetchChatHistory(chatId: string) {
		if (!chatId) {
			console.error('Chat ID is not available');
			return;
		}
		try {
			const response = await fetch(`/api/projects/${projectId}/chats/${chatId}`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				throw new Error('Server responded with an error!');
			}

			const result = await response.json();

			// Update the messages store with the new chat history
			messages.set(
				result.conversation.map((item: ChatMessage) => `${item.sender}: ${item.message}`)
			);

			// Extract unique senders and update the uniqueSenders store
			let senders = new Set(result.conversation.map((item: ChatMessage) => item.sender));
			uniqueSenders.set(senders);

			scrollToBottomChatContainer(); // Scroll to the bottom of the chat
		} catch (error) {
			console.error('Error fetching chat messages:', error);
		}
	}

	function getResultWithProjectData(stage: Stage, isSuccess: boolean) {
		let resultWithProjectData = isSuccess ? stage.successResult : stage.errorResult;

		if (resultWithProjectData.includes('{project.idea_initial}')) {
			resultWithProjectData = resultWithProjectData.replace(
				'{project.idea_initial}',
				project.idea_initial
			);
		}
		if (resultWithProjectData.includes('{project.idea_final}')) {
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
				<div class="max-h-[400px] w-full overflow-auto" bind:this={stagesContainer}>
					<ul class="timeline timeline-vertical timeline-compact">
						{#each phases[$currentPhaseIndex].stages as stage, index (stage.key)}
							<li class="stage-item-{index}">
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
									{:else if hasPhaseStarted && (index < $currentStageIndex || (index === $currentStageIndex && !loading))}
										<p class={stageSuccessStatus[index] === false ? 'text-error' : ''}>
											{stageSuccessStatus[index] !== null
												? getResultWithProjectData(stage, !!stageSuccessStatus[index])
												: getResultWithProjectData(stage, true)}
										</p>
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
				{#if !stagesDone && !phasesDone}
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
				{:else if stagesDone && !phasesDone}
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
						<div class={'chat ' + determineAlignment(message.split(':')[0]) + ' my-4'}>
							<div class="chat-header">
								{message.split(':')[0]}
							</div>
							<div
								class={'chat-bubble ' + determineBubbleStyle(message.split(':')[0]) + ' shadow-sm'}
							>
								{message.split(':').slice(1).join(':')}
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
