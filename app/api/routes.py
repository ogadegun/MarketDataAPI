"""
API route definitions
"""
from fastapi import APIRouter, HTTPException
from app.core.database import get_db_connection
from app.models.schemas import TickerListResponse, TickerInfo, ErrorResponse

router = APIRouter(prefix="/api/v1", tags=["market-data"])


@router.get(
    "/tickers",
    response_model=TickerListResponse,
    summary="List all available tickers",
    description="Get a list of all available stock tickers with metadata including record counts and date ranges"
)
async def list_tickers():
    """
    Returns all available tickers with:
    - Total number of records per ticker
    - Date range of available data (earliest and latest)
    
    This endpoint queries the market_data table and aggregates information
    by ticker symbol.
    """
    query = """
    SELECT 
        ticker,
        COUNT(*) as total_records,
        MIN(date) as earliest_date,
        MAX(date) as latest_date
    FROM market_data
    GROUP BY ticker
    ORDER BY ticker
    """
    
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
                
                tickers = [
                    TickerInfo(
                        ticker=row['ticker'],
                        total_records=row['total_records'],
                        earliest_date=row['earliest_date'],
                        latest_date=row['latest_date']
                    )
                    for row in results
                ]
                
                return TickerListResponse(
                    total_tickers=len(tickers),
                    tickers=tickers
                )
                
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


@router.get(
    "/health",
    summary="Health check",
    description="Check if API is running and database is accessible"
)
async def health_check():
    """
    Simple health check endpoint
    
    Returns service status and verifies database connectivity
    """
    try:
        # Test database connection
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        
        return {
            "status": "healthy",
            "service": "market-data-api",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Service unhealthy: {str(e)}"
        )