from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "local"

    BOT_TOKEN: str
    # DISCORD_BOT_TOKEN: str = None
    # DISCORD_CDN_CHAT_ID: int = None

    DATABASE_HOST: str = "localhost"
    DATABASE_USER: str = "sample_tg_bot_app"
    DATABASE_PASSWORD: str = "sample_tg_bot_app"
    DATABASE_NAME: str = "sample_tg_bot_app"
    DATABASE_PORT: int = 5432

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}"
            f":{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

    @property
    def LOCAL(self) -> bool:
        return self.ENVIRONMENT == "local"




settings = Settings()
