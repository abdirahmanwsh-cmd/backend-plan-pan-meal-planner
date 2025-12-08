# FitPlate API

A FastAPI backend for meal planning and management with PostgreSQL database.

## Live Deployment

🚀 **API is live on Render:**
- **Base URL:** https://backend-plan-pan-meal-planner.onrender.com/
- **API Documentation:** https://backend-plan-pan-meal-planner.onrender.com/docs
- **Alternative Docs:** https://backend-plan-pan-meal-planner.onrender.com/redoc
- **Frontend repo:** https://github.com/abdirahmanwsh-cmd/frontend-plan-pan-meal-planner
## Features

- User authentication with Firebase
- Meal CRUD operations (Create, Read, Update, Delete)
- Meal planning functionality
- PostgreSQL database for persistent storage
- Interactive API documentation (Swagger UI)

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Server:** Gunicorn + Uvicorn
- **Authentication:** Firebase Admin SDK
- **Hosting:** Render

## Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL
- pip

### Setup

1. Clone the repository:
```bash
git clone <repo-url>
cd backend-plan-pan-meal-planner
```

2. Create and activate virtual environment:
```bash
python -m venv plateplan
source plateplan/bin/activate  # On Windows: plateplan\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your DATABASE_URL and Firebase credentials
```

5. Run locally:
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs to see the API documentation.

## API Endpoints

### Root
- `GET /` - Health check

### Meals
- `GET /meals` - List all meals
- `POST /meals` - Create a new meal
- `GET /meals/{meal_id}` - Get meal by ID
- `PUT /meals/{meal_id}` - Update a meal
- `DELETE /meals/{meal_id}` - Delete a meal

### Auth
- `GET /auth/me` - Get current user (requires authentication)

### Plans
- `GET /plans` - List all meal plans
- `POST /plans` - Create a new plan
- `GET /plans/{plan_id}` - Get plan by ID
- `PUT /plans/{plan_id}` - Update a plan

## Deployment

This project is deployed on **Render** with:
- Docker containerization (see `Dockerfile`)
- Managed PostgreSQL database
- Auto-deploy on git push to `dev` branch

### Deploy Configuration Files
- `Dockerfile` - Container image definition
- `render.yaml` - Render deployment manifest
- `docker-compose.yml` - Local Docker Compose setup

## Environment Variables

Required for production:
- `DATABASE_URL` - PostgreSQL connection string (auto-set by Render Postgres plugin)
- `FIREBASE_SERVICE_ACCOUNT_JSON` - Firebase service account credentials (JSON string)

## License

MIT
