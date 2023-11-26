project_config = {
    "global_properties": {
        "max_exchanges": 5,
        "chat_end": "<END_CHAT>",
        "tech_scope": "Concentrate on web development with Flask for backend and HTML, CSS, and JavaScript with Flask templates for the frontend. No use of additional frameworks, dbs, clouds, platforms or technologies outside this stack.",
        "output_format_instructions": "Please respond in a clear, third-person format. Start directly with the content, avoiding first-person statements or lead-in phrases. The response should consist only of the specific, essential details necessary for the task, with no additional commentary or explanatory text."
    },
    "chats": {
        "stakeholder_consultant": {
            "chat_goal": "Focus on detailing the project concept, emphasizing the use of Flask for backend and HTML/CSS/JS with Flask templates for the frontend.",
            "initial_message_chat_1": "Tech Scope: {tech_scope}. Goal: {chat_goal}. help me refine my project idea and its concept. Initial idea: {idea_initial}. Keep exchanges concise. Limit: {max_exchanges} messages each.",
            "initial_message_chat_2": "Tech Scope: {tech_scope}. Goal: {chat_goal}. Your initial idea: {idea_initial}. Keep the conversation concise. If you agree with the final idea, signify the end with {chat_end}. Limit: {max_exchanges} messages each. Respond concisely to: {response_from_secondary}.",
            "output_request": "Provide a detailed summary of the refined project concept, focusing on key features and implementation strategies."
        },
        "ceo_cto": {
            "chat_goal": "Implement the project's technical specifications using Flask for the backend and HTML/CSS/JS with Flask templates for the frontend. No talk about other technologies and frameworks, only the product features.",
            "initial_message_chat_1": "Goal: {chat_goal}. List all project features give details for each. Here is the project idea: {idea_final}. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Exchange thoughts on the feature list and confirm if they align with project Idea. Consider the project idea: {idea_final}. If you agree with the plan, signify the end with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Provide the comprehensive technical plan of all features with clear specifications so developers can use."
        },
        "cto_programmer": {
            "chat_goal": "Translate the technical plan into executable code, focusing on implementing full-stack features with pure HTML/CSS/JS for the frontend and Flask for the backend. Only generate one file for each type.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Implement features as per the technical plan. Input: {technical_plan}, {tech_scope}. Focus on feature implementation. Consolidate all HTML code into a single file index.html, all CSS into another called style.css, and so on like script.js and app.py. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Here is the technical plan, please ensure that I as the developer create correct implementation, you act as a supervisor. Input: {technical_plan}. Ensure my code quality and adherence to specifications. Finalize with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Provide completed final code for the assigned features that is executable, ensuring compliance with the technical specifications and best coding practices. Consolidate all HTML code into a single file, all CSS into another, and so on. Use comments to indicate sections or features, e.g., `/* Start of Feature X CSS */`."
        },
        "programmer_tester": {
            "chat_goal": "Test the application's functionality, focusing on the integration of Flask backend and the frontend built with HTML/CSS/JS and Flask templates.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Test the software functionality and performance. Focus on unit, integration, and system testing. Input: Source code: {source_code} . Technical plan: {technical_plan}. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Ensure the software's functionality and optimization. Input: Source code. Your task is to conduct testing and report findings. Conclude with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Change the code if needed so the application functions as is intended, provide a completed final code."
        },
        "cto_technical-writer": {
            "chat_goal": "Create technical documentation that covers the use of Flask for backend and HTML/CSS/JS with Flask templates for the frontend.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Compile technical documentation. Input: Source code: {source_code}. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Collaborate to create technical documentation. Input: Technical specifications: {technical_plan} and source code: {source_code}. Confirm completion with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Produce technical documentation, code documentation for the provided source code in Markdown Format just as text and dont file."
        },
        "ceo_user-documentation": {
            "chat_goal": "Develop end-user documentation that explains the use and functionality of the Flask backend and HTML/CSS/JS frontend.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Create end-user manuals and guides in Markdown Format. Input: code: {source_code} and technical plan {technical_plan}, UX/UI design details, and user interface prototypes. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Help to align the user manual to the created source code. Finalize with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Generate end-user documentation including user manuals, how-to guides, FAQs in Markdown Format just as text and dont file."
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
            "instructions": "As a CEO, aligning them with both the project's technical aspects and the projects idea and goal."
        },
        "cto": {
            "instructions": "As a CTO, focus on technical features specifications, collaborating with the CEO and Programmers to align technical decisions with product goals."
        },
        "programmer": {
            "instructions": "As a Programmer, translate technical specifications into executable code, focusing on functionality and efficiency."
        },
        "tester": {
            "instructions": "As a Tester, conduct rigorous tests to ensure software quality, usability, and reliability."
        },
        "technical-writer": {
            "instructions": "As a Technical Writer, your can create required project specific files like requirements.txt or package.json and more for other software systems."
        },
        "user-documentation": {
            "instructions": "As a User Documentation Specialist, develop clear and concise end-user manuals and guides, enhancing user understanding and engagement."
        }
    }
}
