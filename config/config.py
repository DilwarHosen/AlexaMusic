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

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

OWNER_ID = int(getenv("OWNER_ID", None))

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

.youtube.com	TRUE	/	TRUE	1754985309	VISITOR_INFO1_LIVE	27lxucQ955A
.youtube.com	TRUE	/	TRUE	1754985309	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgLw%3D%3D
.youtube.com	TRUE	/	TRUE	1754968132	__Secure-ROLLOUT_TOKEN	COud-Lv2nPvMRxCF496F1r-LAxiF496F1r-LAw%3D%3D
accounts.google.com	FALSE	/	TRUE	1742008139	OTZ	7951869_34_34__34_
.google.com	TRUE	/	FALSE	1773976164	SID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xrXbsHT-V-idIjs3_2w0k6QACgYKAQgSAQASFQHGX2MiW7n-yWT-ngEhgC1kzGPYphoVAUF8yKppG8M4vQoGxTIn3bvDgC7E0076
.google.com	TRUE	/	TRUE	1773976164	__Secure-1PSID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xuSVackxWNnyefmtcNW7SEgACgYKAXoSAQASFQHGX2Mibbejfm6hzbKJtCdL6Oa5yBoVAUF8yKqwXBmjRqs3-abepCX5tv6e0076
.google.com	TRUE	/	TRUE	1773976164	__Secure-3PSID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xPFxhr52ilVFL6SQ3Isqq6AACgYKAd4SAQASFQHGX2MiaOXSbrPCTqgWc_I3BMjIKBoVAUF8yKrOcKnpVMmlDppoj-xmLpEF0076
.google.com	TRUE	/	FALSE	1773976164	HSID	An5_FCViM2pjcKw9V
.google.com	TRUE	/	TRUE	1773976164	SSID	A6x9ny_zY7d-BNwig
.google.com	TRUE	/	FALSE	1773976164	APISID	HR1rH5YkDWxQdH04/AfHKRlnsoOjs5vwmi
.google.com	TRUE	/	TRUE	1773976164	SAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.google.com	TRUE	/	TRUE	1773976164	__Secure-1PAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.google.com	TRUE	/	TRUE	1773976164	__Secure-3PAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
accounts.google.com	FALSE	/	TRUE	1773976164	__Host-GAPS	1:4oeCqrWhpTeIrm6go9BwIRqSwfxuvr63X-PY0MStvL_WarxPsxWUC-4gg0sc5-wtjccjFvRa-VA1RjOMrzcEDtw7enpUqw:glV5CRHuW4hbHk1j
accounts.google.com	FALSE	/	TRUE	1773976164	ACCOUNT_CHOOSER	AFx_qI4SNdxoe8-FPGEF1swBJ46pHDJb5dor-s_S14LOP9tudOQfKxiR2FfkwZQMcGL9h7ljzh4s5Uvh2pxxB_hACT764RS7q6g4YT-cEMU8QgHFDp1VqSFaXW-H_zQa3sxCoHDuStV1cUM8434_KaGuYDgA_STWdQ
.youtube.com	TRUE	/	FALSE	1773976165	SID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xrXbsHT-V-idIjs3_2w0k6QACgYKAQgSAQASFQHGX2MiW7n-yWT-ngEhgC1kzGPYphoVAUF8yKppG8M4vQoGxTIn3bvDgC7E0076
.youtube.com	TRUE	/	TRUE	1770952165	__Secure-1PSIDTS	sidts-CjEBEJ3XVyIrBOg86jLMeRi74jbKTwEQ6NvIjcMXtxj73IMinuyR7I2kfUdn8TdWsOkuEAA
.youtube.com	TRUE	/	TRUE	1770952165	__Secure-3PSIDTS	sidts-CjEBEJ3XVyIrBOg86jLMeRi74jbKTwEQ6NvIjcMXtxj73IMinuyR7I2kfUdn8TdWsOkuEAA
.youtube.com	TRUE	/	TRUE	1773976165	__Secure-1PSID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xuSVackxWNnyefmtcNW7SEgACgYKAXoSAQASFQHGX2Mibbejfm6hzbKJtCdL6Oa5yBoVAUF8yKqwXBmjRqs3-abepCX5tv6e0076
.youtube.com	TRUE	/	TRUE	1773976165	__Secure-3PSID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xPFxhr52ilVFL6SQ3Isqq6AACgYKAd4SAQASFQHGX2MiaOXSbrPCTqgWc_I3BMjIKBoVAUF8yKrOcKnpVMmlDppoj-xmLpEF0076
.youtube.com	TRUE	/	FALSE	1773976165	HSID	AouFOvprU31A9bmEE
.youtube.com	TRUE	/	TRUE	1773976165	SSID	A_y9cCQb0zMtnMem0
.youtube.com	TRUE	/	FALSE	1773976165	APISID	HR1rH5YkDWxQdH04/AfHKRlnsoOjs5vwmi
.youtube.com	TRUE	/	TRUE	1773976165	SAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.youtube.com	TRUE	/	TRUE	1773976165	__Secure-1PAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.youtube.com	TRUE	/	TRUE	1773976165	__Secure-3PAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.google.co.in	TRUE	/	FALSE	1773976165	SID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xrXbsHT-V-idIjs3_2w0k6QACgYKAQgSAQASFQHGX2MiW7n-yWT-ngEhgC1kzGPYphoVAUF8yKppG8M4vQoGxTIn3bvDgC7E0076
.google.co.in	TRUE	/	TRUE	1773976165	__Secure-1PSID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xuSVackxWNnyefmtcNW7SEgACgYKAXoSAQASFQHGX2Mibbejfm6hzbKJtCdL6Oa5yBoVAUF8yKqwXBmjRqs3-abepCX5tv6e0076
.google.co.in	TRUE	/	TRUE	1773976165	__Secure-3PSID	g.a000twijBGXVF9ChnurLjBK8D4UbjYGF5STK2vHi7UAvbV_l8h4xPFxhr52ilVFL6SQ3Isqq6AACgYKAd4SAQASFQHGX2MiaOXSbrPCTqgWc_I3BMjIKBoVAUF8yKrOcKnpVMmlDppoj-xmLpEF0076
.google.co.in	TRUE	/	FALSE	1773976165	HSID	AouFOvprU31A9bmEE
.google.co.in	TRUE	/	TRUE	1773976165	SSID	A_y9cCQb0zMtnMem0
.google.co.in	TRUE	/	FALSE	1773976165	APISID	HR1rH5YkDWxQdH04/AfHKRlnsoOjs5vwmi
.google.co.in	TRUE	/	TRUE	1773976165	SAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.google.co.in	TRUE	/	TRUE	1773976165	__Secure-1PAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.google.co.in	TRUE	/	TRUE	1773976165	__Secure-3PAPISID	xkDYU-IAhBjferEJ/Au7UEUHAHoTsII5SL
.google.co.in	TRUE	/	TRUE	1755227365	NID	521=qHVsf6kdZwjOli2b5SlFrsGMr-TVIe6MyT-cBsTJYNeC58LPU7D562iS6aYI3CiDKTBgnkqgtD-BGxn6TrKt3zvn_HVARq2i_W-z6b1g79nXNIPP2FCAqyoUeT2hzNVaZCj-xeBttvSQO04suWTbYHNeszEql5b4e7uBX-fEwoUj9NNzOlf-oUlvS9KAilV1Lvg2yQo
.youtube.com	TRUE	/	TRUE	1773976166	LOGIN_INFO	AFmmF2swRAIgMhWWiSRPbVtSr5WF9BayIgArUYCIU4MH3zO0M8x3mI8CIHNoMShwjcFxy29UxPzKcoK1FHCR5DheTIXC4iRe2n2c:QUQ3MjNmeWZnMTRmYWQ2MXN4VWF0S1FUbjhEcThJTC01OHMzdHNMX1BLcndEcWNyZEFmN2NYbS1Id2pvbHRoWEFUc3gyanByU3MtT2ladUFwN2lZTDRROVVHaWNTZGIwWXNFSkdkNjBTT3hOZUZWNWE0QW1VN01ySWhDVXZPdXA1T19ROFZweFg3bTNjdEMwc2dmeVN6NmcwdU9OUURaLURB
accounts.google.com	FALSE	/	TRUE	1773977815	LSID	o.chromewebstore.google.com|s.IN|s.youtube:g.a000twijBC-JQbT8hTyYs8Tt6roTY0vWt9V0preSt8RrbHyAAckVL0-dQ8dymyiEkurtVYHwawACgYKAUoSAQASFQHGX2MiLyP1HiTO5JsG3hrOT7oQJRoVAUF8yKq8Ek8osEd8YCGgz8tkRaOJ0076
accounts.google.com	FALSE	/	TRUE	1773977815	__Host-1PLSID	o.chromewebstore.google.com|s.IN|s.youtube:g.a000twijBC-JQbT8hTyYs8Tt6roTY0vWt9V0preSt8RrbHyAAckVbpvJl5DXCRjPRn7RIPEhNAACgYKAasSAQASFQHGX2Mi_du7Nk8f62PNEBkaJUQxLBoVAUF8yKpMTr4KatOp9kHJMhpwDSGO0076
accounts.google.com	FALSE	/	TRUE	1773977815	__Host-3PLSID	o.chromewebstore.google.com|s.IN|s.youtube:g.a000twijBC-JQbT8hTyYs8Tt6roTY0vWt9V0preSt8RrbHyAAckVMElmXmm7yr6jo5vApsKrhAACgYKAYYSAQASFQHGX2MigdO7DGNTZ8jZT7TZ2KMQIhoVAUF8yKo74MzHF-0rrCLbUFH71csE0076
chromewebstore.google.com	FALSE	/	TRUE	1773977816	OSID	g.a000tQijBKN0tHL9dSciJrxKH31_TMsFrWX6oOmgLMOvOVfB-GdCWGazMo9J-fSMg9acb4EWsQACgYKAc8SARQSFQHGX2Mie_yEC52lcRI_aMhQfd9cdxoVAUF8yKo2L6gGE5tC28z-Y12IVF5f0076
chromewebstore.google.com	FALSE	/	TRUE	1773977816	__Secure-OSID	g.a000tQijBKN0tHL9dSciJrxKH31_TMsFrWX6oOmgLMOvOVfB-GdCi7n-BaVN6qG0FgompB7jQwACgYKAQ8SARQSFQHGX2Mi6Xr3t-j6EouqdhfCCkPRbhoVAUF8yKpyevcNufBJA1rV1nevt_JC0076
.chromewebstore.google.com	TRUE	/	FALSE	1773993297	_ga	GA1.1.1701678325.1739417818
chromewebstore.google.com	FALSE	/	TRUE	1742009818	OTZ	7951897_34_34__34_
ogs.google.com	FALSE	/	TRUE	1742009821	OTZ	7951897_34_34__34_
.google.com	TRUE	/	TRUE	1755244452	NID	521=rk1pUjQ-DSXI8Nwjboyxir6eq5KQPhP9S9V97HPo_6FdZhCaYf7JXtW0fnbw0oqr8QWnEqtvxKutx8tjoELEgjpIHfXX9U7SoDbxGEVI2JbebGofd9wXvys__epdOQ2K-ruaH_xm8rw1sM2uSK9kzHnr36hhCCfg52QJBCtdMibL5km6cZjm6ypv1ggBBHKn7RmpzQhd2fO6cKPUKzdIR0XuQXEx3T27HiySHLqaRaphVk35wVmgRWxgfjxxpZLXwqX3VRlrXEH5RHOIfCbbHvjpMocrtGroLnJlBy4a9i9yFDDyhy_C2rbt-RGIcp-8g7B1NuGfHoG2se8vtMrd0c_Epq1UfdIA93sQzZvpu3dlpW_zqkF9lD_NekhpTwHrpkZK0GciPu2I4Jo0swPv03s42t9XoU8PDiWIc8TIADBj8msrGP0cWcKKn5ncVybCus5OUS2DpMR9mmjjw67dOou4YQrVQ3wWPyC5bMvQCrHyVj4W3V6xcTfeixFjC3nRCtM-RkJ0jTx4v5TiCOdAzMr_7OBjWeysf9zJNMJjdnPIfo2z1k-8-JMRLFMkK-daRwBE6wfWuWA-IqXV-YU1-kAGcV7n6MbJM0oA5dpjxNS6sIFElM_M1wpw4CoS916513hlijJsuYtSdftpGCJKOIwMxyjbwOZkSbLH0lH3F0Ul97L-fXbY2iN_n8cYvjLqz06Fnhiy04g
.chromewebstore.google.com	TRUE	/	FALSE	1773993297	_ga_KHZNC1Q6K0	GS1.1.1739433251.2.1.1739433297.0.0.0
.youtube.com	TRUE	/	TRUE	0	YSC	vIU3X-xfi-I
.youtube.com	TRUE	/	TRUE	1773993314	PREF	f6=40000000&tz=Asia.Calcutta&f7=100
.google.com	TRUE	/	FALSE	1770969419	SIDCC	AKEyXzWHLOe-7SSqlAkIH2cfMNVFERvFxjhlwsIrJ0sv5pHTG6lCArn0mTRgESdx6cCkEMos
.google.com	TRUE	/	TRUE	1770969419	__Secure-1PSIDCC	AKEyXzWSm3DrgueIcktUh7YnuTmh7oYq1XP6tZkSD-1sdQZ6BjWAz1LlqEUDBxek1zCQWQfT
.google.com	TRUE	/	TRUE	1770969419	__Secure-3PSIDCC	AKEyXzUSQJPowBaDIrqbbyRfgiTgnH0opsrd3_Smumy6J-_5mTwDVCz76hMcdZn1wob5Rcm3BQ
.youtube.com	TRUE	/	FALSE	1770969448	SIDCC	AKEyXzW4JAC7SmTk9pgdldb0fZ2eQ1M21w_kBfHbzcAHzlUYKegW_khTJZ4ws9f6GEPIXssdCw
.youtube.com	TRUE	/	TRUE	1770969448	__Secure-1PSIDCC	AKEyXzWs10f5moV8nONCZoYp47O5qbRiDZeZtv5S3k0E5ukwM1VFCdQ2iunq156sB7wVNxOP
.youtube.com	TRUE	/	TRUE	1770969448	__Secure-3PSIDCC	AKEyXzX04no-hcYB5UubeKgRJVv6eOm2U2kciWISYffoMVm7kYPPVOFR5aOvaQBI-7AIfs7bvg")
# https://batbin.me

STRING1 = getenv("STRING_SESSION", None)
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
    "START_IMG_URL", "https://te.legra.ph/file/8e43d1a66ca355ea0b7a5.jpg"
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
