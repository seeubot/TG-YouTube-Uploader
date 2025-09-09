import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7599815904:AAHWE869Ic4IQOpk9j6wF6aL8WFvix_L-n0")

    APP_ID = int(os.environ.get("APP_ID", 23054736))

    API_HASH = os.environ.get("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://t.me/PredatorHackerzZ_bot")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://t.me/PredatorHackerzZ_bot")
