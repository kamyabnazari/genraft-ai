chat_config = {
    "stakeholder_consultant": {
        "end_protocol": "<END_SC>",
        "output_format_start": "<START_FINAL_IDEA_SC>",
        "output_format_end": "<END_FINAL_IDEA_SC>",
        "initial_message_chat_1": "The goal of this conversation is: {chat_goal}. Here is my initial project idea: {idea_initial}. Please keep the conversation concise. Enclose your final idea within <FINAL_IDEA_SC>...</FINAL_IDEA_SC>, and mark the final sentence with <END_SC> to conclude the chat.",
        "initial_message_chat_2": "The goal of this conversation is: {chat_goal}. This was your initial idea: {idea_initial}. Here was my first response to your initial idea: {response_from_secondary}. Please respond concisely to my response."
    },
    "programmer_cto": {
        "end_protocol": "<END_PC>",
        "output_format_start": "<START_CODE_PC>",
        "output_format_end": "<END_CODE_PC>",
        "initial_message_chat_1": "The goal of this coding discussion is: {chat_goal}. Please provide your initial code snippet and keep the discussion focused. Enclose your final code within <CODE_PC>...</CODE_PC>, and mark the final line with <END_PC> to conclude the chat.",
        "initial_message_chat_2": "The goal of this coding discussion is: {chat_goal}. Here is the initial code snippet you provided: {idea_initial}. Here was my feedback: {response_from_secondary}. Please make the necessary changes to the code, and keep your response concise."
    }
}