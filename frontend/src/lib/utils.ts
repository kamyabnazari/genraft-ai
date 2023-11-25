export const phases = [
    {
        key: "assistants-creation",
        name: "Assistants Creation",
        title: "Assistants Creation Phase",
        stages: [
            {
                key: "start",
                name: "Start",
                successResult: "Assistants Creation Phase Started",
                errorResult: "Error in Starting Assistants Creation Phase",
                updatesProject: false
            },
            {
                key: 'assistant-stakeholder',
                name: "Stakeholder Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-stakeholder",
                    assistant_type: "stakeholder",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: 'assistant-consultant',
                name: "Consultant Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-consultant",
                    assistant_type: "consultant",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-ceo",
                name: "CEO Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-ceo",
                    assistant_type: "ceo",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-cto",
                name: "CTO Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-cto",
                    assistant_type: "cto",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-programmer",
                name: "Programmer Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-programmer",
                    assistant_type: "programmer",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-designer",
                name: "Designer Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-designer",
                    assistant_type: "designer",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-reviewer",
                name: "Reviewer Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-reviewer",
                    assistant_type: "reviewer",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-tester",
                name: "Tester Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-tester",
                    assistant_type: "tester",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-technical-writer",
                name: "Technical Writer Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-technical-writer",
                    assistant_type: "technical-writer",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "assistant-user-documentation",
                name: "User Documentation Assistant",
                successResult: "Assistant Created",
                errorResult: "Error in Creating Assistant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/assistants/create-assistant",
                method: "POST",
                body: {
                    assistant_name: "project-{id}-assistant-user-documentation",
                    assistant_type: "user-documentation",
                    assistant_model: "gpt-3.5-turbo"
                }
            },
            {
                key: "done",
                name: "Done",
                successResult: "Assistants Creation Phase Completed",
                errorResult: "Error in Completing Assistants Creation Phase",
                updatesProject: false
            }
        ]
    },
    {
        key: 'designing',
        name: "Designing",
        title: "Designing Phase",
        stages: [
            {
                key: 'start',
                name: "Start",
                successResult: "Designing Phase Started",
                errorResult: "Error in Starting Designing Phase",
                updatesProject: false
            },
            {
                key: 'idea-initial',
                name: "Initial Idea",
                successResult: "{project.idea_initial}",
                errorResult: "Error in Getting Initial Idea",
                updatesProject: true
            },
            {
                key: 'chat-stakeholder-and-consultant',
                name: "Chat Stakeholder and Consultant",
                successResult: "Chat Ended Successfully!",
                errorResult: "Error in Starting Chat with Stakeholder and Consultant",
                updatesProject: false,
                endpoint: "/api/projects/{id}/chats/create-chat",
                method: "POST",
                body: {
                    chat_name: "project-{id}-chat-stakeholder-and-consultant",
                    chat_assistant_primary: "project-{id}-assistant-stakeholder",
                    chat_assistant_secondary: "project-{id}-assistant-consultant"
                }
            },
            {
                key: 'idea-final',
                name: "Final Idea",
                successResult: "{project.idea_final}",
                errorResult: "Error in Creating Final Idea",
                updatesProject: true
            },
            {
                key: "chat-ceo-and-cto",
                name: "Chat CEO and CTO",
                successResult: "Chat Ended Successfully!",
                errorResult: "Error in Starting Chat with CEO and CTO",
                updatesProject: false,
                endpoint: "/api/projects/{id}/chats/create-chat",
                method: "POST",
                body: {
                    chat_name: "project-{id}-chat-ceo-and-cto",
                    chat_assistant_primary: "project-{id}-assistant-ceo",
                    chat_assistant_secondary: "project-{id}-assistant-cto"
                }
            },
            {
                key: 'technical-plan',
                name: "Technical Plan",
                successResult: "{project.technical_plan}",
                errorResult: "Error in Getting Technical Plan",
                updatesProject: true
            },
            {
                key: 'done',
                name: "Done",
                successResult: "Designing Phase Completed",
                errorResult: "Error in Completing Designing Phase",
                updatesProject: false
            }
        ]
    },
    {
        key: 'coding',
        name: "Coding",
        title: "Coding Phase",
        stages: [
            {
                key: 'start',
                name: "Start", successResult: "Coding Phase Started",
                errorResult: "Error in Starting Coding Phase",
                updatesProject: false
            },
            {
                key: "chat-cto-and-programmer",
                name: "Chat CTO and Programmer",
                successResult: "Chat Ended Successfully!",
                errorResult: "Error in Starting Chat with CTO and Programmer",
                updatesProject: false,
                endpoint: "/api/projects/{id}/chats/create-chat",
                method: "POST",
                body: {
                    chat_name: "project-{id}-chat-cto-and-programmer",
                    chat_assistant_primary: "project-{id}-assistant-cto",
                    chat_assistant_secondary: "project-{id}-assistant-programmer"
                }
            },
            {
                key: "chat-programmer-and-designer",
                name: "Chat Programmer and Designer",
                successResult: "Chat Ended Successfully!",
                errorResult: "Error in Starting Chat with Programmer and Designer",
                updatesProject: false,
                endpoint: "/api/projects/{id}/chats/create-chat",
                method: "POST",
                body: {
                    chat_name: "project-{id}-chat-programmer-and-designer",
                    chat_assistant_primary: "project-{id}-assistant-programmer",
                    chat_assistant_secondary: "project-{id}-assistant-designer"
                }
            },
            {
                key: 'done',
                name: "Done",
                successResult: "Coding Phase Completed",
                errorResult: "Error in Completing Coding Phase",
                updatesProject: false
            }
        ]
    },
    {
        key: 'testing',
        name: "Testing",
        title: "Testing Phase",
        stages: [
            {
                key: 'start', name: "Start",
                successResult: "Testing Phase Started",
                errorResult: "Error in Starting Testing Phase",
                updatesProject: false
            },
            {
                key: 'done',
                name: "Done",
                successResult: "Testing Phase Completed",
                errorResult: "Error in Completing Testing Phase",
                updatesProject: false
            }
        ]
    },
    {
        key: 'documenting',
        name: "Documenting",
        title: "Documenting Phase",
        stages: [
            {
                key: 'start',
                name: "Start",
                successResult: "Documenting Phase Started",
                errorResult: "Error in Starting Documenting Phase",
                updatesProject: false
            },
            {
                key: 'done',
                name: "Done",
                successResult: "Documenting Phase Completed",
                errorResult: "Error in Completing Documenting Phase",
                updatesProject: false
            }
        ]
    },
    {
        key: 'project-completion',
        name: "Project Completion",
        title: "Project Completion Phase",
        stages: [
            {
                key: 'start',
                name: "Start",
                successResult: "Project Completion Phase Started",
                errorResult: "Error in Starting Project Completion Phase",
                updatesProject: false
            },
            {
                key: 'done',
                name: "Done",
                successResult: "Project Completion Phase Completed",
                errorResult: "Error in Completing Project Completion Phase",
                updatesProject: false
            }
        ]
    },
];
