from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file if present
load_dotenv()

# Get OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Ensure the OpenAI API key is available
if not openai.api_key:
    raise ValueError("No OPENAI_API_KEY set for Flask application")

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    # Call the OpenAI API with the prompt
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or the engine you wish to use
            prompt=prompt,
            max_tokens=150
        )
        return jsonify(response), 200
    except openai.error.OpenAIError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
