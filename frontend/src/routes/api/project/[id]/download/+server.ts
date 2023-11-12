import { env } from '$env/dynamic/private';
import { error } from '@sveltejs/kit';

export async function GET({ params }) {
    const { id } = params;

    try {
        const backendResponse = await fetch(`${env.PRIVATE_BACKEND_URL}/api/project/${id}/download`);
        if (!backendResponse.ok) {
            throw new Error(`Backend responded with status: ${backendResponse.status}`);
        }

        // Convert the response into a buffer
        const fileBuffer = await backendResponse.arrayBuffer();

        // Create headers object with index signature
        const headers: Record<string, string> = {
            'Content-Type': 'application/zip',
        };
        const contentDisposition = backendResponse.headers.get('Content-Disposition');
        if (contentDisposition) {
            headers['Content-Disposition'] = contentDisposition;
        }

        const options = {
            status: 200,
            headers: headers
        };

        // Return the buffer in the response
        return new Response(fileBuffer, options);
    } catch (err) {
        console.error('Error in server-side file download:', err);
        throw error(500, 'Internal Server Error');
    }
}

