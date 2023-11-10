<script lang="ts">
	// Icons imports
	import IconClose from '~icons/solar/alt-arrow-left-bold';
	import IconArrow from '~icons/solar/alt-arrow-right-bold';

	// Essential imports
	import { writable } from 'svelte/store';
	import { tick } from 'svelte';

	let messages = writable([]);
	let chatContainer: HTMLDivElement;

	async function scrollToBottom() {
		await tick();
		if (chatContainer) {
			chatContainer.scrollTop = chatContainer.scrollHeight;
		}
	}

	let messagesArray = [];
	let messagesArrayString: string;
	messages.subscribe((value) => {
		messagesArray = value;
		messagesArrayString = JSON.stringify(value);
	});
</script>

<div class="mx-auto flex min-h-full max-w-7xl flex-col gap-8">
	<a href="/dashboard">
		<button class="btn btn-link text-primary"><IconClose style="font-size: x-large;" />close</button
		>
	</a>
	<div class="self-center">
		<h1 class="mb-8 text-2xl font-bold md:text-3xl">Project Creation</h1>
	</div>
	<div class="flex flex-col-reverse justify-center gap-8 md:flex-row">
		<div class="flex flex-row justify-center">
			<div class="flex-grow">
				<ul class="steps steps-vertical w-full">
					<li data-content="?" class="step step-primary">Idea</li>
					<li class="step">Project Preview</li>
					<li class="step">Company Creation</li>
					<li class="step">Assistants Creation</li>
					<li class="step">Designing</li>
					<li class="step">Coding</li>
					<li class="step">Testing</li>
					<li class="step">Documentation</li>
					<li data-content="✓" class="step">Done</li>
				</ul>
			</div>
		</div>
		<div class="bg-base-200 mb-4 flex-1 rounded-lg p-8 shadow-lg md:mb-0">
			<div class="flex flex-col gap-8">
				<div class="flex flex-row justify-center">
					<h1 class="text-l font-bold md:text-xl">What is your idea?</h1>
				</div>
				<div class="flex flex-row justify-center">
					<div class="flex justify-center">
						<div class="form-control w-full md:w-96">
							<label for="" class="label">
								<span class="label-text">What do you want to generate?</span>
							</label>
							<textarea
								class="textarea border-primary h-48 w-full rounded-md border-2"
								placeholder="I want a personal protfolio website..."
								id="idea"
								name="idea"
							/>
						</div>
					</div>
				</div>
				<div class="mx-8 flex flex-row justify-center">
					<div class="flex-auto">
						<a href="/dashboard"><button class="btn btn-ghost">Cancel</button></a>
					</div>
					<button class="btn btn-primary" type="submit">Next</button>
				</div>
			</div>
		</div>
		<div class="divider divider-horizontal">
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
			80vh - 20rem
		); /* Adjust the subtraction value according to your header and footer size */
	}
</style>
