import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function GET({ params }) {
    const { id } = params;
    const { chat_id } = params;

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}/chats/${chat_id}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}