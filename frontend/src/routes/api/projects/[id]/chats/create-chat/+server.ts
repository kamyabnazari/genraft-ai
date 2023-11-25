import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function POST({ params, request }) {
    const { id } = params;
    const body = await request.json();
    const requestBody = {
        chat_name: body.chat_name,
        chat_assistant_primary: body.chat_assistant_primary,
        chat_assistant_secondary: body.chat_assistant_secondary
    }

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}/chats/create-chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            // If the response is not OK (e.g., 500 error), throw an error to be caught in the catch block
            throw new Error(`Backend returned an error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}