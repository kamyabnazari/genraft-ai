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
	import { phases } from '$lib/utils';
	import type { Phases, Project, Stage, ChatMessage, ChatHistory } from '$lib/models';

	let project: Project = {
		id: '',
		name: '',
		idea_initial: '',
		idea_final: '',
		technical_plan: '',
		folder_path: '',
		created_at: '',
		current_phase: '',
		current_stage: ''
	};

	// Reactive declaration for projectId
	let projectId: string = '';
	$: projectId = $page.params.id;

	const currentPhaseIndex = writable(0);
	const currentStageIndex = writable(0);
	let messages = writable<string[]>([]);
	let automaticMode = writable(false);
	let chatContainer: HTMLDivElement;
	let stagesContainer: HTMLDivElement;
	let previousStageIndex = 0;
	let phasesDone: boolean = false;
	let stagesDone: boolean = false;
	let loading: boolean = false;
	let hasPhaseStarted: boolean = false;
	let stageSuccessStatus: (boolean | null)[] = [];
	let uniqueSenders = writable(new Set());
	let firstSender: string | unknown = '';
	let chatId: string;
	let chatIds = writable<ChatHistory[]>([]);

	onMount(async () => {
		if (projectId) {
			await getProjectById();
			await getInitialProjectProgress();
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

	async function updateProjectProgress(phaseKey: string, stageKey: string) {
		try {
			const response = await fetch(`/api/projects/${projectId}/update-progress`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					current_phase: phaseKey,
					current_stage: stageKey
				})
			});

			if (!response.ok) {
				throw new Error('Failed to update project progress');
			}
		} catch (error) {
			console.error('Error updating project progress:', error);
		}
	}

	async function getInitialProjectProgress() {
		// Update the endpoints with the correct projectId
		let projectPhases = updatePhaseEndpoints(phases, projectId);

		const phaseIndex = phases.findIndex((p) => p.key === project.current_phase);
		currentPhaseIndex.set(phaseIndex >= 0 ? phaseIndex : 0);

		const stageIndex =
			phaseIndex >= 0
				? phases[phaseIndex].stages.findIndex((s) => s.key === project.current_stage)
				: 0;
		currentStageIndex.set(stageIndex >= 0 ? stageIndex : 0);

		if ($currentPhaseIndex !== 0 || $currentStageIndex !== 0) {
			// Set hasPhaseStarted to true only if beyond the first stage
			if ($currentStageIndex > 0) {
				hasPhaseStarted = true;
			}

			stageSuccessStatus = phases[$currentPhaseIndex].stages.map((_, index) =>
				index < $currentStageIndex ? true : null
			);

			if ($currentStageIndex === phases[$currentPhaseIndex].stages.length - 1) {
				stagesDone = true;
			}

			// Call API for each completed stage of all phases to fetch chat history if necessary
			for (let p = 0; p <= $currentPhaseIndex; p++) {
				const currentPhase = projectPhases[p];
				// Determine the last stage to check in the current iteration phase
				let lastStageToCheck = currentPhase.stages.length;

				// If it's the current phase, only iterate up to the current stage
				if (p === $currentPhaseIndex) {
					lastStageToCheck = $currentStageIndex + 1; // Include the current stage as well
				}

				for (let s = 0; s < lastStageToCheck; s++) {
					const stage = currentPhase.stages[s];
					// Assuming stages before the current stage in the current phase are completed
					// and all stages in previous phases are completed.
					if (stage.endpoint && stage.endpoint.includes('/chats/')) {
						await callStageApi(stage, s); // Force call for completed stages
					}
				}
			}
		}
		scrollToBottomStagesContainer();
	}

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

				chatIds.update((currentChatIds: ChatHistory[]) => {
					const existingChatId = currentChatIds.find((chat) => chat.chat_id === data.chat_id);
					if (!existingChatId) {
						// If this chat_id is not already in the list, add it
						return [...currentChatIds, { chat_id: data.chat_id, name: stage.name }];
					} else {
						// Otherwise, return the list unmodified
						return currentChatIds;
					}
				});
			}

			return { success: true, data };
		} catch (error) {
			console.error('Error calling stage API:', error);
			stageSuccessStatus[stageIndex] = false;
			return { success: false, data: null };
		}
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

			const currentPhaseKey = phases[$currentPhaseIndex].key;
			const currentStageKey = phases[$currentPhaseIndex].stages[$currentStageIndex].key;
			await updateProjectProgress(currentPhaseKey, currentStageKey);
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

		const nextPhaseKey = phases[$currentPhaseIndex].key;
		const nextStageKey = phases[$currentPhaseIndex].stages[0].key;
		await updateProjectProgress(nextPhaseKey, nextStageKey);
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

	function getResultWithProjectData(stage: Stage, isSuccess: boolean, project: Project) {
		let resultWithProjectData = isSuccess ? stage.successResult : stage.errorResult;

		// Define the placeholders with an index signature
		const placeholders: { [key: string]: string } = {
			'{project.idea_initial}': project.idea_initial,
			'{project.idea_final}': project.idea_final,
			'{project.technical_plan}': project.technical_plan
		};

		for (const key in placeholders) {
			if (placeholders.hasOwnProperty(key)) {
				resultWithProjectData = resultWithProjectData.replace(key, placeholders[key]);
			}
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
		<h1 class="mb-8 text-2xl font-bold md:text-3xl">{project.name}</h1>
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
												? getResultWithProjectData(stage, !!stageSuccessStatus[index], project)
												: getResultWithProjectData(stage, true, project)}
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
				<h1 class="text-l text-center font-bold md:text-xl">Chats</h1>
				<select
					class="select select-bordered w-full"
					bind:value={chatId}
					on:change={() => fetchChatHistory(chatId)}
				>
					{#each $chatIds as { chat_id, name }, index}
						<option value={chat_id}>{index + 1}: {name}</option>
					{/each}
				</select>
				<div
					class="form-control chat-container bg-base-100 border-rounded border-base-300 flex-grow overflow-y-auto rounded-lg border-2 p-2"
					bind:this={chatContainer}
				>
					{#each $messages as message (message)}
						<div class={'chat ' + determineAlignment(message.split(':')[0]) + ' my-4'}>
							<div class="chat-header">
								{message.split(':')[0].toUpperCase()}
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
			65vh - 20rem
		); /* Adjust the subtraction value according to your header and footer size */
	}
</style>
