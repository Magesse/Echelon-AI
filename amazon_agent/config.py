import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

# Çıktı klasörünü güvenli bir şekilde oluştur
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class Settings(BaseSettings):
    # API Keys (SecretStr kullanımı loglarda sızmasını engeller)
    tavily_api_key: SecretStr
    gemini_api_key: SecretStr
    groq_api_key: SecretStr
    
    # Araştırma Limitleri
    max_research_results: int = 8
    max_competitor_pages: int = 5
    max_review_count: int = 20
    request_timeout: int = 15
    
    # Model İsimleri
    groq_model: str = "llama-3.3-70b-versatile"
    gemini_model: str = "gemini-2.5-flash"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

try:
    settings = Settings()
except Exception as e:
    raise EnvironmentError(f"Yapılandırma hatası! Lütfen .env dosyanızı kontrol edin:\n{e}")