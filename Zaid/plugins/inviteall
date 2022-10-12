import asyncio
import os
import sys
from datetime import datetime

import telethon.utils
from telethon import TelegramClient, events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.tl import functions
from telethon.tl.functions.channels import (
    GetFullChannelRequest,
    InviteToChannelRequest,
    LeaveChannelRequest,
)
from telethon.tl.functions.messages import GetFullChatRequest

grp = GROUP_USERNAME

if "@" in grp:
    grp = grp.replace("@", "")


SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@events.register(events.NewMessage(pattern="^/scrap"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            kartik = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            kartik = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await kartik.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await kartik.edit(
            "**📡[Ͳєямιиαℓ Տτατυѕ](https://t.me/Elric_xD)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await wdk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await kartik.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await kartik.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Elric_xD) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )
