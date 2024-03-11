import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 24172165))

    API_HASH = os.environ.get("API_HASH", "b8075104a36275bf855e10b26b08ed2c")
