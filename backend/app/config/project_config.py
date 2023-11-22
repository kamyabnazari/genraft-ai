project_config = {
    "global_properties": {
        "max_exchanges": 5,
        "output_format_start": "[START]",
        "output_format_end": "[END]",
        "tech_scope": "Focus on Python, HTML, CSS, JavaScript, and web technologies only."
    },
    "chats": {
        "stakeholder_consultant": {
            "chat_goal": "The objective is to collaboratively refine and expand the initial project idea into a detailed project idea, focusing exclusively on the idea's details. Discussions should center on elaborating the idea's specifics, potential features, while avoiding unrelated business or operational topics and even technical details, this should be very much surface level details.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Here is my initial project idea: {idea_initial}. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. This was your initial idea: {idea_initial}. Please keep the conversation concise. Enclose only the concise final idea within {output_format_start}...{output_format_end}, without additional commentary. If a conclusion is not reached within {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your message: {response_from_secondary}. Please respond concisely to my response."
        },
        "stakeholder_ceo": {
            "chat_goal": "The objective is to set company goals and align them with the detailed product idea to create a comprehensive company goals description.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Here is the final project idea: {idea_final}. Let's discuss this to create a comprehensive company goals description. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. We are discussing the final project idea: {idea_final}. Based on this, let’s refine our company's direction. Enclose the final company goals within {output_format_start}...{output_format_end}. Please limit exchanges to a maximum of {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your message: {response_from_secondary}. Please respond concisely to my response."
        },
        "ceo_cpo": {
            "chat_goal": "Develop product design specifications and UX strategy in Markdown format, based on company goals and detailed product idea.",
            "initial_message_chat_1": "Tech Scope: {tech_scope}. The goal of this conversation is: {chat_goal}. Inputs: {company_goal} and {idea_final}. Limit to {max_exchanges} messages.",
            "initial_message_chat_2": "Focus: {tech_scope}. The goal of this conversation is: {chat_goal}. Develop a plan in Markdown format detailing UX strategy and design specifications. Consider {company_goal} and {idea_final}. Enclose your detailed plan within {output_format_start}...{output_format_end}. Limit to {max_exchanges} messages. Here was my first response to your message: {response_from_secondary}. Please respond concisely to my response."
        },
        "ceo_cto": {
            "chat_goal": "Produce a detailed plan in Markdown format addressing technical challenges, architecture, and integration strategies, aligned with the product idea and company goals.",
            "initial_message_chat_1": "Tech Scope: {tech_scope}. The goal of this conversation is: {chat_goal}. Our conversation aims to produce a detailed plan in Markdown format on technical architecture and integration strategies. Inputs: {company_goal}, {idea_final}. Limit to {max_exchanges} messages.",
            "initial_message_chat_2": "Tech Scope: {tech_scope}. The goal of this conversation is: {chat_goal}. We're creating a detailed plan in Markdown format for our architecture and tech stack. Consider {company_goal} and {idea_final}. Enclose the plan within {output_format_start}...{output_format_end}. Limit to {max_exchanges} messages. Here was my first response to your message: {response_from_secondary}. Please respond concisely to my response."
        }
    },
    "assistants": {
        "stakeholder": {
            "instructions": "You play the role of a Stakeholder, your role involves presenting and discussing your initial idea."
        },
        "consultant": {
            "instructions": "You play the role of a Consultant, assist in refining and elaborating the project idea."
        },
        "ceo": {
            "instructions": "You play the role of a CEO, focus on setting the strategic direction."
        },
        "cpo": {
            "instructions": "You play the role of a CPO, oversee the product design and user experience strategy."
        },
        "cto": {
            "instructions": "You play the role of a CTO, your primary focus is on the technical architecture, technology stack, and integration of technologies. Collaborate effectively with other team members, particularly the CEO and CPO, to ensure technical decisions align with the overall product strategy and company goals."
        },
        "programmer": {
            "instructions": "You play the role of a Programmer, your role is to turn technical specifications into executable code."
        },
        "designer": {
            "instructions": "You play the role of a Designer, focus on creating visual assets."
        },
        "reviewer": {
            "instructions": "You play the role of a Reviewer, provide feedback on code quality and performance."
        },
        "tester": {
            "instructions": "You play the role of a Tester, conduct various tests to ensure software quality."
        },
        "technical-writer": {
            "instructions": "You play the role of a Technical Writer, create detailed documentation."
        },
        "user-documentation": {
            "instructions": "You play the role of a User Documentation Specialist, focus on end-user manuals and guides."
        }
    }
}