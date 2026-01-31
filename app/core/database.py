"""
Database connection management
"""
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from typing import Generator
from .config import get_settings

settings = get_settings()


@contextmanager
def get_db_connection() -> Generator:
    """
    Context manager for database connections
    Automatically handles connection opening and closing
    
    Usage:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM market_data")
    """
    conn = None
    try:
        conn = psycopg2.connect(
            settings.database_url,
            cursor_factory=RealDictCursor  # Returns results as dictionaries
        )
        yield conn
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()