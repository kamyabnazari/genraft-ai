project_config = {
    "global_properties": {
        "max_exchanges": 5,
        "chat_end": "<END_CHAT>",
        "tech_scope": "Concentrate on web development with Flask for backend and HTML, CSS, and JavaScript with Flask templates for the frontend. No use of additional frameworks and do not talk about deployments, platforms or technologies outside this stack.",
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
            "chat_goal": "Translate the technical plan into executable code, generating files for each segment: HTML, CSS, JavaScript, and Flask.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Implement features as per the technical plan. Input: {technical_plan}, {tech_scope}. Focus on feature implementation. Consolidate all HTML code into a single file index.html, all CSS into another called style.css, and so on like script.js and app.py. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Here is the technical plan, please ensure that I as the developer create correct implementation, you act as a supervisor. Input: {technical_plan}. Ensure my code quality and adherence to specifications. Finalize with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Generate separate files for each part of the code: index.html for HTML, style.css for CSS, script.js for JavaScript, and app.py for Flask."
        },
        "programmer_tester": {
            "chat_goal": "Write unit tests for the source code provided.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Test the software functionality and performance. Focus on unit, integration, and system testing. Input: Source code: {source_code} . Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Ensure the software's functionality and optimization. Technical plan: {technical_plan}. Your task is to conduct testing and report findings. Conclude with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Test the code and organize it into the correct file formats. Any modifications should be made directly in the respective files."
        },
        "cto_technical-writer": {
            "chat_goal": "Create technical documentation in one large Markdown file, covering all aspects of the Flask backend and frontend.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Compile technical documentation. Input: Source code: {source_code}. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Collaborate to create technical documentation. Input: Technical specifications: {technical_plan} and source code: {source_code}. Confirm completion with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Generate technical documentation in one large Markdown file, detailing source code and architecture."
        },
        "ceo_user-documentation": {
            "chat_goal": "Develop end-user documentation as one large file, explaining the Flask backend and frontend.",
            "initial_message_chat_1": "Goal: {chat_goal}. Task: Create end-user manual and guide as one large Markdown file. Input: code: {source_code} and technical plan {technical_plan}, UX/UI design details, and user interface prototypes. Limit: {max_exchanges} messages.",
            "initial_message_chat_2": "Goal: {chat_goal}. Help to align the user manual to the created source code. Finalize with {chat_end}. Limit: {max_exchanges} messages. Respond to: {response_from_secondary}.",
            "output_request": "Create end-user manual, guide, and FAQs as one large Markdown file."
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
            "instructions": "As a Programmer, translate technical specifications into executable code. You create and generate code files as your responses."
        },
        "tester": {
            "instructions": "As a Tester, conduct tests to ensure software quality, usability, and reliability. Your task is to generate/create test files."
        },
        "technical-writer": {
            "instructions": "As a Technical Writer, your create required technical documentation file for the project."
        },
        "user-documentation": {
            "instructions": "As a User Documentation Specialist, develop clear and concise end-user manuals and guide, enhancing user understanding and engagement."
        }
    }
}
