export const phases = [
    {
        key: 'preparation',
        name: "Preparation",
        title: "Preparation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Preparation", endpoint: "/api/project/{id}/preparation/start", method: "POST" },
            { key: 'idea', name: "Idea", result: "Initial Idea: {project.idea_initial}", endpoint: "/api/project/{id}/preparation/idea", method: "GET" },
            { key: 'stakeholder-assistant', name: "Stakeholder Assistant", result: "Stakeholder Assistant Created Successfully!", endpoint: "/api/project/{id}/preparation/stakeholder-assistant", method: "POST" },
            { key: 'consultant-assistant', name: "Consultant Assistant", result: "Consultant Assistant Created Successfully!", endpoint: "/api/project/{id}/preparation/consultant-assistant", method: "POST" },
            { key: 'done', name: "Done", result: "Preparation Phase Done!", endpoint: "/api/project/{id}/preparation/done", method: "GET" }
        ]
    },
    {
        key: 'idea-creation',
        name: "Idea Creation",
        title: "Idea Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Idea Creation", endpoint: "/api/project/{id}/idea-creation/start", method: "POST" },
            { key: 'idea', name: "Idea", result: "Initial Idea: {project.idea_initial}", endpoint: "/api/project/{id}/idea-creation/idea", method: "GET" },
            { key: 'chat-stakeholder-and-consultant', name: "Chat Between Stakeholder and Consultant", result: "Chat Concluded!", endpoint: "/api/project/{id}/idea-creation/chat-stakeholder-consultant", method: "POST" },
            { key: 'result', name: "Result", result: "Final Idea: {project.idea_final}", endpoint: "/api/project/{id}/idea-creation/result", method: "GET" },
            { key: 'done', name: "Done", result: "Idea Creation Phase Done!", endpoint: "/api/project/{id}/idea-creation/done", method: "GET" }
        ]
    },
    {
        key: 'company-creation',
        name: "Company Creation",
        title: "Company Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Company Creation", endpoint: "/api/project/{id}/company-creation/start", method: "POST" },
            { key: 'goal-setting', name: "Goal Setting", result: "Company Goals Set", endpoint: "/api/project/{id}/company-creation/goal-setting", method: "POST" },
            { key: 'role-definition', name: "Role Definition", result: "New Roles Defined", endpoint: "/api/project/{id}/company-creation/role-definition", method: "POST" },
            { key: 'done', name: "Done", result: "Company Creation Phase Done!", endpoint: "/api/project/{id}/company-creation/done", method: "GET" }
        ]
    },
    {
        key: 'designing',
        name: "Designing",
        title: "Designing Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Designing", endpoint: "/api/project/{id}/designing/start", method: "POST" },
            { key: 'product-specification', name: "Product Specification", result: "Product Specifications Defined", endpoint: "/api/project/{id}/designing/product-specification", method: "POST" },
            { key: 'prototype-development', name: "Prototype Development", result: "Prototypes Developed", endpoint: "/api/project/{id}/designing/prototype-development", method: "POST" },
            { key: 'done', name: "Done", result: "Designing Phase Done!", endpoint: "/api/project/{id}/designing/done", method: "GET" }
        ]
    },
    {
        key: 'coding',
        name: "Coding",
        title: "Coding Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Coding", endpoint: "/api/project/{id}/coding/start", method: "POST" },
            { key: 'implementation', name: "Implementation", result: "Code Implemented", endpoint: "/api/project/{id}/coding/implementation", method: "POST" },
            { key: 'ui-design', name: "UI Design", result: "UI Designed", endpoint: "/api/project/{id}/coding/ui-design", method: "POST" },
            { key: 'done', name: "Done", result: "Coding Phase Done!", endpoint: "/api/project/{id}/coding/done", method: "GET" }
        ]
    },
    {
        key: 'testing',
        name: "Testing",
        title: "Testing Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Testing", endpoint: "/api/project/{id}/testing/start", method: "POST" },
            { key: 'code-review', name: "Code Review", result: "Code Reviewed", endpoint: "/api/project/{id}/testing/code-review", method: "POST" },
            { key: 'quality-assurance', name: "Quality Assurance", result: "QA Tests Passed", endpoint: "/api/project/{id}/testing/quality-assurance", method: "POST" },
            { key: 'done', name: "Done", result: "Testing Phase Done!", endpoint: "/api/project/{id}/testing/done", method: "GET" }
        ]
    },
    {
        key: 'documenting',
        name: "Documenting",
        title: "Documenting Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Documenting", endpoint: "/api/project/{id}/documenting/start", method: "POST" },
            { key: 'technical-writing', name: "Technical Writing", result: "Technical Documentation Completed", endpoint: "/api/project/{id}/documenting/technical-writing", method: "POST" },
            { key: 'user-guides', name: "User Guides", result: "User Guides Created", endpoint: "/api/project/{id}/documenting/user-guides", method: "POST" },
            { key: 'done', name: "Done", result: "Documenting Phase Done!", endpoint: "/api/project/{id}/documenting/done", method: "GET" }
        ]
    },
    {
        key: 'project-completion',
        name: "Project Completion",
        title: "Project Completion Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Final Phase", endpoint: "/api/project/{id}/project-completion/start", method: "POST" },
            { key: 'final-review', name: "Final Review", result: "Final Review Completed", endpoint: "/api/project/{id}/project-completion/final-review", method: "POST" },
            { key: 'project-download', name: "Project Download", result: "Project Ready for Download", endpoint: "/api/project/{id}/project-completion/project-download", method: "POST" },
            { key: 'done', name: "Done", result: "Project Creation Done!", endpoint: "/api/project/{id}/project-completion/done", method: "GET" }
        ]
    },
];
