# Backend

## Setup

### Environment variables

Create a `.env` file in the root of the backend directory with the following variables:

```
OPENAI_API_KEY={your openai api key}
PUBLIC_FRONTEND_URL=http://genraft-ai-frontend:3000
```

### Running the backend

To install the required packages for this service, run the following commands:

```
pip install -r requirements.txt
```

To run this service, run the following commands:

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 5003
```

### Testing the backend

To test this service, run the following commands:

```
pytest
```

To test this service without warnings, run the following commands:

```
pytest -p no:warnings
```
