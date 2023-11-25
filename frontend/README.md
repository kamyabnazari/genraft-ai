# Frontend

## Setup

### Environment variables

Create a `.env` file in the root of the frontend directory with the following variables:

```
PRIVATE_BACKEND_URL=http://localhost:5003
PUBLIC_SECURE=true // if testing on safari or firefox, set to false
PUBLIC_HTTPONLY=false
PUBLIC_SAMESITE=None
BODY_SIZE_LIMIT=0
```

### Install packages for the frontend

```
npm install
```

### Running the frontend in dev mode

```
npm run dev
```

### Building the project

To create a production version of your app:

```
npm run build
```

You can preview the production build with `npm run preview`.

### Test the frontend

```
npm test
```