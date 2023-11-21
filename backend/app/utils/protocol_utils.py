chat_config = {
    "global_properties": {
        "tech_scope": "Focus on Python, HTML, CSS, JavaScript, and web technologies only.",
        "max_exchanges": 5
    },
    "chats": {
        "stakeholder_consultant": {
            "output_format_start": "[START]",
            "output_format_end": "[END]",
            "chat_goal": "The objective is to collaboratively refine and expand the initial project idea into a detailed project idea, focusing exclusively on the idea's details. Discussions should center on elaborating the idea's specifics, potential features, while avoiding unrelated business or operational topics and even technical details, this should be very much surface level details.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Here is my initial project idea: {idea_initial}. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. This was your initial idea: {idea_initial}. Please keep the conversation concise. Enclose only the concise final idea within {output_format_start}...{output_format_end}, without additional commentary. If a conclusion is not reached within {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
        },
        "stakeholder_ceo": {
            "output_format_start": "[START]",
            "output_format_end": "[END]",
            "chat_goal": "The objective is to set company goals and align them with the detailed product idea to create a comprehensive company goals description.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Here is the final project idea: {idea_final}. Let's discuss this to create a comprehensive company goals description. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. We are discussing the final project idea: {idea_final}. Based on this, let’s refine our company's direction. Enclose the final company goals within {output_format_start}...{output_format_end}. Please limit exchanges to a maximum of {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
        },
        "ceo_coo": {
            "output_format_start": "[START]",
            "output_format_end": "[END]",
            "chat_goal": "The objective is to discuss and define the operational strategy, resource allocation, and create new job roles, ensuring alignment with the company goals.",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Our discussion, based on the final idea: {idea_final} and company goals: {company_goal}, should focus on operational strategy, resource allocation, and creating new job roles. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. With our final idea: {idea_final} and company goals: {company_goal} in mind, let’s define our operational strategy and discuss resource allocation and new job roles. Enclose the final operational strategy and job roles within {output_format_start}...{output_format_end}. Please limit exchanges to a maximum of {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
        }
    }
}