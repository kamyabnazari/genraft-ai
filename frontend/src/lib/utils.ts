export const phases = [
    {
        key: 'preparation',
        name: "Preparation",
        title: "Preparation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Preparation", endpoint: "/api/preparation/start" },
            { key: 'idea', name: "Idea", result: "Initial Idea: {project.idea_initial}", endpoint: "/api/preparation/idea" },
            { key: 'stakeholderAssistant', name: "Stakeholder Assistant", result: "Assistant Created Successfully!", endpoint: "/api/preparation/stakeholder-assistant" },
            { key: 'ideaConsultantAssistant', name: "Idea Consultant Assistant", result: "Assistant Created Successfully!", endpoint: "/api/preparation/idea-consultant-assistant" },
            { key: 'stakeholderAndIdeaConsultantChat', name: "Chat Between James and Max", result: "Chat Concluded!", endpoint: "/api/preparation/chat-between-james-and-max" },
            { key: 'result', name: "Result", result: "Final Idea: {project.idea_final}", endpoint: "/api/preparation/result" },
            { key: 'done', name: "Done", result: "Preparation Phase Done!", endpoint: "/api/preparation/done" }
        ]
    },
    {
        key: 'ideaCreation',
        name: "Idea Creation",
        title: "Idea Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Idea Creation", endpoint: "/api/idea_creation/start" },
            { key: 'work', name: "Work", result: "Work Done!", endpoint: "/api/idea_creation/work" },
            { key: 'done', name: "Done", result: "Idea Creation Phase Done!", endpoint: "/api/idea_creation/done" }
        ]
    },
    {
        key: 'companyCreation',
        name: "Company Creation",
        title: "Company Creation Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Company Creation", endpoint: "/api/company_creation/start" },
            { key: 'work', name: "Work", result: "Work Done!", endpoint: "/api/idea_creation/work" },
            { key: 'done', name: "Done", result: "Company Creation Phase Done!", endpoint: "/api/company_creation/done" }
        ]
    },
    {
        key: 'designing',
        name: "Designing",
        title: "Designing Phase",

        stages: [
            { key: 'start', name: "Start", result: "Start Designing", endpoint: "/api/designing/start" },
            { key: 'work', name: "Work", result: "Work Done!", endpoint: "/api/idea_creation/work" },
            { key: 'done', name: "Done", result: "Designing Phase Done!", endpoint: "/api/designing/done" }
        ]
    },
    {
        key: 'coding',
        name: "Coding",
        title: "Coding Phase",

        stages: [
            { key: 'start', name: "Start", result: "Start Coding", endpoint: "/api/coding/start" },
            { key: 'work', name: "Work", result: "Work Done!", endpoint: "/api/idea_creation/work" },
            { key: 'done', name: "Done", result: "Coding Phase Done!", endpoint: "/api/coding/done" }
        ]
    },
    {
        key: 'testing',
        name: "Testing",
        title: "Testing Phase",

        stages: [
            { key: 'start', name: "Start", result: "Start Testing", endpoint: "/api/testing/start" },
            { key: 'work', name: "Work", result: "Work Done!", endpoint: "/api/idea_creation/work" },
            { key: 'done', name: "Done", result: "Testing Phase Done!", endpoint: "/api/testing/done" }
        ]
    },
    {
        key: 'documenting',
        name: "Documenting",
        title: "Documenting Phase",

        stages: [
            { key: 'start', name: "Start", result: "Start Documenting", endpoint: "/api/documenting/start" },
            { key: 'work', name: "Work", result: "Work Done!", endpoint: "/api/idea_creation/work" },
            { key: 'done', name: "Done", result: "Documenting Phase Done!", endpoint: "/api/documenting/done" }
        ]
    },
    {
        key: 'done',
        name: "Done",
        title: "Done Phase",
        stages: [
            { key: 'start', name: "Start", result: "Start Final Phase", endpoint: "/api/done/start" },
            { key: 'download', name: "download", result: "Download the project!", endpoint: "/api/done/download" },
            { key: 'done', name: "Done", result: "Project Creation Done!", endpoint: "/api/done/done" }
        ]
    },
];