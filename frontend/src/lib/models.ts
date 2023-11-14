export interface Project {
  id: string;
  name: string;
  idea_initial: string;
  idea_final: string;
  folder_path: string;
  created_at: string;
}

export interface ProjectStats {
  total_projects: number;
  total_files: number;
  total_assets: number;
}

export interface Stage {
  key: string;
  name: string;
  result: string;
  endpoint: string;
}