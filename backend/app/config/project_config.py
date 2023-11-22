project_config = {
    "global_properties": {
        "max_exchanges": 5,
        "chat_end": "<END_CHAT>",
        "tech_scope": "Focus on Python, HTML, CSS, JavaScript, and web technologies only.",
        "output_format_instructions": "Please respond in a clear, third-person format. Start directly with the content, avoiding first-person statements or lead-in phrases. The response should consist only of the specific, essential details necessary for the task, with no additional commentary or explanatory text."
    },
    "chats": {
        "stakeholder_consultant": {
            "chat_goal": "Collaboratively refine and detail the initial project concept, focusing on specific features and implementation strategies.",
            "initial_message_chat_1": "Tech Scope: {tech_scope}. Goal: {chat_goal}. Initial idea: {idea_initial}. Keep exchanges concise. Limit: {max_exchanges} messages each.",
            "initial_message_chat_2": "Tech Scope: {tech_scope}. Goal: {chat_goal}. Your initial idea: {idea_initial}. Keep the conversation concise. If you agree with the final idea, signify the end with {chat_end}. Limit: {max_exchanges} messages each. Respond concisely to: {response_from_secondary}.",
            "output_request": "Provide a detailed summary of the refined project concept, focusing on key features and implementation strategies."
        },
        "stakeholder_ceo": {
            "chat_goal": "Align the project's vision with strategic goals to form a cohesive project direction.",
            "initial_message_chat_1": "Goal: {chat_goal}. Final project idea: {idea_final}. Discuss to create a comprehensive company goals description. Limit: {max_exchanges} messages each.",
            "initial_message_chat_2": "Goal: {chat_goal}. Discussing final project idea: {idea_final}. Refine company goals. If you agree with the final goals, signify the end with {chat_end}. Limit: {max_exchanges} messages each. Respond to: {response_from_secondary}.",
            "output_request": "Provide a concise statement aligning the project vision with strategic goals, detailing how the project integrates with broader objectives."
        },
        "ceo_cpo": {
            "chat_goal": "Develop detailed product design and UX strategy, ensuring alignment with the project's vision and goals.",
            "initial_message_chat_1": "Goal: {chat_goal}. Inputs: {company_goal}, {idea_final}. Develop a plan in Markdown. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Develop UX strategy and design specs in Markdown. Consider {company_goal}, {idea_final}. If satisfied with the plan, signify the end with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Outline the product design and UX strategy, emphasizing essential design elements and user experience considerations in relation to the project's vision."
        },
        "ceo_cto": {
            "chat_goal": "Formulate a comprehensive technical plan covering architecture, technology stack, and integration strategies.",
            "initial_message_chat_1": "Goal: {chat_goal}. Produce a detailed technical plan. Inputs: {company_goal}, {idea_final}. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Detail architecture and tech stack in Markdown. Consider {company_goal}, {idea_final}. If you agree with the plan, signify the end with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Provide a comprehensive technical plan, focusing on architecture, technology stack, and integration strategies with clear technical specifics."
        }
    },
    "assistants": {
        "stakeholder": {
            "instructions": "As a Stakeholder, present and discuss your initial idea, focusing on its viability and alignment with business objectives."
        },
        "consultant": {
            "instructions": "As a Consultant, refine and elaborate the project idea, providing insights on feasibility and potential improvements."
        },
        "ceo": {
            "instructions": "As a CEO, set strategic directions, aligning them with both the project's technical aspects and the company's broader goals."
        },
        "cpo": {
            "instructions": "As a CPO, lead product design and UX strategy, ensuring they align with company goals and user needs."
        },
        "cto": {
            "instructions": "As a CTO, focus on technical architecture and integration strategies, collaborating with the CEO and CPO to align technical decisions with product and company goals."
        },
        "programmer": {
            "instructions": "As a Programmer, translate technical specifications into executable code, focusing on functionality and efficiency."
        },
        "designer": {
            "instructions": "As a Designer, create compelling visual assets that enhance user experience and align with the product's branding."
        },
        "reviewer": {
            "instructions": "As a Reviewer, evaluate code quality and performance, providing constructive feedback for improvements."
        },
        "tester": {
            "instructions": "As a Tester, conduct rigorous tests to ensure software quality, usability, and reliability."
        },
        "technical-writer": {
            "instructions": "As a Technical Writer, create detailed documentation that accurately represents the software's functionality and usage."
        },
        "user-documentation": {
            "instructions": "As a User Documentation Specialist, develop clear and concise end-user manuals and guides, enhancing user understanding and engagement."
        }
    }
}