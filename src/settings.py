from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    BOT_NAME: str

    class Config:
        env_file = '../.env'


config = Settings()
