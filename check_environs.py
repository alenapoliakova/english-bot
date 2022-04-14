from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
BOT_NAME = env("BOT_NAME")
BOT_CONTAINER_NAME = env("BOT_CONTAINER_NAME")
ADMIN = env("ADMIN")
