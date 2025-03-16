import re
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#---------------------------------------------------------------
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '26553080'))  # Replace with your API ID
API_HASH = environ.get('API_HASH', 'bfc2a72e9d69e8dc5675bd9370e4f437')
BOT_TOKEN = environ.get('BOT_TOKEN', '6960970165:AAHGGZa6utChpUmOdQLqvkatt6NijD-pf20')
#---------------------------------------------------------------

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5733833742').split()]
USERNAME = environ.get('USERNAME', "https://t.me/Nightfuries_007")  # Replace with your Telegram username
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002353120423'))  # Replace with your log channel ID
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+8uYM2yGw4BA4MmY1')

CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001224814913').split()]
#---------------------------------------------------------------

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Nighty007:AAdmin2025@cluster0.dr0dx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Movies')
#---------------------------------------------------------------

LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '0'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', '0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))

auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '0')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/your_support_chat')
#---------------------------------------------------------------

IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'True'), True)

SHORTENER_API = environ.get("SHORTENER_API", "72c7c135d638aad02a8927a98000cfbcbf3ba9aa")  # Updated API Key
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'example.com')

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]
QUALITIES = ["HdRip", "web-dl", "bluray", "hdr", "fhd", "720p", "1080p", "4k"]
YEARS = [f'{i}' for i in range(2024, 2002, -1)]
SEASONS = [f'season {i}' for i in range(1, 23)]

AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled(environ.get('AUTO_FILTER', 'True'), True)
IS_PM_SEARCH = is_enabled(environ.get('IS_PM_SEARCH', 'False'), False)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', 'True'), True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))

IMDB = is_enabled(environ.get('IMDB', 'False'), False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled(environ.get('LONG_IMDB_DESCRIPTION', 'False'), False)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', 'False'), False)
SPELL_CHECK = is_enabled(environ.get('SPELL_CHECK', 'True'), True)
LINK_MODE = is_enabled(environ.get('LINK_MODE', 'True'), True)

STREAM_MODE = bool(environ.get('STREAM_MODE', True))  # Set True or False
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False

URL = environ.get("FQDN", "")

SETTINGS = {
    'spell_check': SPELL_CHECK,
    'auto_filter': AUTO_FILTER,
    'file_secure': PROTECT_CONTENT,
    'auto_delete': AUTO_DELETE,
    'template': IMDB_TEMPLATE,
    'caption': FILE_CAPTION,
    'tutorial': TUTORIAL,
    'shortner': SHORTENER_WEBSITE,
    'api': SHORTENER_API,
    'log': LOG_VR_CHANNEL,
    'imdb': IMDB,
    'link': LINK_MODE,
    'is_verify': IS_VERIFY,
    'verify_time': TWO_VERIFY_GAP,
}
