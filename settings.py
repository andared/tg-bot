from environs import Env
from dotenv import load_dotenv


load_dotenv()
env = Env()


class Settings:
    BOT_TOKEN = env.str("BOT_TOKEN")
    ADMIN_ID = env.int("ADMIN_ID")
    WEBHOOK_TOKEN = env.str("WEBHOOK_TOKEN")
    ADMIN_PASSWORD = env.str("ADMIN_PASSWORD")
    IS_PRODUCTION = env.bool("IS_PRODUCTION", False)
    LOG_BOT_TOKEN = env.str("LOG_BOT_TOKEN", "")
    HOST = env.str("HOST", "")
