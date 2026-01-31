"""
Configuration management using environment variables
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings loaded from environment variables"""
    
    def __init__(self):
        # Database
        self.database_url = os.getenv('DATABASE_URL')
        
        # API Metadata
        self.api_title = os.getenv('API_TITLE', 'Market Data API')
        self.api_version = os.getenv('API_VERSION', '1.0.0')
        self.api_description = os.getenv(
            'API_DESCRIPTION', 
            'REST API for accessing historical stock market data'
        )


# Create a single instance
_settings = None

def get_settings() -> Settings:
    """Get settings instance"""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings