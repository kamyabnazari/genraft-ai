chat_config = {
    "global_properties": {
        "tech_scope": "Focus on Python, HTML, CSS, JavaScript, and web technologies only.",
        "max_exchanges": 5
    },
    "chats": {
        "stakeholder_consultant": {
            "output_format_start": "[START]",
            "output_format_end": "[END]",
            "initial_message_chat_1": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. Here is my initial project idea: {idea_initial}. Please keep the conversation concise and limit exchanges to a maximum of {max_exchanges} messages per participant.",
            "initial_message_chat_2": "The Tech Scope is: {tech_scope}. The goal of this conversation is: {chat_goal}. This was your initial idea: {idea_initial}. Please keep the conversation concise. Enclose only the concise final idea within {output_format_start}...{output_format_end}, without additional commentary. If a conclusion is not reached within {max_exchanges} exchanges each, summarize the discussion and provide a provisional final idea. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
        }
    }
}
