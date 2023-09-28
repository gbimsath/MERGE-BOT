import os


class Config(object):
    API_HASH = os.environ.get("ea8263e0393b6c06d4cf83ca6c5014ad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TELEGRAM_API = os.environ["8657438"]
    OWNER = os.environ.get("1404096450")
    OWNER_USERNAME = os.environ.get("bimzath")
    PASSWORD = os.environ.get("bimzath@000")
    DATABASE_URL = os.environ.get("mongodb+srv://bimzathx:deshx@deshx.vojtx48.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001962430444")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
