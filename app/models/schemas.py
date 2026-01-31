"""
Pydantic models for request/response validation
These define the API's data contracts
"""
from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class TickerInfo(BaseModel):
    """Basic ticker information with metadata"""
    ticker: str
    total_records: int
    earliest_date: Optional[date]
    latest_date: Optional[date]


class TickerListResponse(BaseModel):
    """Response for listing all tickers"""
    total_tickers: int
    tickers: List[TickerInfo]


class ErrorResponse(BaseModel):
    """Standard error response"""
    error: str
    detail: Optional[str] = None