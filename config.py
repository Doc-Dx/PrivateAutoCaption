# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "@Mo_Tech_YT @Mo_Tech_Group")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
