class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "21715744"
    API_HASH = "cfc3fb8746f3659aa7707eb19c0487de"

    CASH_API_KEY = "101UHM3PVG8QQUIS"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001873246625"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Vishnuofficial:Vishnuofficialvp@cluster0.sqsph7w.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "vpvpofficial"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5925859471:AAEZ5vaZSEGw6K3U3P788SqK4yK_o6zCj0I"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "TNN59Z47QBCS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "2090221565"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
