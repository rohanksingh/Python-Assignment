from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	NUM_PROCESSES: int = 4

	class config:
		env_file= ".env"

settings= Settings()