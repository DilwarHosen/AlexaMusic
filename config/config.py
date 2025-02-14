# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
Alexa is a Telegram Audio and video streaming bot
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23710378"))
API_HASH = getenv("API_HASH", "a5ebe1fd8ae5715a9eb2a9364001189a")

BOT_TOKEN = getenv("BOT_TOKEN", "5963562690:AAF5v58Y_0nBw_VW41cQGzS4EGH695-gcfA")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001603822916"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Alone")

OWNER_ID = int(getenv("OWNER_ID", "7552579717"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DilwarHosen/AlexaMusic")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneXBots")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+1iN6Tuz0-atmODI1")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "900"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", None)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

COOKIES = getenv("COOKIES", "# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	TRUE	1751130644	NID	520=bXHoWBsVZxOPzdVqPHOUBCI7M_M28KOn2cf42zSSnHDb-cslzrEogNvx9wnQ6GyVTO7lr_XRptaona_HH8273sjMUtRcsE9t2W94xsrRAJaha5c9eG0jRJXVgyrshC0iqBCMWpCcVz-olGNJonE8GOhxlBHPxjEcew-wLSVZ6HT4YwvtSX7CeCo9ftrpxxha0xqhaoH2eERZGZlGE7P6y7INg9hRE5EfVMCFJs4VtGQKlqdtcOhgu8VbSRR_vPlpDnk
.youtube.com	TRUE	/	TRUE	1774066141	PREF	tz=Asia.Calcutta&f7=100
.youtube.com	TRUE	/	FALSE	1773905277	SID	g.a000tQh7qDc7vIBjkhh8HwRVQ6CNw1eAyqS3oSfUQzr-uP16BIe7lr0razv287QBNqy0JUONugACgYKAR4SARQSFQHGX2MiPGEOu8v716-FzdJfDssFpBoVAUF8yKq5XrDsiFB2sDDNuNEy29_F0076
.youtube.com	TRUE	/	TRUE	1770881277	__Secure-1PSIDTS	sidts-CjIBEJ3XVzuPka4UUL39btCc0cylGuY9c6SsEmcMp6nJFvrk5dKdkXbPsTPEA41TJ_g-JRAA
.youtube.com	TRUE	/	TRUE	1770881277	__Secure-3PSIDTS	sidts-CjIBEJ3XVzuPka4UUL39btCc0cylGuY9c6SsEmcMp6nJFvrk5dKdkXbPsTPEA41TJ_g-JRAA
.youtube.com	TRUE	/	TRUE	1773905277	__Secure-1PSID	g.a000tQh7qDc7vIBjkhh8HwRVQ6CNw1eAyqS3oSfUQzr-uP16BIe7AISM3LCrdE8_ofZVA8EnjgACgYKAfkSARQSFQHGX2MiAKxFdH-ZsoTWiYRBHh7qtxoVAUF8yKokMT536RCxS0DGnWp_3JlK0076
.youtube.com	TRUE	/	TRUE	1773905277	__Secure-3PSID	g.a000tQh7qDc7vIBjkhh8HwRVQ6CNw1eAyqS3oSfUQzr-uP16BIe7VSi2oomXZcBrfXwaCLkGQQACgYKAWYSARQSFQHGX2MibnGpNIpCFRNMFTpPf4mtsxoVAUF8yKrwY_-eXvFZGNQF7HI-Vqnl0076
.youtube.com	TRUE	/	FALSE	1773905277	HSID	ASXOOv0EmGJzgHf7d
.youtube.com	TRUE	/	TRUE	1773905277	SSID	AeN1Y9x8zLvezmZaE
.youtube.com	TRUE	/	FALSE	1773905277	APISID	JGlIq4YdEvh-xF-j/AtxdrfbZXolXO7A-u
.youtube.com	TRUE	/	TRUE	1773905277	SAPISID	5TBw9fn1-JVO2UfB/AjLYVfc4uWwC4Xbpb
.youtube.com	TRUE	/	TRUE	1773905277	__Secure-1PAPISID	5TBw9fn1-JVO2UfB/AjLYVfc4uWwC4Xbpb
.youtube.com	TRUE	/	TRUE	1773905277	__Secure-3PAPISID	5TBw9fn1-JVO2UfB/AjLYVfc4uWwC4Xbpb
.youtube.com	TRUE	/	TRUE	1774066129	LOGIN_INFO	AFmmF2swRgIhAOAYpMwFbyy5XtlnbZt2OJkYyBNLyjEjzj5BMCKU5MUaAiEA-XkvRIZqht7Eld3Olj4xyvqzE53TYsEISor4HBAux4I:QUQ3MjNmekRPSU5mUGtwcnFOU3M5MkdYdGhwUVNYb2t3YVFHTm11cS1lQzd1eDQtUU1TNEpRb0t2RWNZRGtnTjVDZXFMM19CeTFqajhuZjBwZTJoVGN6RGNUN0hDdHZoN3ZFWC1HVDhteVVoaGhGSklrSUxqMUgwTGpKcVBFRENna29XZU1JTEoyQ2hrc3NxWHRmbEUya2tKbE5WZGx4TG1R
.youtube.com	TRUE	/	FALSE	1771042350	SIDCC	AKEyXzXN9JgDwkE7aZVNfZB9QSzE_yaaDC-e6oHgIIfLj4eqa8ACBhSQwHN3I0PmVrrUpkpnEw
.youtube.com	TRUE	/	TRUE	1771042350	__Secure-1PSIDCC	AKEyXzVUl6YCuahywXoc9Kp8L6ARhJEFx5XTFCmfGgOk31iNrl8Oloa0mHrdTXDPbRT3d1nrrw
.youtube.com	TRUE	/	TRUE	1771042350	__Secure-3PSIDCC	AKEyXzWL-eY7uWesYSUNJmnn8_MHkI9pyQoGMnZkGLJv9vBsto5eD1ZvG9JIArkIS9IQiam0xA")

STRING1 = getenv("STRING_SESSION", "BQFpyqoAiGOYboTQWK7NXZmliA2f8m4SCle4X0VlsEiAKWAjsnjVvtNQVlpMknuqGEWI0yP1ldVRT4gaNL6PfBYavqf53ofvIfGHVvhmM3HY4xjk-lbOjKT7CR0OXGh0MD-xqS2X2n9JBlZg3DtBarNgg2AL9Qt3TVTPs13EcW3SdzrsFBbfMPYHnVoSS8JS4L_XIVPhxxprcZFSZlwpSO4kLLuKdCwgMpxt9Y4W0HLAJ2Haw7KAdBUkAxZsAtbKhlYIj9kDqLEpQrvjmZ3lWw4HNpOIiAtorPC5-4pAGMes2Vk2XvDajsbdjwLZ2Rrd-vjFFpL2TeahkNcYhgpo5XbnNV5OFwAAAAG0Yy8hAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/E8m.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
