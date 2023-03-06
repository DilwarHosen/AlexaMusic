#
# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki



from typing import Dict, List, Union
from AlexaMusic.core.mongo import mongodb

themedb = mongodb.notes


async def _get_theme(chat_id: int) -> Dict[str, int]:
    _notes = await themedb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_theme(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_theme(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_theme(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_theme(chat_id)
    _notes[name] = note
    await themedb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )
