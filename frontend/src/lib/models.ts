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
  successResult: string;
  errorResult: string;
  updatesProject: boolean;
  endpoint?: string;
  method?: string;
  body?: Body;
}

export interface Phase {
  key: string;
  name: string;
  title: string;
  stages: Stage[];
}

export interface Body {
  assistant_name?: string,
  assistant_type?: string,
  assistant_instructions?: string,
  assistant_model?: string,
  chat_name?: string,
  chat_goal?: string,
  chat_assistant_primary?: string,
  chat_assistant_secondary?: string,
}

export type Phases = Phase[];