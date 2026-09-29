from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.8-flash"
    request_timeout_seconds: int = 60
    use_local_explanation: bool = False
    local_explanation_model: str = "MBZUAI/LaMini-Flan-T5-783M"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def has_gemini(self) -> bool:
        return bool(self.gemini_api_key.strip())


settings = Settings()