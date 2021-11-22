from starlette.config import Config

config = Config(".env")

CREDENTIALS_PATH: str = config("CREDENTIALS_PATH")
TIMETABLE_PATH: str = config("TIMETABLE_PATH")
