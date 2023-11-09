import { z } from 'zod';

export const projectCreationPrompt = z.object({
	prompt: z.string().min(1),
});
