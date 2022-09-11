#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & PR0FESS0R-99

import os
from config import Config
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.errors import FloodWait

TXT="""**• @infinityLK | @infinityCLK •**"""
TVT="""**➥ File Name :**"""

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"<code>{TVA}</code><code>{kopp.file_name}</code>\n\n{TXT}")

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
