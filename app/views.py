from flask import Blueprint, request, jsonify, render_template
from .assistants import create_assistant, create_thread, add_message_to_thread, run_assistant, get_assistant_response

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/ask', methods=['POST'])
def ask():
    # Extract the user's question from request data
    user_message = request.json.get('prompt', '')

    # Logic to interact with the assistant
    # For example, create a thread, add a message, run the assistant, and get a response
    assistant = create_assistant()
    thread = create_thread()
    add_message_to_thread(thread.id, user_message)
    run = run_assistant(thread.id, assistant.id)
    response = get_assistant_response(thread.id, run.id)

    if response:
        print(response)
        print(response.json())
        return jsonify(response), 200
    else:
        return jsonify({"error": "Assistant is still processing the request."}), 202