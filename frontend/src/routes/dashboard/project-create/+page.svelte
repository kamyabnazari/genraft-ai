<div class="hero bg-base-100 min-h-full">
	<div class="hero-content">
		<div class="card bg-base-200 p-8 shadow-lg sm:p-16">
			<div class="flex flex-col gap-8">
				<div class="flex flex-row justify-center">
					<h1 class="text-2xl font-bold md:text-3xl">Create a new project</h1>
				</div>
				<div class="flex flex-row justify-center">
					<div class="flex-grow">
						<ul class="steps w-full">
							<li class="step step-primary">Idea</li>
							<li class="step">Preview</li>
							<li class="step">Done</li>
						</ul>
					</div>
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
				<div class="flex flex-row justify-center">
					<div class="flex-auto">
						<a href="/dashboard"><button class="btn btn-ghost">Cancel</button></a>
					</div>
					<button class="btn btn-primary" type="submit">Create</button>
				</div>
			</div>
		</div>
	</div>
</div>
