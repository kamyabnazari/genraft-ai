export const phases = [
    {
        key: 'idea-creation',
        name: "Idea Creation",
        title: "Idea Creation Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Idea Creation Phase Started",
                errorResult: "Error in Starting Idea Creation Phase", updatesProject: false
            },
            {
                key: 'idea-initial', name: "Initial Idea", successResult: "Initial Idea Retrieved: {project.idea_initial}",
                errorResult: "Error in Getting Initial Idea", updatesProject: true
            },
            {
                key: 'assistant-stakeholder', name: "Stakeholder Assistant", successResult: "Stakeholder Assistant Created",
                errorResult: "Error in Creating Stakeholder Assistant", updatesProject: false, endpoint: "/api/projects/{id}/assistants/create-assistant", method: "POST",
                "body": {
                    "assistant_name": "project-{id}-assistant-stakeholder",
                    "assistant_type": "stakeholder",
                    "assistant_instructions": "You play the role of a stakeholder, you have an initial idea that you want to be created. You goal is to talk with your employees about your initial idea and give answares to their questions.",
                    "assistant_model": "gpt-3.5-turbo"
                }
            },
            {
                key: 'assistant-consultant', name: "Consultant Assistant", successResult: "Consultant Assistant Created",
                errorResult: "Error in Creating Consultant Assistant", updatesProject: false, endpoint: "/api/projects/{id}/assistants/create-assistant", method: "POST",
                "body": {
                    "assistant_name": "project-{id}-assistant-consultant",
                    "assistant_type": "consultant",
                    "assistant_instructions": "You play the role of an idea consultant that helps stakeholder in the creation of a detailed project from a short one. You help the stakeholder with his/her initial idea. try to lead the conversation and not ask the same question multiple time.",
                    "assistant_model": "gpt-3.5-turbo"
                }
            },
            {
                key: 'chat-stakeholder-and-consultant', name: "Chat Stakeholder and Consultant", successResult: "Chat Ended Successfully!",
                errorResult: "Error in Starting Chat with Stakeholder and Consultant", updatesProject: false, endpoint: "/api/projects/{id}/chats/create-chat", method: "POST",
                "body": {
                    "chat_name": "project-{id}-chat-stakeholder-and-consultant",
                    "chat_assistant_primary": "project-{id}-assistant-stakeholder",
                    "chat_assistant_secondary": "project-{id}-assistant-consultant",
                    "chat_goal": "The objective is to collaboratively refine and expand the initial project idea into a detailed and actionable project concept, focusing exclusively on the idea's development. Discussions should center on elaborating the idea's specifics, potential features, while avoiding unrelated business or operational topics and even technical details, this should be very much surface level details."
                }
            },
            {
                key: 'idea-final', name: "Final Idea", successResult: "Final Idea Created: {project.idea_final}",
                errorResult: "Error in Creating Final Idea", updatesProject: true
            },
            {
                key: 'done', name: "Done", successResult: "Idea Creation Phase Completed",
                errorResult: "Error in Completing Idea Creation Phase", updatesProject: false
            }
        ]
    },
    {
        key: 'company-creation',
        name: "Company Creation",
        title: "Company Creation Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Company Creation Phase Started",
                errorResult: "Error in Starting Company Creation Phase", updatesProject: false
            },
            {
                key: 'goal-setting', name: "Goal Setting", successResult: "Goal Setting Started",
                errorResult: "Error in Starting Goal Setting", updatesProject: false, endpoint: "/api/projects/{id}/company-creation/goal-setting", method: "POST", "body": {}
            },
            {
                key: 'role-definition', name: "Role Definition", successResult: "Role Definition Started",
                errorResult: "Error in Starting Role Definition", updatesProject: false, endpoint: "/api/projects/{id}/company-creation/role-definition", method: "POST", "body": {}
            },
            {
                key: 'done', name: "Done", successResult: "Company Creation Phase Completed",
                errorResult: "Error in Completing Company Creation Phase", updatesProject: false
            }
        ]
    },
    {
        key: 'designing',
        name: "Designing",
        title: "Designing Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Designing Phase Started",
                errorResult: "Error in Starting Designing Phase", updatesProject: false
            },
            {
                key: 'product-specification', name: "Product Specification", successResult: "Product Specification Started",
                errorResult: "Error in Starting Product Specification", updatesProject: false, endpoint: "/api/projects/{id}/designing/product-specification", method: "POST", "body": {}
            },
            {
                key: 'prototype-development', name: "Prototype Development", successResult: "Prototype Development Started",
                errorResult: "Error in Starting Prototype Development", updatesProject: false, endpoint: "/api/projects/{id}/designing/prototype-development", method: "POST", "body": {}
            },
            {
                key: 'done', name: "Done", successResult: "Designing Phase Completed",
                errorResult: "Error in Completing Designing Phase", updatesProject: false
            }
        ]
    },
    {
        key: 'coding',
        name: "Coding",
        title: "Coding Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Coding Phase Started",
                errorResult: "Error in Starting Coding Phase", updatesProject: false
            },
            {
                key: 'implementation', name: "Implementation", successResult: "Implementation Started",
                errorResult: "Error in Starting Implementation", updatesProject: false, endpoint: "/api/projects/{id}/coding/implementation", method: "POST", "body": {}
            },
            {
                key: 'ui-design', name: "UI Design", successResult: "UI Design Started",
                errorResult: "Error in Starting UI Design", updatesProject: false, endpoint: "/api/projects/{id}/coding/ui-design", method: "POST", "body": {}
            },
            {
                key: 'done', name: "Done", successResult: "Coding Phase Completed",
                errorResult: "Error in Completing Coding Phase", updatesProject: false
            }
        ]
    },
    {
        key: 'testing',
        name: "Testing",
        title: "Testing Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Testing Phase Started",
                errorResult: "Error in Starting Testing Phase", updatesProject: false
            },
            {
                key: 'code-review', name: "Code Review", successResult: "Code Review Started",
                errorResult: "Error in Starting Code Review", updatesProject: false, endpoint: "/api/projects/{id}/testing/code-review", method: "POST", "body": {}
            },
            {
                key: 'quality-assurance', name: "Quality Assurance", successResult: "Quality Assurance Started",
                errorResult: "Error in Starting Quality Assurance", updatesProject: false, endpoint: "/api/projects/{id}/testing/quality-assurance", method: "POST", "body": {}
            },
            {
                key: 'done', name: "Done", successResult: "Testing Phase Completed",
                errorResult: "Error in Completing Testing Phase", updatesProject: false
            }
        ]
    },
    {
        key: 'documenting',
        name: "Documenting",
        title: "Documenting Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Documenting Phase Started",
                errorResult: "Error in Starting Documenting Phase", updatesProject: false
            },
            {
                key: 'technical-writing', name: "Technical Writing", successResult: "Technical Writing Started",
                errorResult: "Error in Starting Technical Writing", updatesProject: false, endpoint: "/api/projects/{id}/documenting/technical-writing", method: "POST", "body": {}
            },
            {
                key: 'user-guides', name: "User Guides", successResult: "User Guides Started",
                errorResult: "Error in Starting User Guides", updatesProject: false, endpoint: "/api/projects/{id}/documenting/user-guides", method: "POST", "body": {}
            },
            {
                key: 'done', name: "Done", successResult: "Documenting Phase Completed",
                errorResult: "Error in Completing Documenting Phase", updatesProject: false
            }
        ]
    },
    {
        key: 'project-completion',
        name: "Project Completion",
        title: "Project Completion Phase",
        stages: [
            {
                key: 'start', name: "Start", successResult: "Project Completion Phase Started",
                errorResult: "Error in Starting Project Completion Phase", updatesProject: false
            },
            {
                key: 'final-review', name: "Final Review", successResult: "Final Review Started",
                errorResult: "Error in Starting Final Review", updatesProject: false, endpoint: "/api/projects/{id}/project-completion/final-review", method: "POST", "body": {}
            },
            {
                key: 'project-download', name: "Project Download", successResult: "Project Download Started",
                errorResult: "Error in Starting Project Download", updatesProject: false, endpoint: "/api/projects/{id}/project-completion/project-download", method: "POST", "body": {}
            },
            {
                key: 'done', name: "Done", successResult: "Project Completion Phase Completed",
                errorResult: "Error in Completing Project Completion Phase", updatesProject: false
            }
        ]
    },
];
