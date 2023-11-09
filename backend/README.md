# Backend

## Setup

### Environment variables

Create a `.env` file in the root of the backend directory with the following variables:

```
OPENAI_API_KEY={your openai api key}
PUBLIC_FRONTEND_URL=http://genraft-ai-frontend:3000
RUNNING_TESTS=false // if you want to run tests set to true
```

### Running the backend

To install the required packages for this plugin and run the service locally, run the following commands:

```
pip install -r requirements.txt

uvicorn main:app --reload --host 0.0.0.0 --port 5003
```
