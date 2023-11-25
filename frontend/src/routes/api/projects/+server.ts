import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function GET() {
    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
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