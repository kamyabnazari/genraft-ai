import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function POST({ params, request }) {
    const { id } = params;
    const body = await request.json();
    const requestBody = {
        chat_name: body.chat_name,
        chat_assistant_primary: body.chat_assistant_primary,
        chat_assistant_secondary: body.chat_assistant_secondary,
        chat_goal: body.chat_goal
    }

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}/chats/create-chat`, {
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