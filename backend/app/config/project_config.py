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
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. This was your initial idea: {idea_initial}. Please keep the conversation concise. Enclose only the concise final idea within {output_format_start}...{output_format_end}, without additional commentary. If a conclusion is not reached within {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
        },
        "stakeholder_ceo": {
            "chat_goal": "The objective is to set company goals and align them with the detailed product idea to create a comprehensive company goals description.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Here is the final project idea: {idea_final}. Let's discuss this to create a comprehensive company goals description. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. We are discussing the final project idea: {idea_final}. Based on this, let’s refine our company's direction. Enclose the final company goals within {output_format_start}...{output_format_end}. Please limit exchanges to a maximum of {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
        },
        "ceo_cpo": {
            "chat_goal": "The objective is to develop product design specifications and UX strategy, based on the company goals and detailed product idea.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. We need to discuss and create a plan for product design specifications and UX strategy. Input includes: {company_goal} and {idea_final}. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Let's focus on developing a coherent UX strategy and design specifications that align with our company goals: {company_goal} and the detailed idea: {idea_final}. Enclose the final design plan within {output_format_start}...{output_format_end}. Limit exchanges to {max_exchanges} messages per participant."
        },
        "ceo_cto": {
            "chat_goal": "The objective is to address technical challenges, decide on architecture, and integration with existing technologies, aligning with the detailed product idea and company goals.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Our focus is on addressing technical challenges and deciding on the architecture. Input: {company_goal} and {idea_final}. Please keep the conversation concise, limiting to {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. We need to align our architecture and tech stack with the company goals: {company_goal} and our product idea: {idea_final}. Enclose key technical decisions within {output_format_start}...{output_format_end}, keeping the exchange within {max_exchanges} messages."
        }
    },
    "assistants": {
        "stakeholder": {
            "instructions": "As a Stakeholder, your role involves presenting and discussing your initial idea. Ensure your communication is clear, using {output_format_start}...{output_format_end} for key points, and keep exchanges within {max_exchanges}."
        },
        "consultant": {
            "instructions": "As a Consultant, assist in refining and elaborating the project idea. Lead the conversation effectively, using {output_format_start}...{output_format_end} for clarity, and limit exchanges to {max_exchanges}."
        },
        "ceo": {
            "instructions": "As a CEO, focus on setting the strategic direction. Make sure to enclose important decisions within {output_format_start}...{output_format_end} and limit exchanges in a thread to {max_exchanges}."
        },
        "cpo": {
            "instructions": "As a CPO, oversee the product design and user experience strategy. Use {output_format_start}...{output_format_end} to highlight key design decisions and stay within {max_exchanges} exchanges."
        },
        "cto": {
            "instructions": "As a CTO, your primary focus is on the technical architecture, technology stack, and integration of technologies. Collaborate effectively with other team members, particularly the CEO and CPO, to ensure technical decisions align with the overall product strategy and company goals. Enclose key technical details and decisions within {output_format_start}...{output_format_end} to highlight them, and keep your exchanges within the limit of {max_exchanges} messages per conversation to maintain clarity and efficiency."
        },
        "programmer": {
            "instructions": "As a Programmer, your role is to turn technical specifications into executable code. Enclose code-related discussions within {output_format_start}...{output_format_end} and keep exchanges under {max_exchanges}."
        },
        "designer": {
            "instructions": "As a Designer, focus on creating visual assets. Use {output_format_start}...{output_format_end} to frame key design elements and limit exchanges to {max_exchanges}."
        },
        "reviewer": {
            "instructions": "As a Reviewer, provide feedback on code quality and performance. Highlight feedback within {output_format_start}...{output_format_end} and keep exchanges within {max_exchanges}."
        },
        "tester": {
            "instructions": "As a Tester, conduct various tests to ensure software quality. Document test findings using {output_format_start}...{output_format_end} and limit exchanges to {max_exchanges}."
        },
        "technical-writer": {
            "instructions": "As a Technical Writer, create detailed documentation. Enclose key documentation aspects within {output_format_start}...{output_format_end} and limit exchanges to {max_exchanges}."
        },
        "user-documentation": {
            "instructions": "As a User Documentation Specialist, focus on end-user manuals and guides. Use {output_format_start}...{output_format_end} for essential user instructions, limiting exchanges to {max_exchanges}."
        }
    }
}