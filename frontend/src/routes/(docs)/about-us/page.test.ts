import { afterEach, describe, test } from 'vitest';
import { cleanup, render } from '@testing-library/svelte';
import Page from './+page.svelte';

describe('Page', () => {
	afterEach(cleanup);

	test('renders the title', async () => {
		const { getByText } = render(Page);
		const element = getByText('Genraft AI');
		if (!element || element.textContent !== 'Genraft AI') {
			throw new Error('Expected text not found');
		}
	});
});
