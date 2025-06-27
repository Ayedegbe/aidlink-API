# 📦 AidLink API

_A RESTful API for managing disaster relief supplies, locations, and resource requests._

---

## 🌍 Overview

AidLink is a backend system built with **FastAPI** to support relief logistics. It provides RESTful endpoints for managing:
- **Supplies** – items available for distribution
- **Locations** – areas that need aid
- **Requests** – supply needs from each location

Includes a simple frontend for quick input via HTML/JavaScript.

---

## 🚀 Getting Started

### ✅ Requirements
- Python 3.9+
- pip

### 📦 Installation

```bash
git clone <repo-url>
cd aidlink_api
pip install -r requirements.txt
```

### ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Visit the app:

- **Frontend**: [http://localhost:8000](http://localhost:8000)
- **Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📁 Project Structure

```
aidlink_api/
├── main.py              # FastAPI backend with all routes
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── frontend/
    └── index.html       # Basic frontend interface
```

---

## 🧠 API Endpoints

### 📦 Supplies

| Method | Endpoint       | Description           |
|--------|----------------|-----------------------|
| GET    | `/supplies`    | List all supplies     |
| POST   | `/supplies`    | Add a new supply      |

**POST /supplies** Example:
```json
{
  "name": "Water Bottles",
  "quantity": 100,
  "unit": "litres"
}
```

---

### 📍 Locations

| Method | Endpoint        | Description         |
|--------|-----------------|---------------------|
| GET    | `/locations`    | List all locations  |
| POST   | `/locations`    | Add a new location  |

**POST /locations** Example:
```json
{
  "name": "Kano",
  "region": "Northwest"
}
```

---

### 🛎️ Requests

| Method | Endpoint       | Description                  |
|--------|----------------|------------------------------|
| POST   | `/requests`    | Create a new supply request  |

**POST /requests** Example:
```json
{
  "locationId": 1,
  "supplyName": "Blankets",
  "quantity": 50
}
```

---

## ⚠️ Error Handling Examples

| Scenario                      | Code | Response                          |
|-------------------------------|------|-----------------------------------|
| Missing field                 | 422  | FastAPI validation error          |
| Location not found            | 404  | `{ "detail": "Location not found" }` |

---

## 🧪 Testing

You can use:
- Swagger UI (`/docs`) to test interactively
- Postman (optional) — export from Swagger

---

## 🧠 Powered By

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Vanilla HTML/JS

---

## 📌 Notes

- CORS enabled: browser-based JS can access the API.
- In-memory data store used for simplicity — no database setup required.
