import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function GET() {
    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}

export async function POST({ request }) {
    const body = await request.json();
    const requestBody = {
        name: body.name,
        idea: body.idea
    }

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects`, {
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