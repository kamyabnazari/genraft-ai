import { error, json } from '@sveltejs/kit';

export async function POST({ locals }) {
    try {
        
        return json();

    } catch {
        throw error(400, 'User not found for recently added document!');
    }
}
