import { env } from '$env/dynamic/private';
import { error, json } from '@sveltejs/kit';

export async function PATCH({ params, request }) {
    const { id } = params;
    const body = await request.json();
    const requestBody = {
        current_phase: body.current_phase,
        current_stage: body.current_stage
    }

    try {
        const response = await fetch(`${env.PRIVATE_BACKEND_URL}/api/projects/${id}/update-progress`, {
            method: 'PATCH',
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