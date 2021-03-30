from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
import os
from asyncio.exceptions import TimeoutError

from userbot.events import xubot_cmd


@bot.on(xubot_cmd(outgoing=True, pattern="gen(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    gen = "gen"
    await event.edit("```Processing```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            response2 = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            link1 = await conv.send_message(f'/{gen} {link}')
            response = await response
            response2 = await response2
        except YouBlockedUserError:
            await event.reply("```Unblock plox```")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.reply(f"{response2.message.message}")
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(xubot_cmd(outgoing=True, pattern=r"chk(?: |$)(.*)"))
async def _(event):
    try:
        query = event.pattern_match.group(1)
        await event.edit("`Processing..`")
        async with bot.conversation("@Carol5_bot") as conv:
            try:
                query1 = await conv.send_message(f"/ss {query}")
                asyncio.sleep(3)
                r1 = await conv.get_response()
                r2 = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await event.reply("Unblock @SaitamaRobot plox")
            if r1.text.startswith("Waiting"):
                return await event.edit(f"`No result found for` **{query}**")
                p = await event.edit(
                    r2,
                    reply_to=event.reply_to_msg_id,
                )
                await event.client.delete_messages(
                    conv.chat_id, [r1.id, r2.id, query1.id]
                )
