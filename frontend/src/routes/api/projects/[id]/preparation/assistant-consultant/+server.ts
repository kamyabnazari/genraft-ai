import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function POST({ params, request }) {
    const { id } = params;
    const body = await request.json();
    const requestBody = {
        assistant_name: body.assistant_name,
        assistant_instructions: body.assistant_instructions,
        assistant_model: body.assistant_model
    }

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}/preparation/assistant-consultant`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}