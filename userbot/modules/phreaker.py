
from telethon import events
import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import xubot_cmd
from userbot import CUSTOM_CMD as xcm


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
            link1 = await conv.send_message(f'/{gen} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock plox```")
            return
        else:
            await event.delete()
            await event.edit(response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])
