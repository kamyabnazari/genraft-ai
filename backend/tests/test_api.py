import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestGenerateMessage(unittest.TestCase):

    @patch('openai.OpenAI.chat.completions')
    def test_generate_message(self, mock_chat_completion_create):
        # Setup the mock return value
        mocked_content = "Generated message from OpenAI."
        mock_chat_completion_create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content=mocked_content))]
        )

        sample_prompt = {
            "prompt": "Translate the following English text to French: 'Hello, how are you?'"
        }

        response = client.post("/api/generate_message", json=sample_prompt)

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": mocked_content})

if __name__ == '__main__':
    unittest.main()