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