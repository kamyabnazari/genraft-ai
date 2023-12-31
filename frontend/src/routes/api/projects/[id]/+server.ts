import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function DELETE({ params }) {
    const { id } = params;

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}

export async function GET({ params }) {
    const { id } = params;

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });

        const data = await response.json();
        return json(data);
    } catch {
        throw error(500, 'Internal Server Error');
    }
}