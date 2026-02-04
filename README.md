\# Market Data REST API



FastAPI-based REST API for accessing historical stock market data stored in PostgreSQL.




FastAPI - Modern Python web framework

PostgreSQL - Database (AWS RDS)

Pydantic - Data validation

uvicorn - ASGI server



\## Setup



\### Prerequisites

\- Python 3.12+

\- PostgreSQL database with market data



\### Installation



1\. Clone the repository

```bash

git clone <your-repo-url>

cd market-data-api

```



2\. Create virtual environment

```bash

python -m venv venv

venv\\Scripts\\activate  # Windows

```



3\. Install dependencies

```bash

pip install -r requirements.txt

```



4\. Configure environment

```bash

cp .env.example .env

\# Edit .env with your database credentials

```



\### Running Locally

```bash

uvicorn app.main:app --reload

```



API will be available at: http://localhost:8000



Interactive API docs: http://localhost:8000/docs



\## API Endpoints



\### `GET /api/v1/tickers`

List all available stock tickers with metadata



\*\*Response:\*\*

```json

{

&nbsp; "total\_tickers": 50,

&nbsp; "tickers": \[

&nbsp;   {

&nbsp;     "ticker": "AAPL",

&nbsp;     "total\_records": 1500,

&nbsp;     "earliest\_date": "2025-11-03",

&nbsp;     "latest\_date": "2025-11-07"

&nbsp;   }

&nbsp; ]

}

```



\### `GET /health`

Health check endpoint



\*\*Response:\*\*

```json

{

&nbsp; "status": "healthy",

&nbsp; "service": "market-data-api",

&nbsp; "database": "connected"

}

```

\## Project Context



This API layer sits on top of an existing market data pipeline that ingests data from Financial Modeling Prep API and stores it in PostgreSQL (AWS RDS). The API provides standardized REST endpoints for querying this data.



\## Architecture

```

\[Market Data Pipeline] → \[PostgreSQL Database] ← \[FastAPI] → \[Clients]

```



\- \*\*Pipeline\*\*: Fetches and validates data from FMP API

\- \*\*Database\*\*: Stores 86,000+ market data records

\- \*\*API\*\*: Exposes data through REST endpoints



