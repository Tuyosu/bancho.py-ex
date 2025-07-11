from __future__ import annotations

import os
import tomllib
from urllib.parse import quote

from dotenv import load_dotenv

from app.settings_utils import read_bool
from app.settings_utils import read_list

load_dotenv()

APP_HOST = os.environ["APP_HOST"]
APP_PORT = int(os.environ["APP_PORT"])

DB_HOST = os.environ["DB_HOST"]
DB_PORT = int(os.environ["DB_PORT"])
DB_USER = os.environ["DB_USER"]
DB_PASS = quote(os.environ["DB_PASS"])
DB_NAME = os.environ["DB_NAME"]
DB_DSN = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])
REDIS_USER = os.environ["REDIS_USER"]
REDIS_PASS = quote(os.environ["REDIS_PASS"])
REDIS_DB = int(os.environ["REDIS_DB"])

# ext
LOCAL_HOST = os.environ["LOCAL_HOST"]
ENABLE_PUBSUBS = read_bool(os.environ["ENABLE_PUBSUBS"])
FIRST_PLACES_WEBHOOK = os.environ["FIRST_PLACES_WEBHOOK"]
ENABLE_FIRST_PLACES_WEBHOOK = read_bool(os.environ["ENABLE_FIRST_PLACES_WEBHOOK"])
DISCORD_URL = os.environ["DISCORD_URL"]
SERVER_NAME = os.environ["SERVER_NAME"]
DISCORD_BEATMAP_UPDATES_WEBHOOK=os.environ["DISCORD_BEATMAP_UPDATES_WEBHOOK"]

DISALLOW_INGAME_RESTRICTION = read_bool(os.environ["DISALLOW_INGAME_RESTRICTION"])
DISALLOW_INGAME_REGISTRATION = read_bool(os.environ["DISALLOW_INGAME_REGISTRATION"])

# irc
ENABLE_IRC = read_bool(os.environ["ENABLE_IRC"])
IRC_HOST = os.environ["IRC_HOST"]
IRC_PORT = int(os.environ["IRC_PORT"])

ENABLE_PROMETHEUS= read_bool(os.environ["ENABLE_PROMETHEUS"])
PROMETHEUS_PORT = int(os.environ["PROMETHEUS_PORT"])


REDIS_AUTH_STRING = f"{REDIS_USER}:{REDIS_PASS}@" if REDIS_USER and REDIS_PASS else ""
REDIS_DSN = f"redis://{REDIS_AUTH_STRING}{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

OSU_API_KEY = os.environ.get("OSU_API_KEY") or None
OSU_API_CLIENT_ID = int(os.environ["OSU_API_CLIENT_ID"])
OSU_API_CLIENT_SECRET = os.environ["OSU_API_CLIENT_SECRET"]
OSU_DAILY_API_KEY = os.environ.get("OSU_DAILY_API_KEY") or None

DOMAIN = os.environ["DOMAIN"]
MIRROR_SEARCH_ENDPOINT = os.environ["MIRROR_SEARCH_ENDPOINT"]
MIRROR_DOWNLOAD_ENDPOINT = os.environ["MIRROR_DOWNLOAD_ENDPOINT"]

COMMAND_PREFIX = os.environ["COMMAND_PREFIX"]

SEASONAL_BGS = read_list(os.environ["SEASONAL_BGS"])

MENU_ICON_URL = os.environ["MENU_ICON_URL"]
MENU_ONCLICK_URL = os.environ["MENU_ONCLICK_URL"]

DATADOG_API_KEY = os.environ["DATADOG_API_KEY"]
DATADOG_APP_KEY = os.environ["DATADOG_APP_KEY"]

DEBUG = read_bool(os.environ["DEBUG"])
REDIRECT_OSU_URLS = read_bool(os.environ["REDIRECT_OSU_URLS"])

PP_CACHED_ACCURACIES = [int(acc) for acc in read_list(os.environ["PP_CACHED_ACCS"])]

DISALLOWED_NAMES = read_list(os.environ["DISALLOWED_NAMES"])
DISALLOWED_PASSWORDS = read_list(os.environ["DISALLOWED_PASSWORDS"])
DISALLOW_OLD_CLIENTS = read_bool(os.environ["DISALLOW_OLD_CLIENTS"])

DISCORD_AUDIT_LOG_WEBHOOK = os.environ["DISCORD_AUDIT_LOG_WEBHOOK"]

AUTOMATICALLY_REPORT_PROBLEMS = read_bool(os.environ["AUTOMATICALLY_REPORT_PROBLEMS"])

LOG_WITH_COLORS = read_bool(os.environ["LOG_WITH_COLORS"])

# advanced dev settings

## WARNING touch this once you've
##          read through what it enables.
##          you could put your server at risk.
DEVELOPER_MODE = read_bool(os.environ["DEVELOPER_MODE"])

with open("pyproject.toml", "rb") as f:
    VERSION = tomllib.load(f)["tool"]["poetry"]["version"]
