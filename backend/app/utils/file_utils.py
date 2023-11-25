import re
from app.utils.project_utils import get_project_folder_path_util
from typing import List, Dict
import json
import os

async def save_conversation_to_file_util(project_id: int, chat_name: str, conversation: List[Dict]):
    try:
        # Get the project folder path
        folder_path = await get_project_folder_path_util(project_id)

        # Create the 'logs' directory if it does not exist
        logs_folder_path = os.path.join(folder_path, "logs")
        if not os.path.exists(logs_folder_path):
            os.makedirs(logs_folder_path)
        
        # Format the file name
        json_name = chat_name.replace('-', '_').lower()
        file_name = f"logs_chat_messages_{json_name}.json"
        
        # Define the complete file path
        conversation_file_path = os.path.join(logs_folder_path, file_name)

        # Save the conversation to a JSON file
        with open(conversation_file_path, 'w') as file:
            json.dump(conversation, file, indent=4)
        
        return True
    except Exception as e:
        # Handle any exceptions (logging, custom error handling, etc.)
        print(f"Error saving conversation to file: {e}")
        return False

async def save_markdown_to_file_util(project_id: int, base_file_name: str, output_content):
    try:
        # Get the project folder path
        folder_path = await get_project_folder_path_util(project_id)
        
        # Format the file name
        markdown_name = f"{base_file_name}.md"
        
        # Define the complete file path
        conversation_file_path = os.path.join(folder_path, markdown_name)

        with open(conversation_file_path, 'w') as file:
            file.write(output_content)
    except Exception as e:
        # Handle any exceptions (logging, custom error handling, etc.)
        print(f"Error saving markdown to file: {e}")
        return False

async def save_code_to_file_util(project_id: int, base_file_name: str, output_content):
    try:
        # Get the project folder path
        folder_path = await get_project_folder_path_util(project_id)

        # Define code type patterns
        code_patterns = {
            'py': r"```python\s+(.*?)\s+```",
            'html': r"```html\s+(.*?)\s+```",
            'css': r"```css\s+(.*?)\s+```",
            'js': r"```js\s+(.*?)\s+```",
            'txt': r"```txt\s+(.*?)\s+```",
            # Add other code types here
        }

        file_counter = 1

        # Iterate through code types
        for code_type, pattern in code_patterns.items():
            for match in re.finditer(pattern, output_content, re.DOTALL):
                code_content = match.group(1)

                # Format the file name with the correct extension and counter
                file_name_with_extension = f"{base_file_name}_{file_counter}.{code_type}"

                # Define the complete file path
                file_path = os.path.join(folder_path, file_name_with_extension)

                # Save the code content to a file
                with open(file_path, 'w') as file:
                    file.write(code_content)

                file_counter += 1

        if file_counter == 1:
            # If no code pattern matches, handle it as plain text or error
            raise ValueError("No recognized code pattern found in the content.")

    except Exception as e:
        # Handle any exceptions (logging, custom error handling, etc.)
        print(f"Error saving code to file: {e}")
        return False