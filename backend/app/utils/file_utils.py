import re
from app.utils.project_utils import get_project_folder_path_util
from typing import List, Dict
import json
import os

async def save_conversation_to_file_util(project_id: int, chat_name: str, conversation: List[Dict]):
    try:
        # Get the project folder path
        folder_path = await get_project_folder_path_util(project_id)
        
        # Format the file name
        json_name = chat_name.replace('-', '_').lower()
        file_name = f"logs_chat_messages_{json_name}.json"
        
        # Define the complete file path
        conversation_file_path = os.path.join(folder_path, file_name)

        # Save the conversation to a JSON file
        with open(conversation_file_path, 'w') as file:
            json.dump(conversation, file, indent=4)
        
        return True
    except Exception as e:
        # Handle any exceptions (logging, custom error handling, etc.)
        print(f"Error saving conversation to file: {e}")
        return False

async def save_markdown_to_file_util(project_id: int, chat_name: str, markdown_content):
    try:
        # Get the project folder path
        folder_path = await get_project_folder_path_util(project_id)
        
        # Format the file name
        markdown_name = f"{chat_name}_output.md"
        
        # Define the complete file path
        conversation_file_path = os.path.join(folder_path, markdown_name)

        with open(conversation_file_path, 'w') as file:
            file.write(markdown_content)
    except Exception as e:
        # Handle any exceptions (logging, custom error handling, etc.)
        print(f"Error saving markdown to file: {e}")
        return False

async def save_python_to_file_util(project_id: int, chat_name: str, output_content):
    try:
        # Extract Python code from the markdown content
        match = re.search(r"```python\s+(.*?)\s+```", output_content, re.DOTALL)
        if match:
            python_content = match.group(1)
        else:
            print("No Python code block found.")
            return False
        
        # Get the project folder path
        folder_path = await get_project_folder_path_util(project_id)
        
        # Format the file name
        python_name = f"{chat_name}_code.py"
        
        # Define the complete file path
        conversation_file_path = os.path.join(folder_path, python_name)

        with open(conversation_file_path, 'w') as file:
            file.write(python_content)
    except Exception as e:
        # Handle any exceptions (logging, custom error handling, etc.)
        print(f"Error saving markdown to file: {e}")
        return False