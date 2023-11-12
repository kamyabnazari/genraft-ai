import { writable } from 'svelte/store';

export const statistics = writable({
    total_projects: 0,
    total_files: 0,
    total_assets: 0
});

export async function refreshStatistics() {
    const response = await fetch(`/api/stats/projects`);
    if (response.ok) {
        const stats = await response.json();
        statistics.set(stats);
    }
}
