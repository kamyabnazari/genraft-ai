export const phases = [
    {
        key: 'idea-creation',
        name: "Idea Creation",
        title: "Idea Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Idea Creation", updatesProject: false },
            { key: 'idea-initial', name: "Initial Idea", result: "Initial Idea: {project.idea_initial}", updatesProject: true },
            {
                key: 'assistant-stakeholder', name: "Stakeholder Assistant", result: "Created Successfully!", updatesProject: false, endpoint: "/api/projects/{id}/assistants/create-assistant", method: "POST",
                "body": {
                    "assistant_name": "project-{id}-assistant-stakeholder",
                    "assistant_type": "stakeholder",
                    "assistant_instructions": "You are a stakeholder for a software company that creates financial software.",
                    "assistant_model": "gpt-3.5-turbo"
                }
            },
            {
                key: 'assistant-consultant', name: "Consultant Assistant", result: "Created Successfully!", updatesProject: false, endpoint: "/api/projects/{id}/assistants/create-assistant", method: "POST",
                "body": {
                    "assistant_name": "project-{id}-assistant-consultant",
                    "assistant_type": "consultant",
                    "assistant_instructions": "You are a idea consultant for a software company that help in the creation a detailed project from a short one.",
                    "assistant_model": "gpt-3.5-turbo"
                }
            },
            {
                key: 'chat-stakeholder-and-consultant', name: "Chat Stakeholder and Consultant", result: "Chat Concluded!", updatesProject: false, endpoint: "/api/projects/{id}/chats/chat-stakeholder-consultant", method: "POST",
                "body": {
                    "chat_name": "project-{id}-chat-stakeholder-and-consultant",
                    "chat_assistant_primary": "project-{id}-assistant-stakeholder",
                    "chat_assistant_secondary": "project-{id}-assistant-consultant",
                    "chat_goal": "The goal of this conversation is to use the initial project idea and create a detailed project idea out of it. When you have reached the final result, mark the final sentence with <END>"
                }
            },
            { key: 'idea-final', name: "Final Idea", result: "Final Idea: {project.idea_final}", updatesProject: true },
            { key: 'done', name: "Done", result: "Idea Creation Phase Done!", updatesProject: false }
        ]
    },
    {
        key: 'company-creation',
        name: "Company Creation",
        title: "Company Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Company Creation", updatesProject: false },
            { key: 'goal-setting', name: "Goal Setting", result: "Company Goals Set", updatesProject: false, endpoint: "/api/projects/{id}/company-creation/goal-setting", method: "POST", "body": {} },
            { key: 'role-definition', name: "Role Definition", result: "New Roles Defined", updatesProject: false, endpoint: "/api/projects/{id}/company-creation/role-definition", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Company Creation Phase Done!", updatesProject: false }
        ]
    },
    {
        key: 'designing',
        name: "Designing",
        title: "Designing Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Designing", updatesProject: false },
            { key: 'product-specification', name: "Product Specification", result: "Product Specifications Defined", updatesProject: false, endpoint: "/api/projects/{id}/designing/product-specification", method: "POST", "body": {} },
            { key: 'prototype-development', name: "Prototype Development", result: "Prototypes Developed", updatesProject: false, endpoint: "/api/projects/{id}/designing/prototype-development", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Designing Phase Done!", updatesProject: false }
        ]
    },
    {
        key: 'coding',
        name: "Coding",
        title: "Coding Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Coding", updatesProject: false },
            { key: 'implementation', name: "Implementation", result: "Code Implemented", updatesProject: false, endpoint: "/api/projects/{id}/coding/implementation", method: "POST", "body": {} },
            { key: 'ui-design', name: "UI Design", result: "UI Designed", updatesProject: false, endpoint: "/api/projects/{id}/coding/ui-design", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Coding Phase Done!", updatesProject: false }
        ]
    },
    {
        key: 'testing',
        name: "Testing",
        title: "Testing Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Testing", updatesProject: false },
            { key: 'code-review', name: "Code Review", result: "Code Reviewed", updatesProject: false, endpoint: "/api/projects/{id}/testing/code-review", method: "POST", "body": {} },
            { key: 'quality-assurance', name: "Quality Assurance", result: "QA Tests Passed", updatesProject: false, endpoint: "/api/projects/{id}/testing/quality-assurance", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Testing Phase Done!", updatesProject: false }
        ]
    },
    {
        key: 'documenting',
        name: "Documenting",
        title: "Documenting Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Documenting", updatesProject: false },
            { key: 'technical-writing', name: "Technical Writing", result: "Technical Documentation Completed", updatesProject: false, endpoint: "/api/projects/{id}/documenting/technical-writing", method: "POST", "body": {} },
            { key: 'user-guides', name: "User Guides", result: "User Guides Created", updatesProject: false, endpoint: "/api/projects/{id}/documenting/user-guides", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Documenting Phase Done!", updatesProject: false }
        ]
    },
    {
        key: 'project-completion',
        name: "Project Completion",
        title: "Project Completion Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Final Phase", updatesProject: false },
            { key: 'final-review', name: "Final Review", result: "Final Review Completed", updatesProject: false, endpoint: "/api/projects/{id}/project-completion/final-review", method: "POST", "body": {} },
            { key: 'project-download', name: "Project Download", result: "Project Ready for Download", updatesProject: false, endpoint: "/api/projects/{id}/project-completion/project-download", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Project Creation Done!", updatesProject: false }
        ]
    },
];
