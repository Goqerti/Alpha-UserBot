# Copyright (C) 2020 U S Σ R Δ T O R
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import bot


@register(outgoing=True, pattern="^.tik ?(.*)")
async def tiktok(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Yükləmək üçün bir linkə cavab verin.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Bir linkə cavab olaraq istifadə edin.`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Real istifadəçilərə cavab olaraq istifadə edin.")
        return
    asc = await event.edit("`Yüklənilir...` 🔥")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("@SaveAsbot'u `blokdan çıxardın və yenidən yoxlayın`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "gizlilik ayarlarınızı düzəldin."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"@AlphaUserBot ;)",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()
            
@register(outgoing=True, pattern="^.ig(?: |$)(.*)")
@register(outgoing=True, pattern="^.pnt(?: |$)(.*)")
async def _(event):
    rtext = await event.get_reply_message()
    d_link = event.pattern_match.group(1)
    if d_link:
        pass
    elif rtext:
        d_link = rtext.text
    if ".com" not in d_link:
        await event.edit("Zəhmət olmasa, düzgün bir link daxil edin")
    else:
        await event.edit("Yüklənilir...")
    chat = "@iziBot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            video = await conv.get_response()
            details = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(f"{chat}'u blokdan çıxarın")
            return
        await event.client.send_file(event.chat_id, video, caption=f"{details.text} \n\n@AlphaUserBot `ilə yükləndi`")
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await event.delete()

CmdHelp('sosial').add_command(
    'ig', '<link>', 'Cavab verdiyiniz Instagram linkini media olaraq göndərər\n⚠️Diqqət: Verdiyiniz linkdəki hesab gizli olmamalıdır.'
).add_command(
    'tik', '<link>', 'Cavab verdiyiniz TikTok linkini media olaraq göndərər.'
).add_command(
    'pnt', '<link>', 'Cavab verdiyiniz Pinterest linkini media olaraq göndərər.'
).add()
