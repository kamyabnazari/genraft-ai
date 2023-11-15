import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function POST({ params }) {
    const { id } = params;

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/project/${id}/idea-creation/chat-stakeholder-consultant`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}