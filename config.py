import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6699672036:AAGxv6YrRdoAdUItfJ2AVtJOydtH8mAfXd4")

    APP_ID = int(os.environ.get("APP_ID", 26281496))

    API_HASH = os.environ.get("API_HASH", "a9b8db3efd4be04118d0391f124982c7")
