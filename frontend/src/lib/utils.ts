export const phases = [
    {
        key: 'preparation',
        name: "Preparation",
        title: "Preparation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Preparation", endpoint: "/api/projects/{id}/preparation/start", method: "POST", "body": {} },
            { key: 'idea', name: "Idea", result: "Initial Idea: {project.idea_initial}", endpoint: "/api/projects/{id}/preparation/idea", method: "GET", "body": {} },
            {
                key: 'assistant-stakeholder', name: "Stakeholder Assistant", result: "Stakeholder Assistant \n Created Successfully!", endpoint: "/api/projects/{id}/preparation/assistant-stakeholder", method: "POST",
                "body": {
                    "assistant_name": "project-{id}-assistant-stakeholder",
                    "assistant_instructions": "You are a stakeholder for a software company that creates financial software.",
                    "assistant_model": "gpt-3.5-turbo"
                }
            },
            {
                key: 'assistant-consultant', name: "Consultant Assistant", result: "Consultant Assistant \n Created Successfully!", endpoint: "/api/projects/{id}/preparation/assistant-consultant", method: "POST",
                "body": {
                    "assistant_name": "project-{id}-assistant-consultant",
                    "assistant_instructions": "You are a idea consultant for a software company that help in the creation a detailed project from a short one.",
                    "assistant_model": "gpt-3.5-turbo"
                }
            },
            { key: 'done', name: "Done", result: "Preparation Phase Done!", endpoint: "/api/projects/{id}/preparation/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'idea-creation',
        name: "Idea Creation",
        title: "Idea Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Idea Creation", endpoint: "/api/projects/{id}/idea-creation/start", method: "POST", "body": {} },
            { key: 'idea', name: "Idea", result: "Initial Idea: {project.idea_initial}", endpoint: "/api/projects/{id}/idea-creation/idea", method: "GET", "body": {} },
            { key: 'chat-stakeholder-and-consultant', name: "Chat Stakeholder and Consultant", result: "Chat Concluded!", endpoint: "/api/projects/{id}/idea-creation/chat-stakeholder-consultant", method: "POST", "body": {} },
            { key: 'result', name: "Result", result: "Final Idea: {project.idea_final}", endpoint: "/api/projects/{id}/idea-creation/result", method: "GET", "body": {} },
            { key: 'done', name: "Done", result: "Idea Creation Phase Done!", endpoint: "/api/projects/{id}/idea-creation/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'company-creation',
        name: "Company Creation",
        title: "Company Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Company Creation", endpoint: "/api/projects/{id}/company-creation/start", method: "POST", "body": {} },
            { key: 'stakeholder-assistant', name: "Stakeholder Assistant", result: "Stakeholder Assistant Created Successfully!", endpoint: "/api/projects/{id}/preparation/stakeholder-assistant", method: "POST", "body": {} },
            { key: 'goal-setting', name: "Goal Setting", result: "Company Goals Set", endpoint: "/api/projects/{id}/company-creation/goal-setting", method: "POST", "body": {} },
            { key: 'role-definition', name: "Role Definition", result: "New Roles Defined", endpoint: "/api/projects/{id}/company-creation/role-definition", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Company Creation Phase Done!", endpoint: "/api/projects/{id}/company-creation/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'designing',
        name: "Designing",
        title: "Designing Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Designing", endpoint: "/api/projects/{id}/designing/start", method: "POST", "body": {} },
            { key: 'product-specification', name: "Product Specification", result: "Product Specifications Defined", endpoint: "/api/projects/{id}/designing/product-specification", method: "POST", "body": {} },
            { key: 'prototype-development', name: "Prototype Development", result: "Prototypes Developed", endpoint: "/api/projects/{id}/designing/prototype-development", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Designing Phase Done!", endpoint: "/api/projects/{id}/designing/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'coding',
        name: "Coding",
        title: "Coding Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Coding", endpoint: "/api/projects/{id}/coding/start", method: "POST", "body": {} },
            { key: 'implementation', name: "Implementation", result: "Code Implemented", endpoint: "/api/projects/{id}/coding/implementation", method: "POST", "body": {} },
            { key: 'ui-design', name: "UI Design", result: "UI Designed", endpoint: "/api/projects/{id}/coding/ui-design", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Coding Phase Done!", endpoint: "/api/projects/{id}/coding/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'testing',
        name: "Testing",
        title: "Testing Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Testing", endpoint: "/api/projects/{id}/testing/start", method: "POST", "body": {} },
            { key: 'code-review', name: "Code Review", result: "Code Reviewed", endpoint: "/api/projects/{id}/testing/code-review", method: "POST", "body": {} },
            { key: 'quality-assurance', name: "Quality Assurance", result: "QA Tests Passed", endpoint: "/api/projects/{id}/testing/quality-assurance", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Testing Phase Done!", endpoint: "/api/projects/{id}/testing/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'documenting',
        name: "Documenting",
        title: "Documenting Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Documenting", endpoint: "/api/projects/{id}/documenting/start", method: "POST", "body": {} },
            { key: 'technical-writing', name: "Technical Writing", result: "Technical Documentation Completed", endpoint: "/api/projects/{id}/documenting/technical-writing", method: "POST", "body": {} },
            { key: 'user-guides', name: "User Guides", result: "User Guides Created", endpoint: "/api/projects/{id}/documenting/user-guides", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Documenting Phase Done!", endpoint: "/api/projects/{id}/documenting/done", method: "GET", "body": {} }
        ]
    },
    {
        key: 'project-completion',
        name: "Project Completion",
        title: "Project Completion Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Final Phase", endpoint: "/api/projects/{id}/project-completion/start", method: "POST", "body": {} },
            { key: 'final-review', name: "Final Review", result: "Final Review Completed", endpoint: "/api/projects/{id}/project-completion/final-review", method: "POST", "body": {} },
            { key: 'project-download', name: "Project Download", result: "Project Ready for Download", endpoint: "/api/projects/{id}/project-completion/project-download", method: "POST", "body": {} },
            { key: 'done', name: "Done", result: "Project Creation Done!", endpoint: "/api/projects/{id}/project-completion/done", method: "GET", "body": {} }
        ]
    },
];
