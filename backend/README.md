# Deriv AI Decision Assistant - Backend

Python FastAPI backend for market analysis using Gemini AI.

## Project Structure

```
backend/
├── main.py                 # FastAPI app entry point
├── routes/                 # API route handlers
│   ├── health.py          # Health check endpoint
│   └── analyze.py         # Market analysis endpoint
├── clients/               # External service clients
│   └── gemini_client.py   # Gemini LLM API client (singleton, async)
├── auxiliary/             # Helper logic
│   └── analyze_logic.py   # Business logic for routes
└── pyproject.toml         # Project dependencies
```

## Setup

1. **Install dependencies:**

   ```bash
   pip install -e .
   ```

2. **Configure environment:**

   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Run the server:**
   ```bash
   python main.py
   # or
   uvicorn main:app --reload
   ```

Server runs on `http://localhost:8000`

## API Endpoints

### Health Check

- **GET** `/` - Server health status

### Analyze

- **POST** `/analyze` - Analyze market data with Gemini insights

  Request body:

  ```json
  {
    "data": [
      { "price": 100, "volume": 1000, "timestamp": "2024-01-01" },
      { "price": 101, "volume": 1100, "timestamp": "2024-01-02" }
    ],
    "market_symbol": "AAPL",
    "analysis_type": "summary"
  }
  ```

## Features

- ✅ FastAPI with async support
- ✅ Pandas DataFrame processing
- ✅ Gemini API integration (reusable singleton client)
- ✅ Request/response validation with Pydantic
- ✅ CORS enabled
- ✅ Environment variable configuration
