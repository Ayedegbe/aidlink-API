# AidLink API

AidLink is a RESTful API for tracking disaster relief resources like food, water, and medical supplies across various affected locations.

## Features

- Add and view relief supplies
- Add and view locations
- Create resource requests from locations
- Auto-generated Swagger docs at `/docs`

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the server:

```bash
uvicorn main:app --reload
```

3. Visit the Swagger UI at:

```
http://localhost:8000/docs
```

## Endpoints Overview

| Method | Endpoint      | Description            |
|--------|---------------|------------------------|
| GET    | /supplies     | List all supplies      |
| POST   | /supplies     | Add a new supply       |
| GET    | /locations    | List all locations     |
| POST   | /locations    | Add a new location     |
| POST   | /requests     | Create a new request   |

## Error Handling

Returns informative HTTP errors, such as:

- `400` for missing data
- `404` if location not found
