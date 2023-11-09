from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@patch("openai.Completion.create")
def test_generate_message(mock_completion_create):
    # Setup the mock return value for the `Completion.create` method
    mock_completion_create.return_value = Mock(choices=[Mock(text="Bonjour, comment ça va?")])
    
    # Define a sample prompt to send in the request
    sample_prompt = {
        "prompt": "Translate the following English text to French: 'Hello, how are you?'"
    }
    
    # Make a POST request to the /generate_message endpoint with the prompt
    response = client.post("/api/generate_message", json=sample_prompt)
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200, response.text
