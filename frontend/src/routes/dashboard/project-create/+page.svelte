<script lang="ts">
	// Icons imports
	import IconClose from '~icons/solar/alt-arrow-left-bold';
	import IconArrow from '~icons/solar/alt-arrow-right-bold';
	import IconSend from '~icons/solar/square-arrow-up-bold';

	// Essential imports
	import { writable } from 'svelte/store';
	import { tick } from 'svelte';

	let messages = writable([]);
	let message: string;
	let loading: boolean;
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
	<div class="flex flex-col justify-center gap-8 lg:flex-row">
		<div class="flex flex-row justify-center">
			<div class="flex-grow">
				<ul class="steps steps-horizontal lg:steps-vertical w-full">
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
		<div class="divider divider-vertical lg:divider-horizontal">
			<IconArrow style="font-size: xx-large;" />
		</div>
		<div class="bg-base-200 flex-1 rounded-lg p-8 shadow-lg">
			<div class="flex flex-col gap-8">
				<div class="flex flex-row justify-center">
					<h1 class="text-l font-bold md:text-xl">What is your idea?</h1>
				</div>
				<div class="flex w-full flex-row justify-center">
					<div class="flex w-full justify-center">
						<div class="form-control w-full">
							<label for="" class="label">
								<span class="label-text">What project do you want to generate?</span>
							</label>
							<textarea
								class="textarea border-primary h-96 w-full rounded-md border-2"
								placeholder="I want a personal protfolio website..."
								id="idea"
								name="idea"
							/>
						</div>
					</div>
				</div>
				<div class="mx-4 flex flex-row justify-center">
					<div class="flex-auto">
						<a href="/dashboard"><button class="btn btn-ghost">Cancel</button></a>
					</div>
					<button class="btn btn-primary" type="submit">Next</button>
				</div>
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
					<!-- Hidden input field for messagesArray -->
					<input type="hidden" name="messagesArray" bind:value={messagesArrayString} />
					<button
						class="btn btn-primary btn-square btn-ghost"
						class:loading
						type="submit"
						disabled={loading}><IconSend style="font-size: xx-large;" /></button
					>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.chat-container {
		height: calc(
			70vh - 20rem
		); /* Adjust the subtraction value according to your header and footer size */
	}
</style>
